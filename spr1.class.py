class Phonebook:
    def __init__(self, filename='book.txt'):
        self.filename = filename
        self.phonebook = self.read_phonebook()

    def read_phonebook(self):
        phonebook = {}
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    name, phone_number = line.strip().split('; ')
                    phonebook[phone_number] = name
        except FileNotFoundError:
            pass
        return phonebook

    def save_phonebook(self):
        with open(self.filename, 'w') as file:
            for phone_number, name in self.phonebook.items():
                file.write(f"{name}; {phone_number}\n")
        print("Phonebook saved.")

    def display_phonebook(self):
        for phone_number, name in self.phonebook.items():
            print(f"{name}: {phone_number}")

    def validate_number(self, phone_number):
        return len(phone_number) == 9 and phone_number.isdigit()

    def add_entry(self, name, phone_number):
        if not self.validate_number(phone_number):
            print("Invalid phone number.")
            return
        if phone_number in self.phonebook:
            print("Phone number already exists.")
            return
        self.phonebook[phone_number] = name
        self.save_phonebook()
        print("Phone number added.")

    def remove_entry(self, phone_number):
        if phone_number in self.phonebook:
            del self.phonebook[phone_number]
            self.save_phonebook()
            print("Phone number removed.")
        else:
            print("Phone number not found.")

    def modify_entry(self, old_phone_number, new_name, new_phone_number):
        if old_phone_number not in self.phonebook:
            print("Old phone number not found.")
            return False
        if not self.validate_number(new_phone_number):
            print("Invalid new phone number.")
            return False
        del self.phonebook[old_phone_number]
        self.phonebook[new_phone_number] = new_name
        self.save_phonebook()
        print("Phonebook entry modified.")
        return True

# Użycie klasy
phonebook = Phonebook()
phonebook.add_entry("Krzysztof", "123456789")
phonebook.display_phonebook()
phonebook.modify_entry("123456789", "Ania", "000000000")
phonebook.remove_entry("123456789")
phonebook.display_phonebook()