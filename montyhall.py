#!/usr/bin/env python

"""
Description: Monty Hall Problem Simulator
References: https://en.wikipedia.org/wiki/Monty_Hall_problem
Usage:
    montyhall [-i] <ndoors>
    montyhall (-i)
"""

# libs
import sys
import random
import readline
import termcolor


# funcs
def ctxt(txt, color='yellow'):
    """Print out colored text to stdout."""
    return termcolor.colored(txt, color)

def warn(txt, exit=True):
    """Print exit message and exit."""
    if exit:
        sys.exit(ctxt(txt, color='red'))
    else:
        print(ctxt(txt, color='red'))


# classes
class MontyHall(object):
    """A class with various methods for simulating the Monty Hall problem."""
    def __init__(self, clargs):
        # startup readline
        readline.parse_and_bind("tab: complete")

        # store clargs
        self.clargs = clargs

        # get user prompt
        self.prompt = '> '

        # command dictionary
        self.commands = {
                         'run': self._run,
                         'help': self._print_help
                         }

    @staticmethod
    def simulate(ndoors):
        """Run Monty Hall simulations."""
        # calculate probabilities for not switching vs. switching
        no_switch = 1.0 / float(ndoors)
        switch = 1.0 - no_switch

        # return results dictionary
        return {'ndoors': ndoors, 'noswitch': no_switch, 'switch': switch}

    @staticmethod
    def print_results(results):
        """Print results from Monty Hall simulations to terminal."""
        # final operations on results
        ndoors = results['ndoors']
        switch_prob = results['switch'] * 100      # convert to percent
        noswitch_prob = results['noswitch'] * 100  # convert to percent

        # format output text with result values
        text_report = (
            'Monty Hall problem:         {0} doors\n'
            'Winning with switching:     {1:.2f}%\n'
            'Winning without switching:  {2:.2f}%'
        ).format(ndoors, switch_prob, noswitch_prob)

        # send to stdout (with color)
        print(ctxt(text_report))

    def interpreter(self):
        """Starts interactive session to store state of games."""
        while True:
            try:
                cmd = input(self.prompt)
                self._execute_cmd(cmd)
            except EOFError:
                warn('\nClosing interactive session')
            except KeyboardInterrupt:
                print('')

    def _parse_cmd(self, cmd):
        """Parse commands for interactive mode."""
        # first split
        return cmd.split()

    def _execute_cmd(self, command):
        """Execute commands passed in interactive mode."""
        # first parse
        cmd_list = self._parse_cmd(command)

        # now execute
        try:
            self.commands[cmd_list[0]](cmd_list)
        except KeyError:
            warn('Unknown command {0}'.format(cmd_list[0]), exit=False)

    def _run(self, cmd_list):
        """Setup simulation parameters and execute."""
        try:
            # see if ndoors present in command list from interpreter
            ndoors = int(cmd_list[1])

            # now update clargs
            self.clargs['<ndoors>'] = ndoors

        except IndexError:
            # if not in command list check state
            if self.clargs['<ndoors>']:
                ndoors = int(self.clargs['<ndoors>'])
            else:
                warn('Usage Error: Type \'help\' for more details', exit=False)
                return

        # execute simulation
        results = self.simulate(ndoors)

        # print out results
        self.print_results(results)

    def _print_help(self, args):
        """Prints help message during interactive session."""
        help_msg = ('run [<ndoors>]       Runs the simulation with inputs\n'
                    'help                 Prints this help message\n')

        # print help
        print(ctxt(help_msg, color='red'))


# executable only
if __name__ == '__main__':

    # libs
    from docopt import docopt

    # get args
    args = docopt(__doc__)

    # check interactive
    if args['-i']:
        # we need to store state
        game = MontyHall(args)

        # start interactive
        game.interpreter()

    else:
        try:
            # number of doors
            ndoors = int(args['<ndoors>'])

            # execute simulation
            results = MontyHall.simulate(ndoors)

            # print out results
            MontyHall.print_results(results)

        except ValueError:
            # must be int
            warn('ValueError: Number of doors must be an integer.')
