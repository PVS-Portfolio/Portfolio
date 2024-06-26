''' File: bruteforce.py
    A small class which explores the brute force solution method on the traveling salesman problem
    Primarily written by Dr. Jan Pearce of Berea College'''

#    number_routes method written by: TODO: ADD NAME(S) HERE


import random # possibly needed by main()
from inspect import getframeinfo, stack


def unittest(did_pass):
    """
    Print the result of a unit test.
    :param did_pass: a boolean representing the test
    :return: None
    """

    caller = getframeinfo(stack()[1][0])
    linenum = caller.lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

class BruteForce:
    """ The BruteForce class illustrates some computations related to the brute force solution method
    applied to the traveling salesman problem"""

    def __init__(self, n=3, rate = 0.00000000000000000033):
        '''Constructor instantiates an object containing the number of cities
        uses an optional parameter rate is the seconds needed by 1 computation
        whose default value is approximately the time it takes light to cross
        the width of the smallest atom 0.00000000000000000033 seconds
        Calls two helper methods'''
        self.n = int(n) # number of cities INCLUDING the starting and ending place (home)
        self.rate = float(rate)

        self.num_routes = -1 #set in number_routes() method
        self.totalseconds = -1 # in seconds set in get_times() method
        self.timelist = [] # [years, days, hours, minutes, seconds]

        self.number_routes()
        self.get_times()

    def number_routes(self):
        ''' Returns the number of possible routes assuming that home is one specific city'''
        count=1
        #TODO Complete this method

        # print(count) # for debugging
        return (count)

    def get_times(self):
        '''Returns the processing time in years needed to test all possible routes given self.rate
        as a list of [years, days, hours, minutes, seconds].'''

        self.totalseconds=float(self.num_routes)*float(self.rate)
        amountleft=self.totalseconds

        for timeunit in [365.242*24*60*60, 24*60*60, 60*60, 60]: # Computes years, days, hours, and minutes
            tempamount=amountleft
            amountleft=amountleft//timeunit # forces years, days, and minutes to be integer
            self.timelist.append(amountleft)
            amountleft=tempamount%timeunit

        self.timelist.append(amountleft) # Allows seconds to be fractional
        # print(self.timelist) # for debugging
        return (self.timelist)

def bruteforce_test_suite():
    '''The test_suite function utilizes the testit() function,
    and is designed to test the bruteforce'''
    epsilon=0.000000000001 # We use this to deal with floating point round-off error
    print("\nRunning bruteforce_test_suite()).")
    tsp1 = BruteForce(11, 0.05) # visit 11 cities using a widget speed
    unittest(tsp1.number_routes()== 3628800) # because 10! = 3628800
    unittest(tsp1.timelist==[0, 2, 2, 24.0, 0]) # This is [0 years, 2 days, 2 hours, 24 minutes, 0 seconds]

    tsp2 = BruteForce(7, 0.05) # visit 11 cities using a widget speed
    unittest(tsp2.number_routes()== 720) # because 10! = 3628800
    unittest(tsp2.timelist==[0, 0, 0, 0, 36.0]) # This is [0 years, 0 days, 0 hours, 0 minutes, 36 seconds]

    tsp3 = BruteForce(49, 0.00000000000000000033) # visit 49 cities using the time it takes light to cross the width of the smallest atom
    unittest(tsp3.number_routes()== 12413915592536072670862289047373375038521486354677760000000000)
    unittest(tsp3.timelist==[1.2981601498106503e+35, 311.0, 5.0, 15.0, 5.955653518438339])

    print("Run of bruteforce_test_suite() complete.")

def main():
    '''Program demonstrates use of the Brute force class'''

    num = int(input("Please enter the number of cities you wish to visit: "))
    rate = float(input('Please enter the rate of checking number of seconds per route: '))
    tsp = BruteForce(num, rate)         # Instantiate an object of type BruteForce
    print('With '+str(num)+' cities, there are '+str(tsp.num_routes)+' routes.')
    print('With a rate of '+str(rate)+' it will take '),
    print(tsp.timelist),
    print(' of [years, days, hours, minutes, seconds].')

    bruteforce_test_suite()

main()