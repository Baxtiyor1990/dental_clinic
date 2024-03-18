
class Patient:
    def __init__(self, name, age, medical_history=None):
        self.name = name
        self.age = age
        self.medical_history = medical_history if medical_history else []

    def add_medical_history(self, entry):
        self.medical_history.append(entry)

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Medical History: {', '.join(self.medical_history)}"
