import wikipedia
import string
import random

# Birder - run with: python Parker_Birder.py

# make dictionary from text file
def makedict(filename):
    with open(filename, 'r') as f:
        birds = {}
        maintype = ""
        for line in f:
            stripped = line.strip() # remove \n at end of line in file
            info = stripped.split(", ")
            if len(info) == 1: # if bird type
                birds[stripped] = {}
                maintype = stripped
            else: # rest of line is info to put in dict
                birds[maintype][info[0]] = info[1:]
    return birds

# this prints the entirety of the bird text file
# currently only ~100 birds
def printdict(birds):
    for category in sorted(birds):
        print ("** "+ category +" **\n")
        for bird in sorted(birds[category]):
            info = ", ".join(birds[category][bird]) # join elements in list by ", "
            print("%-30s\t%s" % (bird, info)) # format line
        print("")

# right now all this does is returns just the summary of the wiki page
# based on the english name of the bird, not the latin name
def getwikiinfo(birdname):
    page = wikipedia.page(birdname)
    return wikipedia.summary(page)

def getwikisummary(birdname):
    page = wikipedia.page(birdname)
    summary = wikipedia.summary(page)
    splits = summary.split("\n")
    full = ""
    for paragraph in splits:
        sents = paragraph.split(".")
        full += sents[0] + ". "
    return full

# searches for bird in list or tells user name is invalid
def getbirdinfo(searchingbird, birds):
    searchingbird = string.capwords(searchingbird.strip().lower())
    for category in sorted(birds):
        if searchingbird in birds[category]:
            # return getwikiinfo(searchingbird)
            return getwikisummary(searchingbird)
    return "NOT A VALID BIRD NAME"

def getbirdinfobyname(birds):
    user = raw_input("Do you want info on a bird? (y/n) ")
    while (user[0].lower() == "y"):
        bird = raw_input("\nEnter bird name: ")
        print(getbirdinfo(bird, birds))

        user = raw_input("\nDo you want info on another bird? (y/n) ")

def getrandombird(birds):
    # get random category
    categories = birds.keys()
    category = categories[random.randint(0, len(categories)-1)]

    # get random bird in category
    birdlist = birds[category].keys()
    bird = birdlist[random.randint(0, len(birdlist)-1)]

    # print("category: "+ category + ", bird: "+ bird)

    return bird

def swipebirds(birds):
    yesbirds = set()
    nobirds = set()

    while True:
        bird = getrandombird(birds)
        while (bird in yesbirds or bird in nobirds): # make sure bird not seen yet
            bird = getrandombird(swipebirds)

        print("Bird: " + bird)
        user = raw_input("Press 'M' for more info, 'S' to skip, or 'X' to stop swiping: ")
        while (user != "M" and user != "S" and user != "X"):
            print("INVALID OPTION, TRY AGAIN")
            user = raw_input("Press 'M' for more info, 'S' to skip, or 'X' to stop swiping: ")

        if user.upper() == "M":
            yesbirds.add(bird)
            print(getwikisummary(bird) + "\n")
            # print(getbirdinfo(bird, birds) + "\n")
        elif user.upper() == "S":
            nobirds.add(bird)
            print("")
        else: # 'X' case
            nobirds.add(bird)
            break

    print("\nYour Stats:")
    print ("\nBirds You Liked: " + ", ".join(list(yesbirds)))
    print ("\nBirds You Didn't Like: " + ", ".join(list(nobirds)))


def main():
    birds = makedict("birds.txt")
    # printdict(birds)

    # getbirdinfobyname(birds)

    swipebirds(birds)

    print("\nThank you for using Birdr. Goodbye!")

if __name__=="__main__":
    main()
