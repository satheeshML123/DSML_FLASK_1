from square import get_square

def test_get_square():
    a = 4
    results = get_square(a)
    assert results==16
    '''#if results ==16:
        #return True
    #else:
        #return False'''

if __name__ == '__main__':
    print(test_get_square())