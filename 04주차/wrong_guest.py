
guest_book = """�谩,123456789
����,010-1234-5678
�ں�,010-5678-111
����,111-1111-1111
����,010-3333-3333"""


def wrong_guest_book(guest_book): 
    file = open('guest_book.txt', 'w') 
    file.write(guest_book) 
    file.close 
    guest_list = list(guest_book.split('\n'))  
    for guest in guest_list: 
        name , phone_number = guest.split(',') 
        if phone_number.startswith('010-') and len(phone_number) == 13 and phone_number[8] == '-':
            continue 
        print(f"�߸� �� ���:{name}\n�߸� �� ��ȣ:{phone_number}\n") 
    return
wrong_guest_book(guest_book)