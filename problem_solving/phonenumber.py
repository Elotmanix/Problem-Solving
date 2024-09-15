
import phonenumbers
from phonenumbers import geocoder, carrier, timezone


entered_num = input("Please enter a phone number: ")

# create PhoneNumber object
phone_num = phonenumbers.parse(entered_num, None)
# phone_num = phonenumbers.parse(entered_num, "EG")

print(phone_num)

# information about the location that corresponds to a phone number.
print(geocoder.description_for_number(phone_num, "ar"))

# For mobile numbers in some countries,
# information about which carrier originally owned a phone number.
print(carrier.name_for_number(phone_num, "en"))


# retrieve a list of time zone names that the number potentially belongs to.
print(timezone.time_zones_for_number(phone_num))
