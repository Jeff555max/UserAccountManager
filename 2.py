class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'
        self._users = []

    def add_user(self, user):
        if isinstance(user, User):
            self._users.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Ошибка добавления: объект не является экземпляром класса User.")

    def remove_user(self, user_id):
        for user in self._users:
            if user.get_user_id() == user_id:
                self._users.remove(user)
                print(f"Пользователь {user.get_name()} удален.")
                return
        print("Пользователь не найден.")

    def list_users(self):
        if self._users:
            print("Список пользователей:")
            for user in self._users:
                print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")
        else:
            print("Нет зарегистрированных пользователей.")

def main():
    admin = Admin("1", "Администратор")

    while True:
        print("\nВыберите действие:")
        print("1: Добавить пользователя")
        print("2: Удалить пользователя")
        print("3: Показать список пользователей")
        print("4: Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            user_id = input("Введите уникальный ID пользователя: ")
            name = input("Введите имя пользователя: ")
            access_level = input("Введите уровень доступа (user/admin): ").lower()

            if access_level == 'admin':
                new_user = Admin(user_id, name)
            else:
                new_user = User(user_id, name)

            admin.add_user(new_user)

        elif choice == "2":
            user_id = input("Введите ID пользователя для удаления: ")
            admin.remove_user(user_id)

        elif choice == "3":
            admin.list_users()

        elif choice == "4":
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()