import json


class ColorizeMixin():
    def __init__(self, color: str):
        color_dict = {
            'black': 30,
            'red': 31,
            'green': 32,
            'yellow': 33,
            'blue': 34,
            'purple': 35,
            'cyan': 36,
            'white': 37,

        }
        self.repr_color_code = color_dict[color]


class Advert(ColorizeMixin):
    repr_color_code = 32  # green

    def __init__(self, data: json) -> object:
        for key, value in data.items():
            if isinstance(value, dict):
                value = Advert(value)
            if key == 'price':
                self._price = value
            elif key == 'class':
                self.class_ = value
            else:
                setattr(self, key, value)

    @property
    def price(self):
        if hasattr(self, '_price'):
            if self._price < 0:
                raise ValueError('price must be >= 0')
            else:
                return self._price
        else:
            return 0

    def __repr__(self):
        return f'\033[1;{self.repr_color_code};40m {self.title} | {self.price} ₽  \n'


# lesson_str = """{
#     "title": "python",
#     "price": 5,
#     "location": {
#         "address": "город Москва, Лесная, 7",
#         "metro_stations": ["Белорусская"]
#         }
#     }"""

lesson_str = """{
    "title": "Вельш-корги",
    "price": 1000,
    "class": "dogs",
    "location": {
        "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
        }
    }"""

lesson = json.loads(lesson_str)
print(lesson)
lesson_ad = Advert(lesson)
print(lesson_ad.location.address)
print(lesson_ad.price)
print(lesson_ad.class_)
print(lesson_ad)
# print(lesson_ad.location.metro_stations)

# for key, value in lesson.items():
#     print(key, value)
