from faker import Faker
from random import randint
fake = Faker()


class Worker:
    def __init__(self, name, address, experience, since):
        self.name = name
        self.address = address
        self.experience = experience
        self.since = since

    def __str__(self):
        return f'{self.name:<20} {self.address:20} {self.experience:<3} {self.since:<10}'


def get_employees():
    workers = []
    for i in range(10):
        worker = Worker(fake.name(), fake.address(),
                        randint(1, 7)*3, fake.date())
        print(worker)
        workers.append(worker)
