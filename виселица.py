import random
HANGMAN_PICS = ['''

    +---+
    |   |
        |
        |
        |
        |
 =========''','''
                
    +---+
    |   |
    0   |
        |
        |
        |
 =========''','''

    +---+
    |   |
    0   |
    |   |
        |
        |
 =========''','''
                
    +---+
    |   |
    0   |
   /|\  |
        |
        |
 =========''','''
 
    +---+
    |   |
    0   |
   /|\  |
   /    |
        |
 =========''','''

    +---+
    |   |
    0   |
   /|\  |
   / \  |
        |
 =========''']

words ='муравей, бабуин барсук медведь бобр верблюд кошка моллюск кобра пума койот ворона олень собака осел утка орел хорек лиса лягушка коза гусь ястреб ящерица лама моль обезьяна лось мышь мул тритон выдра сова панда попугай голубь питон кролик баран крыса носорог лосось акула змея паук аист лебедь тигр жаба форель индейка черепаха ласка кит волк вомбат зебра'.split()
def getRandomWord():
    # эта функция возвращает случайную строку из переданного списка.
    wordIndex = random.randint(0, len(words)-1)
    return words[wordIndex]
def displayBoard(misseddLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(misseddLetters)])
    print()
    print('Ошибочные буквы:', end='')
    for letter in misseddLetters:
        print(letter, end='')
    print()

    blanks = '_'*len(secretWord)

    for i in range(len(secretWord)): # заменяет пропуски отгаданными буквами
        if secretWord[i] in correctLetters:
            blanks = blanks[:i]+secretWord[i]+blanks[i+1:]

    for letter in blanks: # показывает секретное слово с пробелами между буквами
        print(letter, end='')
    print()

def getGuess(alreadyGuessed):
    #Возвращает букву введенную игроком. Эта функция проверяет, что игрок ввел только одну букву и ничего больше.
    while True:
        print('Введите букву:')
        guess = input()
        guess = guess.lower()
        if len(guess)!=1:
            print('Пожалуйста, введите одну букву.')
        elif guess is alreadyGuessed:
            print('Вы уже называли эту букву. Назовите другую:')
        elif guess not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста, введите БУКВУ.')
        else:
            return guess

def playAgain():

    print('Хотите сыграть еще? (да или нет)')
    return input().lower().startswith('д')

print('Виселица')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters,correctLetters,secretWord)

    guess=getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('ДА! Секретное слово - "'+secretWord+'"! Вы угадали!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)

            print('Вы исчерпали все попытки!\nНе угадано букв:'+ str(len(missedLetters))+'и угадано букв:' + str(len(correctLetters)) + '. Было загадано слово"'+ secretWord+ '".')
            gameIsDone = True
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
    else:
        break



