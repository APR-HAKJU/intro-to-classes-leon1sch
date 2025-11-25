# TODO: Aufgabe 1:
# Ändere den Code unten, so dass die Eigenschaften des Hauses als Attribute im Konstruktor definiert sind.
# Aktuell werden die Eigenschaften als separate Variablen definiert.
# Definiere einen Konstruktor (__init__), um die Attribute zu initialisieren.
class Haus:
    def __init__(self, quadratmeter):
        print("Neues Haus wurde erstellt")
            self.quadratmeter = quadratmeter
            self.schlafzimmer= schalfzimmer
            self.badezimmer= badezimmer
            print("Neues Haus wurde erstellt")

haus1 = Haus(quadratmeter= 120, schlafzimmer = 3, badezimmer=2)




haus2 = Haus(quadratmeter= 85, schlafzimmer= 4, badezimmer= 4)




haus3 = Haus(quadratmeter= 200, schlafzimmer=3, badezimmer= 4)




haus4 = Haus(quadratmeter=140, schlafzimmer= 3, badezimmer= 3)
print(f"Haus 4 hat {haus4.quadratmeter}m²")

print(f"Haus: {haus1.quadratmeter}m², {haus1.schlafzimmer} Schlafzimmer")
print(f"Haus: {haus2.quadratmeter}m², {haus2.schlafzimmer} Schlafzimmer")
print(f"Haus: {haus3.quadratmeter}m², {haus3.schlafzimmer} Schlafzimmer")

# TODO: Aufgabe 2: Erstelle drei weitere Objekte der Klasse Haus mit unterschiedlichen Eigenschaften.


# TODO: Aufgabe 3: Gib die Anzahl der Schlafzimmer und Badezimmer für jedes Haus aus.