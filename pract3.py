import abc
import random


class AnimeMon(abc.ABC):

    def __init__(self) -> object:
        self._exp = 10

    @property
    @abc.abstractmethod
    def exp(self):
        return self._exp

    @classmethod
    @abc.abstractmethod
    def inc_exp(self, val: int):
        self._exp += val * 8


class BasePokemon:
    def __str__(self):
        return f'{self.name}/{self.poketype}'


class EmojiMixin:
    emogy = {'grass': '🌿', 'fire': '🔥', 'water': '🌊', 'electric': '⚡' }

    def __str__(self):
        text_poketype = super().__str__()
        return text_poketype.replace(self.poketype, self.emogy[self.poketype])


class Pokemon(EmojiMixin, AnimeMon, BasePokemon):
    def __init__(self, name: str, poketype: str) -> object:
        super().__init__()
        self.name = name
        self.poketype = poketype


class Digimon(AnimeMon):
    def __init__(self, name: str) -> object:
        super().__init__()
        self.name = name


def train(animemon: AnimeMon):
    step_size, level_size = 10, 100
    sparring_qty = (level_size - animemon.exp % level_size) // step_size
    for i in range(sparring_qty):
        win = random.choice([True, False])
        if win:
            animemon.inc_exp(step_size)


bulbasaur = Pokemon(name='Bulbasaur', poketype='water')
print(bulbasaur)
print(bulbasaur.exp)
train(bulbasaur)
print(bulbasaur.exp)

agumon = Digimon(name='Agumon')
print(agumon.exp)
train(agumon)
print(agumon.exp)