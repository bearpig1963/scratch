import sys

def Anumber(someint):
    """

    :param someint:
    :return: v_text -- a text representation of base numbers 0-9
    """
    print('In Anumber with arg ', someint)

    v_val = int(someint)
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

    print( ' found ..:', v_text)


if __name__ == "__main__":
        Anumber(sys.argv[1])
