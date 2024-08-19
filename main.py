# TODO: pozdravni ekran
# TODO: izbor sifrovanje ili desifrovanje
# TODO: vajl petlja i rec za izlazak iz programa
# TODO: prebacivanje u klase i vise fajlova
# TODO: za vezbu proba i obrnutog preko masine stanja
# ---------- Dictionary's ----------#
kljc = {
    "g": "1",
    "e": "2",
    "r": "3",
    "m": "4",
    "a": "5",
    "n": "6",
    "i": "7",
    "k": "8",
    "u": "9",
    "s": "0"
}

rec = input("Ukucaj rec za sifrovanje:\n").lower()
sifrovana_rec = ""
for slovo in rec:
    if slovo in kljc:
        sifrovana_rec += kljc[slovo]
    else:
        sifrovana_rec += slovo

print(sifrovana_rec)
