import random

STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = "+"
PONOVLJENA_CRKA = "o"
NAPACNA_CRKA = "-"
ZMAGA = "W"
PORAZ = "X"

class Igra:
    def __init__(self, geslo):
        self.geslo = geslo.upper()
        self.crke = []
    
    def napacne_crke(self):
        return [c for c in self.crke if c not in self.geslo]
    
    def pravilne_crke(self):
        return [c for c in self.crke if c in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        return all(c in self.crke for c in self.geslo)
    
    def poraz(self):
        return self.stevilo_napak() >= STEVILO_DOVOLJENIH_NAPAK
        
    def pravilni_del_gesla(self):
        novi = ""
        for c in self.geslo:
            if c in self.crke:
                novi += c
            else:
                novi += "_"
        return novi

    def nepravilni_ugibi(self):
        return " ".join(c for c in self.crke if c not in self.geslo)

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        elif crka in self.geslo:
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        self.crke.append(crka)
        if self.poraz():
            return PORAZ
        else:
            return NAPACNA_CRKA

with open("Vislice/besedilo.txt") as f:
    bazen_besed = [beseda.strip() for beseda in f.readlines()]

def nova_igra():
    nova = Igra(random.choice(bazen_besed))
    return nova
    
print(nova_igra())