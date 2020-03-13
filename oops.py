# Importatnt terms
# class -> Tell Python to make a new type of thing.
# object -> Two meanings: the most basic type of thing, and any instance of some thing.
# instance -> What you get when you tell Python to create a class.
# def -> How you define a function inside a class.
# self -> Inside the functions in a class, self is a variable for the instance/object being accessed.
# inheritance -> The concept that one class can inherit traits from another class, much like you and
#                your parents.
# composition -> The concept that a class can be composed of other classes as parts, much like how
#                a car has wheels.
# attribute -> A property classes have that are from composition and are usually variables.
# is-a -> A phrase to say that something inherits from another, as in a “salmon” is-a “fish.”
# has-a -> A phrase to say that something is composed of other things or has a trait, as in “a salmon
#          has-a mouth.”

# Important phrases
# class X(Y) -> “Make a class named X that is-a Y.”
# class X(object): def __init__(self, J) -> “class X has-a __init__ that takes self and J parameters.”
# class X(object): def M(self, J) -> “class X has-a function named M that takes self and J parameters.”
# foo = X() -> “Set foo to an instance of class X.”
# foo.M(J) -> “From foo, get the M function, and call it with parameters self, J.”
# foo.K = Q -> “From foo, get the K attribute, and set it to Q.”


class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

# Inheritance : Inheritance is used to indicate that one class will get most or all of its features from a parent class.
# There are three ways that the parent and child classes
# can interact:
# 1. Actions on the child imply an action on the parent.
# 2. Actions on the child override the action on the parent.
# 3. Actions on the child alter the action on the parent.

# Implicit inheritance
class Parent():

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()  # Notice how even though I’m calling son.implicit() on line 13 and 
                # even though Child does not have an implicit function defined, it 
                # still works, and it calls the one defined in Parent. This shows you that
                # if you put functions in a base class (i.e., Parent), then all subclasses 
                # (i.e., Child) will automatically get those features. 
                # Very handy for repetitive code you need in many classes.

# Override Explicitly
class Parent():

    def override(self):
        print("PARENT override()")

class Child(Parent):
    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()

dad.override() #  when line 14 runs, it runs the Parent.override function because that variable (dad) is a Parent.
son.override() #  But when line 15 runs, it prints out the Child.override messages because son is an
               # instance of Child and Child overrides that function by defining its own version.

# Alter
class Parent():
    def altered(self):
        print("PARENT altered()")

class Child(Parent):
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered() # 
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()

# TODO: super() && Method Resolution Order(MRO)

# Composition
class Other():

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Child():

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son = Child()
son.implicit()
son.override()
son.altered()
