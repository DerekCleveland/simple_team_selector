import random


def main():
    players = []
    finished_input = False
    count = 0
    team_number = 1

    team_size = int(input("Enter the team size! "))

    print("Enter 0 to exit!")
    while finished_input is not True:
        response = input("Enter a players name! ")

        if response == "0":
            finished_input = True
        else:
            players.append(response)

    random.shuffle(players)

    for player in players:
        if count % team_size == 0:
            print(f"TEAM {team_number}")
            team_number = team_number + 1

        count = count + 1

        print(player)


if __name__ == "__main__":
    main()