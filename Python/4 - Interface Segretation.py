# Interface Segregation: No client should be forced to depend on methods it doesnt use.
# Segregación de la Interfaz: Ningun cliente debe ser forzado a depender de los metodos que no usan.


# Bad
class Bird:
    def swim(self):
        pass

    def fly(self):
        pass


class Pinguin(Bird):
    def swim(self):
        print("swim")

    def fly(self):
        print("fly")
    

class Parrot(Bird):
    def swim(self):
        raise Exception("Error")

    def fly(self):
        print("fly")


# Correct
class SmallBird:
    pass


class MediumBird:
    pass


class Swim:
    def swim(self):
        pass

class Fly:
    def fly(self):
        pass


class Pinguin(Swim, MediumBird):
    def swim(self):
        print("swim")


class Parrow(Fly, SmallBird):
    def fly(self):
        print("fly") 