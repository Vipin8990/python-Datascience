class cat:
    name = ""
    age = 0
    fur_color = ""
    breed = ""

    def eat(self):
        print("Cat is eating!")

    def sleep(self):
        print("Cat is sleeping!")

# creating objects 
tom = cat()
snow = cat()
tom.name = "Tom"
tom.age = 3
tom.fur_color = 'gray'
tom.breed = 'City Cat'
snow.name = 'Snowbell'
snow.age = 5
snow.fur_color = 'white'
snow.breed = 'persain'

# calling method
tom.eat()
snow.sleep()
tom.sleep()


# displaying attributes
print(tom.name, tom.age, tom.fur_color, tom.breed)
print(snow.age, snow.breed, snow.name, snow.fur_color)


