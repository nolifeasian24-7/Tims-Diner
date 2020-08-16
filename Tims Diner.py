#this is currently in the alpha stage, whilst being develpoed it can still function and to a certain extent with no errors. 
import time#time, which allows for sleeping and various other execution manipulations, i used this only for asthetic purpose e.g. time.sleep() in order to allow the program to individially present parts

def restart():
      while True:
            try:
                  x=int(input("please enter the table your sitting at?"))    
                  if x < 1 or x > 10:
                        print("sorry,this table does not exist!")
                        continue
                  else:
                      print("this table is free, please enter your order details after the menu has loaded")
                      break
            except:
                  print("please enter the table number")
def ordering():
      time.sleep(1)#printing menu
      print("here is our menu")
      time.sleep(0.5)
      print("**********************************menu**********************************")
      time.sleep(1)
      print("breakfast:")
      print("all day breakfast(£5.50):code number[1]")
      print("all day breakfast small(£3.50):code number[2]")
      time.sleep(1)
      print("for mains we serve:")
      print("hotdog(£3.00):code number[3]")
      print("burger(£4.00):code number[4]")
      print("cheese burger(£4.25):code number[5]")
      print("chicken goujons(£3.50):code number[6]")
      time.sleep(1)
      print("for extras we serve:")
      print("Fries(£1.75):code number[7]")
      print("salad(£2.20):code number[8]")
      time.sleep(1)
      print("for drinks:")
      print("milkshake(£2.20):code number[9]")
      print("choice of soft drinks(£1.30):code number[10]")
      print("water(£0.90):code number[11]")
      print("and sparkling water(£0.90):code number[12]")
      menu_price = {"ADBL":5.00,"ABDS":3.50,"HOT":3.00,"Burger":4.00,"cheese burger":4.25,"chicken Gouj":3.50,"fries":1.75,"salad":2.20,"milkshake":2.20,"soft drinks":1.30,"water":0.90,"still water":0.90}
      menu_items = {1:"ADBL",2:"ABDS",3:"HOT",4:"Burger",5:"cheese burger",6:"chicken Gouj",7:"fries",8:"salad",9:"milkshake",10:"soft drinks",11:"water",12:"still water"}
      #defining function to allow for repetiton of the following lines 
      total=0
      a=True
      #choice=range(1,12)
      while a==True:
          try:
              incorrect = 0
              select_menu=input("please enter your items in a list seperated by commas. Enter the code number shown next to the item choice")
              z=select_menu.split(",")
              for items in z:
                  items=int(items)
                  #print(items)
                  if items > 0 and items < 13:
                      print("verified...")
                      
                  elif items < 0 or items > 12:
                      print("sorry that item does not exist")
                      incorrect = 1
              print(incorrect)
              if incorrect != 1:
                  a = False
          except ValueError:
              print("please enter the code number next to the menu choices")
              continue
      print("loading")
      print("*")#some random thing to serve as a loading bar, unfortunatley as of this time i have no experience with tkinter
      print("*")
      print("*")
      print("*")
      print("*")
      print("*")
      print("*")
      print("*")
      print("*")
      print("*")
      time.sleep(0.5)
      print(select_menu)
      order=[]
      for items in z:
          order.append(int(items))

      for i in order:
          x = menu_items.get(i)
          print(x)
          price = menu_price.get(x)
          print(price)
          total =float(round(total + price,3))
      print(total)
      print("......")
      file=open("select_menu.txt","w")
      file.write(select_menu)
      file.close()

      file=open("select_menu.txt","r")
      print(file.read())

      file=open("total.txt","w")
      file.write(str(total))
      file.close()

      file=open("total.txt","r")
      print(float(file.read()))
      confirm=input("can you confirm your order to be the final descision?(Yes or No)")
      if confirm=="Yes":
            print("thank you for ordering at tims diner, enjoy your meal!")
            restart()
      elif confirm=="No":
            print("re-enter your table number and items again")
            ordering()
while True:#this while allows the function line42 to re-loop to the beginning of t
      restart()
      ordering()
