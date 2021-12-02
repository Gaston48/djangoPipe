from django.test import TestCase
from . models import Post


class ModelTests(TestCase):

    def setUp(self):
        self.blog = Post.objects.create(title='django', author='djangoAuthor', slug='djangoSlug')

    def test_post_model(self):
        d = self.blog
        self.assertTrue(isinstance(d, Post))

    def test_post_return_title_on_default(self):
        d = self.blog
        self.assertEqual(str(d), 'django')

    def test_get_author(self):
        d = self.blog
        self.assertEqual(d.get_author(), 'djangoAuthor')
