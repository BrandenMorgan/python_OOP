class Protected: # call dir(instance) to reveal private members
    __name = 'Security' # name mangling. starts with dunder but does not end with it

    def __method(self):
        return self.__name
# prot._Protected__method() for full access
