# coding_platform Python Template

## Python Best Practices
### Folder Structure
```
 project
 |__ src
    |__tests
       |__  __init__.py
       |__  test_file_one.py
       |__  test_file_two.py
    |__ __init__.py
    |__ main.py (Code for Functions goes there. If multiple files, goes under same directory src/)
 |__ README.md
 |__ setup.py (presence of which is an indication that the module/package you are about to install has likely been packaged and distributed with Distutils, which is the standard for distributing Python Modules.)
```
For more details: https://docs.python-guide.org/writing/structure/

**Note:** Both Pytest framework and Unittest framework test files goes under `./src/tests/` directory.


## Test with Unittest Framework

 The following command is needed to test. 
 
 It will consider files start with `test_` naming convention which is inside `./src/tests` directory.
 
 `python -m unittest discover -s ./src/tests  -p 'test_*.py'`
 
 ## Test with Pytest Framework
 
 Follow the folder structure when using pytest. It will consider files start with `test_` naming convention.
 
 The command used to run with pytest is : `pytest`
 
