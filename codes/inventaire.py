from tkinter import *



#creation d'une fonction pour faire appel a l'inventaire
def inventory(player):
    #definition des parametre de bases
    window1 = Tk()
    window1.geometry('450x150')
    window1.title("Inventaire")
    #importation des images+coordonnées
    img = PhotoImage(file="images/Iconecasque.png")
    Label(window1,image=img).grid(column=0,row=2) 
    img1 = PhotoImage(file="images/IconeDegats.png")
    Label(window1,image=img1).grid(column=0,row=4) 
    img2 = PhotoImage(file="images/IconeShield.png")
    Label(window1,image=img2).grid(column=0,row=6) 
    
    txt=Label(window1,text="Stuff Basique : Degats 10 Pv 25")
    txt.grid(column=6,row=2)
    txt1=Label(window1,text="Stuff Degats : Degats 19 Pv 15")
    txt1.grid(column=6,row=4)
    txt2=Label(window1,text="Stuff Tank : Degats 5 Pv 30")
    txt2.grid(column=6,row=6)


    #variable pour savoir quelle stuff est selectionné
    selected = IntVar()
    selected.set(player[6])

    rad1 = Radiobutton(window1,text='First', value=1, variable=selected)
    rad1.grid(column=2, row=2)
    
    rad2 = Radiobutton(window1,text='Second', value=2, variable=selected)
    rad2.grid(column=2, row=4)

    rad3 = Radiobutton(window1,text='Third', value=3, variable=selected)
    rad3.grid(column=2, row=6)


    def clicked():
        if selected.get()==1:
            player[6]=1
            player[0]=10
            player[1]=25
        elif selected.get()==2:
            player[6]=2
            player[0]=19
            player[1]=15
        elif selected.get()==3:
            player[6]=3
            player[0]=5
            player[1]=30
        window1.destroy()

        


    
    #mise en place des boutons
    btn = Button(window1, text="Valide", command=clicked)
    btn.grid(column=4, row=2)
    btn1 = Button(window1, text="Valide", command=clicked)
    btn1.grid(column=4, row=4)
    btn2 = Button(window1, text="Valide", command=clicked)
    btn2.grid(column=4, row=6)

    window1.mainloop()
    return player




