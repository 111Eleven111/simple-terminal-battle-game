"""
Enkelt terminalbasert kampspill for to spillere som benytter objektorientering:
Spillerne skal ta tur i aa angripe og dataen til spillerne lagres som objekter.
Spillerene kan velge eget navn og et vaapen som avgjor
styrke. Elementer av tilfeldighet gir hver kamp en et unikt scenario.

Data klassen "Karakter" i data.py representerer data for en spiller og initierer 
tre instansvariabler. En for navn, en for liv og en teller for antall
ganger spilleren kan bruke "medisin" for aa faa tilbake liv.

Hovedprogrammet benytter "multiprocessing" og "playsound" for å kjøre musikken på egen tråd.
Først forklares spillet til brukerene, så kjøres en kommandoløkke for spillet til en av
spillerene ikke har mer liv.

Skrevet av Bagus André Aarvak
"""
import multiprocessing
from data import Karakter
from playsound import playsound
from random import randint
from multiprocessing.pool import ThreadPool as Pool

def hovedprogram():
	musikk = multiprocessing.Process(target=playsound, args=("musikk/startmusikk.mp3",))
	musikk.start()
	
	print("Velkommen til kamp-spill for to spillere!\nDere kan velge mellom tre klasser:\n")
	print("1: Blade Master (Sverd).\n2: Destroyer (Oks).\n3: Assassin (Kniv).\n")
	print("Sverd: gjor alltid skade\nOks: Gjor mer skade, men kan bomme.")
	print("Kniv: Gjor minst skade, men kan treffe opp til fem ganger.")
	print(input("Trykk ENTER for aa fortsette:\n"))
	
	navn1 = str(input("Spiller 1: Skriv navn: "))
	vaapen1 = str(input("Spiller 1 velg vaapen: (1,2 eller 3) "))
	
	navn2 = str(input("Spiller 2: Skriv navn: "))
	vaapen2 = str(input("Spiller 2 velg vaapen: (1,2 eller 3) "))
	
	p1 = Karakter(navn1, vaapen1)
	p2 = Karakter(navn2, vaapen2)
	
	print("--------------------")
	p1.skriv_ut_info()
	
	print("                  ------  ")
	print(" \        /     /         ")
	print("  \      /      \         ")
	print("   \    /         ---     ")
	print("    \  /              \   ")
	print("     \/               /   ")
	print("                ------    ")
	
	p2.skriv_ut_info()
	print("--------------------")
	
	print("Skriv angrip for aa angripe.")
	print("Skriv medisin for aa ta en medisin (du har kun 1).")
	print("Skriv forsvar for aa oke forsvar (3 er maks).")
	print("")
	print("(Tilfeldig før en tur kan forsvaret ditt synke med en!)")
	print(input("Trykk ENTER for aa starte kampen!"))
	print("...")
	print("FIGTH!")
	
	musikk.terminate()
	musikk = multiprocessing.Process(target=playsound, args=("musikk/kampmusikk.mp3",))
	musikk.start()

	if randint(0, 1) == 1:
		tur = p1
		
	else:
		tur = p2
	
	ferdig = False
	while not ferdig:
		
		if tur == p1:
			p1.senk_forsvar()
			
		elif tur == p2:
			p2.senk_forsvar()
		
		brukervalg = input(f"{tur.hent_navn()} sin tur! Hva gjor du? ")
		
		if brukervalg == "angrip" and tur == p1:
			p1.angrip(p2)
			tur = p2
			print("Spiller 1 sin tur er over!")
			ferdig = p2.kontroll()
			print("")
			print("--------------------")
			print("")
			
		elif brukervalg == "medisin" and tur == p1:
			p1.medisin()
			tur = p2
			print("Spiller 1 sin tur er over!")
			print("")
			print("--------------------")
			print("")
			
		elif brukervalg == "angrip" and tur == p2:
			p2.angrip(p1)
			tur = p1
			print("Spiller 2 sin tur er over!")
			ferdig = p1.kontroll()
			print("")
			print("--------------------")
			print("")
			
		elif brukervalg == "medisin" and tur == p2:
			p2.medisin()
			tur = p1
			print("Spiller 2 sin tur er over!")
			print("")
			print("--------------------")
			print("")
			
		elif brukervalg == "forsvar" and tur == p1:
			p1.ok_forsvar()
			tur = p2
			print("Spiller 1 sin tur er over!")
			print("")
			print("--------------------")
			print("")
			
		elif brukervalg == "forsvar" and tur == p2:
			p2.ok_forsvar()
			tur = p1
			print("Spiller 1 sin tur er over!")
			print("")
			print("--------------------")
			print("")
	
	musikk.terminate()
	musikk = multiprocessing.Process(target=playsound, args=("musikk/sluttmusikk.mp3",))
	musikk.start()
	input("Tast en hvilken som helst tast for å avslutte! ")
	musikk.terminate()

if __name__ == '__main__':
	hovedprogram()
