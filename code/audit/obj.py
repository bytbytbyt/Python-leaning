# everything in pythin is an obiject
# print(type(1))
# print(type([]))
# print(type(()))
# print(type({}))

# my first python class

class Dog:
    species = "mammul"
    def __init__(self,breed):
        self.breed = breed
        pass
sam = Dog(breed = "Lab")
luna = Dog(breed = "Huskie")

print(sam.species)
print(sam.breed)


