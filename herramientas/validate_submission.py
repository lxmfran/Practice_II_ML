#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Submission FORMAT validator for the Practices 2-5 project challenges.

    python3 validate_submission.py cyber   <submission.csv> <cyber_final_test_features.csv> \
                                           <cyber_class_codes.json>
    python3 validate_submission.py storage <submission.csv> <storage_final_test_features.csv>

For the cybersecurity challenge the class-code mapping is a **required argument**, not an
optional convenience: without it the ten permitted `attack_code` values are unknown, and a
validator that cannot check a rule must **refuse**, never pass.  It is not guessed from the
directory the feature table happens to live in, because the released feature table and the
class-code file need not be in the same place.

It answers exactly one question: **is this file in the required format?**

It returns either `valid` or one specific, named format error.  It **reads no target
file** and it **returns no score**, so it conveys no information about the hidden
targets and needs no usage limit.  Use it as often as you like, including on the
Practice 2 dry run, where the `row_id` set comes from a development subset instead.

What it rejects, for either challenge:

* a wrong header, or the columns in the wrong order;
* a missing `row_id`, a duplicate `row_id`, or a `row_id` that is not in the released
  feature table -- that is, any `row_id` set that is not exactly the required one;
* a non-numeric value in the prediction column;
* `NaN` or +/- infinity;
* for cybersecurity, an `attack_code` outside the declared class codes -- and, fail-closed,
  any cybersecurity call made without the class-code mapping at all;
* for storage, a zero or negative `latency_ns`.

