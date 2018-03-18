import random

print("Available game modes:")
print("1 - Play with PC")
print("2 - Play with friend")
print("3 - Play alone")
print("Player1 score is: 1000")
print("Player2 score is: 1000")

gameMode = int(input("Enter game mode: "))
numberOfSteps = int(input("Enter number of steps: "))
betSize = int(input("Enter bet size: "))

stepsCounter = 1
player1Score = 1000
player2Score = 1000

while True:
    computerNumber = str(random.randint(1, 12)) #рандомное число
    print("************************")
    print("Current step: ", stepsCounter)
    print("Random number is: ", computerNumber) #показывает загаданное число
    stepsCounter += 1 #счетчик шагов

    if gameMode == 1 or gameMode == 2:
        userInput1 = input("Player1 enter number: ")
        if userInput1 == "stop":
            break
        if gameMode == 2: #игра с другом
            userInput2 = input("Player2 enter number: ")
            if userInput2 == "stop":
                break
        elif gameMode == 1: #игра с PC
            userInput2 = str(random.randint(1, 12)) #случайное число PC
            print("Player2 (PC) entered: ", userInput2)

        if stepsCounter > numberOfSteps: #если текущий шаг больше максимального хода
            if userInput1 != computerNumber and userInput2 != computerNumber:
                print("Game over. Nobody won")
                break
            if userInput1 == computerNumber and userInput2 != computerNumber:
                print("Player1 won! Game over")
                break
            if userInput1 != computerNumber and userInput2 == computerNumber:
                print("Player2 won! Game over")
                break

        if userInput1 == computerNumber and userInput2 == computerNumber: #если первый и второй игрок угадал число
            print("Game over. Nobody won")
        elif userInput1 != computerNumber and userInput2 == computerNumber: #если первый игрок не угадал, а второй угадал
            player1Score = player1Score - betSize
            player2Score = player2Score + betSize
            print("Player2 got it!")
        elif userInput2 != computerNumber and userInput1 == computerNumber: #если второй игрок не угадал, а первый угадал
            player2Score = player2Score - betSize
            player1Score = player1Score + betSize
            print("Player1 got it!")
        else: #если никто не угадал
            player1Score = player1Score - betSize
            player2Score = player2Score - betSize
            print("Nobody guessed. Continue")

        print("Player1 score is: ", player1Score) #очки первого игрока
        print("Player2 score is: ", player2Score) #очки второго игрока

        #проверка на отрицательный счет
        if player1Score <= 0 and player2Score > 0:
            print("Player2 won! Game over")
            break
        if player1Score > 0 and player2Score <= 0:
            print("Player1 won! Game over")
            break
        if player1Score <= 0 and player2Score <= 0:
            print("Draw. Game over")
            break

    elif gameMode == 3: # для случая игры самим с собой
        userInput1 = input("Enter the number: ")
        if userInput1 == "stop":
            break
        if userInput1 == computerNumber:
            print("You won!")
            break







