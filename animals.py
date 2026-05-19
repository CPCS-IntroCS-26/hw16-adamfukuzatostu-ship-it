class Animal:
    def __init__(self, name, age, sound):
        self.__name = name
        self.__age = age
        self.__sound = sound  

    def set_name(self,name):
        self.__name = name
    def set_age(self,age):
        self.__age = age
    def set_sound(self,sound):
        self.__sound = sound

    def speak(self):
        print(f"{self.__namwe} says {self.__sound}")

    def move(self):
        print("Run")

    def describe(self):
        print({self.__name} {self.__age})

    def __str__(self):
        print({self.__name}, {self.__age}, {self.__sound})


class Dog(Animal):
    def __init__(self, name, age, breed):
        super.__init__(name,age)

    def set_breed(self,breed):
        self.__breed = breed

    def speak(self):
        print(f"{self.__namwe} says {self.__sound}")

    def move(self):
        print("Run")
        
    def breed(self):
        print({self.__breed})


class Bird(Animal):
    def __init__(self, name, age, can_fly):
        super.__init__(name,age)

    def set_can_fly(self,can_fly):
        self.__can_fly = can_fly

    def move(self):
        print("Run")

    def can_fly(self):
        print({self.__can_fly})


class Fish(Animal):
    def __init__(self, name, age, water_type):
        super.__init__(name,age)

    def set_water_type(self,water_type):
        self.__water_type = water_type

    def move(self):
        print("swim")

    def water_type(self):
        print({self.__water_type})


class Cat(Animal):
    def __init__(self, name, age, indoor):
        super.__init__(name,age)

    def set_indoor(self,indoor):
        self.__indoor = indoor 
    
    def speak(self):
        print("meow")

    def move(self):
        print("walk")

    def set_indoors(self):
        print({self.__indoor})
