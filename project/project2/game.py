import BlackJack

while True:
    print("Welcome to BlackJack game!")

    deck = BlackJack.Deck()
    deck.shuffle()

    player = BlackJack.Hand()
    dealer = BlackJack.Hand()

    for c in range(0,2):
       BlackJack.hit(deck,player)
    

    chip = BlackJack.Chips()
    # chip.total = 100

    chip.bet = BlackJack.take_bet()

    BlackJack.show_some(player,dealer)

    while BlackJack.playing:
        pass
