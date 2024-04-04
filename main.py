# Завдання 1
# Іноді ви можете використати property() для створення
# доступу до атрибутів через геттери та сеттери для
# забезпечення певних перевірок або операцій перед
# отриманням або зміною атрибутів. Створіть клас для
# роботи з банківським рахунком, щоб гроші знялися або
# зарахувалися тільки при виконанні певних умов
# (наприклад, якщо гроші на рахунку є).
class Bank_account:
    def __init__(self, balance=0):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        self._balance = amount

    def withdrawal(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f'З рахунку знято: - {amount} грн.\nЗалишок на рахунку: {self._balance} грн.')
        else:
            print('У вас не вистачає коштів на рахунку')

    def transfer(self, amount):
        self._balance += amount
        print(f'Зараховано : + {amount} грн.\nНа рахунку: {self._balance} грн.')


account = Bank_account(2500)
print(f'Початковий баланс: {account.balance}')
account.withdrawal(1000)
account.transfer(15000)
account.withdrawal(16600)


# Завдання 2
# Створіть клас температурного датчика, де обмежується
# температура в межах прийнятних для датчика значень, за
# допомогою property().
class TemperatureSensor:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if -100 <= value <= 100:
            self._temperature = value
        else:
            print(f'Температура є неприпустимою')


temperature_sensor = TemperatureSensor()

print(f'Початкова температура: {temperature_sensor.temperature}')

temperature_sensor.temperature = 10
print(f'Поточна температура: {temperature_sensor.temperature}')

temperature_sensor.temperature = 110
print(f'Поточна температура: {temperature_sensor.temperature}')


# Завдання 3
#  Завдання для функторів. Створіть клас TextModifier,
# який може здійснювати різні операції над текстом:
# • Операція перетворення тексту у верхній регістр.
# • Операція перетворення тексту у нижній регістр.
# • Операція видалення пробілів у тексті.
# • Операція шифрування тексту за допомогою зсуву
# вліво на задану кількість символів
class TextModifier:
    def __init__(self, text):
        self._text = text

    def __call__(self, operation, *args, **kwargs):
        if operation == "upper case":
            self._text = self._text.upper()
        elif operation == "lower case":
            self._text = self._text.lower()
        elif operation == "remove spaces":
            self._text = self._text.replace(" ", "")
        elif operation == "encryption":
            if args:
                shift = args[0]
                self._text = shift_left(self._text, shift)
            else:
                print("Для операції шифрування потрібно вказати зсув")
        else:
            print("Немає такої операції")

def shift_left(text, n=1):
    n = n % len(text)
    return text[n:] + text[:n]

text = "Hi, Python"
modifier = TextModifier(text)

modifier("upper case")
print(f"Текст у верхньому регістрі: {modifier._text}")

modifier("lower case")
print(f"Текст у нижньому регістрі: {modifier._text}")

modifier("remove spaces")
print(f"Текст без пробілів: {modifier._text}")

modifier("encryption", 3)
print(f"Зашифрований текст: {modifier._text}")


