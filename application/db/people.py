from faker import Faker
from random import random
fake = Faker()


class Worker:
    def __init__(self, name, address, experience, since):
        self.name = name
        self.address = address
        self.experience = experience
        self.since = since

    def __str__(self):
        return f'{self.name} {self.address} {self.experience} {self.since}'


def get_employees():
    workers = []
    for i in range(10):
        worker = Worker(fake.name(), fake.address(),
                        random()*10, fake.date())
        print(worker)
        workers.append(worker)
