from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import time
import pygame

import tkinter.messagebox
class MyGUI:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("600x700+100+100")
        self.root.config()
        self.root.resizable(width=False,height=False)

        self.currentPage=StringVar()
        self.currentPage.set("Main Menu")
        self.root.title("Restaurant Simulator: " + self.currentPage.get())
        # Main Menu
        self.moni = 20




        # music player
        pygame.mixer.init()
        pygame.mixer.music.load("music/mm.mp3")
        pygame.mixer.music.play(loops=-1)

        self.currentPage.set("Main Menu")
        self.root.title("Restaurant Simulator: " + self.currentPage.get())
        self.musicFrame = Frame(self.root,width=600,height=120)
        self.musicFrame.place(x=0,y=580)

        self.mainMenu = Frame(self.root, width=600, height=580, bg="red")
        self.mainMenu.pack()
        self.mainMenu.propagate(0)

        self.mmTitle = Label(self.mainMenu, text="Main Menu", font=("Baveuse", "40"),bg="red")
        self.mmTitle.pack()

        self.bbqButton = Button(self.mainMenu, text="BBQ Restaurant", font=("arial",20),command=self.BBQ,width=13)
        self.bbqButton.pack()

        self.bobaButton = Button(self.mainMenu, text="Boba Tea", font=("arial",20),command=self.boba,width=13)
        self.bobaButton.pack()



        self.cheat=Entry(self.musicFrame,width=10,font=14)
        self.cheat.place(x=480,y=30)



        self.showMoney=Label(self.musicFrame,text="Money:$" + format(self.moni,".2f"),font=15)
        self.showMoney.place(x=480,y=10)

        self.clearButton=Button(self.musicFrame,text="reset money",command=self.clearMoney)
        self.clearButton.place(x=520,y=60)
        self.cheatButton = Button(self.musicFrame, text="Add", command=self.cheata)
        self.cheatButton.place(x=480,y=60)

        self.songName = Label(self.musicFrame, text="Playing: " + "Main Menu song",font=("comic sans ms",17),height=3)
        self.songName.place(x=0,y=0)


        self.volumeSlider = ttk.Scale(self.musicFrame, from_=1, to=0, orient=VERTICAL,value=1, command=self.volume, length=100)
        self.volumeSlider.place(x=450,y=0)
        self.root.mainloop()

    def mmFrame(self):
        sound = pygame.mixer.Sound("sfx/button2.mp3")
        sound.play()
        self.songName.config(text="Playing Main Menu song")
        pygame.mixer.music.load("music/mm.mp3")
        pygame.mixer.music.play(loops=-1)
        self.mainMenu.destroy()
        self.currentPage.set("Main Menu")
        self.root.title("Restaurant Simulator: " + self.currentPage.get())


        self.mainMenu = Frame(self.root, width=600, height=580, bg="red")
        self.mainMenu.pack()
        self.mainMenu.propagate(0)

        self.mmTitle = Label(self.mainMenu, text="Main Menu", font=("Baveuse", "40"),bg="red")
        self.mmTitle.pack()

        self.bbqButton = Button(self.mainMenu, text="BBQ Restaurant", font=("arial",20),command=self.BBQ,width=13)
        self.bbqButton.pack()

        self.bobaButton = Button(self.mainMenu, text="Boba Tea", font=("arial",20),command=self.boba,width=13)
        self.bobaButton.pack()

    def clearMoney(self):
        sound = pygame.mixer.Sound("sfx/button2.mp3")
        sound.play()
        self.moni=0
        self.showMoney.config(text="Money$:" + format(self.moni,".2f"))


    def cheata(self):
        sound = pygame.mixer.Sound("sfx/pay.mp3")
        sound.play()
        time.sleep(1)
        sound.stop()
        self.moni+= float(self.cheat.get())

        self.showMoney.config(text="Money$:" + format(self.moni,".2f"))

    def tabulaRasa(self):
        self.mainMenu.destroy()
        self.mainMenu = Frame(self.root, width=600, height=580,bg="red")
        self.mainMenu.pack()
        self.mainMenu.propagate(0)

    def addFood(self):
        sound = pygame.mixer.Sound("sfx/button2.mp3")
        sound.play()
        item = self.choice.get()
        print(item)
        self.food = item.split("$", 1)
        print(self.food)
        price = float(self.food[1])
        self.food = self.food[0]

        if(self.topping1.get() or self.topping2.get() or self.topping3.get() or self.topping4.get()):
            topping="W/"

            if(self.topping1.get()):
                price += 0.50
                topping += "T.Pearls "

            if (self.topping2.get()):
                price += 0.50
                topping += "C.Jelly "
            if (self.topping3.get()):
                price += 0.50
                topping += "BrSgr.Pearl "
            if (self.topping4.get()):
                price += 0.50
                topping += "G.Jelly "
        else:
            topping=""

        self.order.append(self.food)
        self.total += price
        self.showTotal.config(text="Total :$" + format(self.total,'.2f'))
        self.bobaReceipt.insert(END,self.food + " " + topping + "$"+ str(price))
    def addFoodAlt(self):
        sound = pygame.mixer.Sound("sfx/button2.mp3")
        sound.play()
        if (self.bbq1Ch.get()):
            self.bbqReceipt.insert(END,self.bbq1.cget('text'))
            self.total +=11.50
            self.order.append(self.bbq1.cget('text'))
        if (self.bbq2Ch.get()):
            self.bbqReceipt.insert(END, self.bbq2.cget('text'))
            self.total += 8.99
            self.order.append(self.bbq2.cget('text'))
        if (self.bbq3Ch.get()):
            self.bbqReceipt.insert(END, self.bbq3.cget('text'))
            self.total += 7.50
            self.order.append(self.bbq3.cget('text'))
        if (self.bbq4Ch.get()):
            self.bbqReceipt.insert(END, self.bbq4.cget('text'))
            self.total += 4.99
            self.order.append(self.bbq4.cget('text'))
        if (self.bbq5Ch.get()):
            self.bbqReceipt.insert(END, self.bbq5.cget('text'))
            self.total += 5.50
            self.order.append(self.bbq5.cget('text'))
        if (self.bbq6Ch.get()):
            self.bbqReceipt.insert(END, self.bbq6.cget('text'))
            self.total +=13.69
            self.order.append(self.bbq6.cget('text'))
        self.showTotal.config(text="Total :$" + format(self.total,'.2f'))
        self.cookFood()
    def removeFood(self):
        self.order.remove(self.food)
        removeMoni = self.bobaReceipt.get(ANCHOR)
        removeMoni = removeMoni.split("$")
        removeMoni = removeMoni[1]
        self.total -= float(removeMoni)
        self.showTotal.config(text="Total :$" + format(self.total,'.2f'))
        sound = pygame.mixer.Sound("sfx/button3.mp3")
        sound.play()
        self.bobaReceipt.delete(ANCHOR)

    def payFood(self):
        if (self.moni - self.total <0 ):
            tkinter.messagebox.showinfo("Hey Deadbeat", "You do not have enough money")
        elif(len(self.order)>0):
            sound = pygame.mixer.Sound("sfx/pay.mp3")
            sound.play()
            time.sleep(1)
            sound.stop()
            self.moni -=self.total
            self.showMoney.config(text="Money$:" + format(self.moni,".2f"))
            self.bobaReceipt.delete(0,END)
            self.total=0
            self.showTotal.config(text="Total :$" + format(self.total,'.2f'))
            self.cookFood()

    def cookFood(self):
        self.root2 =Toplevel()
        self.root2.geometry("300x200+800+0")
        progress = Label(self.root2,text="")
        progress.pack()
        load = ttk.Progressbar(self.root2, orient=HORIZONTAL,length=100, mode='determinate')
        load.pack()
        for x in self.order:

            if x=="Water":
                foodTime=10
                sound = pygame.mixer.Sound("sfx/watersfx.mp3")
            elif self.currentPage.get()=="Texas Big Gun America Town":
                foodTime=30
                sound = pygame.mixer.Sound("sfx/bbq.mp3")
            else:
                foodTime=15
                sound = pygame.mixer.Sound("sfx/bobasfx.mp3")
            count = foodTime
            for i in range(foodTime):
                if i ==0:
                    sound.play()
                time.sleep(1)
                self.root2.update_idletasks()
                count -=1
                load['value'] += 100/foodTime
                progress.config(text="Preparing your:" + x + ", done in " + str(count))



            sound.stop()

            progress.config(text=x + " is done!")
            self.showFood(x)
        if (self.currentPage.get() == "Texas Big Gun America Town" and len(self.order)>0):
            self.payUp = Button(self.mainMenu, text="Pay", command=self.bbqPay)
            self.payUp.place(x=280,y=420)
            self.showTotal.config(text="Total :$" + format(self.total,'.2f'))
        self.order.clear()
        self.root2.quit()
        self.root2.destroy()
        self.root2.mainloop()
    def volume(self,s):
        pygame.mixer.music.set_volume(self.volumeSlider.get())
    def doubleExit(self):
        if (self.currentPage.get() == "Texas Big Gun America Town"):
            sound = pygame.mixer.Sound("sfx/nom.mp3")
        else:
            sound = pygame.mixer.Sound("sfx/drink.mp3")
        sound.play()
        self.root3.quit()
        self.root3.destroy()
        time.sleep(2)
    def showFood(self,x):
        self.root3 = Toplevel()
        self.root3.geometry("450x450")
        sound = pygame.mixer.Sound("sfx/done.mp3")
        sound.play()
        whatever = ImageTk.PhotoImage(Image.open(x+".png"))

        foodPic = Label(self.root3, image=whatever)
        foodPic.pack()


        eat = Button(self.root3,text="CONSUME",command=self.doubleExit)
        eat.pack()

        self.root3.mainloop()
    def gameOver(self):
        self.tabulaRasa()
        pygame.mixer.music.load("music/over.mp3")
        pygame.mixer.music.play(loops=-1)

        theEnd = Label(self.mainMenu,text="Game Over",font=("Arial",50),bg="red")
        theEnd.pack()
        deadText=Label(self.mainMenu,text="Poor people will not be tolerated.",font=("comic sans ms",28),bg="red")
        deadText.pack()
        quitButt=Button(self.mainMenu,text="Exit",font=("comic sans ms",50),command=self.root.destroy)
        quitButt.pack()
    def bbqPay(self):
        if self.moni - self.total<0:
            sound = pygame.mixer.Sound("sfx/gun.mp3")
            sound.play()
            self.gameOver()
        else:
            sound = pygame.mixer.Sound("sfx/pay.mp3")
            sound.play()
            time.sleep(1)
            sound.stop()
            self.moni -=self.total
            self.showMoney.config(text="Money$:" + format(self.moni,".2f"))

            self.BBQ()
    def boba(self):
        # music player
        sound = pygame.mixer.Sound("sfx/button2.mp3")
        sound.play()
        pygame.mixer.music.load("music/ss.mp3")
        pygame.mixer.music.play(loops=-1)
        self.songName.config(text="Playing: Boba Shop music")
        self.tabulaRasa()
        self.currentPage.set("Boba Place")
        self.root.title("Restaurant Simulator: " + self.currentPage.get())
        self.bobaTitle=Label(self.mainMenu,text="Boba Place",font=("Arial","40"),bg="pink")
        self.bobaTitle.pack()
        self.currentPage.set("Boba Buns")
        self.mainMenu.config(bg="pink")

        self.choice=StringVar()
        self.choice.set("Milk Tea")
        self.rb1=Radiobutton(self.mainMenu,text="Milk Tea - $4.99",value="Milk Tea$4.99",variable=self.choice,bg="pink")
        self.rb1.pack()
        self.rb2=Radiobutton(self.mainMenu,text="Mango Slush - $3.75",value="Mango Slush$3.75",variable=self.choice,bg="pink")
        self.rb2.pack()
        self.rb3=Radiobutton(self.mainMenu,text="Water - $0.00",value="Water$0.00",variable=self.choice,bg="pink")
        self.rb3.pack()
        self.rb4=Radiobutton(self.mainMenu,text="Taro Time - $6.99",value="Taro Time$6.99",variable=self.choice,bg="pink")
        self.rb4.pack()
        self.buyFood=Button(self.mainMenu,text="Add",command=self.addFood,width=5)
        self.buyFood.place(x=90,y=310)
        self.mmButton=Button(self.mainMenu,text="Main Menu",command=self.mmFrame)
        self.mmButton.place(x=20,y=40)
        self.total = 0


        #Toppings
        self.topping1 = IntVar()
        self.topping2 = IntVar()
        self.topping3 = IntVar()
        self.topping4 = IntVar()
        self.topping1.set(0)
        self.topping2.set(0)
        self.topping3.set(0)
        self.topping4.set(0)
        self.cb1 = Checkbutton(self.mainMenu, text="Tapioca Bubble  $0.50", font=14, variable=self.topping1,bg="pink")
        self.cb1.pack()
        self.cb2 = Checkbutton(self.mainMenu, text="Coconut Jelly  $0.50", font=14, variable=self.topping2,bg="pink")
        self.cb2.pack()
        self.cb3 = Checkbutton(self.mainMenu, text="brown sugar pearls  $0.50", font=14, variable=self.topping3,bg="pink")
        self.cb3.pack()
        self.cb4 = Checkbutton(self.mainMenu, text="Grass Jelly  $0.50", font=14, variable=self.topping4,bg="Pink")
        self.cb4.pack()

        #listbox things
        self.bobaReceipt = Listbox(self.mainMenu, width=50)
        self.bobaReceipt.pack(pady=12)
        self.showTotal = Label(self.mainMenu, text=self.total,bg="pink")
        self.showTotal.pack()
        self.deleteFoodButton = Button(self.mainMenu, text="Delete", command=self.removeFood)
        self.deleteFoodButton.place(x=90,y=370)
        self.payButton = Button(self.mainMenu, text="Pay", command=self.payFood,width=5)
        self.payButton.place(x=90,y=420)

        self.order=[]

    def BBQ(self):
        sound = pygame.mixer.Sound("sfx/button2.mp3")
        sound.play()
        pygame.mixer.music.load("music/s&m.mp3")
        pygame.mixer.music.play(loops=-1)
        self.songName.config(text="Playing: BBQ Jazz")
        self.currentPage.set("Texas Big Gun America Town")
        self.root.title("Restaurant Simulator: " + self.currentPage.get())
        self.tabulaRasa()
        self.bbqTitle = Label(self.mainMenu,text="BBQ Place",font=("times new roman","40"),bg="orange")
        self.bbqTitle.pack()
        self.mainMenu.config(bg="orange")
        self.mmButton = Button(self.mainMenu, text="Main Menu", command=self.mmFrame)
        self.mmButton.place(x=20, y=40)
        self.total = 0
        self.order = []
        self.bbq1Ch = IntVar()
        self.bbq2Ch = IntVar()
        self.bbq3Ch = IntVar()
        self.bbq4Ch = IntVar()
        self.bbq5Ch = IntVar()
        self.bbq6Ch = IntVar()
        self.bbq1Ch.set(0)
        self.bbq2Ch.set(0)
        self.bbq3Ch.set(0)
        self.bbq4Ch.set(0)
        self.bbq5Ch.set(0)
        self.bbq6Ch.set(0)


        self.bbq1 = Checkbutton(self.mainMenu,text="BBQ Ribs $11.50",variable=self.bbq1Ch,bg="orange")
        self.bbq1.pack()
        self.bbq2 = Checkbutton(self.mainMenu, text="Burger $8.99",variable=self.bbq2Ch,bg="orange")
        self.bbq2.pack()
        self.bbq3 = Checkbutton(self.mainMenu, text="Chicken Wings $7.50",variable=self.bbq3Ch,bg="orange")
        self.bbq3.pack()
        self.bbq4 = Checkbutton(self.mainMenu, text="Corn Bread $4.99",variable=self.bbq4Ch,bg="orange")
        self.bbq4.pack()
        self.bbq5 = Checkbutton(self.mainMenu, text="Hot Dog $5.50",variable=self.bbq5Ch,bg="orange")
        self.bbq5.pack()
        self.bbq6 = Checkbutton(self.mainMenu, text="Salad $13.69",variable=self.bbq6Ch,bg="orange")
        self.bbq6.pack()

        self.bbqReceipt = Listbox(self.mainMenu,width=40)
        self.bbqReceipt.pack()
        self.showTotal = Label(self.mainMenu, text=self.total, bg="orange")
        self.showTotal.pack()

        self.orderButton = Button(self.mainMenu, text="Order", command=self.addFoodAlt, width=5)
        self.orderButton.place(x=200, y=420)



GUI=MyGUI()