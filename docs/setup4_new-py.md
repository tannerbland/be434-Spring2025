# Using new.py

I hate writing code from scratch! This week you learned about using a program called `new.py` that will create a program for you to start from. We will use this template each time we start one of our coding assignments.

In the _bin_ directory of your repo, you should find a program called `new.py` that will help you make a new Python program.
You can use a few simple unix commands to create a program with this script, for example:

Here is how you can create the `testing.py` using `new.py`:

```
$ ~/workspace/bin/new.py -p 'This is a test script' testing.py
Done, see new script "testing.py."
```

You can also get a help message to see all of the options:

```
~/workspace/bin/new.py -h
usage: new.py [-h] [-n NAME] [-e EMAIL] [-p PURPOSE] [-f] program

Create Python argparse program

positional arguments:
  program               Program name

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Name for docstring (default: Ken Youens-Clark)
  -e EMAIL, --email EMAIL
                        Email for docstring (default: kyclark@gmail.com)
  -p PURPOSE, --purpose PURPOSE
                        Purpose for docstring (default: Rock the Casbah)
  -f, --force           Overwrite existing (default: False)
```

You can run this command in Replit each time you need to create a script.

## Completing your homework

Next, we are going to make sure you set up everything up correctly, and make sure you can "commit" changes.

* Go to replit, on the left side at the bottom you will see an icon with 4 squares. 
* Hover over the icon with 4 squares and select "Git" from "all tools"
* Under "Commit", you should see all changes you have made to your repository in replit. 
* Write a summary of your commit like, "testing commit", and click on "Stage and commit all changes"
* Under "Remote Updates", click on the "Sync with Remote" button to push your changes back to GitHub

Important note, all changes need to be in your remote GitHub repository, so I can grade them.

Important note, pushing your testing.py script to your remote GitHub is part of the 00_getting_started homework grade item.

