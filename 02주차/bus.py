def bus_fare(age,fare) :
    if age < 8 :
        bus_fare = "버스요금:무료"
    elif age < 14 :
        bus_fare = "버스요금:450원"
    elif age < 20 and fare == "카드" :
        bus_fare = "버스요금:720원"
    elif age < 20 and fare == "현금" :
        bus_fare = "버스요금:1000원"
    elif age >= 20 and fare == "카드" :
        bus_fare = "버스요금:1200원"
    elif age >= 20 and fare == "현금" :
        bus_fare = "버스요금:1300원"
    else :
        bus_fare = "버스요금:무료"
    return bus_fare
age = int(input("나이:"))
fare = input("지불유형:")
print(bus_fare(age,fare))