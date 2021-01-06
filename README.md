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
```
montyhall [-i] <ndoors>
montyhall (-i)
```

## Example
### Basic: Instance Mode
Running a single instance with **3 doors**:
```
$ python montyhall.py 3
Monty Hall problem:         3 doors
Winning with switching:     66.67%
Winning without switching:  33.33%
```
Running a single instance with **10 doors**:
```
$ python montyhall.py 10
Monty Hall problem:         10 doors
Winning with switching:     90.00%
Winning without switching:  10.00%
```
Running a single instance with **100 doors**:
```
python montyhall.py 100
Monty Hall problem:         100 doors
Winning with switching:     99.00%
Winning without switching:  1.00%
```

### Advanced: Interactive Mode
Whereas the basic usage is only single instances with no saved state, the
advanced usage drops into an interactive interpreter that saves state between
games. For example:
```
$ python montyhall.py -i 3
> run
Monty Hall problem:         3 doors
Winning with switching:     66.67%
Winning without switching:  33.33%
> run 10
Monty Hall problem:         10 doors
Winning with switching:     90.00%
Winning without switching:  10.00%
```
The user can choose to not pass an argument if using the `-i` option:
```
$ python montyhall.py -i
> run 100
Monty Hall problem:         100 doors
Winning with switching:     99.00%
Winning without switching:  1.00%
> run 1000
Monty Hall problem:         1000 doors
Winning with switching:     99.90%
Winning without switching:  0.10%
```
In the above example you can see we are increasing the number of doors using
the **interactive** command `run`, but there are a few other commands we can
use while in the **interpreter**:
```
> help
run [<ndoors>]       Runs the simulation with inputs
help                 Prints this help message
```
While the `help` command should be self-explanatory, the other commands could
benefit from some clarification:

+ The `run` command can **optionally** except an argument (e.g. the number of
  doors to play
  [Lets Make A Deal](https://en.wikipedia.org/wiki/Monty_Hall_problem#The_paradox)).
  Without an argument it will repeat the same
  simulations with the previous argument values given for `<ndoors>`.
