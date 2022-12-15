class Persona: # Cuando yo creo una clase puedo hacer un print de 
    def __init__(self, name, surname, gender, age):
            self.name = name
            self.surname = surname
            self.gender = gender
            self.age = age
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
ps = Persona("Paquita", "Salas", "F", 25)
nm = Persona("Roberto", "Burgos", "M", 35)
n = ps.get_name() # n = "Paquita"
nm.set_name("Pedro") #Ahora se llama Pedro