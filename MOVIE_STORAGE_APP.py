import sys


print("\n")
print("                                                              ||  /\  ||  ||\  ||     / /\   / /\ \  ||\  /||  ||\ ")
print("                                                              || /  \ ||  ||-  ||    | |     ||  ||  || \/ ||  ||- ")
print("                                                              ||/    \||  ||/  ||__   \ \/   \ \/ /  ||    ||  ||/ ")

class TreeNode:
    def __init__(self, year, title, duration, rating, cast=[]):
        self.title = title
        self.year = year
        self.duration = duration
        self.rating = rating
        self.left = None
        self.right = None
        self.cast = cast


class BST:
    def __init__(self):
        self.root = None
        
    def inorder_print_tree(self):
        if self.root:
            self._inorder_print_tree(self.root)
            return True

    def _inorder_print_tree(self, cur_node):
        if cur_node:
            
            self._inorder_print_tree(cur_node.left)
            print("\n")
            print("The release year of the Movie : " + str(cur_node.year))
            print("Title of Movie : " + str(cur_node.title))
            print("Rating of the Movie : " + str(cur_node.rating))
            print("Duration of Movie : " + str(cur_node.duration))
            print("Cast of the Movie : ")

            cur_node.cast.print_list()

            
            self._inorder_print_tree(cur_node.right)  

    def insert(self, year, title, duration, rating, cast=[]):
        if self.root is None:
            self.root = TreeNode(year, title, duration, rating, cast)
        else:
            self._insert(year, title, duration, rating, cast, self.root)

    def _insert(self, year, title, duration, rating, cast, cur_node):
        if title != cur_node.title and title < cur_node.title:
            if cur_node.left is None:
                cur_node.left = TreeNode(year, title, duration, rating, cast)
                cur_node.left.parent = cur_node
            else:
                self._insert(year, title, duration, rating, cast, cur_node.left)

        elif title != cur_node.title and title > cur_node.title:
            if cur_node.right is None:
                cur_node.right = TreeNode(year, title, duration, rating, cast)
                cur_node.right.parent = cur_node
            else:
                self._insert(year, title, duration, rating, cast, cur_node.right)
        else:
            print("Movie Is Already In The Storage!")



    def _find(self, title, cur_node):

        if title > cur_node.title and cur_node.right:
            return self._find(title, cur_node.right)
        elif title < cur_node.title and cur_node.left:
            return self._find(title, cur_node.left)
        if title == cur_node.title:

            print("The release year of the Movie : " + str(cur_node.year))
            print("Title of Movie : " + str(cur_node.title))
            print("Rating of the Movie : " + str(cur_node.rating))
            print("Duration of Movie : "+ str(cur_node.duration))
            print("Cast of the Movie : ")
            cur_node.cast.print_list()
           
            
            print("\n")

    def find(self, title):
        if self.root:
            is_found = self._find(title, self.root)
            if is_found:
                return self._find(title, self.root)
            return False
        else:
            return None
    

    
    def year(self,year):
        if self.root:
            self._year(self.root,year)
            return False

    def _year(self, cur_node,year):
        
        if cur_node:
           
            self._year(cur_node.left,year)
            
            if cur_node.year == year:
                print("*******  MOVIE RELEASE IN THE YEAR", f"{year}  *******")
                print("\n")
                print("The release year of the Movie : " + str(cur_node.year))
                print("Title of Movie : " + str(cur_node.title))
                print("Rating of the Movie : " + str(cur_node.rating))
                print("Duration of Movie : " + str(cur_node.duration))
                print("Cast of the Movie : ")
                cur_node.cast.print_list()

                print("\n")
               
            self._year(cur_node.right,year)
           

    def ratings(self,rating):
        if self.root:
            self._ratings(self.root,rating)
            return False

    def _ratings(self, cur_node,rating):
        
        if cur_node:
            self._ratings(cur_node.left,rating)
        
            if cur_node.rating == rating:
                print("*******  MOVIE RATING WITH ", f"{rating}  *******")
                print("\n")
                print("The release year of the Movie :" + str(cur_node.year))
                print("Title of Movie : " + str(cur_node.title))
                print("Rating of the Movie : " + str(cur_node.rating))
                print("Duration of Movie : " + str(cur_node.duration))
                print("Cast of the Movie : ")
                cur_node.cast.print_list()
                print("\n")
              
            self._ratings(cur_node.right,rating)
    
    def _actorfind(self, cur_node,actor):
        
        if cur_node:
                  
            
            self._actorfind(cur_node.left,actor)
            
            for i in  cur_node.cast.show():
                if i == actor :
                    print("*******  ACTOR WORK IN THIS MOVIE *******")
                    print("\n")
                    print("The release year of the Movie : " + str(cur_node.year))
                    print("Title of Movie : " + str(cur_node.title))
                    print("Rating of the Movie : " + str(cur_node.rating))
                    print("Duration of Movie : " + str(cur_node.duration))
                    print("Cast of the Movie : ")
                    cur_node.cast.print_list()
                   
                    print("\n")
            self._actorfind(cur_node.right,actor)

    def duoyear(self,Iyear,Fyear):
        
        if self.root:
            self._duoyear(self.root,Iyear,Fyear)
            
            return ("No More Available")
    
    def _duoyear(self, cur_node,Iyear,Fyear):
        
        
        if cur_node:
            
        
            self._duoyear(cur_node.left,Iyear,Fyear)
            if cur_node.year >= Iyear:
                
                
                if cur_node.year <= Fyear:
               
                    print("*******  MOVIE RELEASE FROM "+ Iyear +" TO " + Fyear + "  *******")
                    print("\n")
                    print("The release year of the Movie : " + str(cur_node.year))
                    print("Title of Movie : " + str(cur_node.title))
                    print("Rating of the Movie : " + str(cur_node.rating))
                    print("Duration of Movie : " + str(cur_node.duration))
                    print("Cast of the Movie : ")
                    cur_node.cast.print_list()    
                    print("\n")               
                 
            self._duoyear(cur_node.right,Iyear,Fyear)


    def __deleteNodeHelper(self, node, key):
        if node == None: 
            return node
        elif key < node.title:
            node.left = self.__deleteNodeHelper(node.left, key)
        elif key > node.title:
            node.right = self.__deleteNodeHelper(node.right, key)
        else:
            if node.left == None and node.right == None:
                node = None
            elif node.left == None:
                temp = node
                node = node.right
            elif node.right == None:
                temp = node
                node = node.left
            else:
                temp = self.minimum(node.right)
                node.title = temp.title
                node.right = self.__deleteNodeHelper(node.right, temp.data)
        return node

    def minimum(self, node):                  
        while node.left != None:        
            node = node.left

        return node
    def deleteNode(self, data):
        print("******* " + f"{data} DELETED SUCCESSFILLY *******")
        return self.__deleteNodeHelper(self.root, data)


    def actorfind(self,actor):
        if self.root:
            self._actorfind(self.root,actor)
        else:
            return False

   
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node != None:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def show(self):
    
        count = []
        cur_node = self.head

        while cur_node:
            count.append(cur_node.data)
            cur_node = cur_node.next
        return count

