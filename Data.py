def valid(hand):
    if hand < 0 or hand > 2 :
        return False 
    return True

def print_hand(hand, name ):
    hands = ['Batu','Kertas','Gunting']
    print(name + ' memilih ' + hands[hand])

def eksekusi(player,computer):
    if player == computer:
        return 'Seri'
    elif player == 0 and computer == 1 :
        return 'Kalah'
    elif player == 1 and computer == 2 :
        return 'Kalah'
    elif player == 2 and computer == 0 :
        return 'Kalah'
    else:
        return 'Menang'