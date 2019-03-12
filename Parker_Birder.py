import wikipedia

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
                birds[maintype][info[0].lower()] = info[1:]
    return birds

# this prints the entirety of the bird text file
# currently only ~100 birds
def printdict(birds):
    for category in sorted(birds):
        print ("** "+ category +" **\n")
        for bird in sorted(birds[category]):
            info = ", ".join(birds[category][bird]) # join elements in list by ", "
            print("%-30s\t%s" % (bird.title(), info)) # format line
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
    searchingbird = searchingbird.strip().lower()
    for category in sorted(birds):
        if searchingbird in birds[category]:
            # return getwikiinfo(searchingbird)
            return getwikisummary(searchingbird)
    return "NOT A VALID BIRD NAME"

def main():
    birds = makedict("birds.txt")
    printdict(birds)

    user = raw_input("Do you want info on a bird? (y/n) ")
    while (user[0].lower() == "y"):
        bird = raw_input("Enter bird name: ")
        print(getbirdinfo(bird, birds))

        user = raw_input("Do you want info on another bird? (y/n) ")
        
    print("Thank you for using Birdr. Goodbye!")

if __name__=="__main__":
    main()