bst= BST()

ShapeOfWater = LinkedList()
ShapeOfWater.append("Sally Hawkins")
ShapeOfWater.append("Michael Shannon")
ShapeOfWater.append("Richard Jenkins")
ShapeOfWater.append("Octavia Spencer")
ShapeOfWater.append("Michael Stuhlbarg")
bst.insert("2013", "Shape Of Water", "3:42:50", "NR", ShapeOfWater)


Babylyon = LinkedList()
Babylyon.append("Margo Martindale ")
Babylyon.append("Riki Lindhome ")
Babylyon.append("Benito Martinez ")
Babylyon.append("Bruce MacVittie ")
Babylyon.append("David Powledge ")
Babylyon.append("Joe D'Angerio ")
bst.insert("2017", "Baby lyon", "2:22:10", "PG", Babylyon)


TheShining = LinkedList()
TheShining.append("Steve Blum ")
TheShining.append("Brianne Brozey ")
TheShining.append("Melissa Fahn ")
TheShining.append("Barbara Goodson ")
TheShining.append("Steve Kramer ")
bst.insert("1969", "The Shining", "2:22:50", "PG-16", TheShining)


TheSixthSense = LinkedList()
TheSixthSense.append("Bruce Willis ")
TheSixthSense.append("Haley Joel Osment ")
TheSixthSense.append("Toni Collette ")
TheSixthSense.append("Trevor Morgan ")
TheSixthSense.append("Peter Anthony Tambakis ")
bst.insert("1996", "The Sixth Sense", "3:14:40", "R", TheSixthSense)


