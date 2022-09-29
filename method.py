class Dad:
    __superPassword = "DadHaveOnlyAccess"  ## __ double underscore - private attribute
    _chilPass = "IfYouAreFirstInClass"  ## _ single underscore Protected from outside world but can be accessed by child
    passwordForAll = "Public"  ## public attribute
    __hobby = "IMyOwn"

    def __init__(self) -> None:

        print("Dad init")

    def __hobby(self):
        print(self.__hobby)

    def getAccountPass(self, hobby):
        if (hobby == self.__hobby()):
            return self.__superPassword

    def setAccountPass(self, oldPass, newPass):
        if (oldPass == self.__superPassword):
            self.__superPassword = newPass
        else:
            print("Enter valid old password")

    def bankAcccount(self):
        accountPass = input("Enter bank account")
        if (accountPass == self._chilPass):
            print("Account is malamal")
        else:
            print("Wrong password")


class Mom:
    def __init__(self) -> None:
        print("Mom init")

    def hobby(self):
        print("Cooking")

    def bankAcccount(self):
        print("Account is super malamal")


class Beta(Mom, Dad):  ## method order resolution, jo pahila base class hoga uska method call karo
    def __init__(self) -> None:
        print("Beta init")

    def hobby(self):  ## method overriding - requires inheritance, same method with diffrent class
        print("party, Insta, facebook")

    def khilone(self):  ## method overloading -
        print("cycle")

   # def khilone(self, a, h):  ## method overloading - same method in same class
        #print("Video Game")


### Python does not support method overloading
### if you want to have method overloading, you can use default parameter


objDad = Dad()
# print(objDad.__superPassword)   # we can not access private attribute outside class


obj = Beta()
# print(obj.__superPassword)

obj.bankAcccount()  ## Dad

obj.hobby()

obj.khilone()

# obj._chilPass = "OnlyMineMoney"

# objDad = Dad()

# objMom = Mom()

# obj
