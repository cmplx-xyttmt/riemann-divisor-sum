# Divisor Sums for the Riemann Hypothesis

![Project Build](https://github.com/cmplx-xyttmt/riemann-divisor-sum/actions/workflows/python-app.yml/badge.svg)
[![codecov](https://codecov.io/gh/cmplx-xyttmt/riemann-divisor-sum/branch/main/graph/badge.svg?token=HYUDWD4WYJ)](https://codecov.io/gh/cmplx-xyttmt/riemann-divisor-sum)

This project is based on [Jeremy Kun's searching for RH counterexamples blog](https://jeremykun.com/2020/09/11/searching-for-rh-counterexamples-setting-up-pytest/).

I'm using this to practice and learn about TDD in python and productionizing.

#### Some options to use with Pytest
- `pytest test/dir`: test only files that directory or `pytest test/dir/test_file.py` to test only tests in that file.
- `pytest -k STR`: only run tests whose name contains "STR"
- `pytest -s`: see any logs or print statements inside tested code
