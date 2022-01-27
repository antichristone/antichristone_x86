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
            self.request_service(random.choice(self.services))
        except Exception:
            pass

    def request_service(self, service):
        try:
            exec("self.number_attack."+service+"()")
        except Exception:
            pass
