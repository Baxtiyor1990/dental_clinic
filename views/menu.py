
from models.patient import Patient
from models.appointment import Appointment
from models.dental_clinic import DentalClinic
from services.dental_service import DentalService
from utils.date_utils import parse_date

def print_menu():
    print("Меню:")
    print("1. Добавить пациента")
    print("2. Добавить врача")
    print("3. Записать на прием")
    print("4. Показать пациентов")
    print("5. Показать записи на прием")
    print("0. Выйти")

def add_patient(clinic):
    name = input("Введите имя пациента: ")
    age = int(input("Введите возраст пациента: "))
    clinic.open_patient_card(name, age)
    print("Пациент добавлен успешно.")

def add_doctor(clinic):
    name = input("Введите имя врача: ")
    clinic.add_doctor(name)
    print("Врач добавлен успешно.")

def schedule_appointment(clinic):
    patient_name = input("Введите имя пациента: ")
    doctor_name = input("Введите имя врача: ")
    date = input("Введите дату приема в формате ГГГГ-ММ-ДД: ")
    services = input("Введите список услуг через запятую: ").split(',')
    patient = clinic.find_patient(patient_name)
    if not patient:
        print("Пациент не найден.")
        return
    appointment = clinic.schedule_appointment(patient, doctor_name, parse_date(date), services)
    print("Прием записан успешно.")

def show_patients(clinic):
    print("Список пациентов:")
    clinic.view_patients()

def show_appointments(clinic):
    print("Записи на прием:")
    clinic.view_appointments()

def main():
    clinic = DentalClinic("Smile Clinic")

    while True:
        print_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            add_patient(clinic)
        elif choice == "2":
            add_doctor(clinic)
        elif choice == "3":
            schedule_appointment(clinic)
        elif choice == "4":
            show_patients(clinic)
        elif choice == "5":
            show_appointments(clinic)
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
