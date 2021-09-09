from application import app, db
import unittest

class FlaskTesting(unittest.TestCase):
    #testing routes
    def test_index_route(self):
        tester = app.test_client(self)
        response = tester.get("/index", content_type="html/text")
        self.assertEqual(response.status_code, 200)



    def test_base_route(self):
        tester = app.test_client(self)
        response = tester.get("/", content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_artists_route(self):
        tester = app.test_client(self)
        response = tester.get("/artists", content_type="html/text")
      

# if __name__ == "__main__":
#     unittest.main()