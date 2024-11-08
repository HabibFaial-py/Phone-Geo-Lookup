from time import time
from numpy import number
import phonenumbers
from phonenumbers import (timezone , geocoder , carrier ,is_valid_number,is_possible_number
,number_type,PhoneNumberType)
numbers = input("enter a number ")
phone = phonenumbers.parse(numbers,"UK",)
times = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone , "en")
is_valid= is_valid_number(phone)
is_possible = is_possible_number(phone)
phone_type=number_type(phone)
print(f"Is the number valid? {is_valid}")
print(f"Is the number possible? {is_possible}")
if phone_type == PhoneNumberType.MOBILE:
    print("The Number is a Mobile Number")
elif phone_type == PhoneNumberType.FIXED_LINE:
    print("The Number is a Fixed line")
elif phone_type == PhoneNumberType.TOLL_FREE:
    print("The Number is a Toll Free Number")
elif phone_type == PhoneNumberType.PREMIUM_RATE:
    print("The Number is a Mobile Number")

print(phone)
print(times)
print(car)
print(reg)