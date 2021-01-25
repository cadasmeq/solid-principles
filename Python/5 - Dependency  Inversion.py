# Dependency Inversion: 
# Inversion de la Dependencia: Los modulos de alto nivel, no deben dependen de modulos de bajo nivel, ambos deben depender de interfaces.



class Repository:
    def get_data(self):
        data = MongoDB.find()
        return data


class Controller:
    data = Repository.get_data()
    do_something(data)


class Repository:
    def get_data(self):
        data = SQLite.query('SELECT * FROM data')
        return data


class Controller:
    data = Repository.data()
    do_something(data)