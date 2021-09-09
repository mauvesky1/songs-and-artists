from application import app
import unittest

class FlaskTesting(unittest.TestCase):
    #testing routes
    def test_index_route(self):
        tester = app.test_client(self)
        response = tester.get("/index", content_type="html/text")
        self.assertTrue(response.status, 200)

    def test_base_route(self):
        tester = app.test_client(self)
        response = tester.get("/", content_type="html/text")
        self.assertTrue(response.status, 200)

    def test_delete_song_route(self):
        tester = app.test_client(self)
        response = tester.get("/delete/song/1", content_type="html/text")
        self.assertTrue(response.status, 200)

    def test_update_song_route(self):
        tester = app.test_client(self)
        response = tester.get("/update/song/1", content_type="html/text")
        self.assertTrue(response.status, 200)


    def test_artists_route(self):
        tester = app.test_client(self)
        response = tester.get("/artists", content_type="html/text")
        self.assertTrue(response.status, 200)

    def test_delete_artists_route(self):
        tester = app.test_client(self)
        response = tester.get("/delete/artist/1", content_type="html/text")
        self.assertTrue(response.status, 200)

    def test_update_artists_route(self):
        tester = app.test_client(self)
        response = tester.get("/update/artist/1", content_type="html/text")
        self.assertTrue(response.status, 200)


# if __name__ == "__main__":
#     unittest.main()