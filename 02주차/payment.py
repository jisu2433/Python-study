monthly_payment = input("월급을 입력해주세요(숫자만) : ")
monthly = int(monthly_payment)
yearly_payment = monthly * 12

if 12000000 >= yearly_payment :
    pre_tax = yearly_payment
    tax_payment = yearly_payment - (yearly_payment * 0.06)
    print("세전 연봉:%d"%pre_tax+ "만원")
    print("세후 연봉:%d"%tax_payment + "만원")
elif 46000000 >= yearly_payment :
    pre_tax = yearly_payment
    tax_payment = yearly_payment - (yearly_payment * 0.15)
    print("세전 연봉:%d"%pre_tax + "만원")
    print("세후 연봉:%d"%tax_payment + "만원")
elif 88000000 >= yearly_payment :
    pre_tax = yearly_payment
    tax_payment = yearly_payment - (yearly_payment * 0.24)
    print("세전 연봉:%d"%pre_tax + "만원")
    print("세후 연봉:%d"%tax_payment + "만원")
elif 150000000 >= yearly_payment :
    pre_tax = yearly_payment
    tax_payment = yearly_payment - (yearly_payment * 0.35)
    print("세전 연봉:%d"%pre_tax + "만원")
    print("세후 연봉:%d"%tax_payment + "만원")
elif 300000000 >= yearly_payment :
    pre_tax = yearly_payment
    tax_payment = yearly_payment - (yearly_payment * 0.38)
    print("세전 연봉:%d"%pre_tax + "만원")
    print("세후 연봉:%d"%tax_payment + "만원")
elif 500000000 >= yearly_payment :
    pre_tax = yearly_payment
    tax_payment = yearly_payment - (yearly_payment * 0.40)
    print("세전 연봉:%d"%pre_tax + "만원")
    print("세후 연봉:%d"%tax_payment + "만원")
else :
    pre_tax = yearly_payment
    tax_payment = yearly_payment - (yearly_payment * 0.42)
    print("세전 연봉:%d"%pre_tax + "만원")
    print("세후 연봉:%d"%tax_payment + "만원")