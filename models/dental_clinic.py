
from .appointment import Appointment
from models.patient import Patient

class DentalClinic:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.appointments = []
        self.doctors = []

    def add_doctor(self, doctor_name):
        self.doctors.append(doctor_name)

    def add_patient(self, patient):
        self.patients.append(patient)

    def open_patient_card(self, name, age):
        new_patient = Patient(name, age)
        self.add_patient(new_patient)
        return new_patient

    def schedule_appointment(self, patient, doctor, date, services):
        appointment = Appointment(patient, doctor, date, services)
        self.appointments.append(appointment)
        return appointment

    def view_appointments(self):
        for appointment in self.appointments:
            print(appointment)

    def view_patients(self):
        for patient in self.patients:
            print(patient)

    def find_patient(self, name):
        for patient in self.patients:
            if patient.name == name:
                return patient
        return None
