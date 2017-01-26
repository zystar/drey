from tornado.testing import AsyncHTTPTestCase

import drey.app as app


class TestHelloApp(AsyncHTTPTestCase):
    def get_app(self):
        return app.make_app()

    def test_homepage(self):
        response = self.fetch('/')
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, b'Hello, world')
