'''
typechecks.py
'''
def check(variable, *type_list):
    '''
    Raises an exception if vrong type

    Parameters
    ----------
    variable : any
        Variable to check
    *type_list : list<types | None>
        Accepted types
    '''
    if variable is None and None in type_list:
        return
    if type(variable) not in type_list:
        raise TypeError('Wrong type')
