# Imports fresh_tomatoes.py and the media module.
import fresh_tomatoes
import media

# Defines my 6 favorite movies:
inception = media.Movie(
    "Inception",
    "A thief, who steals corporate secrets through use of "
    "dream-sharing technology, is given the inverse task of "
    "planting an idea into the mind of a CEO.",
    "https://upload.wikimedia.org/wikipedia/en/2/2e/"
    "Inception_%282010%29_theatrical_poster.jpg",
    "https://www.youtube.com/watch?v=8hP9D6kZseM")

the_matrix = media.Movie(
    "The Matrix",
    "A computer hacker learns from mysterious rebels about the true nature "
    "of his reality and his role in the war against its controllers.",
    "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
    "https://www.youtube.com/watch?v=m8e-FF8MsqU")

star_wars = media.Movie(
    "Star Wars Episode V - The Empire Strikes Back",
    "Luke Skywalker takes advanced Jedi training with Master Yoda, while his "
    "friends are pursued by Darth Vader as part of his plan to capture Luke.",
    "https://upload.wikimedia.org/wikipedia/"
    "en/3/3c/SW_-_Empire_Strikes_Back.jpg",
    "https://www.youtube.com/watch?v=JNwNXF9Y6kY")

reservoir_dogs = media.Movie(
    "Reservoir Dogs",
    "After a simple jewelry heist goes terribly wrong, the surviving "
    "criminals begin to suspect that one of them is a police informant.",
    "https://upload.wikimedia.org/wikipedia/en/f/f6/Reservoir_dogs_ver1.jpg",
    "https://www.youtube.com/watch?v=vayksn4Y93A")

schindlers_list = media.Movie(
    "Schindler's List",
    "In German-occupied Poland during World War II, Oskar Schindler "
    "gradually becomes concerned for his Jewish workforce after "
    "witnessing their persecution by the Nazi Germans.",
    "https://upload.wikimedia.org/wikipedia/"
    "en/3/38/Schindler%27s_List_movie.jpg",
    "https://www.youtube.com/watch?v=JdRGC-w9syA")

arrival = media.Movie(
    "Arrival",
    "When twelve mysterious spacecraft appear around the world, "
    "linguistics professor Louise Banks is tasked with interpreting "
    "the language of the apparent alien visitors.",
    "https://upload.wikimedia.org/wikipedia/"
    "en/d/df/Arrival%2C_Movie_Poster.jpg",
    "https://www.youtube.com/watch?v=tFMo3UJ4B4g")

# Creates an array with previously defined movies.
movies = [inception, the_matrix, star_wars,
          reservoir_dogs, schindlers_list, arrival]

'''
Uses the fresh_tomatoes.py file to call open_movies_page
to generate an HTML page of my favorite movies.
'''
fresh_tomatoes.open_movies_page(movies)
