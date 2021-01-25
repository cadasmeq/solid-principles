# Liskov Substitution: A child class of another class, might be used as the father class itself.
# Substitutción de Liskov: Toda clase que es hija de otra clase, debe poder usarse como si fuese el mismo padre.

# Bad
class Duck:
    def fly(self):
        pass
    
    def cuack(self):
        pass
    
    def swim(self):
        pass


class RuberDuck(Duck):
    def fly(self):
        raise Exception("Error")
    
    def cuack(self):
        print("Cuack")
    
    def swim(self):
        print("Swim")


# Correct
class Fly:
    def fly(self):
        print("fly")


class Swim:
    def swim(self):
        print("swim")


class Cuack:
    def cuack(self):
        print("Cuak")


class Duck(Fly, Swim, Cuack):
    pass


class RuberDuck(Swim, Cuack):
    pass

