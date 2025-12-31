from abc import ABC, abstractmethod

class Bank(ABC):
    def __init__(self, pin):
        self._pin = pin
        self._balance = 0
        self._history = []

    def authenticate(self, p):
        if p != self._pin:
            raise ValueError("Invalid PIN")

    @abstractmethod
    def withdraw(self, a):
        pass

    @abstractmethod
    def deposit(self, a):
        pass

    def check_balance(self):
        return self._balance

    def show_history(self):
        for h in self._history:
            print(h)

class SBI(Bank):
    def __init__(self, pin):
        super().__init__(pin)
        self._balance = 10000

    def withdraw(self, a):
        if a > self._balance:
            raise ValueError("Insufficient balance")
        self._balance -= a
        self._history.append(f"SBI Withdraw: {a}")

    def deposit(self, a):
        self._balance += a
        self._history.append(f"SBI Deposit: {a}")

class HDFC(Bank):
    def __init__(self, pin):
        super().__init__(pin)
        self._balance = 20000

    def withdraw(self, a):
        self._balance -= a
        self._history.append(f"HDFC Withdraw: {a}")

    def deposit(self, a):
        self._balance += a
        self._history.append(f"HDFC Deposit: {a}")


def atm(b):
    p = int(input("Enter PIN: "))
    try:
        b.authenticate(p)
    except ValueError as e:
        print(e)
        return

    while True:
        print("\n1.Balance 2.Withdraw 3.Deposit 4.History 5.Exit")
        c = int(input("Choice: "))

        try:
            if c == 1:
                print("Balance:", b.check_balance())
            elif c == 2:
                a = int(input("Amount: "))
                b.withdraw(a)
                print("Withdraw success")
            elif c == 3:
                a = int(input("Amount: "))
                b.deposit(a)
                print("Deposit success")
            elif c == 4:
                b.show_history()
            elif c == 5:
                break
            else:
                print("Invalid option")
        except ValueError as e:
            print(e)

            
print("1.SBI  2.HDFC")
c = int(input("Choose bank: "))

if c == 1:
    bank = SBI(1234)
elif c == 2:
    bank = HDFC(5678)
else:
    print("Invalid bank")
    exit()

atm(bank)
