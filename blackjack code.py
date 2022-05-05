import os
import random


decks = input("Kullanılıcak deste sayısını girin: ")


deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*(int(decks)*4)


def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "K"
        if card == 14:card = "A"
        hand.append(card)
    return hand

def play_again():
    again = input("bi daha oynamak istiyon mu? (E/H) : ").lower()
    if again == "e":
        dealer_hand = []
        player_hand = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
        os.system('cls')
        game()
    else:
        print("bi daha gel bb")
        exit()

def total(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total+= 10
        elif card == "A":
            if total >= 11: total+= 1
            else: total+= 11
        else: total += card
    return total

def hit(hand):
    card = deck.pop()
    if card == 11:card = "J"
    if card == 12:card = "Q"
    if card == 13:card = "K"
    if card == 14:card = "A"
    hand.append(card)
    return hand

def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

def print_results(dealer_hand, player_hand):
    clear()

    print("\n    BLACKJACK'E HOS GELDIN!\n")
    print ("Kasanın eli " + str(dealer_hand) + " toplamı " + str(total(dealer_hand)))
    print ("Senin elin " + str(player_hand) + " toplamı " + str(total(player_hand)))

def blackjack(dealer_hand, player_hand):
    global wins
    global losses
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("Tebrikler!Blacjack cektin! helal\n")
        wins += 1
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("kasa blackjack çekti.kaybettin . gecmis olsun :D\n")
        losses += 1
        play_again()

def score(dealer_hand, player_hand):
        
        if total(player_hand) == 21:
            print_results(dealer_hand, player_hand)
            print ("Tebrikler!Blacjack cektin! helal\n")
            
        elif total(dealer_hand) == 21:
            print_results(dealer_hand, player_hand)
            print ("Uzugunum, kasa blackjack cekti.\n")
           
        elif total(player_hand) > 21:
            print_results(dealer_hand, player_hand)
            print ("Kasa kazandı. Sen kaybettin. gecmis olsun :D\n")
            
        elif total(dealer_hand) > 21:
            print_results(dealer_hand, player_hand)
            print ("Kasa kaybetti. Sen kazandın!\n")
        
        elif total(player_hand) < total(dealer_hand):
            print_results(dealer_hand, player_hand)
            print ("Gecmis olsun senin skorun kasanınkinden daha az. Kaybettin\n")
           
        elif total(player_hand) > total(dealer_hand):
            print_results(dealer_hand, player_hand)
            print ("Helal be! Senin skorun kasanınkinden daha fazla\n")
           

def game():
    choice = 0
    clear()
    print("\n    BLACKJACK'E HOSGELDIN\n")
    print("-"*30+"\n")
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    print ("Kasanın eli " + str(dealer_hand[0]))
    print ("Senin elin " + str(player_hand) + " toplam " + str(total(player_hand)))
    blackjack(dealer_hand, player_hand)
    quit=False
    while not quit:
        choice = input("Hangisini istiyorsun [H]it, [S]tand, or [Q]uit: ").lower()
        if choice == 'h':
            hit(player_hand)
            print(player_hand)
            print("Elin toplamı: " + str(total(player_hand)))
            if total(player_hand)>21:
                print('Keybettin ')
                play_again()
        elif choice=='s':
            while total(dealer_hand)<17:
                hit(dealer_hand)
                print(dealer_hand)
                if total(dealer_hand)>21:
                    print('Kasa kaybetti. Sen kazandın helal')
                    play_again()
            score(dealer_hand,player_hand)
            play_again()
        elif choice == "q":
            print("bi daha gel bb")
            quit=True
            exit()


if __name__ == "__main__":
   game()
