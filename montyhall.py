#!/usr/bin/env python

# libs
import random

# classes
class MontyHall(object):
    """A class with various methods for simulating the Monty Hall problem."""

    def lmad(self):
        """Interactive version of Monty Hall problem (i.e. Lets Make A Deal)."""
        # start game
        print('Let\'s Make A Deal')

        try:
            # how many doors
            ndoors = int(input('How many doors: '))

            # which door would you like
            first_choice = int(input('Choose one door out of {}: '.format(ndoors)))

            # now the host calculates
            results = self.simulate(ndoors, first_choice)

            # would you like to switch
            switch = input('Would you like to switch doors [y/n]: ')

            # converst switch to true/false
            switch = True if switch in {'y', 'Y', 'yes', 'Yes', 'YES'} else False

            # check switch
            final_choice = results['second_choice'] if switch else first_choice

            # prepare results
            results['final_choice'] = final_choice

            # return results
            return results

        except EOFError or KeyboardInterrupt:
            # do nothing but end silently
            pass

    @staticmethod
    def predict(ndoors):
        """Calculate the predicted probabilities of no switch vs. switch.

        Args:
            ndoors (int): The number of doors to use.

        Returns:
            ndoors (int): The number of doors used.
            noswitch (float): Probability of winning if players does not switch.
            switch (float): Probability of winning if player switches.
        """

        # calculate probabilities
        no_switch = 1.0 / float(ndoors)
        switch = 1.0 - no_switch

        # return results dictionary
        return {
            'ndoors': ndoors,
            'noswitch': no_switch,
            'switch': switch
        }

    @staticmethod
    def simulate(ndoors, first_choice):
        """Non-interactive version of Monty Hall problem.

        Args:
           ndoors (int): The number of doors to use.
           first_choice (int): The first door the player chooses.

        Returns:
           first_choice (int): The first door the player chooses.
           second_choice (int): The second door the player can switch to.
           car (int): The door hiding the car.
        """
        # get random number in range of ndoors (representing the car to be won)
        car = random.randint(1, ndoors)

        # get second_choice (i.e. 2nd door to choose from)
        if first_choice != car:
            second_choice = car
        else:
            while True:
                second_choice = random.randint(1, ndoors)
                if second_choice != car:
                    break

        # return results
        return {
            'first_choice': first_choice,
            'second_choice': second_choice,
            'car': car
        }

    def experiment(self, ndoors, first_choice, ngames):
        """Run multiple games of Monty Hall problem.

        Args:
           ndoors (int): The number of doors to use.
           first_choice (int): The first door the player chooses.
           ngames (int): The number of games to run.

        Returns:
           noswitch (float): Experimental percent of winning without switching.
           switch (float): Experimental percent of winning with switching.
        """
        # setup initial values
        switch, noswitch = 0, 0

        # setup loop
        for _ in range(ngames):
            # get results of game
            game = self.simulate(ndoors, first_choice)

            # update statistics
            if game['first_choice'] == game['car']:
                noswitch += 1.0
            else:
                switch += 1.0

        # calculate results
        return {
            'noswitch': noswitch / (switch + noswitch),
            'switch': switch / (switch + noswitch)
        }


# executable only
if __name__ == '__main__':

    # libs
    import fire

    # bang bang
    fire.Fire(MontyHall)
