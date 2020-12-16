import random
import time


hearts = [
    '2♥',
    '3♥',
    '4♥',
    '5♥',
    '6♥',
    '7♥',
    '8♥',
    '9♥',
    '10♥',
    'J♥',
    'Q♥',
    'K♥',
    'A♥',]
diamonds = [
    '2♦',
    '3♦',
    '4♦',
    '5♦',
    '6♦',
    '7♦',
    '8♦',
    '9♦',
    '10♦',
    'J♦',
    'Q♦',
    'K♦',
    'A♦',]
clubs = [
    '2♣',
    '3♣',
    '4♣',
    '5♣',
    '6♣',
    '7♣',
    '8♣',
    '9♣',
    '10♣',
    'J♣',
    'Q♣',
    'K♣',
    'A♣',]
spades = [
    '2♠',
    '3♠',
    '4♠',
    '5♠',
    '6♠',
    '7♠',
    '8♠',
    '9♠',
    '10♠',
    'J♠',
    'Q♠',
    'K♠',
    'A♠',]

cards = hearts[:] + diamonds[:] + clubs[:] + spades[:] #This line might be redundant

def draw_card():
    '''Pick a random index number to pop from cards list.
        Returns card name (with suit)'''
    deck = len(cards) - 1
    random_num = random.randint(0,deck)
    card = cards.pop(random_num)
    
    deck -= 1
    
    return card
    
def card_value(card):
    '''Input the card name, return card value (used in hit_ methods)'''  
    if card in hearts:
        card_index = hearts.index(card)
    elif card in diamonds:
        card_index = diamonds.index(card)
    elif card in clubs:
        card_index = clubs.index(card)
    elif card in spades:
        card_index = spades.index(card)
    
    if card_index <= 8:
        card_value = card_index + 2
    elif card_index >= 9 and card_index <= 11:
        card_value = 10
    elif card_index == 12:
        card_value = 11

    return card_value

def hit_me():
    '''Draws a card; its name and value are added to appropriate user_ lists'''
    next_card = draw_card()
    value_next_card = card_value(next_card)
    user_card_values.append(value_next_card)
    user_hand.append(next_card)
    user_hand_value = sum(user_card_values)

def hit_cpu():
    '''Draws a card; its name and value are added to appropriate CPU_ lists'''
    next_card = draw_card()
    value_next_card = card_value(next_card)
    cpu_card_values.append(value_next_card)
    cpu_hand.append(next_card)
    cpu_hand_value = sum(cpu_card_values)

def hand_type_check(hand):
    '''Checks the two first two dealt cards for aces to initialize the hand_type variable.
        Returns hand_type = 'soft' or 'hard'.'''
    ace_at_0 = False
    ace_at_1 = False
    
    #Check for Ace at index 0
    if hand[0] == 'A♥' or hand[0] == 'A♦' or hand[0] == 'A♣' or hand[0] == 'A♠':
        ace_at_0 = True
    else:
        ace_at_0 == False

    #Check for Ace at index 1
    if hand[1] == 'A♥' or hand[1] == 'A♦' or hand[1] == 'A♣' or hand[1] == 'A♠':
        ace_at_1 = True
    else:
        ace_at_1 == False
    
    #Decide if hand_type is hard or soft
    if ace_at_0 == True and ace_at_1 == False:
        hand_type = 'soft'
    elif ace_at_0 == False and ace_at_1 == True:
        hand_type = 'soft'
    elif ace_at_0 == True and ace_at_1 == True:
        hand_type = 'soft'
    elif ace_at_0 == False and ace_at_1 == False:
        hand_type = 'hard'
    
    return hand_type

def pocket_rockets_check(hand):
    '''Raises the pocket_rockets flag.
    Lets the program know to adjust the hand value prior to the decision loop.
    Returns True/False'''
    rocket_0 = False
    rocket_1 = False
    
    #Check for Ace at index 0
    if hand[0] == 'A♥' or hand[0] == 'A♦' or hand[0] == 'A♣' or hand[0] == 'A♠':
        rocket_0 = True
    else:
        rocket_0 == False

    #Check for Ace at index 1
    if hand[1] == 'A♥' or hand[1] == 'A♦' or hand[1] == 'A♣' or hand[1] == 'A♠':
        rocket_1 = True
    else:
        rocket_1 == False
    
    #Change pocket_rockets True/False flag
    if rocket_0 == True and rocket_1 == True:
        pocket_rockets = True
    else:
        pocket_rockets = False
    
    #Return variable
    return pocket_rockets

