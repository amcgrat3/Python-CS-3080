# Andrew McGrath
# 02/28/2020
# amcgrat3@uccs.edu
# Script for HW 3: Movie class information

from datetime import datetime


class Movie:
    def __init__(self, title, genre, director, writer, star1, star2,
                 star3, runTime, rating, releaseDate):
        self._title = title
        self._genre = genre
        self._director = director
        self._writer = writer
        self._star1 = star1
        self._star2 = star2
        self._star3 = star3
        self._runTime = runTime
        self._rating = rating
        self._releaseDate = releaseDate

    def __str__(self):
        returnStr = ""
        returnStr += ("-" * 80 + "\n")
        title = self.getTitle()
        title1 = ""
        title2 = ""
        title3 = ""

        # Divy up the title
        if len(title) < 56:
            title1 = title
        elif len(title) < 56 + 35:
            subTitle = title[0:56]
            lastSpace = subTitle.rindex(" ")
            title1 = title[0:lastSpace]
            title2 = title[lastSpace + 1:]
        else:
            subTitle = title[0:56]
            lastSpace1 = subTitle.rindex(" ")
            title1 = title[0:lastSpace1]
            subTitle = title[lastSpace1: lastSpace1 + 35]
            lastSpace2 = subTitle.rindex(" ") + len(title1)
            title2 = title[lastSpace1 + 1:lastSpace2]
            title3 = title[lastSpace2 + 1:]

        runTime = int(self.getRunTime())
        hours = str(runTime // 60)
        minutes = str(runTime % 60)

        if int(minutes) < 10:
            minutes = "0" + minutes

        rating = self.getRating()

        # Print line 1
        returnStr += (title1.ljust(55, ' ') + "  |  " + hours + " h " + minutes + " min" + "  |  " +
                      str(rating).rjust(5, ' ') + "\n")

        director = self.getDirector()

        # Print line 2
        returnStr += (title2.ljust(35, ' ') + "  |  " + "Director:".ljust(10, ' ') + director + "\n")

        writer = self.getWriter()

        # Print line 3
        returnStr += (title3.ljust(35, ' ') + "  |  " + "Writer:".ljust(10, ' ') + writer + "\n")

        genre = self.getGenre()

        # Print line 4
        returnStr += ("Genre:".ljust(9, ' ') + genre + "\n")

        fullStars = self.getStar1() + ", " + self.getStar2() + ", " \
                    + self.getStar3()
        finalStars = ""
        needFinalStars = False

        if len(fullStars) > 71:
            subStars = fullStars[0:71]
            lastSpace = subStars.rindex(" ")
            finalStars = fullStars[lastSpace + 1:]
            fullStars = fullStars[0:lastSpace]
            needFinalStars = True

        # Print line 5
        returnStr += ("Stars:".ljust(9, ' ') + fullStars + "\n")

        # Print optional line 6
        if needFinalStars:
            returnStr += (" ".ljust(9, ' ') + finalStars + "\n")

        date_ob = datetime.strptime(self.getReleaseDate(), '%m/%d/%Y').date()

        # Print line 7
        returnStr += ("Release:".ljust(9, ' ') + date_ob.strftime("%B %#d, %Y"))

        return returnStr

    #  Getters and Setters  #
    def getTitle(self):
        return self._title

    def setTitle(self, title):
        self._title = title

    def getGenre(self):
        return self._genre

    def setGenre(self, genre):
        self._genre = genre

    def getDirector(self):
        return self._director

    def setDirector(self, director):
        self._director = director

    def getWriter(self):
        return self._writer

    def setWriter(self, writer):
        self._writer = writer

    def getStar1(self):
        return self._star1

    def setStar1(self, star1):
        self._star1 = star1

    def getStar2(self):
        return self._star2

    def setStar2(self, star2):
        self._star2 = star2

    def getStar3(self):
        return self._star3

    def setStar3(self, star3):
        self._star3 = star3

    def getRunTime(self):
        return self._runTime

    def setRunTime(self, runTime):
        self._runTime = runTime

    def getRating(self):
        return self._rating

    def setStar1(self, rating):
        self._rating = rating

    def getReleaseDate(self):
        return self._releaseDate

    def setReleaseDate(self, releaseDate):
        self._releaseDate = releaseDate
