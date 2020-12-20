scores={"A":5,"B":4,"C":3,"D":2,"E":1,"F":0}

# Given the players list w r t its team with  initial score zero
teams={"Gyrhuna":[{"Jaons Diak":0},{"Susu":0}],
       "Achni":[{"Meilong":0},{"Tianlong":0}],
       "Bathar":[{"Pakhangba":0},{"Poubi Lai Paphal":0}]}

bonusteam={"Gyrhuna":0,"Achni":0,"Bathar":0}
teamscore={"Gyrhuna":0,"Achni":0,"Bathar":0}

playerscores={}

def won(teamscore):
    global scores
    for r in range(1,10):
        print('Round',r)
        print("Select the score from {A,B,C,D,E,F}")
        for team in teams:
            bonuscheck=[]
            bonusplayer=[]
            teamscore[team]=0
            
            for pl in teams[team]:
                key, value = list(pl.items())[0]
                temp=0
                playerscore=input("Enter the score of " +str(key)+" from team "+team+" : ")
                if playerscore not in (["A","B","C","D","E","F"]):
                    print("Please select the score from {A,B,C,D,E,F}")
                    exit(0)
                
                bonuscheck.append(playerscore)
                bonusplayer.append(key)
                prefix=key
                
                if prefix  not in  playerscores:
                    playerscores[prefix]=scores[playerscore]
                    #print(playerscores[prefix])
                else:
                    playerscores[prefix]+=scores[playerscore]
                    temp=playerscores[prefix]
                teamscore[team]+=playerscores[prefix]

            if(len(set(bonuscheck))==1):
                #print("has bonus")
                bonusteam[team]+=2
            teamscore[team]+=bonusteam[team]

        scores={key:value+1 if(key!="F") else value for key,value in(scores.items())}
                
        for (key, value) in teamscore.items():
            if value >= 60 :
                print('*'*35)
                print("Round",r,"Result")
                print('Player\'s Scores :',playerscores)
                print('Bonus :',bonusteam)
                print('Team\'s Score',teamscore)
                return "Game over. {} won by {} score!!!".format(key,value)
        else:
            print('*'*35)
            print("Round",r,"Result")

        print('Player\'s Scores :',playerscores)
        print('Bonus :',bonusteam)
        print('Team\'s Score',teamscore)
        print('*'*35)
            
w=won(teamscore)
print(w)


