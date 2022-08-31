
guest_book = """김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333"""


def wrong_guest_book(guest_book): 
    file = open('guest_book.txt', 'w') 
    file.write(guest_book) 
    file.close 
    guest_list = list(guest_book.split('\n'))  
    for guest in guest_list: 
        name , phone_number = guest.split(',') 
        if phone_number.startswith('010-') and len(phone_number) == 13 and phone_number[8] == '-':
            continue 
        print(f"잘못 쓴 사람:{name}\n잘못 쓴 번호:{phone_number}\n") 
    return
wrong_guest_book(guest_book)