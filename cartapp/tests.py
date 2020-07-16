from django.test import TestCase

from .views import re_email


class IndexTests(TestCase):

    def test_blank_cartlist(self):
        r = self.client.get('/index/')
        self.assertEqual(r.context['cartnum'], 0)


class CartOrderTests(TestCase):

    def test_error_mail(self):
        customer = dict()
        customer['CustomerName'] = 'tester'
        customer['CustomerPhone'] = '0800000000'
        customer['CustomerAddress'] = '台中市西屯區文華路100號'
        customer['paytype'] = 'ATM 轉帳'

        customer['CustomerEmail'] = 'tester@mail.fcu.edu.tw'
        r = self.client.post('/cartok/', customer)
        self.assertEqual(r.status_code, 200)

        customer['CustomerEmail'] = 'tester#mail.fcu.edu.tw'
        r = self.client.post('/cartok/', customer)
        self.assertEqual(r.status_code, 302)
        self.assertEqual(r.url, '/cartorder/')

    def test_blank_field(self):
        customer = dict()
        customer['CustomerName'] = 'tester'
        customer['CustomerPhone'] = '0800000000'
        customer['CustomerAddress'] = '台中市西屯區文華路100號'
        customer['CustomerEmail'] = 'tester@mail.fcu.edu.tw'

        for key, value in customer.items():
            customer1 = customer.copy()
            customer1[key] = ''
            r = self.client.post('/cartok/', customer1)
            self.assertEqual(r.status_code, 302)
            self.assertEqual(r.url, '/cartorder/')


class UtilFuncTests(TestCase):

    def test_re_email_true(self):
        self.assertIs(re_email('a123456789@gmail.com'), True)
        self.assertIs(re_email('jjieli@yahoo.com.tw'), True)
        self.assertIs(re_email('98732115@mail.fcu.edu.tw'), True)
        self.assertIs(re_email('198asd@o365.hkg.org.hk'), True)

    def test_re_email_false(self):
        self.assertIs(re_email('a123456789#gmail.com'), False)
        self.assertIs(re_email('a123456789@gmail'), False)
        self.assertIs(re_email('a12345gmailcom'), False)
        self.assertIs(re_email('sdfe*ls.@mail.fcu.tw'), False)

