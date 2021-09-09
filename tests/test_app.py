from flask_testing import TestCase
from flask import url_for
import unittest
from application import app, db
from application.models import Artists, Songs

class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///test.db'
            ,
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app
    def setUp(self):
        # Will be called before every test
        # Create table schema
        db.create_all()
        # Create test data

        test_artist = Artists(artist_name="Houses", individuals_in_group="individuals_in_group", year_founded=1951)
        test_song = Songs(song_name="Rain", album_name="Fall", trivia="Recorded in Argyle", artists_id=1)

        # save sample data to database
        db.session.add(test_artist)
        db.session.add(test_song)

        db.session.commit()

    def tearDown(self):
             db.session.remove()
             db.drop_all()

class TestViews(TestBase):

    def test_index_get(self):
         response = self.client.get(url_for("index"))
         self.assertEqual(response.status_code, 200)
         self.assertIn(b'Rain', response.data)     

    def test_artist_get(self):
         response = self.client.get(url_for("artists"))
         self.assertEqual(response.status_code, 200)
         self.assertIn(b'Houses', response.data)
    
    def test_artist_post(self):
        response = self.client.post(url_for("artists"),
        data = dict(artist_name="of therein", individuals_in_group="individuals_in_group", year_founded=1955),
        follow_redirects=True  )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'of therein', response.data)

    def test_artist_delete(self):
        response = self.client.delete(url_for("deleteartist"),
        data = dict(id=1),
        follow_redirects=True  )
        self.assertEqual(response.status_code, 200)

    def test_artist_update(self):
        response = self.client.post(url_for("updateartist"),
        data = dict(artist_name="therein", individuals_in_group="individuals_in_group", year_founded=1950),
        follow_redirects=True  )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"1950", response.data)
    
             
    # def test_song_post(self):
    #     response = self.client.post(url_for("index"), data=dict(song_name="Sun", album_name="TheLi", trivia="Recorded in Bangui", artists_id=1),  follow_redirects=True   )
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn(b'Sun', response.data)

# class FlaskTesting(unittest.TestCase):
    #testing routes
#     def test_index_route(self):
#         tester = app.test_client(self)
#         response = tester.get("/index", content_type="html/text")
#         self.assertEqual(response.status_code, 200)

#     def test_base_route(self):
#         tester = app.test_client(self)
#         response = tester.get("/", content_type="html/text")
#         self.assertEqual(response.status_code, 200)

#     def test_artists_route(self):
#         tester = app.test_client(self)
#         response = tester.get("/artists", content_type="html/text")
#         self.assertEqual(response.status_code, 200)
      

# # if __name__ == "__main__":
#     unittest.main()