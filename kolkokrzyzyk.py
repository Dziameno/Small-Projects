def wypiszplansze(plansza):
    for row in plansza:
        print("%s|%s|%s" % (row[0], row[1], row[2]))


def zaznaczruch(plansza, ruch, aktualnyznak):
    ruch = ruch - 1
    x = int(ruch / 3)
    y = int(ruch % 3)
    plansza[x][y] = aktualnyznak


def sprawdzczywygrana(plansza):
    # sprawdzenie rzędów
    if plansza[0][0] == plansza[0][1] and plansza[0][1] == plansza[0][2]:
        print("Wygrał: " + plansza[0][0])
        exit(0)
    if plansza[1][0] == plansza[1][1] and plansza[1][1] == plansza[1][2]:
        print("Wygrał: " + plansza[1][0])
        exit(0)
    if plansza[2][0] == plansza[2][1] and plansza[2][1] == plansza[2][2]:
        print("Wygrał: " + plansza[2][0])
        exit(0)
    # sprawdzenie kolumn
    if plansza[0][0] == plansza[1][0] and plansza[1][0] == plansza[2][0]:
        print("Wygrał: " + plansza[0][0])
        exit(0)
    if plansza[0][1] == plansza[1][1] and plansza[1][1] == plansza[2][1]:
        print("Wygrał: " + plansza[0][1])
        exit(0)
    if plansza[0][2] == plansza[1][2] and plansza[1][2] == plansza[2][2]:
        print("Wygrał: " + plansza[0][2])
        exit(0)
    # sprawdzenie skosow
    if plansza[0][0] == plansza[1][1] and plansza[1][1] == plansza[2][2]:
        print("Wygrał: " + plansza[0][0])
        exit(0)
    if plansza[0][2] == plansza[1][1] and plansza[1][1] == plansza[2][0]:
        print("Wygrał: " + plansza[0][2])
        exit(0)
    # Remis
    mozliweruchy = ("x", "o")
    for row in plansza:
        for col in row:
            if col not in mozliweruchy:
                return
    print("Remis!")
    exit(0)


def czyzajete(plansza, ruch):
    ruch = ruch - 1
    x = int(ruch / 3)
    y = int(ruch % 3)
    if plansza[x][y] == krzyzyk or plansza[x][y] == kolko:
        return True

    return False


def pobierzruch(aktualnyznak, plansza):
    while True:
        try:
            ruch = input("Wybierz miejsce dla " + aktualnyznak + ":")
            ruch = int(ruch)
            if ruch > 9 or ruch <= 0 or czyzajete(plansza, ruch):
                raise ValueError
            return ruch
        except ValueError:
            print("Musisz podać liczbę od 1 do 9!")


kolko = "o"
krzyzyk = "x"
plansza = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
aktualnyznak = krzyzyk
print("Witaj w kółko i krzyżyk. Krzyżyk zaczyna.")
while True:
    wypiszplansze(plansza)
    ruch = pobierzruch(aktualnyznak, plansza)
    zaznaczruch(plansza, ruch, aktualnyznak)
    sprawdzczywygrana(plansza)

    aktualnyznak = krzyzyk if aktualnyznak == kolko else kolko