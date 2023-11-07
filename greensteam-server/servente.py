import os
import greensteam_pb2   

class Game:

    def __init__(self, name, publisher, description, downloadQuantity, reviewsPercentage):
        self.name = name
        self.publisher = publisher
        self.description = description
        self.downloadQuantity = downloadQuantity
        self.reviewsPercentage = reviewsPercentage

class User:

    def __init__(self, name, bio, library, achivements) -> None:
        self.name = name
        self.bio = bio,
        self.library = library
        self.achivements = achivements

class Publisher:

    def __init__(self, name, followers, gamesQuantity) -> None:
        self.name = name
        self.followers = followers
        self.gamesQuantity = gamesQuantity

class Comment:
    def __init__(self, authorName, recomendation, content) -> None:
        self.authorName = authorName
        self.recomendation = recomendation
        self.content = content