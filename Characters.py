class Character:
    def __init__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)

class Thief(Character):
    sneaky = True

    def __init__(self, name, sneaky=True, **kwargs):
        super().__init__(name, **kwargs)
        self.sneaky = sneaky

        for key, value in kwargs.items():
            setattr(self, key, value)

    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))

    def hide(slef, light_level):
        return self.sneaky and light_level < 10
