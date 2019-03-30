import re

x = input("textul va fi criptat, scrie o propozitie: ")



regex = r"[a-zA-Z]"

if x in regex:
	print("trebuie sa pui numar nu ")
else:
	print("ai pus un numar")