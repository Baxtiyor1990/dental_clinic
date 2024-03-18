from services.dental_service import DentalService
class Appointment:
    def __init__(self, patient, doctor, date, services):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.services = services

    def calculate_cost(self):
        total_cost = sum(service.cost for service in self.services)
        return total_cost

    def __str__(self):
        if all(isinstance(service, str) for service in self.services):
            services_str = ", ".join(self.services)
        else:
            services_str = ", ".join(service.name for service in self.services)
        return f"Patient: {self.patient.name}, Doctor: {self.doctor}, Date: {self.date}, Services: {services_str}"
