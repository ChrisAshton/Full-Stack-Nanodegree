# this is the current respository of movies. Add another movie by following the
# format below, paying attention that you are instanting the Movie class detailed
# in media.py; add the movie to the list of Movie instances below, and saving the
# file.
#
# The function at the bottom of the file, fresh_tomatoes.open_movies_page(movies),
# takes a list of these movie objects, creates an HTML file and opens it in the
# default browser to display the movies
#

import media
import fresh_tomatoes

toy_story = media.Movie("Guardians of the Galaxy Vol.2",
                        "Our hero, Peter Quill, searches for meaning during adventures with his friends",
                        "https://upload.wikimedia.org/wikipedia/en/a/ab/Guardians_of_the_Galaxy_Vol_2_poster.jpg",
                        "https://www.youtube.com/watch?v=duGqrYw4usE")


avatar = media.Movie("Avatar",
                     "A Marine on an alien planet integrates with native population",
                     "https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

edge_of_tomorrow = media.Movie("Edge of Tomorrow",
                               "Tom Cruise and Emily Blunt teach some Aliens a thing or two",
                               "https://upload.wikimedia.org/wikipedia/en/f/f9/Edge_of_Tomorrow_Poster.jpg",
                               "https://www.youtube.com/watch?v=yUmSVcttXnI")

school_of_rock = media.Movie("School of Rock",
                            "Using rock to learn",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://youtu.be/3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
                          "A rat is a chef in Paris",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back in time to meet authors",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://youtu.be/FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games",
                           "Katniss leads a rebellion against District One",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch/?v=PbA63a7H0bo")

movies = [toy_story, avatar, edge_of_tomorrow, school_of_rock, ratatouille, midnight_in_paris, hunger_games]


fresh_tomatoes.open_movies_page(movies)
