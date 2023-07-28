import re

def najdi_nejcastejsi_slovo(text):
    # Odstranění interpunkce a převedení na malá písmena
    ocisteny_text = re.sub(r'[^\w\s]', '', text.lower())

    # Rozdělení textu na slova
    slova = ocisteny_text.split()

    # Vytvoření slovníku pro počítání výskytů jednotlivých slov a jejich délky
    slovnik_vyskytu = {}
    for slovo in slova:
        slovnik_vyskytu[slovo] = slovnik_vyskytu.get(slovo, 0) + 1

    # Nalezení nejčastějšího slova
    nejcastejsi_slovo = max(slovnik_vyskytu, key=slovnik_vyskytu.get)
    pocet_vyskytu = slovnik_vyskytu[nejcastejsi_slovo]

    return nejcastejsi_slovo, pocet_vyskytu

def najdi_nejdelsi_slovo(text):
    # Odstranění interpunkce a převedení na malá písmena
    ocisteny_text = re.sub(r'[^\w\s]', '', text.lower())

    # Rozdělení textu na slova
    slova = ocisteny_text.split()

    # Nalezení nejdelšího slova
    nejdelsi_slovo = max(slova, key=len)

    return nejdelsi_slovo

# Načtení textu ze souboru
def nacti_text_z_souboru(cesta_k_souboru):
    try:
        with open(cesta_k_souboru, 'r', encoding='utf-8') as soubor:
            text = soubor.read()
        return text
    except FileNotFoundError:
        print(f"Soubor '{cesta_k_souboru}' nebyl nalezen.")
        return None

# Příklad použití
cesta_k_souboru = 'FinalText.txt'  # Nahraďte skutečným umístěním souboru
text = nacti_text_z_souboru(cesta_k_souboru)

if text is not None:
    nejcastejsi_slovo, pocet_vyskytu = najdi_nejcastejsi_slovo(text)
    print(f"Nejčastější slovo: '{nejcastejsi_slovo}', počet výskytů: {pocet_vyskytu}")

    nejdelsi_slovo = najdi_nejdelsi_slovo(text)
    print(f"Nejdelší slovo: '{nejdelsi_slovo}'")