ShawasankRedemtion = LinkedList()
ShawasankRedemtion.append("Tim Robbins ")
ShawasankRedemtion.append("Morgan Freeman ")
ShawasankRedemtion.append("Bob Gunton ")
ShawasankRedemtion.append("William Sadler ")
ShawasankRedemtion.append("Clancy Brown ")
bst.insert("1994", "Shawasank Redemtion", "2:52:50", "PG-18", ShawasankRedemtion)


Rocky = LinkedList()
Rocky.append("Sylvester Stallone")
Rocky.append("Talia Shire")
Rocky.append("Burt Young")
Rocky.append("Carl Weathers")
bst.insert("1973", "Rocky", "3:41:10", "NR", Rocky)


Driver = LinkedList()
Driver.append("Ryan O'Neal")
Driver.append("Bruce Dern")
Driver.append("Isabelle Adjani")
Driver.append("Ronee Blakley")
bst.insert("2011", "Driver", "1:54:12", "PG-12", Driver)


JusticeLeague = LinkedList()
JusticeLeague.append("Ben Affleck")
JusticeLeague.append("Henry Cavill")
JusticeLeague.append("Amy Adams")
JusticeLeague.append("Gal Gadot")
JusticeLeague.append("Ezra Miller")
bst.insert("2015", "Justice League", "3:15:20", "PG", JusticeLeague)


Departed = LinkedList()
Departed.append("Leonardo DiCaprio")
Departed.append("Matt Damon")
Departed.append("Jack Nicholson")
Departed.append("Mark Wahlberg")
Departed.append("Martin Sheen")
Departed.append("Ray Winstone")
bst.insert("2018", "Departed", "3:15:23", "G", Departed)


Parasite = LinkedList()
Parasite.append(" Kang-ho Song")
Parasite.append("Sun-kyun Lee")
Parasite.append("Yeo-jeong Jo")
Parasite.append("Woo-sik Choi")
Parasite.append(" So-dam Park")
bst.insert("2019", "Parasite", "3:5:44", "R", Parasite)


ToyStory = LinkedList()
ToyStory.append("Tom Hanks")
ToyStory.append("Tim Allen")
ToyStory.append("Don Rickles")
ToyStory.append("Jim Varney")
ToyStory.append("Wallace Shawn")
bst.insert("1995", "Toy Story", "3:2:45", "NR", ToyStory)


SchindlerList = LinkedList()
SchindlerList.append("Liam Neeson")
SchindlerList.append("Ben Kingsley")
SchindlerList.append("Ralph Fiennes")
SchindlerList.append("Embeth Davidtz")
SchindlerList.append("Jonathan Sagall")
bst.insert("1993", "Schindler List", "3:2:45", "NR", SchindlerList)


PulpFiction = LinkedList()
PulpFiction.append("John Travolta")
PulpFiction.append("Samuel L. Jackson")
PulpFiction.append("Uma Thurman")
PulpFiction.append("Harvey Keitel")
PulpFiction.append("Tim Roth")
bst.insert("1999", "Pulp Fiction", "3:2:15", "PG-18", PulpFiction)


Seven = LinkedList()
Seven.append("Brad Pitt")
Seven.append("Morgan Freeman")
Seven.append("Gwyneth Paltrow")
Seven.append("John C. McGinley")
Seven.append("David Fincher")
bst.insert("1995", "Seven", "3:2:45", "PG-18", Seven)

SevenSamurai = LinkedList()
SevenSamurai.append("Toshiro Mifune")
SevenSamurai.append("Takashi Shimura")
SevenSamurai.append("Keiko Tsushima")
SevenSamurai.append("Isao Kimura")
SevenSamurai.append("Daisuke Katō")
bst.insert("1954", "Seven Samurai", "3:2:25", "G", SevenSamurai)


SpiritedAway = LinkedList()
SpiritedAway.append("Rumi Hiiragi")
SpiritedAway.append("Miyu Irino")
SpiritedAway.append("Mari Natsuki")
SpiritedAway.append("Bunta Sugawara")
SpiritedAway.append("Horsti")
bst.insert("2001", "Spirited Away", "3:2:35", "PG", SpiritedAway)


