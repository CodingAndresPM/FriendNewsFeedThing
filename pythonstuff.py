## Made by Andres Pinon
## My Social Network

class User:
        def __init__(self, firstname, lastname, username, bio, userID):
            self.firstname = firstname
            self.lastname = lastname
            self.username = username
            self.bio = bio
            self.userID = userID
            self.friends = []
            self.posts = []

        def addFriends (self, username):
            self.friends.append(username)

        def viewnewsfeed (self, friends):
            self.friend.append(username)
        
if __name__ == "__main__":
    firstname = "Andres"
    lastname = "Pinon"
    username = "Shmecs"
    bio = "i am amazing"
    userID = "0000"

    Pinon = User(firstname, lastname, username, bio, userID)
    Jaqualin = User("Jaqualin", "woodard", "Jakie100", "HELLO I AM A FRIEND", "0002")
    Andres = User(firstname, lastname, username, bio, userID)
    lucy = User("lucy", "smith", "lucy1234", "hello", "0001")
    print(lucy.firstname)
    print(Jaqualin.firstname)
    
    Andres.addFriends ("Jakie100")
    Andres.addFriends("lucy1234")
    print(Andres.friends)
    lucy.posts.append("HELLO FRIEND")
    Jaqualin.posts.append("HI")
    ##print (lucy.posts)
    ##print (Jaqualin.posts)
    for friend in self.friends:
                print(friend.posts)
    Andres.viewnewsfeed(Andres.friends)
    
