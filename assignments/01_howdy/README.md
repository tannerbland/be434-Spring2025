# Assignment 1: Howdy

Create Python program called `howdy.py` that will print a friendly greeting.

## Using new.py 

I hate writing code from scratch! This week you learned about using a program called `new.py` that will create a program for you to start from. Now, we are going to learn to use it.

In the _bin_ directory of your repo, you should find a program called `new.py` that will help you make a new Python program.

Let's use a few easy Unix commands to create a draft program called howdy.py that we can edit.

```
cd ./assignments/01_howdy
~/workspace/bin/new.py --help
```

You should see something like this:
```
usage: new.py [-h] [-n NAME] [-e EMAIL] [-p PURPOSE] [-f] program

Create Python argparse program

positional arguments:
  program               Program name

options:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Name for docstring (default: runner)
  -e EMAIL, --email EMAIL
                        Email for docstring (default: runner@11ec487482cf)
  -p PURPOSE, --purpose PURPOSE
                        Purpose for docstring (default: Rock the Casbah)
  -f, --force           Overwrite existing (default: False)
```

## Getting Started with new.py

Here is how you can create the `howdy.py` using `new.py`:

```
$ ~/workspace/bin/new.py -p 'Print greeting' howdy.py
Done, see new script "howdy.py."
```

Open the new `howdy.py` program and modify it to accept three optional arguments:

* `-g|--greeting`: A greeting, defaults to "Howdy"
* `-n|--name`: A name to greeting, defaults to "Stranger"
* `-e|--excited`: A flag to terminate the greeting with an exclamation point

The program should respond to `-h|--help` to print the following usage:

```
$ ./howdy.py -h
usage: howdy.py [-h] [-g str] [-n str] [-e]

Greetings and howdy

optional arguments:
  -h, --help            show this help message and exit
  -g str, --greeting str
                        The greeting (default: Howdy)
  -n str, --name str    Whom to greet (default: Stranger)
  -e, --excited         Include an exclamation point (default: False)
```

When run with no arguments, it should use the default values to print the following:

```
$ ./howdy.py
Howdy, Stranger.
```

The `-g|--greeting` option should cause it to use the provided greeting:

```
$ ./howdy.py -g Sup
Sup, Stranger.
```

The `-n|--name` option should cause it to use the provided name:

```
$ ./howdy.py -n Amanda
Howdy, Amanda.
```

The `-e|--excited` flag should cause the greeting to end with a bang:

```
$ ./howdy.py -e
Howdy, Stranger!
```

The program should accept any combination of the short or long names of the arguments:

```
$ ./howdy.py --greeting Sup --name Dude --excited
Sup, Dude!
```

## Testing

You can run the test suite with the following command:

```
$ pytest -xv test.py howdy.py
$ flake8 howdy.py
$ pylint howdy.py
```

You can also use the Makefile shortcut:

```
$ make test
```

The tests include linting with `pylint` and `flake8`, these programs check to make sure your code is formatted well. For example, code can run/work, but be ugly and hard to read. Be sure that you format your code with something like `yapf` or `black` in replit. If you haven't installed these per instructions in 00_getting_started, there is no time like the present!

A passing test suite looks like this:

```
============================= test session starts ==============================
...
--------------------------------------------------------------------------------
Linting files
.
--------------------------------------------------------------------------------

test.py::PYLINT PASSED                                                   [ 11%]
test.py::FLAKE8 PASSED                                                   [ 22%]
test.py::test_exists PASSED                                              [ 33%]
test.py::test_usage PASSED                                               [ 44%]
test.py::test_defaults PASSED                                            [ 55%]
test.py::test_greeting PASSED                                            [ 66%]
test.py::test_name PASSED                                                [ 77%]
test.py::test_excited PASSED                                             [ 88%]
test.py::test_all_options PASSED                                         [100%]

============================== 9 passed in 0.51s ===============================
```

Your grade is whatever percentage of tests your code passes.

## Authors

Bonnie Hurwitz <bhurwitz@arizona.edu> and Ken Youens-Clark <kyclark@gmail.com>