LifeIsBeautiful = LinkedList()
LifeIsBeautiful.append("Roberto Benigni")
LifeIsBeautiful.append("Nicoletta Braschi")
LifeIsBeautiful.append("Giorgio Cantarini")
LifeIsBeautiful.append("Giustino Durano")
LifeIsBeautiful.append("Horst Buchholz ")
bst.insert("1991", "Life Is Beautiful", "2:2:45", "G", LifeIsBeautiful)


TheGreenMile = LinkedList()
TheGreenMile.append("Tom Hanks")
TheGreenMile.append("David Morse")
TheGreenMile.append("Bonnie Hunt")
TheGreenMile.append("Michael Clarke Duncan")
TheGreenMile.append("James Cromwell")
bst.insert("1999", "The Green Mile", "3:2:25", "PG-18", TheGreenMile)




Goodfellas = LinkedList()
Goodfellas.append("Robert De Niro")
Goodfellas.append("Ray Liotta")
Goodfellas.append("Joe Pesci")
Goodfellas.append("Lorraine Bracco")
Goodfellas.append("Paul Sorvino")
bst.insert("1989", "Good fellas", "3:32:10", "NR", Goodfellas)


ForrestGump = LinkedList()
ForrestGump.append("Tom Hanks")
ForrestGump.append(" Robin Wright")
ForrestGump.append("Gary Sinise")
ForrestGump.append("Mykelti Williamson ")
ForrestGump.append("Sally Field")
bst.insert("1995", "Forrest Gump", "2:22:12", "PG-12", ForrestGump)


CityofGod = LinkedList()
CityofGod.append(" Alexandre Rodrigues")
CityofGod.append("Leandro Firmino da Hora")
CityofGod.append("Jonathan Haagensen")
CityofGod.append("Phellipe Haagensen")
CityofGod.append("Douglas Silva")
bst.insert("1986", "City Of God", "3:25:45", "G", CityofGod)


FightClub = LinkedList()
FightClub.append("Brad Pitt")
FightClub.append("Edward Norton")
FightClub.append("Helena Bonham Carter")
FightClub.append("Meat Loaf Aday")
FightClub.append("Jared Leto")
FightClub.append("James Haygood")
bst.insert("1999", "Fight Club", "2:21:45", "PG-16", FightClub)

Streetfighter = LinkedList()
Streetfighter.append("Jean-Claude Van Damme")
Streetfighter.append("Raul Julia")
Streetfighter.append("Ming-Na Wen ")
Streetfighter.append("Damian Chapa")
Streetfighter.append("Kylie Minogue ")

bst.insert("2015", "Street Fighter", "2:10:45", "PG", Streetfighter)


HarryPotterandtheDeathlyHallowsPart2 = LinkedList()
HarryPotterandtheDeathlyHallowsPart2.append("Ralph Fiennes")
HarryPotterandtheDeathlyHallowsPart2.append("Michael Gambon")
HarryPotterandtheDeathlyHallowsPart2.append("Alan Rickman")
HarryPotterandtheDeathlyHallowsPart2.append("Daniel Radcliffe")
HarryPotterandtheDeathlyHallowsPart2.append("Rupert Grint")
bst.insert("2011","Harry Porter Deathly Hallows","3:50:4","PG-12",HarryPotterandtheDeathlyHallowsPart2)

Angelique = LinkedList()
Angelique.append("Michèle Mercier")
Angelique.append("Robert Hossein")
Angelique.append("Jean Rochefort")
Angelique.append("Claude Giraud")
Angelique.append("Giuliano Gemma")
bst.insert("2002","Angelique","3:21:45","R",Angelique)


MeetJoeBlack = LinkedList()
MeetJoeBlack.append("Brad Pitt")
MeetJoeBlack.append("Anthony Hopkins")
MeetJoeBlack.append("Claire Forlani")
MeetJoeBlack.append("Jake Weber")
MeetJoeBlack.append("Marcia Gay Harden")
bst.insert("2004","Meet Joe Black","2:2:45","R",MeetJoeBlack)


TheNotebook = LinkedList()
TheNotebook.append("Tim Ivey")
TheNotebook.append("Starletta DuPois")
TheNotebook.append("Gena Rowlands")
TheNotebook.append("James Garner")
TheNotebook.append("Anthony-Michael Q. Thomas")
bst.insert("2005","The Notebook","4:2:45","PG-17",TheNotebook)



