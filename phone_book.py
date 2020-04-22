

class PhoneBook:
    def __init__(self) -> None:
        self.users = []

    def show_users(self) -> list:
        return self.users

    def find_users_by_name(self, name: str) -> list:
        found_users = []
        for user in self.users:
            for user_name in user.names:
                if user_name.name.lower() == name.lower():
                    found_users.append(user)
                    break
        return found_users

    def find_users_by_surname(self, surname: str) -> list:
        found_users = []
        for user in self.users:
            if user.surname.surname.lower() == surname.lower():
                found_users.append(user)
        return found_users

    def find_users_by_phonenumber(self, phone_number: int) -> list:
        found_users = []
        for user in self.users:
            for phone in user.phone_numbers:
                if phone.phone_number == phone_number:
                    found_users.append(user)
                    break
        return found_users

    def create_user(self, names: list, surname: str, phone_numbers: list) -> object:

        for phone_number in phone_numbers:
            if self.find_users_by_phonenumber(phone_number):
                return None

        phone_numbers = [PhoneNumber(phone_number) for phone_number in phone_numbers]
        surname = Surname(surname)
        names = [UserName(name) for name in names]

        new_user = User(names=names, surname=surname, phone_numbers=phone_numbers)
        self.users.append(new_user)
        return new_user


class User:
    def __init__(self, names: list, surname: object, phone_numbers: list) -> None:
        self.names = names
        self.surname = surname
        self.phone_numbers = phone_numbers

    def __repr__(self):
        return f'Class User: {self.surname}, {self.names}, {self.phone_numbers}. '


class UserName:
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self):
        return f'UserName class {self.name}'


class Surname:
    def __init__(self, surname: str) -> None:
        self.surname = surname

    def __repr__(self):
        return f'Surname class {self.surname}'


class PhoneNumber:
    def __init__(self, phone_number: int) -> None:
        self.phone_number = phone_number

    def __repr__(self):
        return f'PhoneNumber class {self.phone_number}'


if __name__ == '__main__':
    phone_book = PhoneBook()
    test_users = [
        (['John'], 'Smith', [123454321]),
        (['Elsie'], 'Gagne', [123456789]),
        (['Rachel'], 'Galbreath', [987654321]),
        (['Cynthia'], 'Boyd', [123456789]),
        (['Jack'], 'Mitchell', [111111111, 222222222]),
        (['Ramona', 'Marie'], 'Henry', [333333333, 444444444]),
    ]

    for test_user in test_users:
        new_test_user = phone_book.create_user(names=test_user[0], surname=test_user[1], phone_numbers=test_user[2])
        if new_test_user is None:
            print(f'User with this phone number {test_user[2]} is already exist.')
        else:
            print(f'User {new_test_user.surname.surname} was successfully created.')

    print('Users was added to PhoneBook')

    for user in phone_book.users:
        print(user)

    print('Let find a user with a name Ramona')
    print(phone_book.find_users_by_name('ramona'))

    print('Let find a user with a phone number 333333333')
    print(phone_book.find_users_by_name('ramona'))

    print('Let find a user with a surname Mitchell')
    print(phone_book.find_users_by_surname('mitchell'))
