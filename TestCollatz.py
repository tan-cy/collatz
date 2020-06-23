#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval_helper, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "100 200\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  100)
        self.assertEqual(j, 200)

    def test_read_3(self):
        s = "201 210\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  201)
        self.assertEqual(j, 210)

    def test_read_4(self):
        s = "900 1000\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  900)
        self.assertEqual(j, 1000)

    # -----------
    # eval helper
    # -----------

    def test_helper_1(self):
        v = collatz_eval_helper(10)
        self.assertEqual(v, 7)

    def test_helper_2(self):
        v = collatz_eval_helper(99999)
        self.assertEqual(v, 227)

    def test_helper_3(self):
        v = collatz_eval_helper(1)
        self.assertEqual(v, 1)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5(self):
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    def test_eval_6(self):
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_7(self):
        v = collatz_eval(5, 6)
        self.assertEqual(v, 9)

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 201, 210, 89)
        self.assertEqual(w.getvalue(), "201 210 89\n")

    def test_print_4(self):
        w = StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assertEqual(w.getvalue(), "900 1000 174\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO("20 30\n1 53\n86 90\n580 689\n40 234\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "20 30 112\n1 53 112\n86 90 31\n580 689 145\n40 234 128\n")

    def test_solve_3(self):
        r = StringIO("1 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 1 1\n")

    def test_solve_4(self):
        r = StringIO("3000 900\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "3000 900 217\n")

# ----
# main
# ----


if __name__ == "__main__":
    main()

""" #pragma: no cover
$ coverage run --branch TestCollatz.py >  TestCollatz.out 2>&1


$ cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK


$ coverage report -m                   >> TestCollatz.out



$ cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          12      0      2      0   100%
TestCollatz.py      32      0      0      0   100%
------------------------------------------------------------
TOTAL               44      0      2      0   100%
"""
