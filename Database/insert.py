import tmdbapi, Backend.database as database

m_id = 0
cur = database.connect()
cur.execute("SELECT movie_id FROM movie")
movies = {row[0] for row in cur.fetchall()}
cur.execute("SELECT genre_id FROM genres")
genres = {row[0] for row in cur.fetchall()}
cur.execute("SELECT p_id FROM people")
people = {row[0] for row in cur.fetchall()}
                    
for page in range(1,460):
    url1 =  f"https://api.themoviedb.org/3/movie/top_rated?page={page}"    
    data1 = tmdbapi.api_request(url1)
    
    for movie in data1["results"]:
        if movie["id"] not in movies:
            movie_id = movie["id"]
            url2 = f"https://api.themoviedb.org/3/movie/{movie_id}"
            data2 = tmdbapi.api_request(url2)
            m_id += 1
            title = data2["title"]
            lang = data2["original_language"]
            release = data2["release_date"]
            runtime = data2["runtime"]
            overview = data2["overview"]
            tmdb_rating = data2["vote_average"]
            poster = data2["poster_path"]
            backdrop =  data2["backdrop_path"]
            prod_co = "Unknown"
            if len(data2["production_companies"]) > 0:
                prod_co = data2["production_companies"][0]["name"]
            url3 = f"https://api.themoviedb.org/3/movie/{movie_id}/videos"
            data3 = tmdbapi.api_request(url3)
            trailer = "Unknown"
            if len(data3["results"]) > 0:
                trailer = data3["results"][0]["key"]
            query1 = ("INSERT INTO movie(movie_id, title, language, release_date, runtime, overview, tmdb_rating, posterpath, backdroppath, trailerlink, prod_co) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
            value1 = (m_id, title, lang, release, runtime, overview, tmdb_rating, poster, backdrop, trailer, prod_co)
            cur.execute(query1, value1)
            movies.add(movie_id)
            
            for genre in data2["genres"]:
                genre_id = genre["id"]
                if genre_id not in genres:
                    genre_name = genre["name"]
                    query2 = "INSERT INTO genres(genre_id, genre) VALUES(%s, %s)"
                    value2 = (genre_id, genre_name)
                    cur.execute(query2, value2)
                    genres.add(genre_id)
                query3 = "INSERT INTO moviegenres(movie_id, genre_id) VALUES(%s, %s)"
                value3 = (m_id, genre_id)
                cur.execute(query3, value3)
                    
            url4 = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
            data4 = tmdbapi.api_request(url4)
            count = 0
            for cast in data4["cast"]:
                if count < 7:
                    role = "Unknown"
                    if cast["character"] != "":
                        role = cast["character"][:250]
                    position = cast["order"]
                    count += 1
                    person_id = cast["id"]
                    if person_id not in people:
                        url5 = f"https://api.themoviedb.org/3/person/{person_id}"
                        data5 = tmdbapi.api_request(url5)
                        p_name = data5["name"]
                        bio = data5["biography"]
                        dob = data5["birthday"]
                        imgpath = data5["profile_path"]
                        query4 = "INSERT INTO people(p_id, name, dob, bio, imgpath) VALUES(%s, %s, %s, %s, %s)"
                        value4 = (person_id, p_name, dob, bio, imgpath)
                        cur.execute(query4, value4)
                        people.add(person_id)
                    query5 = "INSERT INTO cast (movie_id, p_id, role, position) VALUES(%s, %s, %s, %s)"
                    value5 = (m_id, person_id, role, position)
                    cur.execute(query5, value5)
              
            exec_prod = False
            for crew in data4["crew"]:
                if crew["job"] == "Executive Producer" and not exec_prod:
                    exec_prod = True
                    job = crew["job"]
                    person_id = crew["id"]
                    if person_id not in people:
                        url6 = f"https://api.themoviedb.org/3/person/{person_id}"
                        data6 = tmdbapi.api_request(url6)
                        p_name = data6["name"]
                        bio = data6["biography"]
                        dob = data6["birthday"]
                        imgpath = data6["profile_path"]
                        query4 = "INSERT INTO people(p_id, name, dob, bio, imgpath) VALUES(%s, %s, %s, %s, %s)"
                        value4 = (person_id, p_name, dob, bio, imgpath)
                        cur.execute(query4, value4)
                        people.add(person_id)
                    query6 = "INSERT INTO crew(movie_id, p_id, job) VALUES(%s, %s, %s)"
                    value6 = (m_id, person_id, job)
                    cur.execute(query6, value6)
                elif crew["job"] == "Director":
                    job = crew["job"]
                    person_id = crew["id"]
                    if person_id not in people:
                        url6 = f"https://api.themoviedb.org/3/person/{person_id}"
                        data6 = tmdbapi.api_request(url6)
                        p_name = data6["name"]
                        bio = data6["biography"]
                        dob = data6["birthday"]
                        imgpath = data6["profile_path"]
                        query4 = "INSERT INTO people(p_id, name, dob, bio, imgpath) VALUES(%s, %s, %s, %s, %s)"
                        value4 = (person_id, p_name, dob, bio, imgpath)
                        cur.execute(query4, value4)
                        people.add(person_id)
                    query6 = "INSERT INTO crew(movie_id, p_id, job) VALUES(%s, %s, %s)"
                    value6 = (m_id, person_id, job)
                    cur.execute(query6, value6)
                    
        print("Added Movie: ", m_id)
    cur.execute('COMMIT')
    print("Added Page: ", page)
print("Completed Successfully!")