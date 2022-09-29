class Dificulltfinder:

    def amstrong_finder(self):

        self.num = int(input("Enter a number: "))

        self.sum = 0

        self.temp = self.num
        while self.temp > 0:
            self.digit = self.temp % 10
            self.sum += self.digit ** 3
            self.temp //= 10

        if self.num == sum:
            print(self.num, "is an Armstrong number")
        else:
            print(self.num, "is not an Armstrong number")


    def primefind(self):
        self.start = int(input("enter a starting number to print prime numbers"))

        self.stop = int(input("enter a limit to stop "))

        self.num: int
        print("prime numbers between " + str(self.start), "and " + str(self.stop))
        for self.num in range(self.start, self.stop):
            if self.num > 1:
                for i in range(2, self.num):
                    if self.num % i == 0:
                        break
                else:
                    print(self.num)
        if self.stop <= 1:
            print("Nothing")
        if self.stop == self.start:
            print("Nothing")

    def primefinder_intervel(self):
        self.start = int(input("enter a starting number to print prime numbers"))

        self.stop = int(input("enter a limit to stop "))

        self.num: int
        print("prime numbers between " + str(self.start), "and " + str(self.stop))
        for self.num in range(self.start, self.stop):
            if self.num > 1:
                for i in range(2, self.num):
                    if self.num % i == 0:
                        break
                else:
                    print(self.num)
        if self.stop <= 1:
            print("Nothing")
        if self.stop == self.start:
            print("Nothing")


    def oddfinder(self):
        self.number = int(input("Enter a number"))

        if self.number % 2 == 0:
            print(str(self.number), " is an Even number\n")
        else:
            print(str(self.number), " is an Odd number")



    def factorial_finder(self):
        self.num = int(input("Enter a number: "))

        factorial = 1
        if self.num < 0:
            print("factorial not for negative numbers")
        elif self.num == 0:
            print("The factorial of 0 is 1")
        else:
            for i in range(1, self.num + 1):
                factorial = factorial * i
            print("The factorial of", self.num, "is", factorial)

    def multiplication_table(self):

        self.num = int(input("enter a number for multiplicatttion table"))
        self.limit = int(input("enter a how much limit for stop"))
        for i in range(1, self.limit + 1):
            print(self.num, 'x', i, '=', self.num * i)

    def arearectangle(self):

        self.l = int(input("Length of rectangle : "))
        self.w = int(input("Width of rectangle : "))
        self.area = self.l * self.w
        self.perimeter = 2 * (self.l + self.w)
        print("Area of Rectangle : ", self.area)
        print("Perimeter of Rectangle : ", self.perimeter)




class Mathematicoperators:

    def addition(self):
        self.x = int(input("Enter a number: "))
        self.y = int(input("Enter another number: "))
        self.z = self.x + self.y
        print("Result is :" + str(self.z))

    def substraction(self):
        self.x = int(input("Enter a number: "))
        self.y = int(input("Enter another number: "))
        self.z = self.x - self.y
        print("Result is :" + str(self.z))

    def multiplication(self):
        self.x = int(input("Enter a number: "))
        self.y = int(input("Enter another number: "))
        self.z = self.x * self.y
        print("Result is :" + str(self.z))

    def division(self):
        self.x = float(input("Enter a number: "))
        self.y = float(input("Enter another number: "))
        self.z = self.x / self.y
        self.b = float(self.z)
        print("Result is :" + str(self.b))



class Option(Dificulltfinder, Mathematicoperators):
    def option_function(self):
        print("Options:\n")
        self.a = int(input(
            ">>Enter 1 for Addition\n>>Enter 2 for subtraction\n>>Enter 3 for multiplication\n>>Enter 4 for Division\n>>Enter 5 for prime number finder\n"
            ">>Enter 6 for Odd,even number finder\n>>Enter 7 for print prime numbers\n>>Enter 8 for factorial finder"
            "\n>>Enter 9 for multtiplication table"
            "\n>>Enter 10 for Find area and Perimeter of rectangle"
            "\n>>Enter 11 for Armstrong checker\n\n >>>Enter a option: "))
        self.b = 1
        self.c = 2
        self.d = 3
        self.f = 4
        self.g = 5
        self.h = 6
        self.i = 7
        self.j = 8
        self.k = 9
        self.l = 10
        self.m = 11

        if self.a > 11 or self.a < 1:
            print("\nPlease enter a valid option !!\n\n")
            obj_option = Option
            obj_option.option_function(self)
        else:
            if self.a == self.b:
                obj_addition = Mathematicoperators
                obj_addition.addition(self)
            else:
                if self.a == self.c:
                    obj_subtraction = Mathematicoperators
                    obj_subtraction.substraction(self)
                else:

                    if self.a == self.d:
                        obj_multiplication = Mathematicoperators
                        obj_multiplication.multiplication(self)
                    else:

                        if self.a == self.f:
                            obj_division = Mathematicoperators
                            obj_division.division(self)
                        else:

                            if self.a == self.g:
                                obj_primefinder = Dificulltfinder
                                obj_primefinder.primefind(self)

                            else:
                                ()

                                if self.a == self.h:
                                    obj_oddfind = Dificulltfinder
                                    obj_oddfind.oddfinder(self)

                                else:
                                    ()

                                    if self.a == self.i:
                                        obj_primeprint = Dificulltfinder
                                        obj_primeprint.primefinder_intervel(self)
                                    else:
                                        ()

                                        if self.a == self.j:
                                            obj_factorial = Dificulltfinder
                                            obj_factorial.factorial_finder(self)
                                        else:
                                            ()

                                            if self.a == self.k:
                                                obj_multiplicationtable = Dificulltfinder
                                                obj_multiplicationtable.multiplication_table(self)
                                            else:
                                                ()

                                                if self.a == self.l:
                                                    obj_areafind = Dificulltfinder
                                                    obj_areafind.arearectangle(self)
                                                else:
                                                    ()

                                                    if self.a == self.m:
                                                        obj_amstrong = Dificulltfinder
                                                        obj_amstrong.amstrong_finder(self)
                                                    else:
                                                        ()





class Calculator(Option):
    def firstline(self):
        print("\n*********** Basic and Hard Mathematics calculator ***********\n")


obj = Calculator()
obj.firstline()
obj.option_function()











print("its a just basic mathemthics calculator")
print("Created by Ajju")

# *********************************************************************************************************#

