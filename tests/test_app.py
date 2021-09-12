from flask_testing import TestCase
from flask import url_for
import unittest
from application import app, db
from application.models import Artists, Songs

class TestBase(TestCase):

    def create_app(self):

        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///test.db',
            DEBUG=True,
            WTF_CSRF_ENABLED=False)
        return app
    def setUp(self):

        db.create_all()

        test_artist = Artists(artist_name="Houses", individuals_in_group="individuals_in_group", year_founded=1951)
        test_song = Songs(song_name="Rain", album_name="Fall", trivia="Recorded in Argyle", artists_id=1)

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
        data = {"artist_name":"of therein", "individuals_in_group":"individuals_in_group", "year_founded":1955},
        follow_redirects=True  )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'of therein', response.data)

    def test_artist_delete(self):
        response = self.client.get(url_for("deleteartist", id=1, table=1),
        follow_redirects=True  )
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b"Houses", response.data)
    
    def test_song_delete(self):
        response = self.client.get(url_for("deleteartist", id=1, table=2),
        follow_redirects=True  )
        print("this is the printing right here", response.data)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b"Rain", response.data)

    def test_artist_update(self):
        response = self.client.post(url_for("updateartist", id=1,table=1),
        data = {"artist_name":"therein", "individuals_in_group":"individuals_in_group", "year_founded":1950},
        follow_redirects=True  )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"1950", response.data)
    
    def test_song_update(self):
        response = self.client.post(url_for("updateartist", id=1, table=2),
        data = {"artists_id":1, "song_name":"Yet name", "album_name":"Yet", "trivia":"trivia"}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Yet name", response.data)
        
