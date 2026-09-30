import random

user_score = 0
pc_score = 0
run = True

# Steg 1
options = ["s", "x", "p"]

names = {
    "s": "🪨 Sten",
    "x": "✂️ Sax",
    "p": "📄 Påse"
}

while run:

    # Steg 2
    print("s: Sten, x: Sax, p: Påse")
    user_choice = input("Vänligen välj ett av alternativen ovan: \n")

    if user_choice in options:

        # Steg 3
        pc_choice = random.choice(options)
        print(f"Datorn valde: {names[pc_choice]}")

        # Steg 4
        if user_choice == pc_choice:
            print("Lika! Testa en gång till!")

        elif user_choice == "s":
            if pc_choice == "p":
                pc_score += 1
                print("Datorn vann rundan! 🤖")
            else:
                user_score += 1
                print("Du vann rundan! 🎉")

        elif user_choice == "p":
            if pc_choice == "x":
                pc_score += 1
                print("Datorn vann rundan! 🤖")
            else:
                user_score += 1
                print("Du vann rundan! 🎉")

        elif user_choice == "x":
            if pc_choice == "s":
                pc_score += 1
                print("Datorn vann rundan! 🤖")
            else:
                user_score += 1
                print("Du vann rundan! 🎉")

        print(f"Du: {user_score} - Datorn: {pc_score}")

        # Spelet slutar när någon får 3 poäng
        if user_score == 3 or pc_score == 3:

            if user_score == 3:
                print("Grattis! Du vann! 🎉")
            else:
                print("Tyvärr, datorn vann! 🤖")

            run = False

    else:
        print("ERROR: Vänligen välj ett av alternativen!")