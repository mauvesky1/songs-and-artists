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
        #Songs(song_name="Las", album_name="Housses", trivia="trivia", artists_id=1)
        test_artist = Artists(artist_name="Houses", individuals_in_group="individuals_in_group", year_founded=1951)

        # save sample data to database
        db.session.add(test_artist)
        db.session.commit()

    def tearDown(self):
             db.session.remove()
             db.drop_all()

class TestViews(TestBase):
     def test_artist_get(self):
         response = self.client.get(url_for("artists"))
         self.assertEqual(response.status_code, 200)
         self.assertIn(b'Houses', response.data)
             

# class FlaskTesting(unittest.TestCase):
#     #testing routes
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
      

# if __name__ == "__main__":
#     unittest.main()