QuantumofSolace = LinkedList()
QuantumofSolace.append("Daniel Craig")
QuantumofSolace.append("Olga Kurylenko")
QuantumofSolace.append("Mathieu Amalric")
QuantumofSolace.append("Judi Dench")
QuantumofSolace.append("Giancarlo Giannini")
bst.insert("2006","Quantom Of Solace","1:42:45","PG",QuantumofSolace )


CocoBeforeChanel = LinkedList()
CocoBeforeChanel.append("Audrey Tautou")
CocoBeforeChanel.append("Benoît Poelvoorde")
CocoBeforeChanel.append("Alessandro Nivola")
CocoBeforeChanel.append("Marie Gillain")
CocoBeforeChanel.append("Emmanuelle Devos")
bst.insert("2007","Coco Before Chanel","2:22:15","NR",CocoBeforeChanel)


MemoirsofaGeisha = LinkedList()
MemoirsofaGeisha.append("Suzuka Ohgo")
MemoirsofaGeisha.append("Togo Igawa")
MemoirsofaGeisha.append("Mako")
MemoirsofaGeisha.append("Samantha Futerman")
MemoirsofaGeisha.append("Elizabeth Sung")
bst.insert("1965","Memoirs Of AGeisha","2:21:45","G",MemoirsofaGeisha)



PiratesoftheCaribbeanAtWorldsEnd = LinkedList()
PiratesoftheCaribbeanAtWorldsEnd.append("Johnny Depp")
PiratesoftheCaribbeanAtWorldsEnd.append("Geoffrey Rush")
PiratesoftheCaribbeanAtWorldsEnd.append("Orlando Bloom")
PiratesoftheCaribbeanAtWorldsEnd.append("Keira Knightley")
PiratesoftheCaribbeanAtWorldsEnd.append("Jack Davenport")
bst.insert("2008","Pirates Of The Caribbean At Worlds End","","PG",PiratesoftheCaribbeanAtWorldsEnd )


CasinoRoyale = LinkedList()
CasinoRoyale.append("Daniel Craig")
CasinoRoyale.append("Eva Green")
CasinoRoyale.append("Mads Mikkelsen")
CasinoRoyale.append("Judi Dench")
CasinoRoyale.append("Jeffrey Wright")
bst.insert("2014","Casino Royale","2:21:10","PG-12",CasinoRoyale)





while (True):
    print( )
    print(" 1: List all Movies")
    print(" 2: Find a Movie by Title")
    print(" 3: Add a Movie")
    print(" 4: Delete a Movie")
    
    print(" 5: Find the Movies between specific years" )
    print(" 6: Find Movies by year")
    print(" 7: Find Movies by ratings")
    
    print(" 8: Find Movies by Actor name")

    print(" 9: Exit")
    choice = int(input("Select your Option : "))
    
    if (choice == 9): 
        sys.exit()
    
    if(choice==4):
        print("Enter the movie title to delete it : ")
        movie = input()
        bst.deleteNode(movie)
        
    if(choice==8):
        print("Enter the actor name: ")
        actor= input()
        print(bst.actorfind(actor))
        
    if(choice == 3):
        print("Enter movie title: ")
        title= input()
        print("Enter movie release year: ")
        year= input()
        print("Enter the duration of The movie: ")
        Duration= input()
        print("Enter rating of the movie: ")
        Raing= input()
        # print("Enter the cast of the movie: ")
        # cast=input()
        # temp=cast
        # temp=title
        # cast =temp
        cast = LinkedList()
        arr = []
        n = int(input("Total cast members? : "))

        print("\n")
        for i in range(0, n):
            print("Enter name of cast member: ", [i+1], ":")
            item = input()
            arr.append(item)
        for i in arr:
            cast.append(i)
        print(bst.insert(year,title,Duration,Raing,cast))
    
    if (choice==2):
        print("Enter the Movie title: ")
        title2= input()
        print("\n")
        print("MOVIE DETAILS : ")
        bst.find(title2)
        print('\n')

    if (choice==1):
        print("\n")
        print("*********  LISTING ALL MOVIES  ***********")
        bst.inorder_print_tree()

    if (choice==6):
        print("Enter the Movie release year: ")
        year= input()
        bst.year(year)  

    if (choice==7):
        print("Enter the Movie ratings: ")
        ratings= input()
        bst.ratings(ratings)
        
    if (choice==5):
        print("Starting year: ")
        Initial=input()
        print("Ending year: ")
        Final=input()
        print(f"Total Movies between", Initial, "To",Final  )
        print(bst.duoyear(Initial,Final)) 