from django.test import TestCase
from messenger.views import inbox,sent,view_message,compose
from django.core.urlresolvers import resolve


# Create your tests here.
class Messenger_Tests(TestCase):
    def test_inbox_resolves(self):
        inbox_res=resolve('/messenger/inbox/')
        self.assertEqual(inbox_res.func,inbox)


    def test_sent_resolves(self):
        sent_res=resolve('/messenger/sent/')
        self.assertEqual(sent_res.func,sent)

    def test_view_resolves(self):
        view_res=resolve('/messenger/view_message/1/')
        self.assertEqual(view_res.func,view_message)


    def test_compose_resolves(self):
        compose_res=resolve('/messenger/compose/')
        self.assertEqual(compose_res.func,compose)
        
    def test_message_resolves_id(self):
        error_res=self.client.get('/messenger/view_message')
        self.assertEqual(error_res.status_code,404)
        
  
        
        