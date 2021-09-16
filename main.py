print("Welcome to Weeber land!")

name = input("What might your name be? ")
age = int(input("How old are you? "))


if age >= 18:
    print("Our advanced security system has confirmed you are old enough to play.")
    want_to_play = input("Do you want to play? ").lower()
    if want_to_play == "yes":
      print("Welcome to my game!")

      begin = input("Press enter to continue")

      print("Welcome. You are stranded at an island in the middle of the Pacific Ocean. Your every move will decide your outcome if you survive. There is a cave to your left. There is a treasure chest to your right. Which way do you go? (Left/Right) ")

      left_or_right = input().lower()

      if left_or_right == "left":
        print("You go to the cave and find a talking bird.")
        print("Bird: Hello human. You have found yourself in an unfortunate situation. This island is full of traps. I will guide you through the island so you can escape. My first advice is to not open the treasure chest outside this cave.")
        question2 = input("Listen to the birds advice? (Yes/No) ").lower()
        if question2 == "yes":
          print("You listen to the birds advice")
          print("Bird: Ha! Fool! This island is mine and you cannot escape.")
          attack = input("Attack the bird or run away? (Attack/Run)").lower()
          if attack == "attack":
            print("You hit the bird with a Jab-Right uppercut-Left hook-Right hand and knock the bird out")
            begin = input("Press enter to continue")
            weapon = input("The bird drops a sword and a signal flare. Which do you pick up? (Sword/Flare/Nothing)").lower()


            print("You pick up the", weapon, )
            print("You hear a plane outside and hurry out to see if you can signal it")
            if weapon == "flare":
              print("You use your signal flare to signal the plane down. You get rescured.")
              print("Congradulations, you win!")
            
            elif weapon == "sword":
              print("You run outside and realise you picked up the sword instead of the siganl flare and the plane is already zooming by.")
              print("Don't you feel silly now? You lost.")

            else:
              print("Why didn't you pick up the flare? You question your life choices as you see the plane fly by.")
              print("You lost.")  

  
            


          else:
            print("You run away like the loser you are.")
            print("The End...?")


        else:
          print("You ignore the bird and open the chest outside")  
          begin = input("Press enter to continue")          
          print("You open the chest and it appears to be empty. You look up to find you are not in the island anymore. All you see is white. All the faith I had had had had no effect on the outcome of his life. You got lost into the mysterious ways of the island.")


      else: 
        print("You open the chest and it appears to be empty. You look up to find you are not in the island anymore. All you see is white. All the faith I had had had had no effect on the outcome of his life. You got lost into the mysterious ways of the island.")


    else:
          print("Sorry to hear that. Goodbye")

else:
    print("Our advanced securty system has detected that you are not old enough to play :(")













'''
str - Anything that is in between quotation marks ''
Int - An integer, pretty simple
Float - Any number with a decime
Bool - Any text with that does fancy things. Ex... True, False
'''
# A hashtag will only comment on one line unlike the three quotation marks
# Variables do not need quotation marks
