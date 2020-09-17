class ReversedStr(str):
    def __new__(*args, **kwargs):
        self = str.__new__(*args, **kwargs) #create new instance of str
        self = self[::-1]
        return self
