# задача
# Класс Книга должен содержать информацию о названии, авторе и жанре книги.

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def display(self):
        print(f"Название: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Жанр: {self.genre}")

book1 = Book('Мастер и маргарита', 'Михаил Булгаков', 'Роман')
book1.display()
print('--------------------------------------')
book2 = Book("1984", "Джордж Оруэлл", "Фантастика")
book2.display()

########################################################################################################################

# задача
# Класс БанковскийАккаунт должен хранить информацию о владельце, балансе

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def display(self):
        print(f"Владелец: {self.owner}")
        print(f"Баланс: {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance +- amount
            print(f'Средств пополнено в размере {amount} руб')
        else:
            print(f'сумма депозита должна быть больше 0')

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f'Снятых средств в размере {amount} руб')
        else:
            print(f'недостаточно средств')

print('--------------------------------------')
account1 = BankAccount("Иванов Иван", 1000)
account1.display()
print('--------------------------------------')
account1.deposit(500)
account1.display()
print('--------------------------------------')
account1.withdraw(200)
account1.display()