def last_drawn_ace(hand):
    '''Checks to see if the last card in a list is an Ace
    This line should go after hit_me() or hit_cpu().
    Returns True/False'''
    if hand[-1] == 'A♥' or hand[-1] == 'A♦' or hand[-1] == 'A♣' or hand[-1] == 'A♠':
        return True
    else:
        return False

def aces_in_hand_check(hand):
    '''Checking if there is an ace in the hand up to the penultimate card'''
    length_to_penultimate = len(hand) - 1
    num_aces = 0

    ace_check1 = 'A♥' in hand[:length_to_penultimate]
    ace_check2 = 'A♦' in hand[:length_to_penultimate]
    ace_check3 = 'A♣' in hand[:length_to_penultimate]
    ace_check4 = 'A♠' in hand[:length_to_penultimate]

    if ace_check1 == True:
        num_aces += 1
    
    if ace_check2 == True:
        num_aces += 1
    if ace_check3 == True:
        num_aces += 1
    if ace_check4 == True:
        num_aces += 1

    return num_aces

#MAIN GAME LOOP
play_again = 'y'
while play_again == 'y':

    cards = hearts[:] + diamonds[:] + clubs[:] + spades[:]
    deck = 51
    bust = False
    blackjack = False
    user_hand = []
    user_card_values = []
    user_hand_value = sum(user_card_values[:])
    cpu_hand = []
    cpu_card_values = []
    cpu_hand_value = sum(cpu_card_values[:])
    
    #Dealing out the first two cards, each
    hit_me()
    hit_cpu()
    hit_me()
    hit_cpu()


    #Initial printout of the cards    
    tab = chr(9)
    print("DEALER'S CARDS" + tab + tab + "USER'S CARDS")
    print('--------------------' + tab + '--------------------')
    time.sleep(1)
    print(tab + tab + tab + user_hand[0], end='\r')
    time.sleep(1)
    print("XX" + tab + tab + tab  + user_hand[0], end='\r')
    time.sleep(1)
    print("XX" + tab + tab + tab  + user_hand[0], user_hand[1], end='\r')
    time.sleep(1)
    print("XX", cpu_hand[1] + tab + tab  + tab + user_hand[0], user_hand[1], end = '\r')
    time.sleep(1)

    print('')
    print('')

    #GET HAND VALUE
    user_hand_value = sum(user_card_values)
    #HAND TYPE CHECK
    hand_type = hand_type_check(user_hand)
    #POCKET ROCKETS CHECK
    if pocket_rockets_check(user_hand) == True:
        user_hand_value -= 10
    #BLACKJACK CHECK
    if user_hand_value == 21:
        blackjack = True
    
    #MAIN DECISION LOOP
    while user_hand_value < 21:
        #Prompt the user for actions
        print('')
        print('The user has {}.  Would you like to hit or stand?'.format(user_hand_value))
        hit_or_stand = input("(hit/stand): ")
        
        #decision to hit or stand
        if hit_or_stand.lower() == 'hit':  #if hit is selected
            #print the next card and check the value
            hit_me()
            print('')
            for card in user_hand:
                print(card, end = ' ')    
            print('')
        elif hit_or_stand.lower() == 'stand':
            print('')
            break

        #Adjustments based on hand_type and if the last card drawn is an ace
        user_hand_value = sum(user_card_values)
        aces_in_hand = aces_in_hand_check(user_hand)
        if hand_type == 'hard' and aces_in_hand > 0:
            user_hand_value -= (10 * aces_in_hand)
        
        ace = last_drawn_ace(user_hand)
        if hand_type == 'soft' and ace == True:
            user_hand_value -= 10
        elif hand_type == 'hard' and ace == True:
            hand_type = 'soft'
        
        #USER BUST-ADJUST FOR A SOFT HAND
        if user_hand_value > 21 and hand_type == 'soft':
            user_hand_value -= 10
            hand_type = 'hard'
        elif user_hand_value > 21 and hand_type == 'hard': 
            bust = True
            break
        elif user_hand_value == 21:
            blackjack = True
            break
            
    #End of user's turn / beginning of CPU's turn
    if bust != True and blackjack != True: # if you didn't bust or blackjack, it's the cpu's turn
        #Transition text
        time.sleep(1)
        print("Let's see what the dealer has", end = '\r')
        time.sleep(1)
        print("Let's see what the dealer has.", end = '\r')
        time.sleep(1)
        print("Let's see what the dealer has..", end = '\r')
        time.sleep(1)
        print("Let's see what the dealer has...")
        print('')

        #GET CPU HAND VALUE
        cpu_hand_value = sum(cpu_card_values)
        #HAND TYPE CHECK
        hand_type = hand_type_check(cpu_hand)
        #POCKET ROCKETS CHECK
        if pocket_rockets_check(cpu_hand) == True:
            cpu_hand_value -= 10
        
        #Dealer's rules and decisions             
        while cpu_hand_value < 18:
            if cpu_hand_value < 17: # Hit on Hard 16 or less
                hit_cpu()
            elif cpu_hand_value > 17: # Stand on anything greater than 17
                break
            elif cpu_hand_value == 17:
                if hand_type == 'hard':
                    break # Stand on a hard 17
                elif hand_type == 'soft': 
                    hit_cpu() # Hit on a soft 17

            cpu_hand_value = sum(cpu_card_values)
            aces_in_hand = aces_in_hand_check(cpu_hand)
            if hand_type == 'hard' and aces_in_hand > 0:
                cpu_hand_value -= (10 * aces_in_hand)
            
            ace = last_drawn_ace(cpu_hand)
            if hand_type == 'soft' and ace == True:
                user_hand_value -= 10
            elif hand_type == 'hard' and ace == True:
                hand_type = 'soft'
            
            #CPU BUST-ADJUST FOR A SOFT HAND
            if cpu_hand_value > 21 and hand_type == 'soft':
                cpu_hand_value -= 10
                hand_type = 'hard'
            elif cpu_hand_value > 21 and hand_type == 'hard':
                break

        #Print out CPU's cards
        cpu_hand_length = len(cpu_hand)
        print(cpu_hand[0], end ='\r')
        time.sleep(1)
        print(cpu_hand[0], cpu_hand[1], end='\r')
        time.sleep(1)
        if cpu_hand_length >= 3:
            print(cpu_hand[0], cpu_hand[1], cpu_hand[2], end='\r')
            time.sleep(1)
        if cpu_hand_length >= 4:
            print(cpu_hand[0], cpu_hand[1], cpu_hand[2], cpu_hand[3], end='\r')
            time.sleep(1)
        if cpu_hand_length >= 5:
            print(cpu_hand[0], cpu_hand[1], cpu_hand[2], cpu_hand[3], cpu_hand[4], end='\r')
            time.sleep(1)
        if cpu_hand_length >= 6:
            print(cpu_hand[0], cpu_hand[1], cpu_hand[2], cpu_hand[3], cpu_hand[4], cpu_hand[5], end='\r')
            time.sleep(1)

        print('')
        time.sleep(1)
        print('')        
    
    print('')

    #COMPARE SCORES AND PRINT RESULTS
    if blackjack == True:
        print('BLACKJACK!  You win!')
    elif bust == True:
        print('The user busts!  Better luck next time!')
    elif cpu_hand_value > 21:
        print('The house busts!  You win!')
    elif cpu_hand_value > user_hand_value:
        print('The dealer has {}, the user has {}.'.format(cpu_hand_value,user_hand_value))
        print('')
        print('The house wins!  Better luck next time')
    elif cpu_hand_value < user_hand_value:
        print('The dealer has {}, the user has {}.'.format(cpu_hand_value,user_hand_value))
        print('')
        print('CONGRATULATIONS!  You win!')
    elif cpu_hand_value == user_hand_value:
        print('The dealer has {}, the user has {}.'.format(cpu_hand_value,user_hand_value))
        print('')
        print("It's a push!")
        
    print('')
    print('')

    #PROMPT TO PLAY AGAIN
    play_again = input('Play again? (y/n): ')
    if play_again.lower() == 'y':
        print('')
        print('')
    elif play_again.lower() == 'yes':
        play_again = 'y'
        print('')
    elif play_again.lower() == 'n' or play_again.lower() == 'no':
        print('')
        print('Thank you for playing!')
        print('')
        exit()
        break
    else:
        print('')
