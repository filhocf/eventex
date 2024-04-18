from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Claudio Filho', cpf='12345678901',
                    email='filhocf@gmail.com', phone='61-98118-2975')
       
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'filhocf@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['Claudio Filho',
                    '12345678901',
                    'filhocf@gmail.com',
                    '61-98118-2975']
        
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
