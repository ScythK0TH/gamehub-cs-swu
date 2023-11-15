import random
import pygame, sys
import win32con
from win32gui import SetWindowPos
import base64
import requests
import io

regan_url = 'https://raw.githubusercontent.com/ScythK0TH/gamehub-cs-swu/main/gameover.txt'
regan_text = requests.get(regan_url)
regan = regan_text.text

surprise_url = 'https://raw.githubusercontent.com/ScythK0TH/gamehub-cs-swu/main/youlose.txt'
surprise_text = requests.get(surprise_url)
surprise_a = surprise_text.text

warning_url = 'https://raw.githubusercontent.com/ScythK0TH/gamehub-cs-swu/main/warning.txt'
warning_text = requests.get(warning_url)
warning = warning_text.text

animals_e = ['elephant', 'bear',  'wolf', 'tiger', 'penguin', 'rabbit', 'lion', 'monkey','sheep', 'zebra']

fruits_e = ['apple', 'banana', 'grapes', 'mango', 'lime', 'guava', 'orange', 'papaya', 'pear', 'peach', 'strawberry']

elements = ['lithium' , 'hydrogen' ,'kryptonite','sodium', 'platinum' , 'silver' ,'neon' , 'carbon' ,'oxygen' , 'gold']

score = 0

def start():
    item = []
    bonus = False
    cur_diff = ''
    def save_data():
        global score
        nonlocal item
        save = ''
        save += str(score)
        for i in item:
            save += i + ','
        save = save[:len(save) - 1]
        saved_bytes = save.encode("ascii")
        base64_bytes = base64.b64encode(saved_bytes)
        en_saved = base64_bytes.decode("ascii")
        print(f"Your saved code is here (Copy It): {en_saved}")
        end = input(
            "Press Enter to continue...")
    def load_data():
        global score
        nonlocal item
        temp = ''
        str_score = ''
        try:
            en_saved = input("Enter your backup code: ")
            base64_bytes = en_saved.encode("ascii")
            saved_bytes = base64.b64decode(base64_bytes)
            de_saved = saved_bytes.decode("ascii")
            for i in de_saved:
                try:
                    g = int(i)
                    str_score += str(g)
                    score = int(str_score)
                except:
                    temp += i
            for i in list(temp.split(',')):
                item.append(i)
        except:
            print("\nInvalid backup code... back to main!!")
            start()
        finally:
            wordgussing()

    def rule():
        print('******************************************')
        print('''\nYou need to guess the word that appears on the screen.\nYou will be given life chances for each word according from difficulties.\nThere is no time limit.\nIf you think that the word contains certain letter.
Enter that letter and press Enter.\nIf the word contains it, it would be displayed.\nThere are 3 difficulties, and boss health per difficulty.
You can get special powers by defeating a boss.''')
        print('\n******************************************')
        done = input('Done Reading? (Y/N): ')
        done = done.lower()
        print('\n')
        if done == "y" or done == "yes":
            start()
        elif done == "n" or done == "no":
            print('Then read again...')
            rule()
        else:
            print('\n')
            print("Invalid Choice. Try Again..")
            rule()

    def credit():
        PK = "Pacharadanai Kurakanog"
        TT = "Tinnapop Tongnoon"
        print('******************************************')
        print(f'''\nThis game made by {PK} and {TT}.
Inspired by Python Word Guessing Game for Beginners.
(https://www.youtube.com/watch?v=oPppxUduFFE) 
By Trinity Software Academy.''')
        print('\n******************************************')
        done = input('Done Reading? (Y/N): ')
        print('\n')
        done = done.lower()
        if done == "y" or done == "yes":
            start()
        elif done == "n" or done == "no":
            print('Then read again...')
            credit()
        else:
            print('\n')
            print("Invalid Choice. Try Again..")
            credit()

    def wordgussing():
        nonlocal bonus
        nonlocal cur_diff
        def surprise():
            regan_image = io.BytesIO(base64.b64decode(regan))
            surprise_audio = io.BytesIO(base64.b64decode(surprise_a))
            pygame.init()
            width, height = 1366, 768
            screen = pygame.display.set_mode((width, height))
            pygame.display.set_caption("YOU LOSE HEHE!!")
            SetWindowPos(pygame.display.get_wm_info()['window'], win32con.HWND_TOPMOST, 0, 0, 0, 0,
                         win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
            surprise_sfx = pygame.mixer.Sound(surprise_audio)
            surprise_sfx.play()
            BG = pygame.transform.scale((pygame.image.load(regan_image)), (width, height))
            global score

            def draw():
                screen.blit(BG, (0, 0))
                pygame.display.update()

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        nonlocal item
                        nonlocal bonus
                        pygame.quit()
                        print('\n********************************')
                        print('\nGame over. You Lose. The word is', random_word)
                        print('\n********************************\n')
                        item = []
                        bonus = False
                        def reagain():
                            global score
                            restart1 = input('Restart? (Y/N): ')
                            restart = restart1.lower()
                            if restart == "y" or restart == "yes":
                                print('\n')
                                wordgussing()
                            elif restart == "n" or restart == "no":
                                print('\n')
                                print("******************************************")
                                print(f"Your Highest Score is {score}")
                                print("******************************************")
                                print(
                                    "/// Recommended to save this score as a picture!! (It will gone if you exit this program.) ///")
                                end = input(
                                    "\nPress Enter to continue...")
                                score = 0
                                quit()
                            else:
                                print('\n')
                                print("Invalid Choice. Try Again..")
                                reagain()
                        reagain()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            print('\n********************************')
                            print('\nGame over. You Lose. The word is', random_word)
                            print('\n********************************\n')
                            item = []
                            bonus = False

                            def reagain():
                                global score
                                restart1 = input('Restart? (Y/N): ')
                                restart = restart1.lower()
                                if restart == "y" or restart == "yes":
                                    print('\n')
                                    wordgussing()
                                elif restart == "n" or restart == "no":
                                    print('\n')
                                    print("******************************************")
                                    print(f"Your Highest Score is {score}")
                                    print("******************************************")
                                    print("/// Recommended to save this score as a picture!! (It will gone if you exit this program.) ///")
                                    end = input(
                                        "\nPress Enter to continue...")
                                    score = 0
                                    quit()
                                else:
                                    print('\n')
                                    print("Invalid Choice. Try Again..")
                                    reagain()
                            reagain()
                            sys.exit()
                draw()
        if bonus == True:
            if cur_diff == 'easy' or cur_diff == 'normal':
                words = animals_e + fruits_e
                chances = 5
                blc = 75
                bosslife = 75
                sp = 2.25
                each_c = 300
            elif cur_diff == 'hard':
                words = elements
                chances = 3
                blc = 150
                bosslife = 150
                sp = 3.25
                each_c = 500
        else:
            print("\n******************************************")
            print("Word Guessing Adventure")
            print("******************************************")
            global score
            print(f"Your Current Score is: {score}\n")
            print(f">>>          Easy          <<<")
            print(f">>>         Normal         <<<")
            print(f">>>          Hard          <<<")
            if score > 7000:
                print(f">>>        Hardcore        <<<")
            diff1 = input("\nSelect Difficulty: ")
            diff = diff1.lower()
            if score > 7000:
                if diff == 'hardcore':
                    words = elements
                    chances = 2
                    blc = 100
                    bosslife = 100
                    sp = 3.5
                    each_c = 500
                    cur_diff = diff
                elif diff == 'easy':
                    words = animals_e
                    chances = 5
                    blc = 25
                    bosslife = 25
                    sp = 1
                    each_c = 250
                    cur_diff = diff
                elif diff == 'normal':
                    words = animals_e + fruits_e
                    chances = 4
                    blc = 35
                    bosslife = 35
                    sp = 1.5
                    each_c = 300
                    cur_diff = diff
                elif diff == 'hard':
                    words = elements
                    chances = 3
                    blc = 50
                    bosslife = 50
                    sp = 2
                    each_c = 500
                    cur_diff = diff
                else:
                    print('\n')
                    print("Invalid Choice. Try Again..")
                    wordgussing()
            else:
                if diff == 'easy':
                    words = animals_e
                    chances = 5
                    blc = 25
                    bosslife = 25
                    sp = 1
                    each_c = 250
                    cur_diff = diff
                elif diff == 'normal':
                    words = animals_e + fruits_e
                    chances = 4
                    blc = 35
                    bosslife = 35
                    sp = 1.5
                    each_c = 300
                    cur_diff = diff
                elif diff == 'hard':
                    words = elements
                    chances = 3
                    blc = 50
                    bosslife = 50
                    sp = 2
                    each_c = 500
                    cur_diff = diff
                else:
                    print('\n')
                    print("Invalid Choice. Try Again..")
                    wordgussing()


            # --------------------------------------------------------------
        while True:
            print("******************************************")
            print(f'\nBoss HP {bosslife}/{blc}')
            random_word = random.choice(words)
            if random_word in animals_e:
                print('\nHint: It is an animal')
                if random_word == 'elephant':        #คำใบ้
                    print ('It have big ear.!!!')
                elif random_word == 'bear':
                    print ('My hands not ''gum'' but ...')
                elif random_word == 'wolf':
                    print ('Appears in the story of the 3 little pigs.  ')
                elif random_word == 'tiger':
                    print ('It look like zebra but orange.')
                elif random_word == 'penguin':
                    print ('It have black and white and it cant fly.  ')
                elif random_word == 'rabbit':
                    print ('It was once defeated by a turtle. ')
                elif random_word == 'zebra':
                    print ('It look like horse. ')
                elif random_word == 'monkey':
                    print ('Look like a human.')



            elif random_word in fruits_e:
                print('\nHint: It is an fruits')
                if random_word == 'apple':        #คำใบ้
                    print ('Snow White falls asleep when she eats it. ')
                elif random_word == 'banana':
                    print ('monkey like to eat.  ')
                elif random_word == 'grapes':
                    print ('There are many and purple.  ')
                elif random_word == 'mango':
                    print ('They are green in color and when cooked they are yellow. ')
                elif random_word == 'lime':
                    print ('It look like lemon  ')
                elif random_word == 'guava':
                    print ('It ')
                elif random_word == 'orange':
                    print ('Names that Thai people call foreigners  ')
                elif random_word == 'papaya':
                    print ('Thai people like to use it in cooking with salad.')
                elif random_word == 'pear':
                    print ('Thai stars  ')
                elif random_word == 'peach':
                    print ('It have white to yellow or orange ')
                elif random_word == 'strawberry':
                    print ('It is Migaki-Ichigo ')
            elif random_word in elements:
                print('\nHint: It is an elements')
                if random_word == 'lithium':        #คำใบ้
                    print ('It have 3 atom')
                elif random_word == 'hydrogen':
                    print ('It First in table elements ')
                elif random_word == 'kryptonite':
                    print ('It was something Superman had defeats before.   ')
                elif random_word == 'sodium':
                    print ('You can find them in the ocean. but no chloride  ')
                elif random_word == 'platinum':
                    print ('It  white gold')
                elif random_word == 'silver':
                    print ('It  ')
                elif random_word == 'neon':
                    print ('It bright on night when you go to Tokyo ')
                elif random_word == 'carbon':
                    print ('It money but not money  ')
                elif random_word == 'oxygen':
                    print ('You always use all the time.')
                elif random_word == 'gold':
                    print ('It very expensive  ')

            # --------------------------------------------------------------

            dmg = len(random_word)
            user_guesses = ''
            x = 0
            for hch in random_word:  # 'lime'
                while x < 1:
                    user_guesses += hch
                    x = x + 1
            while chances > 0:
                if bosslife > 0:
                    wrong_guess = 0
                    for ch in random_word:
                        if ch in user_guesses:
                            print(ch, end=' ')
                        else:
                            wrong_guess += 1
                            print('_', end=' ')
                    if wrong_guess == 0:
                        bosslife -= dmg
                        print("\n")
                        if bosslife <= 0:
                            if bonus == True:
                                print(f'Congrats!! You have been defeated {cur_diff.capitalize()} bonus level!!')
                            else:
                                print(f'Congrats!! You have been defeated {cur_diff.capitalize()} mode!!')
                            nonlocal item
                            bonus = False
                            noreward = 'NOPE'
                            randomitem = ['dxt', 'dxt', 'rvl', 'rvl', 'rvl', 'hp', 'hp', 'hp', 'hp', 'hp', 'hp']
                            def againf():
                                global score
                                nonlocal item
                                again1 = input("Play again? (Y/N): ")
                                again = again1.lower()
                                if again == "y" or again == "yes":
                                    print('\n')
                                    wordgussing()
                                elif again == "n" or again == "no":
                                    print('\n')
                                    print("******************************************")
                                    print(f"Your Highest Score is {score}")
                                    print("******************************************")
                                    print(
                                        "/// Recommended to save this score as a picture!! (It will gone if you exit this program.) ///")

                                    save_data()
                                    score = 0
                                    quit()
                                else:
                                    print('\n')
                                    print("Invalid Choice. Try Again..")
                                    againf()

                            def boagain():
                                nonlocal bonus
                                play = input('Yes or No? (Y/N): ')
                                play = play.lower()
                                if play == 'y' or play == 'yes':
                                    bonus = True
                                elif play == 'n' or play == 'no':
                                    againf()
                                else:
                                    print(f"Invalid Choice! Try Again!!")
                                    boagain()

                            if cur_diff == "easy":
                                reward = [noreward, noreward, noreward, 'randomitem']
                                get = random.choice(reward)
                                if get == 'randomitem':
                                    thing = random.choice(randomitem)
                                    print(f'You got {thing}!!')
                                    item.append(thing)
                                isbonus = [noreward, noreward, noreward, 'bonus']
                                getb = random.choice(isbonus)
                                if getb == 'bonus':
                                    print("\n******************************************")
                                    print(f"\nWoahhh!!! You Found BONUS level!!")
                                    print(f"You want to play Bonus level?")
                                    boagain()
                            elif cur_diff == "normal":
                                reward = [noreward, noreward, 'randomitem']
                                get = random.choice(reward)
                                if get == 'randomitem':
                                    thing = random.choice(randomitem)
                                    print(f'You got {thing}!!')
                                    item.append(thing)
                                isbonus = [noreward, noreward, 'bonus']
                                getb = random.choice(isbonus)
                                if getb == 'bonus':
                                    print("\n******************************************")
                                    print(f"\nWoahhh!!! You Found BONUS level!!")
                                    print(f"You want to play Bonus level?")
                                    boagain()
                            elif cur_diff == "hard":
                                reward = [noreward, 'randomitem']
                                get = random.choice(reward)
                                if get == 'randomitem':
                                    thing = random.choice(randomitem)
                                    print(f'You got {thing}!!')
                                    item.append(thing)
                                isbonus = [noreward, 'bonus']
                                getb = random.choice(isbonus)
                                if getb == 'bonus':
                                    print("\n******************************************")
                                    print(f"\nWoahhh!!! You Found BONUS level!!")
                                    print(f"You want to play Bonus level?")
                                    boagain()

                            def againp():
                                global score
                                score += (chances * each_c) * sp
                                score = int(score)
                                again1 = input("Play again? (Y/N): ")
                                again = again1.lower()
                                if again == "y" or again == "yes":
                                    print('\n')
                                    wordgussing()
                                elif again == "n" or again == "no":
                                    print('\n')
                                    print("******************************************")
                                    print(f"Your Highest Score is {score}")
                                    print("******************************************")
                                    print(
                                        "/// Recommended to save this score as a picture!! (It will gone if you exit this program.) ///")
                                    save_data()
                                    score = 0
                                    quit()
                                else:
                                    print('\n')
                                    print("Invalid Choice. Try Again..")
                                    againp()
                            againp()
                        break

                    def options():
                        nonlocal item
                        nonlocal chances
                        nonlocal user_guesses
                        nonlocal random_word
                        nonlocal dmg
                        atkf = "ATTACK"
                        itmf = "USE ITEM"
                        print("\n ⏤ ⏤ ⏤ ⏤ ⏤ ⏤ ⏤ ⏤ ⏤ ⏤ ⏤ ⏤ ⏤ ⏤ ⏤ ")
                        print(f"|      {atkf}      ||      {itmf}      |")
                        print(" ⏤ ⏤ ⏤ ⏤ ⏤ ⏤ ⏤ ⏤ ⏤ ⏤ ⏤ ⏤ ⏤ ⏤ ⏤ ")
                        option = input("Choose your decision (ATK/ITEM): ")
                        option = option.lower()
                        if option == "atk" or option == "attack":
                            guess = input('\nMake a guess: ')
                            user_guesses += guess
                            if guess not in random_word:
                                for i in guess:
                                    if i not in random_word:
                                        if chances > 0:
                                            chances -= 1
                                            print(f'Wrong. You have {chances} more chances')
                                        if chances == 0:
                                            nonlocal bonus
                                            if bonus == True:
                                                bonus = False
                                                print("\n******************************************")
                                                print(f"\nYou Lose Your Bonus Level!! RIP!! :(")
                                                print("\n******************************************")

                                                def againb():
                                                    global score
                                                    again1 = input("Play again? (Y/N): ")
                                                    again = again1.lower()
                                                    if again == "y" or again == "yes":
                                                        print('\n')
                                                        wordgussing()
                                                    elif again == "n" or again == "no":
                                                        print('\n')
                                                        print("******************************************")
                                                        print(f"Your Highest Score is {score}")
                                                        print("******************************************")
                                                        print(
                                                            "/// Recommended to save this score as a picture!! (It will gone if you exit this program.) ///")
                                                        save_data()
                                                        score = 0
                                                        quit()
                                                    else:
                                                        print('\n')
                                                        print("Invalid Choice. Try Again..")
                                                        againb()
                                                againb()
                                                wordgussing()
                                            else:
                                                surprise()
                        elif option == "itm" or option == "item":
                            used = ''
                            print(f'\nYour Inventory: {item}')
                            print(f'Damage X2 is dxt, Auto Correct is rvl, +2 HP is hp')
                            checkitem = input("\nPick your item in your inventory: ")
                            if item == []:
                                print('There is no item inside your inventory back to the fight!')
                                pass
                            else:
                                if checkitem in item:
                                    for i in item:
                                        if checkitem == i:
                                            if checkitem == "dxt":
                                                used = "dxt"
                                            elif checkitem == "rvl":
                                                used = "rvl"
                                            elif checkitem == "hp":
                                                used = "hp"
                                            elif checkitem == "admin":
                                                used = "admin"
                                            else:
                                                print("Not has this item in your inventory back to the fight!")
                                                pass
                                else:
                                    print("Not has this item in your inventory back to the fight!")
                                    pass
                            if used == "dxt":
                                dmg = 2 * dmg
                                item.remove("dxt")
                            elif used == "rvl":
                                for char in random_word:
                                    user_guesses += char
                                item.remove("rvl")
                            elif used == "hp":
                                chances += 2
                                print(f"Now your HP is {chances}!!")
                                item.remove("hp")
                            elif used == "admin":
                                dmg = 3 * dmg
                                for char in random_word:
                                    user_guesses += char
                            else:
                                print("Back to the fight!")
                                pass
                        else:
                            print('\n')
                            print("Invalid Choice. Try Again..")
                            pass
                    options()

    def warn():
        warning_image = io.BytesIO(base64.b64decode(warning))
        pygame.init()
        width, height = 1366, 768
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Warning!!")
        SetWindowPos(pygame.display.get_wm_info()['window'], win32con.HWND_TOPMOST, 0, 0, 0, 0,
                     win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        BG = pygame.transform.scale((pygame.image.load(warning_image)), (width, height))
        cheat = ''
        password = 'abcdef'

        def draw():
            screen.blit(BG, (0, 0))
            pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    wordgussing()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        wordgussing()
                        sys.exit()
                    elif event.key == pygame.K_UP:
                        if 'a' in cheat:
                            cheat = ''
                        else:
                            cheat += 'a'
                    elif event.key == pygame.K_DOWN:
                        if 'b' in cheat:
                            cheat = ''
                        else:
                            cheat += 'b'
                    elif event.key == pygame.K_LEFT:
                        if 'c' in cheat:
                            cheat = ''
                        else:
                            cheat += 'c'
                    elif event.key == pygame.K_RIGHT:
                        if 'd' in cheat:
                            cheat = ''
                        else:
                            cheat += 'd'
                    elif event.key == pygame.K_b:
                        if 'e' in cheat:
                            cheat = ''
                        else:
                            cheat += 'e'
                    elif event.key == pygame.K_a:
                        if 'f' in cheat:
                            cheat = ''
                        else:
                            cheat += 'f'
                    elif event.key == pygame.K_RETURN:
                        if cheat == password:
                            pygame.quit()
                            nonlocal item
                            print("\n**********************************")
                            print("\n|        Cheat Activated!        |")
                            print("\n**********************************")
                            item = ['admin']
                            wordgussing()
                            sys.exit()
                        else:
                            cheat = ''
                    else:
                        cheat = ''

            draw()
    def enter():
        warn()
    print("\n******************************************")
    print("Welcome To Word Guessing Adventure!!!")
    print("******************************************\n")
    print(f">>>         Start         <<<")
    print(f">>>         Load          <<<")
    print(f">>>         Rules         <<<")
    print(f">>>        Credits        <<<")
    choice = input('\nEnter your choice: ')
    print('\n')
    choice = choice.lower()
    if choice == 'start':
        enter()
    elif choice == 'rule' or choice == 'rules':
        rule()
    elif choice == 'credit' or choice == 'credits':
        credit()
    elif choice == 'load' or choice == 'loads':
        load_data()
    else:
        print("Invalid Choice. Try Again..")
        start()

# start
start()
