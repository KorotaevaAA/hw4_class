import random


class Digimon():
    def __init__(self, name: str) -> object:
        self.name = name
        # self.poketype = poketype
        self._exp = 10

    @property
    def exp(self):
        return self._exp

    def inc_exp(self, n: int):
        self._exp += n * 8


def train(digimon: Digimon):
    step_size, level_size = 10, 100
    sparring_qty = (level_size - digimon.exp % level_size) // step_size
    for i in range(sparring_qty):
        win = random.choice([True, False])
        if win:
            digimon.inc_exp(step_size)


agumon = Digimon(name='Agumon')
print(agumon.exp)
train(agumon)
print(agumon.exp)