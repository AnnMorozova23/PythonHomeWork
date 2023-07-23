import csv

from pydantic import (BaseModel, Field)
from pydantic.types import Decimal
from abc import ABC, abstractmethod
from csv import (reader, DictReader, writer, DictWriter)


class Pydentic(BaseModel):
    title: str = Field(max_length=128)
    description: str = Field(max_length=4096)
    price: Decimal = Field(max_digits=8, decimal_places=2)
    count: int = Field(ge=0)


cofee = Pydentic(
    title="Cappuccino",
    description="Good cappuccino",
    price=105.5,
    count=5
)
book = Pydentic(
    title="Gore bez uma",
    description="Good book",
    price=10,
    count=1
)
note = Pydentic(
    title="Like",
    description="Good like",
    price=15,
    count=100
)
data = [cofee, book, note]


class SomeAbstract(ABC):
    schema: Pydentic

    @classmethod
    def parse(cls, file, delimiter) -> list[Pydentic]:
        pass

    @classmethod
    def dump(cls, pydentic: list[Pydentic], delimiter, file):
        pass


class Work(SomeAbstract):
    schema = Pydentic

    @classmethod
    def parse(cls, file="file1.csv", delimiter=';') -> list[Pydentic]:
        objects = []
        with open(file, 'r', encoding='utf-8') as file:
            r = csv.reader(file, delimiter=delimiter)
            for line in r:
                try:
                    objects.append(cls.schema.parse_obj({
                        'title': line[0],
                        'description': line[1],
                        'price': Decimal(line[2]),
                        'count': int(line[3])
                    }))
                except TypeError:
                    pass
        return objects

    @classmethod
    def dump(cls, pydentic: list[Pydentic], delimiter=',', file="file2.csv"):
        with open(file, 'w', encoding='utf-8') as file:
            w = writer(file, delimiter=delimiter)
            w.writerow(['title', 'description', 'price', 'count'])
            for item in pydentic:
                if not isinstance(item, cls.schema):
                    raise TypeError("Error")
                w.writerow([item.title, item.description, str(item.price), str(item.count)])


test = Work.parse('file1.csv', ';')
print(test)

test1 = Work.dump(data, ',', 'file2.csv')
