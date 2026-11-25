import asyncio
from data import *
from queries import *

data_headers={"X-Requested-With": "XMLHttpRequest",
"Connection": "keep-alive",
"Pragma": "no-cache",
"Cache-Control": "no-cache",
"Accept-Encoding": "gzip, deflate, br",
'User-Agent':user_agent(), 'DNT':'1'}

def phone_mask(phone, maska):
    str_list = list(phone)
    for xxx in   x:
        maska=maska.replace("#", xxx, 1)
    return maska

class Service():
    def __init__(self):
        self.start = True


    def number(self, number_phone):
        self.phone = number_phone
        if self.phone[0] == '+':
            self.phone_not_pluse = str(number_phone[1:])
            self.phone_mask = str(phone_mask(phone=self.phone_not_pluse, maska="+# (###) ###-##-##"))

            if self.phone[1] == '3':
                self.country_code = '380'

            elif self.phone[1] == '7':
                self.country_code = '7'

            elif self.phone[1] == '8':
                self.country_code = '7'

            elif self.phone[1] == '9':
                self.country_code = '998'

            else:
                self.country_code = str(self.phone[1])+str(self.phone[2])

        elif isinstance(int(self.phone), int):
            self.phone_not_pluse = str(number_phone)
            self.phone_mask = str(phone_mask(phone=number_phone, maska="+# (###) ###-##-##"))

            if self.phone[0] == '3':
                self.country_code = '380'

            elif self.phone[0] == '7':
                self.country_code = '7'

            elif self.phone[1] == '8':
                self.country_code = '7'

            elif self.phone[0] == '9':
                self.country_code = '998'

            else:
                self.country_code = str(self.phone[0])+str(self.phone[1])
            self.phone = '+'+str(number_phone)


    def dns_shop(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://www.dns-shop.ru/order/order-single-page/check-and-initiate-phone-confirmation/",
            params={"phone": self.phone, "is_repeat": 0, "order_guid": 1},headers=headers_copy))


    def wwwdnsshopru_two(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://www.dns-shop.ru/auth/auth/fast-authorization/', headers=headers_copy, data={'FastAuthorizationLoginLoadForm[login]': self.phone_not_pluse, 'FastAuthorizationLoginLoadForm[token]': ''}))
