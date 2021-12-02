

class Dummy():

    def do_nothing(self):
        return True

    def do_nothing_false(self):
        return False

    def too_many_switches(self):
        if (1 == 1):
            a = "a"
        elif (2 == 2):
            b = "b"
        elif (3 == 4):
            c = "c"
        elif (a == b):
            d = "nicht möglich"
        elif (a == c):
            d = "auch nicht möglich"
        elif (1 == 1):
            d = "weiss nix mehr"
        return d
