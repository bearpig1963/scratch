import sys

def Anumber(someint: str):
    """

    :param someint:
    :return: v_text -- a text representation of base numbers 0-9
    """
    print('In Anumber with arg ', someint)

    v_interrogate = someint

# Here is a handy python trick ... the function object is not typed to string on input (can be in 3+
#   but is not here) ... so we can force our evaluation to consider it a string by using the
#   str() utility then evaluate string content for digit ...
#

    if str(v_interrogate).isdigit():
        v_val = someint
        v_text = '   '

        print(' v_val now assigned as', v_val)

        if v_val == 1:
            v_text = 'one'
        elif v_val == 2:
            v_text = 'two'
        elif v_val == 3:
            v_text = 'three'
        elif v_val == 4:
            v_text = 'four'
        elif v_val == 5:
            v_text = 'five'
        elif v_val == 6:
            v_text = 'six'
        elif v_val == 7:
            v_text = 'seven'
        elif v_val == 8:
            v_text = 'eight'
        elif v_val == 9:
            v_text = 'nine'
        elif v_val == 0:
            v_text = 'zero'
        else:
            v_text = 'undefined'

    else:

        v_val = someint.strip()
        v_text = '   '

        print(' v_val now assigned as', v_val)

        if v_val == 'one':
            v_text = 1
        elif v_val == 'two':
            v_text = 2
        elif v_val == 'three':
            v_text = 3
        elif v_val == 'four':
            v_text = 4
        elif v_val == 'five':
            v_text = 5
        elif v_val == 'six':
            v_text = 6
        elif v_val == 'seven':
            v_text = 7
        elif v_val == 'eight':
            v_text = 8
        elif v_val == 'nine':
            v_text = 9
        elif v_val == 'zero':
            v_text = 0
        else:
            v_text = 'undefined'

    print( ' found ..:', v_text)


if __name__ == "__main__":
        Anumber(sys.argv[1])
