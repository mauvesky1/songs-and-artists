import os
from datetime import datetime

from flask import render_template, url_for, flash, redirect, request
from application import app, db
from application.models import Artists, Songs



@app.route("/", methods=["Post", "GET"])
@app.route("/index", methods=["Post", "GET"])
def index():
        if request.method =="POST":
            
            song_name = request.form['song_name']
            album_name = request.form['album_name']
            trivia = request.form['trivia']
            artists_id = Artists.query.filter_by(artist_name=request.form['artist_name']).first().id

            new_song = Songs(song_name=song_name, album_name=album_name, trivia=trivia, artists_id=artists_id)
            try:
                db.session.add(new_song)
                db.session.commit()
                return redirect("/")
            except:
                return "There was an error adding the song."
        else:
            songs = Songs.query.all()
            results =db.session.query(Songs, Artists).join(Artists).all()


            return render_template("index.html", songs=results)

@app.route('/delete/song/<int:id>')
def delete(id):
    song_to_delete = Songs.query.get_or_404(id)

    try:
        db.session.delete(song_to_delete)
        db.session.commit()
        return redirect("/")
    except:
        return "There was a problem deleting that task"


@app.route('/update/song/<int:id>', methods=['GET', 'POST'])
def update(id):
    song_to_update = Songs.query.get_or_404(id)
    if request.method == 'POST':
        song_to_update.song_name = request.form['song_name']
        song_to_update.album_name = request.form['album_name']
        song_to_update.trivia = request.form['trivia']
        
        try: 
            db.session.commit()
            return redirect("/")
        except:
            return "Error encountered interacting with the database"
    else:
        return render_template('updatesong.html', song=song_to_update)

@app.route("/artists", methods=["Post", "GET"])
def artists():
        if request.method =="POST":
            artist_name = request.form['artist_name']
            individuals_in_group = request.form['individuals_in_group']
            year_founded = request.form['year_founded']

            new_artist = Artists(artist_name=artist_name, individuals_in_group=individuals_in_group, year_founded=year_founded)
            try:
                db.session.add(new_artist)
                db.session.commit()
                return redirect("/artists")
            except:
                return "There was an error adding the song."
        else:
            artists = Artists.query.all()
            return render_template("artists.html", artists=artists)


@app.route('/delete/artist/<int:id>', defaults={"id":1}, methods=['DELETE'])
def deleteartist(id):
    artist_to_delete = Artists.query.get_or_404(id)

    try:
        db.session.delete(artist_to_delete)
        db.session.commit()
        return redirect("/artists")
    except:
        return "There was a problem deleting that task"


@app.route('/update/artist/<int:id>', defaults={ "id":1}, methods=['GET', 'POST'])
def updateartist(id):
    artist_to_update = Artists.query.get_or_404(id)
    if request.method == 'POST':
        artist_to_update.artist_name = request.form['artist_name']
        artist_to_update.individuals_in_group = request.form['individuals_in_group']
        artist_to_update.year_founded = request.form['year_founded']
        try:
       
            db.session.commit()
            return redirect("/artists")
        except:
            return "There was a problem deleting that task"
    else:
        return render_template('updateartist.html', artist=artist_to_update)