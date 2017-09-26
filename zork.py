#Zork First Steps
#Author Andrew DiBella
#Date: 9 September 2017

def main():

    #Instance Variables          
    castleBlack = "You are at Castle Black. The Night's Watch is preparing for battle."
    winterfell  = "You are at Winterfell. The Starks welcome you."
    casterlyRock= "You are at Casterly Rock. Good luck with Cersei Lannister"
    dragonstone = "You are in Dragonstone. Don't piss off the dragons."
    ironIslands = "You are on the Iron Islands. Watch out for sharks."
    northWall   = "You are north of the Wall. Watch out for White Walkers."
    score = 0
    location = ""
    character = ""
    
    #Boolean Variables
    vistCasBlack = True
    visitWinterfell = False
    visitCasRock = False
    visitDragonstone = False
    visitIronIslands = False
    visitNorthWall = False
    
    def titleIntro():
        #Title
        print("\t\t\t Game of Thrones\n"
              "\t\t\t=================\n")
        #Back Story
        print("Winter is coming....You've seen the first white walker beyond\n"
              "the wall and wake up from a short coma in Castle Black. You \n"
              "must warn the people of Westeros to prepare for an attack.\n"
              "Who will you tell first? Who's side will you take?...\n"
              "\t======================================================\n")

    def character():
        while True:
            userInput = input("Please choose a character:\n"
                              "Jon Snow\tTyrion Lannister\n"
                              "Arya Stark\tJaime Lannister\n"
                              "Enter character: \n")
            character = userInput.lower()
        
            if character[0:3] == "jon":
                character = "Jon Snow"
                break
            
            if character[0:3] == "ary":
                character = "Arya"
                break
            
            if character[0:3] == "tyr":
                character = "Tyrion"
                break
            
            if character[0:3] == "jai":
                character = "Jaime"
                break
            
            else:
                print("Not valid character name.")

        return character
          
    
        
    
    def conclusion():
        print("You were killed by white walkers and westeros has been overrun"
              "..\n==\n"
              "Copyright (c) Andrew DiBella       Andrew.DiBella1@marist.edu")


    #################
    titleIntro()
    character = character()
    print(character)
    #################
    
    #Castle Black
    location = castleBlack
    print(location+"\n")

    #Winterfell 
    input("Press Enter: Move to next location\n==\n")
    location = winterfell
    score= score +5
    print("Score:" + str(score))
    print(location+"\n")

    #Casterly Rock 
    input("Press Enter: Move to next location\n==\n")
    location = casterlyRock
    score = score +5
    print("Score:" + str(score))
    print(location+"\n")

    #Dragonstone
    input("Press Enter: Move to next location\n==\n")
    location = dragonstone
    score = score +5
    print("Score:" + str(score))
    print(location+"\n")

    #North of the Wall 
    input("Press Enter: Move to next location\n==\n")
    location = northWall
    score = score +5
    print("Score:" + str(score))
    print(location+"\n")

    conclusion()

main()
    
