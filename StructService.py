from StructPacket import Service
from config import services
import random, time

class Distribution_Service():
    def __init__(self):
        self.number_attack = Service()
        self.services = services

    def phone(self, phone):
        self.number_attack.number(phone)

    def random_service(self):
        try:
            exec(f"self.number_attack.{random.choice(self.services)}()")
        except Exception:
            pass
