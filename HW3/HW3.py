# Andrew McGrath
# 02/28/2020
# amcgrat3@uccs.edu
# Script for HW 3: Loading and query csv of Movies

import re
import csv
import Movie
from Movie import *

###########################################################################
# Functions
###########################################################################
def printMenu(menuItems):
	menuItem = 0
	print("*" * 30)
	for item in menuItems:
		menuItem += 1
		print("%d - %s" % (menuItem, item))
	print("*" * 30)
	return promptForInteger(1, menuItem,
						    "Please make a selection between 1 and %d:" % menuItem,
							"Your response must be number between 1 and %d, try again." % menuItem)


def promptForInteger(minimum, maximum, message, errorMessage):
	try:
		response = int(input(message + "\n"))
	except:
		response = -1

	while (response < minimum or response > maximum):
		try:
			response = int(input(errorMessage + "\n"))
		except:
			response = -1
	return response


def loadFile(message, movies):
	filename = input(message + "\n")
	# Use the csv import to read in data from file
	with open(filename, "r") as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			if line_count == 0:
				# This line catches the first row with col titles
				line_count += 1
			else:
				# Create a Movie object with data from the CSV
				mov = Movie(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
				movies.append(mov)
				line_count += 1


def searchByTitle(message, movies):
	criteria = input(message + "\n")
	criteria = criteria.lower()
	printmovies = []

	for movie in movies:
		# Find movies where the title contains the given criteria
		if re.search(criteria, movie.getTitle().lower()):
			printmovies.append(movie)

	printMovies(sorted(printmovies, key=lambda movie: movie.getTitle()))


def searchByGenre(message, movies):
	criteria = input(message + "\n")
	criteria = criteria.lower()
	printmovies = []

	for movie in movies:
		# Find movies where the genre contains the given criteria
		if re.search(criteria, movie.getGenre().lower()):
			printmovies.append(movie)

	printMovies(sorted(printmovies, key=lambda movie: movie.getTitle()))


def searchByDirector(message, movies):
	criteria = input(message + "\n")
	criteria = criteria.lower()
	printmovies = []

	for movie in movies:
		# Find movies where the director's name contains the given criteria
		if re.search(criteria, movie.getDirector().lower()):
			printmovies.append(movie)

	printMovies(sorted(printmovies, key=lambda movie: movie.getTitle()))


def searchByWriter(message, movies):
	criteria = input(message + "\n")
	criteria = criteria.lower()
	printmovies = []

	for movie in movies:
		# Find movies where the writer's name contains the given criteria
		if re.search(criteria, movie.getWriter().lower()):
			printmovies.append(movie)

	printMovies(sorted(printmovies, key=lambda movie: movie.getTitle()))


def searchByStar(message, movies):
	criteria = input(message + "\n")
	criteria = criteria.lower()
	printmovies = []

	for movie in movies:
		# Find movies where the any of the star's names contains the given criteria
		starSearch1 = re.search(criteria, movie.getStar1().lower())
		starSearch2 = re.search(criteria, movie.getStar2().lower())
		starSearch3 = re.search(criteria, movie.getStar3().lower())

		if starSearch1 or starSearch2 or starSearch3:
			printmovies.append(movie)

	printMovies(sorted(printmovies, key=lambda movie: movie.getTitle()))


def searchByRunningTime(message, movies):
	criteria = input(message + "\n")
	criteria = int(criteria)
	printmovies = []

	for movie in movies:
		# Find movies where the run time is less that the specified amount
		if int(movie.getRunTime()) < criteria:
			printmovies.append(movie)

	printMovies(sorted(printmovies, key=lambda movie: movie.getTitle()))


def searchByRating(message, movies):
	criteria = input(message + "\n")
	criteria = criteria.lower()
	printmovies = []

	for movie in movies:
		# Find movies where the rating is exactly what was given (minus casing)
		if re.search(rf"^{criteria}$", movie.getRating().lower()):
			printmovies.append(movie)

	printMovies(sorted(printmovies, key=lambda movie: movie.getTitle()))


def searchByReleaseYear(message, movies):
	criteria = input(message + "\n")
	criteria = criteria
	printmovies = []

	for movie in movies:
		# Find movies where the release year is exactly as entered
		if re.search(rf"^{criteria}$", movie.getReleaseDate()[-4:]):
			printmovies.append(movie)

	printMovies(sorted(printmovies, key=lambda movie: movie.getTitle()))


def printMovies(movies):
	for movie in movies:
		# Use the __str__ for movies to get the formatted text
		print(str(movie))

###########################################################################
# Main
###########################################################################
movies = [ ]

response = 0
while response != 11:
	response = printMenu( [ "Load a Movie File", "Search by Title", "Search by Genre", "Search by Director", \
							"Search by Writer", "Search by Star", "Search by Running Time", \
							"Search by Rating", "Search by Release Year", "Print all Movies", "Quit" ] )

	if response == 1:
		movies = [ ]
		loadFile("Please enter the movie filename: ", movies)
	elif response == 2:
		searchByTitle("Please enter the movie title or partial title: ", movies)
	elif response == 3:
		searchByGenre("Please enter the movie genre or partial genre: ", movies)
	elif response == 4:
		searchByDirector("Please enter the Director's name or partial name: ", movies)
	elif response == 5:
		searchByWriter("Please enter the Writer's name or partial name: ", movies)
	elif response == 6:
		searchByStar("Please enter the Star's name or partial name: ", movies)
	elif response == 7:
		searchByRunningTime("Please enter the maximum running time in minutes: ", movies)
	elif response == 8:
		searchByRating("Please enter the movie rating: ", movies)
	elif response == 9:
		searchByReleaseYear("Please enter the release year: ", movies)
	elif response == 10:
		printMovies(sorted(movies, key=lambda movie: movie.getTitle()))
	elif response == 11:
		print("Quitting!")
		exit