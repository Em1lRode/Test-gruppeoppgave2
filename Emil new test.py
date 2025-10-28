

print("\nDet har oppstått noen konfliktet innadd i teamet. Erling må prøve å løse alle konfliktene."
      "\nDet er tre konflikter han må løse: "
      "\n-----------------------"
      "\n1. - Hamdi og Jabir"
      "\n2. - Silje og Sivert"
      "\n3. - Noa og Halvgeir"
      "\n-----------------------")


valg1 = input("Konflikt 1 - Hamdi og Jabir"
              "\nHvordan skal Erling løse dette? Alternativ 1 (Kalle inn til et felles møte) eller 2 (Avvente og håpe det ordner seg)?"
              "\n")
if valg1 == "1":
    åpenhet = print("Erling valge å starte en åpen diskusjon for å løse problemet. Dette skaper åpenhet.")
elif valg1 == "2":
    passiv = print("Erling valgte å gå litt mer passivt, avvente og håper det order seg")
else:
    print("Dette er ikke et alternativ.")


print("---------------------------------------------------------------------------------------------")
valg2 = input("\nKonflikt 2 - Silje og Sivert"
              "\nHvordan skal Erling løse dette? Alternativ 1 (Ta det opp i plenum) eller 2 (Ta individuelle samtaler)?"
              "\n")
if valg2 == "1":
    felleskap = print("Erling velger å ta konflikten opp i forsamling, dette kan skape fellesskap")
elif valg2 == "2":
    personlig = print("Erling velger å ta individuelle samtaler med hver enkelt av dem, dette kan bli mer personlig.")
else:
    print("Dette er ikke et alternativ")


print("---------------------------------------------------------------------------------------------")

valg3 = input("\nKonflikt 3 - Noa og Halvgeir"
              "\nHvordan skal Erling løse dette? Alternativ 1 (Aktiv konfliktmegling og felles løsning) eller 2 (Autoritær beslutning og fokus på fremdrift)?"
              "\n")
if valg3 == "1":
    samhold = print("Erling velger å kjøre en strukturert konfliktløsningsøkt. Samholdet kan økes.")
elif valg3 == "2":
    overkjøring = print("Erling velger å bruke makten sin, overkjører partene. I håp om at dette hjelper.")
else:
    print("Dette er ikke et alternativ.")
    
print("---------------------------------------------------------------------------------------------")

slutt1 = "\nEtter å ha gått igjennom alle tre konfliktene styrkes samarbeidet."
slutt2 = "\nEtter å ha gått igjennom alle tre konfliktene blir problemene delvis løst."
slutt3 = "\nEtter å ha gått igjennom alle tre konfliktene blir prosjektet forsinket."

if valg1 == "1" and valg2 == "1" and valg3 == "1":
    print(slutt1)
elif valg1 == "2" and valg2 == "2" and valg3 == "2":
    print(slutt3)
elif valg1 == "1" and valg2 == "2" and valg3 == "2":
    print(slutt2)
elif valg1 == "1" and valg2 == "2" and valg3 == "1":
    print(slutt1)
elif valg1 == "2" and valg2 == "1" and valg3 == "1":
    print(slutt3)
elif valg1 == "2" and valg2 == "1" and valg3 == "2":
    print(slutt2)
elif valg1 == "2" and valg2 == "2" and valg3 == "1":
    print(slutt1)