#this program generates lists of n numbers, their binary equivalents, and the amount of trailing 1s

import sys

def get_number_binary(n):

    print '\n', "Range: [0 - ", n, ')'
    print "Base10", '\t', "Base2", '\t\t', "Ones Count", '\n'

    for x in range(n):

        #convert binary representation to string
        tmp_str = "{0:b}".format(x)
        onesCount = get_ones(tmp_str)
        print x, '\t', tmp_str, '\t\t', onesCount


def get_ones(str):

    count = 0

    #check string elements right to left, keep track of 1s in succession
    for i in range(1, len(str) + 1):
        if str[-i] == "0":
            return count
        else:
            count += 1

    return count



get_number_binary(int(raw_input('> ')))



