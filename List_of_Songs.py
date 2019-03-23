# I
import Constructor
import fresh_tomatoes

# # Importing Library

marri_2 = Constructor.Movie("Maari 2 Rowdy Baby",
                   "marri 2",
                   "2018",
                   "http://tollytweet.com/wp-content/uploads/2018/11/FB_IMG_1543326205642.jpg",
                   "https://www.youtube.com/watch?v=x6Q7c9RyMzk")


Geetha_Govindam = Constructor.Movie("Inkem Inkem",
            "Geetha Govindam",
            "2018",
            "https://assets.voxcinemas.com/posters/P_HO00005825.jpg",
            "https://www.youtube.com/watch?v=VkmXX_jKmZw")

Taxiwaala = Constructor.Movie("Maate Vinadhuga",
            "Taxiwaala",
            "2018",
            "https://data1.ibtimes.co.in/cache-img-0-450/en/full/703289/1542693958_taxiwala.jpg",
            "https://www.youtube.com/watch?v=KMocA8G_puU")

 
list_of_movies = [marri_2,Geetha_Govindam,Taxiwaala]

fresh_tomatoes.open_movies_page(list_of_movies)


