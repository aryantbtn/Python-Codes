# Phone Number Details using Python library named "phonenumbers" -> like company, state, name, etc.
import phonenumbers as ph
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

numbers = "+919528773925"
details = ph.parse(numbers)
print(timezone.time_zones_for_number(details))
print(carrier.name_for_number(details, "en"))
print(geocoder.description_for_number(details, "en"))