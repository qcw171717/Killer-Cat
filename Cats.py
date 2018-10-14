import random


class Cat:
    """
    Mew.
    """
    cats = []

    def __init__(self, name):
        self.name = name
        self.type = ["Normal", "Huge", "Little"][random.randint(0, 2)] + \
            [" Ocicat", " British Shorthair", " Siamese", " American Shorthair",
             " Russian Blue", " Abyssinian", " Maine Coon"][random.randint(0, 6)]
        self.size = 0
        self.reproduced = False
        self.special = ""
        self.sounds = ["Meow?", "Meow...", "Meow!", "Huffff(sleeping)"]
        if random.randint(0, 4) == 3:
            self.specialize()
        self.cats.append(self)

    def specialize(self):
        self.special = ["Dog-liked ", "Robotic ", "Alien "][random.randint(0, 2)]
        if self.special == "Dog-liked":
            self.sounds = ["Bark!", "Fwip fwip fwip...", "Arf!", "Arf?", "zzZZZ..."]
        elif self.special == "Robotic":
            self.sounds = ["Bip--MEW", "ME--OW", "This is not a Turing Test right?",
                           "BOOM!", "(Charging)", "Instruction required"]
        else:
            self.sounds = ["Books are the stepping stones to human progress--no, cat progress.",
                           "I am not your pet.", "Buy me a cat teaser for researching purpose.",
                           "We will rule the earth.", "Huffff(sleeping)", "What?"]

    def __repr__(self):
        return self.name + " is a " + str(self.size) + " size " + self.special + self.type +\
              ". " + self.name + ": " + self.sounds[random.randint(0, len(self.sounds) - 1)]

    def sound(self):
        print(self.name + ": " + self.sounds[random.randint(0, len(self.sounds) - 1)])

    def grow(self):
        if "Huge" in self.type:
            self.size += 2
        elif "Little" in self.type:
            self.size += 0.5
        else:
            self.size += 1

    def exhibition(self):
        for i in self.cats:
            print(i)


if __name__ == "__main__":
    a = Cat("Beta")
    b = Cat("Lambda")
    c = Cat("Alpha")
    print(c)
    c.sound()
    a.sound()
    b.sound()
    print(c.exhibition())
