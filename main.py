def m():
    print("1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9".format(*l))
    print("Chaque case est affectée a un numero, entrez le numero de la case voulue pour jouer.")
    j1 = input("Nom du joueur 1 = ")
    j2 = input("Nom du joueur 2 = ")
    d = {"1":0,"2":1,"3":2,"4":3,"5":4,"6":5,"7":6,"8":7,"9":8}
    score = [0,0]
     
    def playm():

     l=[" "," "," "," "," "," "," "," "," "]
     def printt():
       print("{}|{}|{}\n-+-+-\n{}|{}|{}\n-+-+-\n{}|{}|{}".format(*l))
     printt()
     
     for i in range(9):
        if " " not in l:
            print("Egalite !\nScore : {}-{}".format(score[0],score[1]))
            return
            break
        c1 = input("Tour de {} > ".format(j1))
        if l[d[c1]] == " ":
         print(l[d[c1]])
         l[d[c1]] = "X"

        elif l[d[c1]] != " ":

         while True:
            print("Cette case est deja occupee.")
            c1 = input("Tour de {} > ".format(j1))
            
            if l[d[c1]] == " ":
                
                l[d[c1]] = "X"
                
                break
            else:
                pass
        printt()
        if l[0]==l[1]==l[2]=="X" or l[6]==l[7]==l[8]=="X" or l[2]==l[5]==l[8]=="X" or l[0]==l[3]==l[6]=="X" or l[3]==l[4]==l[5]=="X" or l[0]==l[4]==l[8]=="X" or l[2]==l[4]==l[6]=="X" or l[1]==l[4]==l[7]=="X":
        
            j = j1
            score[0] = score[0] + 1
            print("{} a gagne !\nScore : {}-{}".format(j,score[0],score[1]))
            l=[" "," "," "," "," "," "," "," "," "]
            return
            break

        if " " not in l:
            print("Egalite !\nScore : {}-{}".format(score[0],score[1]))
            return
            break
        c2 = input("Tour de {} > ".format(j2))
        if l[d[c2]] == " ":
         l[d[c2]] = "O"
        
        elif l[d[c2]] != " ":

         while True:
            print("Cette case est déja occupee.")
            c2 = input("Tour de {} > ".format(j2))
            
            if l[d[c2]] == " ":
                
                l[d[c2]] = "O"
                break
            else:
                pass
        printt()
        if l[0]==l[1]==l[2]=="O" or l[6]==l[7]==l[8]=="O" or l[2]==l[5]==l[8]=="O" or l[0]==l[3]==l[6]=="O" or l[3]==l[4]==l[5]=="O" or l[0]==l[4]==l[8]=="O" or l[2]==l[4]==l[6]=="O" or l[1]==l[4]==l[7]=="O":
        
            j = j2
            score[1] = score[1] + 1
            print("{} a gagne !\nScore : {}-{}".format(j,score[0],score[1]))
            l=[" "," "," "," "," "," "," "," "," "]
            return
            break

    playm()
    while True:
        

        print("1. Continuer / 2. Arreter")
        chh = input(">>> ")
        if ch == "1":
            playm()
        if ch == "2":
            return
            break
