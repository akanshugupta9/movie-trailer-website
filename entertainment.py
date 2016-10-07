import media
import fresh_tomatoes

# creating movie objects
inferno = media.Movie("Inferno", "https://www.youtube.com/watch?v=RH2BD49sEZI",
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcT2CzmJg3DA2BmVPFxXRoNCYynKZ1WBgMMbHJSIM-UDiqNhWPuS")
interstellar = media.Movie("Interstellar", "https://www.youtube.com/watch?v=0vxOhd4qlnA&t=5s",
                        "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg")
inception = media.Movie("Inception", "https://www.youtube.com/watch?v=1g4PLj0PlOM",
                        "http://www.impawards.com/2010/posters/inception.jpg")
eternalSunshine = media.Movie("Eternal Sunshine of Spotless Mind", "https://www.youtube.com/watch?v=rb9a00bXf-U",
                        "https://upload.wikimedia.org/wikipedia/en/6/62/Eternal_sunshine_of_the_spotless_mind_ver3.jpg")
pele = media.Movie("Pele", "https://www.youtube.com/watch?v=gcN8ZmYyJVY",
                        "https://upload.wikimedia.org/wikipedia/en/d/df/Pel%C3%A9_%28film_poster%29.jpg")
titanic = media.Movie("Titanic", "https://www.youtube.com/watch?v=kVrqfYjkTdQ",
                      "http://images.allposters.com/images/59/003_titanicrip.jpg")

# creating movies array
movies = [inferno, interstellar, inception, eternalSunshine, pele, titanic]

# calling method to create webpage
fresh_tomatoes.open_movies_page(movies)
