#!/usr/bin/env

"""
    Functions for indexing the english alphabet consisting of 26 letters.

    example usage:
        # letter to index
        print( alphabet('a') )
        >> 0

        # index to letter
        print( alphabet(25, return_lower=False) )
        >> 'Z'

        # letter to index basic
        print(letter2index('a'))
        >> 0

        # index to letter basic
        print( index2letter(25) )
        >> 'z'
"""

__filename__ = "alphabet.py"
__author__ = "L.J. Brown"

def letter2index(letter):
    """ returns index of character in english alphabet (a -> 0, b -> 1, ..., z-> 25)  """
    return ord(letter.lower()) - 97

def index2letter(index, return_lower=True):
    """ returns character located at specified index in english alphabet (0 -> a, 1 -> b, ..., 25-> z)  """
    if return_lower:
        return chr(index + 97).lower()
    return chr(index + 97).upper()
    
def alphabet(arg, return_lower=True):
    """
        Indexing the english alphabet consisting of 26 letters. 

        Note: zero indexed
        
            example usage:
            
                alphabet('a')
                >> 0
                
                alphabet(25, return_lower=False)
                >> 'Z'
        
        :param arg: Either type int or type chr specifying the \
                        index of desired letter or ther letter at \
                        the desired index respectivley.
        :param return_lower: If index is passes, returns letter \
                             with corresponding case. Default is \
                             set to True (lower case returned). 
        :returns: integer representing index of passed character \
                        or character at passed index.
    """

    arg = str(arg)
    assert arg.isdigit() or arg.isalpha()

    if arg.isdigit():
        if return_lower:
            return chr(int(arg) + 97).lower()  
        return chr(int(arg) + 97).upper()

    return ord(arg.lower()) - 97

if __name__ == '__main__':

    #
    # example usage
    #

    # letter to index
    print( alphabet('a') )

    # index to letter
    print( alphabet(25, return_lower=False) )

    # index to letter basic
    print( index2letter(25) )

    # letter to index basic
    print(letter2index('a'))

