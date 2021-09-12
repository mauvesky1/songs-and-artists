import os
from datetime import datetime

from flask import render_template, url_for, flash, redirect, request
from application import app, db
from application.models import Artists, Songs


@app.route("/", methods=["Post", "GET"])
@app.route("/index", methods=["Post", "GET"])
def index():
        if request.method =="POST":
            
            song_name, album_name, trivia = request.form['song_name'], request.form['album_name'],  request.form['trivia']
            artists_id = Artists.query.filter_by(artist_name=request.form['artist_name']).first().id
            new_song = Songs(song_name=song_name, album_name=album_name, trivia=trivia, artists_id=artists_id)

            db.session.add(new_song)
            db.session.commit()
            return redirect("/")

        else:
            songs = Songs.query.all()
            results =db.session.query(Songs, Artists).join(Artists).all()

            return render_template("index.html", songs=results)

@app.route("/artists", methods=["Post", "GET"])
def artists():
        if request.method =="POST":
            artist_name = request.form['artist_name']
            individuals_in_group = request.form['individuals_in_group']
            year_founded = request.form['year_founded']

            new_artist = Artists(artist_name=artist_name, individuals_in_group=individuals_in_group, year_founded=year_founded)
  
            db.session.add(new_artist)
            db.session.commit()
            return redirect("/artists")

        else:
            artists = Artists.query.all()
            return render_template("artists.html", artists=artists)


@app.route('/delete/<int:table>/<int:id>', methods=["DELETE", "GET"])
def deleteartist(table, id):

    if table == 1: row_to_delete = Artists.query.get_or_404(id)

    elif table == 2: 
        row_to_delete = Songs.query.get_or_404(id)

    db.session.delete(row_to_delete)
    db.session.commit()

    if table == 1:   return redirect("/artists")
    elif table == 2: return redirect("/")


@app.route('/update/<int:table>/<int:id>', methods=['GET', 'POST'])
def updateartist(table, id):
    print( table, "HEllo ello")
    if table == 1:
        artist_to_update = Artists.query.get_or_404(id)
    elif table == 2:
        song_to_update = Songs.query.get_or_404(id)
        
    if request.method == 'POST' and table == 1:
      
            artist_to_update.artist_name = request.form['artist_name']
            artist_to_update.individuals_in_group = request.form['individuals_in_group']
            artist_to_update.year_founded = request.form['year_founded']

            db.session.commit()
            return redirect("/artists")

    elif table == 1: return render_template('updateartist.html', artist=artist_to_update)
    #Song Update logic
    if request.method == 'POST' and table == 2:
        song_to_update.song_name = request.form['song_name']
        song_to_update.album_name = request.form['album_name']
        song_to_update.trivia = request.form['trivia']
        
        db.session.commit()
        return redirect("/")
        
    elif table == 2: return render_template('updatesong.html', song=song_to_update)