

# Basic class definition

class person:
    # Class attribute share all instance
    species = "HOMO SAPIENS"

    # constructor method

    def __init__(self,name,age):
        # Instance attributes
        self.name = name 
        self.age = age

    # Instance method
    def introduce (self):
        return f"Hi, I'm {self.name} adn I'm {self.age} years old."

    #  Method with parameters
    def have_birth (self):
        self.age += 1
        return f"Happy Bithday {self.name} is now {self.age}."


# Creating Objects (Instance)

person1 = person ("Lola", 25)
person2 = person ("Lala", 26)

# Accessing attributes
print (person1.name)
print  (person1.age)

# Calling attributes

print (person1.introduce ())
print (person1.have_birth ())

# Class attributes

print (person.species)
print (person1.species)

class BankAcoount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.transaction_history = []
    
    def deposit (self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append (f"Deposited # {amount}")
            return f"Deposited $ {amount}. New Balance: $ {self.balance}"
            
        else:
            return "Invalid Deposit Amount"
    
    def withdraw (self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append (f"withdrew $ {amount}")
            return f"Withdrew $ {amount}. New Balance: $ {self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds"

    
    def get_balance (self):
        return f"Current Balance: $ {self.balance}"
    
    def get_transaction_history (self):
        return self.transaction_history
    
# Using the BankAccount class

account = BankAcoount ("324343", "Lola", 3000)

print (account.deposit (500))
print (account.withdraw (200))
print (account.get_balance ())


