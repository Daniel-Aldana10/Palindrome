
## Coverage

Make sure you have "coverage" in your requirements.txt file and run pip install. Then run `python -m coverage run -m unittest discover` and after that run `python -m coverage report` to get the following table:
```
Name                                  Stmts   Miss  Cover
---------------------------------------------------------
data\constants.py                         2      0   100%
data\data_generator.py                   12      0   100%
palindrome_algorithms\algorithms.py      16      0   100%
test\test_algorithms.py                  22      1    95%
test\test_data_generator.py              16      1    94%
---------------------------------------------------------
TOTAL                                    68      2    97%
If you want to see the lines that are not being used you can run 'python -m cover html' and then 'start htmlcov\index.html'
```

---
