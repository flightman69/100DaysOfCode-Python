import random
from art import logo

cards_dict= {'ace':11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'jack':10, 'queen':10, 'king':10}

def shuffle_cards():
    cards_list = list(cards_dict.keys())
    random.shuffle(cards_list)

    rand_card = random.choice(cards_list)
    choosen_card = {}
    choosen_card[rand_card] = cards_dict[rand_card]
    return  choosen_card

def display_cards(dealer_cards,player_cards):
    dealer_len = len(dealer_cards)
    player_len = len(player_cards)
    
    dealer_only_cards = []
    player_only_cards = []
    
    print("Dealer Cards :",end=" ")
    for i in range(dealer_len):
        card_value = list(dealer_cards[i].keys())[0]
        dealer_only_cards.append(card_value)
    print(' '.join(dealer_only_cards))

    print("Player Cards :",end=" ")
    for i in range(player_len):
        card_value = list(player_cards[i])[0]
        player_only_cards.append(card_value)
    print(' '.join(player_only_cards))
    
def hide_dealer_card(dealer_cards):
    second_card = dealer_cards[1]
    second_card_key = list(second_card.keys())[0]
    second_card['X'] = second_card.pop(second_card_key)
    dealer_cards.pop()
    dealer_cards.append(second_card)
    return dealer_cards

def value_cards(dealer_cards,player_cards):
    # Dealer cards value 
    dealer_cards_value = []
    dealer_len = len(dealer_cards)
    for i in range(dealer_len):
        card_key = list(dealer_cards[i])[0]
        card_value = dealer_cards[i][card_key]
        dealer_cards_value.append(card_value)
    dealer_cards_value = sum(dealer_cards_value)
    # Player cards value
    player_cards_value = []
    player_len = len(player_cards)
    for i in range(player_len):
        card_key = list(player_cards[i])[0]
        card_value = player_cards[i][card_key]
        player_cards_value.append(card_value)
    player_cards_value = sum(player_cards_value)

    return dealer_cards_value, player_cards_value

dealer = []

player = []

cards_in_use = []
while  len(dealer) < 2 or len(player) < 2:
    
    card = shuffle_cards()
    if card not in cards_in_use and len(dealer) < 2:
        dealer.append(card)
        cards_in_use.append(card)
    card = shuffle_cards()
    if card not in cards_in_use and len(player) < 2:
       player.append(card)
       cards_in_use.append(card)

hidden_dealer = hide_dealer_card(dealer)
display_cards(hidden_dealer,player)
while True:
    player_option = input("Hit or Stay [H/S]: ").lower()
    print()
    if player_option == 'h':
        d,p =  value_cards(dealer,player)
        if d > 21:
            display_cards(dealer,player)
            print(f"Dealer Bust {d}, Player Won!")
            break
        elif p > 21:
            display_cards(dealer,player)
            print(f"Player Bust {p}, Dealer Won!")
        elif p > d:
            display_cards(dealer,player)
            print(f"Player Won {p}")
        elif d > p:
            display_cards(dealer,player)
            print(f"Dealer Won {d}")
        else:
            display_cards(dealer,player)
            print(f"It's a Draw, Dealer: {d}, Player: {p}") 
    break

        
