from animals import Animal, Dog, Bird, Fish, Cat


def main():
    dog = Dog("olive",4,"Woof","Bernaoodle")
    bird = Bird("levi",5,"tweet","robin")
    fish = Fish("lucas",2,"Blub","fresh water")
    cat = Cat("London",9,"meow","indoors")


    # Create one instance of each animal subclass
    animals = [dog,bird,fish,cat]

    # TODO: instantiate your animals and add them to the list

    # Loop over all animals and call speak(), move(), and describe()
    for animal in animals:
        print(animal.speak())
        print(animal.move())
        print(animal.age())
        


if __name__ == "__main__":
    main()
