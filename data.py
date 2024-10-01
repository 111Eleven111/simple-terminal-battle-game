"""
Dataklasse som styrer karakterlogikk og data.
Data klassen "Karakter" representerer data for en spiller og initierer 
tre instansvariabler. En for navn, en for liv og en teller for antall
ganger spilleren kan bruke "medisin" for aa faa tilbake liv.

Skrevet av Bagus André Aarvak
"""

from random import randint

#1)
class Karakter:
	def __init__(self, navn, vaapen):
		self._navn = str(navn)
		self._liv = 50
		self._medisin = 1
		self._forsvar = 0
		
		#3)
		if vaapen == "1":
			self._vaapen = 12
			#BladeMaster (Sverd)
			
		elif vaapen == "2":
			self._vaapen = 16
			#Destroyer (Oks)
		
		elif vaapen == "3":
			self._vaapen = 4
			#Assassin (Kniv)
			
		
	def skriv_ut_info(self):
		print("")
		print(f"Navn: {self._navn}.")
		if self._vaapen == 12:
			print("Klasse: Blade Master.")
		elif self._vaapen == 16:
			print("Klasse: Destroyer.")
		elif self._vaapen == 5:
			print("Klasse: Assassin.")
		print(f"Styrke: {self._vaapen}.")
		print(f"Liv: {self._liv}.")
		print("")
		
	def hent_navn(self):
		return(self._navn)
		
	def hent_forsvar(self):
		return(self._forsvar)
		
	def ok_forsvar(self):
		okning = randint(-1, 3)
		if self._forsvar < 3 and not okning == -1 and not okning == 0:
			self._forsvar += okning
		
			print("")
			print(f"Forsvar okt med {okning}!")
			print(f"Resterende forsvar: {self._forsvar}.")
			print(f"{self._navn} sin resterende HP: {self._liv}.")
			
		elif okning == -1:
			self._forsvar += okning
			print("")
			print(f"Du trynte! Forsvar gikk ned med {-1 * okning}!")
			print(f"Resterende forsvar: {self._forsvar}.")
			print(f"{self._navn} sin resterende HP: {self._liv}.")
			
		elif okning == 0:
			print("")
			print("Ingenting hendte...")
			print(f"{self._navn} sin resterende HP: {self._liv}.")
			
		else:
			print("")
			print("Du har maks forsvar!")
			print(f"{self._navn} sin resterende HP: {self._liv}.")
			
	def senk_forsvar(self):
		if randint(0, 5) == 0:
			self._forsvar -= 1
			print(f"Forsvaret til {self._navn} gikk ned med en!")
			print(f"Resterende forsvar: {self._forsvar}.")
		
	def medisin(self):
		if self._medisin > 0:
			print("")
			print("HEAL!")
			
			self._liv += 20
			print(f"{self._navn} sin resterende HP: {self._liv}.")
			
			self._medisin -= 1
			
		else:
			print("Tom for medisin!")
			
	
	#3) (implementasjon)
	def angrip(self, motstander):
		if self._vaapen == 12:
			#Sverd: gjor alltid angitt skade:
			motstander.ta_skade(self._vaapen)
		
		elif self._vaapen == 16:
			#Oks: Gjor mer skade, men kan bomme.
			miss = randint(0, 3)
			
			if miss == 0:
				print("Oksen bommet!")
				
			else:
				motstander.ta_skade(self._vaapen)
				
		elif self._vaapen == 5:
			#Kniv: Gjor minst skade, men kan treffe opp til fem ganger:
			antall = randint(0, 5)
			
			if antall == 0:
				print("Kniven bommet!")
				
			else:
				print(f"Kniven traff {antall} ganger!")
				
				
			for tall in range(antall):
				motstander.ta_skade(self._vaapen)
				
		return self._liv
		
	def ta_skade(self, skade):
		ekstra = randint(0, 10)
		print("")
		
		if ekstra == 0:
			self._liv -= (2 * (skade + randint(0, 3))) - self._forsvar
			print("Kritisk treff! DATZ A LOT OF DAMADGE!")
			
			if not self._liv <= 0:
				print(f"{self._navn} sin resterende HP: {self._liv}.")
		
		else:
			self._liv -= (skade + randint(-2, 3)) - self._forsvar
			
			if not self._liv <= 0:
				print(f"{self._navn} sin resterende HP: {self._liv}.")		
		
	def kontroll(self):
		if self._liv <= 0:
			print(f"{self._navn} dode!")
			
			return True