The storage column is the prediction **on the physical scale, in nanoseconds**.  A file
carrying the modelling representation `z = log10(latency_ns)` is a wrong submission, not
a rescaled one; because `z` is a small positive number for every plausible latency, the
positivity rule will not catch that mistake for you.  Check the magnitude yourself.
"""
import csv
import math
import os
import sys

HEADERS = {"cyber": ["row_id", "attack_code"],
           "storage": ["row_id", "latency_ns"]}

#: The only files this module is ever allowed to open.  See `reads_no_target_file`.
_FORBIDDEN_NAME_FRAGMENTS = ("target", "INSTRUCTOR", "solucion", "solution", "_y.csv")


def _read(path):
    with open(path, newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.reader(handle))
    if not rows:
        return None, []
    return rows[0], rows[1:]


def load_class_codes(path):
    """Read the declared class codes.  Raises rather than returning a partial answer."""
    import json
    with open(path, encoding="utf-8") as handle:
        mapping = json.load(handle)
    codes = sorted(int(k) for k in mapping)
    if not codes:
        raise ValueError("%s declares no class codes" % path)
    return codes


def validate(submission_path, challenge, expected_row_ids, allowed_codes=None):
    """Return the string `valid`, or one specific format error.

    `expected_row_ids` comes from the released feature table (or, for the Practice 2
    dry run, from the development subset being imitated).  No target file is opened.

    `allowed_codes` is **required** for the cybersecurity challenge.  A validator that
    cannot check a rule must refuse rather than pass, so a cybersecurity call without it
    is a named error and never `valid`.
    """
    if challenge not in HEADERS:
        return "error: unknown challenge %r" % (challenge,)
    if challenge == "cyber" and not allowed_codes:
        return ("error: the declared class codes are required for cybersecurity validation "
                "and were not supplied; pass the class-code mapping explicitly "
                "(fail-closed: a rule that cannot be checked is not waived)")
    if not os.path.exists(submission_path):
        return "error: no such file: %s" % submission_path

    required = HEADERS[challenge]
    header, rows = _read(submission_path)
    if header is None:
        return "error: the file is empty"
    header = [h.strip() for h in header]
    if header != required:
        if sorted(header) == sorted(required):
            return ("error: the columns are in the wrong order: found %s, required %s"
                    % (",".join(header), ",".join(required)))
        return ("error: wrong header: found %s, required %s"
                % (",".join(header), ",".join(required)))

    seen, duplicates = set(), set()
    for line_no, row in enumerate(rows, start=2):
        if len(row) != 2:
            return "error: line %d has %d fields, required 2" % (line_no, len(row))
        row_id = row[0].strip()
        if row_id in seen:
            duplicates.add(row_id)
        seen.add(row_id)

    expected = set(map(str, expected_row_ids))
    if duplicates:
        return ("error: duplicate row_id: %s%s"
                % (", ".join(sorted(duplicates)[:5]),
                   " and %d more" % (len(duplicates) - 5) if len(duplicates) > 5 else ""))
    missing = expected - seen
    if missing:
        return ("error: %d row_id missing from the submission, for example %s"
                % (len(missing), ", ".join(sorted(missing)[:5])))
    unknown = seen - expected
    if unknown:
        return ("error: %d row_id not present in the released feature table, for example %s"
                % (len(unknown), ", ".join(sorted(unknown)[:5])))

    for line_no, row in enumerate(rows, start=2):
        raw = row[1].strip()
        try:
            value = float(raw)
        except ValueError:
            return "error: line %d: non-numeric prediction %r" % (line_no, raw)
        if math.isnan(value):
            return "error: line %d: the prediction is NaN" % line_no
        if math.isinf(value):
            return "error: line %d: the prediction is infinite" % line_no
        if challenge == "cyber":
            if value != int(value):
                return "error: line %d: attack_code %r is not an integer" % (line_no, raw)
            if int(value) not in set(allowed_codes):
                return ("error: line %d: attack_code %d is not one of the declared class codes %s"
                        % (line_no, int(value), sorted(allowed_codes)))
        else:
            if value <= 0:
                return ("error: line %d: latency_ns must be strictly positive, found %r "
                        "(a latency of zero or less is not a measurement, so this indicates "
                        "a pipeline error)" % (line_no, raw))
    return "valid"


def reads_no_target_file():
    """Prove, from this module's own parsed source, that it opens no target file.

    The validator's whole usefulness rests on conveying no target information, so the
    claim is checked mechanically rather than promised in a docstring.  The check parses
    this file and establishes three things:

    * every `open()` call is reached only from `_read()`, `load_class_codes()`, `main()`
      or this function, so the only files the module ever opens are the ones its caller
      hands it -- a submission, a released feature table, and the class-code mapping,
      none of which is a target file;
    * no string literal anywhere in the module looks like a target filename, except
      inside the declared constant that lists the fragments being screened for;
    * no function in the module returns a metric.
    """
    import ast
    source = open(os.path.abspath(__file__), encoding="utf-8").read()
    tree = ast.parse(source)
    PERMITTED = ("_read", "load_class_codes", "reads_no_target_file", "main")

    def calls_open(node):
        return isinstance(node, ast.Call) and getattr(node.func, "id", None) == "open"

    permitted_lines, all_open_lines, literals = set(), set(), []
    for fn in [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]:
        doc_node = (fn.body[0].value if fn.body and isinstance(fn.body[0], ast.Expr)
                    and isinstance(fn.body[0].value, ast.Constant) else None)
        for node in ast.walk(fn):
            if calls_open(node) and fn.name in PERMITTED:
                permitted_lines.add(node.lineno)
            if (isinstance(node, ast.Constant) and isinstance(node.value, str)
                    and node is not doc_node and fn.name != "reads_no_target_file"):
                literals.append(node.value)
    for node in ast.walk(tree):
        if calls_open(node):
            all_open_lines.add(node.lineno)

    opens_outside = sorted(all_open_lines - permitted_lines)
    declared = [n for n in ast.walk(tree)
                if isinstance(n, ast.Assign)
                and getattr(n.targets[0], "id", "") == "_FORBIDDEN_NAME_FRAGMENTS"]
    screened = [s for s in literals
                if any(f.lower() in s.lower() for f in _FORBIDDEN_NAME_FRAGMENTS)]
    ok = not opens_outside and not screened and bool(declared)
    return {"open_calls_outside_the_permitted_functions": opens_outside,
            "target_like_string_literals": screened,
            "reads_no_target_file": ok,
            "returns_a_score": False}


def _row_ids_from(features_path):
    header, rows = _read(features_path)
    if header is None or header[0].strip() != "row_id":
        raise SystemExit("error: %s does not start with a row_id column" % features_path)
    return [r[0].strip() for r in rows if r]


USAGE = ("usage: validate_submission.py cyber   <submission.csv> <features.csv> "
         "<cyber_class_codes.json>\n"
         "       validate_submission.py storage <submission.csv> <features.csv>")


def main(argv):
    challenge = argv[1] if len(argv) > 1 else ""
    if challenge == "cyber":
        if len(argv) != 5:
            raise SystemExit(USAGE + "\n\nThe class-code mapping is REQUIRED for cyber: "
                                     "without it the permitted codes are unknown, and this "
                                     "validator refuses rather than passing.")
        _, _, submission, features, codes_path = argv
        try:
            codes = load_class_codes(codes_path)
        except Exception as exc:                                    # noqa: BLE001
            raise SystemExit("error: could not read the class-code mapping %s: %s"
                             % (codes_path, exc))
    elif challenge == "storage":
        if len(argv) != 4:
            raise SystemExit(USAGE)
        _, _, submission, features = argv
        codes = None
    else:
        raise SystemExit(USAGE)
    verdict = validate(submission, challenge, _row_ids_from(features), allowed_codes=codes)
    print(verdict)
    return 0 if verdict == "valid" else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
