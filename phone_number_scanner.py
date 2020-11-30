import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from tabulate import tabulate


def number_scan(phone_number):
    number = phonenumbers.parse(phone_number)
    description = geocoder.description_for_number(number, "en")
    supplier = carrier.name_for_number(number, "en")
    info = [["Country_of_Origin", "Network_Provider"],
            [description,supplier]]
    data = str(tabulate(info,headers="firstrow",tablefmt="github"))
    return data

if __name__ == "__main__":
    number = input("Enter your phone number: ")
    print(number_scan(number))