def get_min(x, y):
    return x if x < y else y


def get_min_without_arguments():
    raise TypeError('misseargument')



def get_min_with_one_argument(x):

    return  x


def get_min_with_many_arguments(*args):


    return min(args)



def get_min_with_one_or_more_arguments(first, *args):
    return min((first, ) + args)


def get_min_bounded(*args, low, high):

    res = float('inf')
    for item in args:
        if res > item and low < item < high:
            res = item

    return  res


def make_min(*, low, high):
    """
        return inner function object which takes at last one argument
        and return smallest number amount it's arguments, but if the
        smallest number is lower than the 'low' which given as required
        argument the inner function has to return it.
    """

    def inner(first, *args):
        pass

    return inner
