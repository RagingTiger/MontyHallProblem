# tl;dr
Simple tool written in **Python 3** to explore the
[Monty Hall Problem](https://en.wikipedia.org/wiki/Monty_Hall_problem) and its
solution.

## Installation
```
git clone https://github.com/RagingTiger/MontyHallProblem.git && cd MontyHallProblem
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Introduction
The version of the **Monty Hall Problem** presented here is the standard version
with the [standard assumptions](https://en.wikipedia.org/wiki/Monty_Hall_problem#Standard_assumptions):

+ **1** The host must always open doors not picked by the contestant.
+ **2** The host must always open doors that reveal goats and never the car.
+ **3** The host must always offer the chance to switch between the originally chosen door and the remaining closed door.

## Usage
The `command line interface` portion of this module uses the
[fire](https://github.com/google/python-fire.git) library, which generates the
below documentation by running `python montyhall.py` as follows:
```
$ python montyhall.py

NAME
    montyhall.py - A class with various methods for simulating the Monty Hall
                   problem.

SYNOPSIS
    montyhall.py COMMAND

DESCRIPTION
    A class with various methods for simulating the Monty Hall problem.

COMMANDS
    COMMAND is one of the following:

     experiment
       Run multiple games of Monty Hall problem

     lmad
       Interactive version of Monty Hall problem (i.e. Lets Make A Deal).

     predict
       Calculate the predicted probabilities of no switch vs. switch.

     simulate
       Non-interactive version of Monty Hall problem
```
To find out more about any of the `COMMANDS` shown above simply run the help
flag `--help` after the command. For example to learn about the `predict`
command:
```
$ python montyhall.py predict --help
NAME
    montyhall.py predict - Calculate the predicted probabilities of no switch vs. switch.

SYNOPSIS
    montyhall.py predict NDOORS

DESCRIPTION
    Calculate the predicted probabilities of no switch vs. switch.

POSITIONAL ARGUMENTS
    NDOORS
        The number of doors to use.

NOTES
    You can also use flags syntax for POSITIONAL ARGUMENTS
```
