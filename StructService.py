from StructPacket import Service
from config import services
import random

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
            if service == 'wwwdnsshopru_two':
                self.number_attack.wwwdnsshopru_two()
            elif service == 'dns_shop':
                self.number_attack.dns_shop()
        except Exception:
            pass
