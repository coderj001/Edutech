from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core.views import *


class TestUrls(SimpleTestCase):
    """ For core urls tests """

    def test_homepage_url_is_resolves(self):
        """ For homepage """

        url = reverse('core:homepage')
        self.assertEquals(resolve(url).func, homepage)

    def test_login_url_is_resolves(self):
        """ For login """

        url = reverse('core:login')
        self.assertEquals(resolve(url).func, login_user)

    def test_logout_url_is_resolves(self):
        """ For logout """

        url = reverse('core:logout')
        self.assertEquals(resolve(url).func, logout_user)

    def test_signup_url_is_resolves(self):
        """ For signup """

        url = reverse('core:signup')
        self.assertEquals(resolve(url).func, signup_user)

    def test_ask_question_url_is_resolves(self):
        """ For Ask Question """

        url = reverse('core:ask_question')
        self.assertEquals(resolve(url).func, ask_question)

    def test_search_question_url_is_resolves(self):
        """ For Searh Question """

        url = reverse('core:search_question')
        self.assertEquals(resolve(url).func, search_question)

    def test_question_url_is_resolves(self):
        """ For Question """

        url = reverse('core:question', args=[1])
        self.assertEquals(resolve(url).func, question)
