import random


class BasePokemon:
    def __str__(self):
        return f'{self.name}/{self.poketype}'


class EmojiMixin:
    emogy = {'grass': '🌿', 'fire': '🔥', 'water': '🌊', 'electric': '⚡' }

    def __str__(self):
        text_poketype = super().__str__()
        return text_poketype.replace(self.poketype, self.emogy[self.poketype])


class Pokemon(EmojiMixin, BasePokemon):
    def __init__(self, name: str, poketype: str) -> object:
        self.name = name
        self.poketype = poketype
        self._exp = 10

    @property
    def exp(self):
        return self._exp

    def inc_exp(self, n: int):
        self._exp += n


def train(pokemon: Pokemon):
    step_size, level_size = 10, 100
    sparring_qty = (level_size - pokemon.exp % level_size) // step_size
    for i in range(sparring_qty):
        win = random.choice([True, False])
        if win:
            pokemon.inc_exp(step_size)


bulbasaur = Pokemon(name='Bulbasaur', poketype='water')
print(bulbasaur)
print(bulbasaur.exp)
train(bulbasaur)
print(bulbasaur.exp)
