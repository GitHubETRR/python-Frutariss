import os

maxLengthName = 30
maxLengthIllness = 40
upload = 1
display = 2
delete = 3
exit = 4
length = 28
roomLength = 12

class patient:
    def __init__(self, room, name, age, illness):
        self.room = room
        self.name = name
        self.age = age
        self.illness = illness
        self.next = None

class patientSystem:
    def __init__(self):
        self.zoneA = None
        self.archivePath = "Lista.txt"
        self.archive = open(self.archivePath, "a+")
        self.menu()
    
    def menu(self):
        while True:
            print("1. Cargar un nuevo paciente")
            print("2. Cargar a los pacientes en la lista")
            print("3. Borrar los datos de la lista")
            print("4. Salir")
            option = int(input("Ingrese una opción: "))
            if option == upload:
                self.uploadPatient()
            elif option == display:
                self.displayList()
            elif option == delete:
                self.delete()
            elif option == exit:
                self.freeMemory()
                self.archive.close()
                break

    def printPatient(self, patient):
        print(f"Habitación N° {patient.room}")
        print(f"Nombre: {patient.name}")
        print(f"Edad: {patient.age}")
        print(f"Enfermedad: {patient.illness}")
        print("------------------------------")

        self.archive.seek(0, os.SEEK_END)
        self.archive.write(f"Habitación #{patient.room}\n")
        self.archive.write(f"Nombre: {patient.name}\n")
        self.archive.write(f"Edad: {patient.age}\n")
        self.archive.write(f"Enfermedad: {patient.illness}\n")
        self.archive.write("------------------------------\n")
        self.archive.flush()

    def requestData(self):
        room = int(input("Ingrese la habitación del paciente: "))
        name = input("Ingrese el nombre del paciente: ")
        age = int(input("Ingrese la edad del paciente: "))
        illness = input("Ingrese la enfermedad del paciente: ")
        return patient(room, name, age, illness)

    def uploadPatient(self):
        patient = self.requestData()
        patient.next = self.zoneA
        self.zoneA = patient

    def displayList(self):
        list = self.zoneA
        while list:
            self.printPatient(list)
            list = list.next

    def delete(self):
        open(self.archivePath, "w").close()
        self.freeMemory()
        print("Todos los datos han sido borrados.")

    def freeMemory(self):
        while self.zoneA:
            aux = self.zoneA
            self.zoneA = self.zoneA.next
            del aux

patientSystem()