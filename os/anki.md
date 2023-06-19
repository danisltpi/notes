# Betriebssysteme Klausur

## Offen

- Was ist ein Prozess?

- Was ist Privileged Mode?

- Was ist Limited Direct Execution?

- Was ist yield?

- Aus welchem Grund verfügt ein MLFQ-Scheduler über mehrere Warteschlangen?

- Woher bezieht ein typischer MLFQ-Scheduler sein Wissen, um Prozesse zu priorisieren?

- Ist die von einem MLFQ-Scheduler vorgenommene Priorisierung eines Prozesses endgültig?

- Scheduling allgemein mit Optimierung von Bearbeitungsreihenfolge

- Dateisysteme allgemein

- Wann spricht man bei einem Dateisystem von einem inkonsistenten Zustand?

- Erklären Sie anhand eines kurzen Szenarios, wie es beim Schreiben von Daten zu einem
  inkonsistenten Zustand kommen kann.

- Welchen Vorteil bietet „Journaling“ gegenüber einem „Check-and-Repair“-Ansatz?

- Welche der folgenden Größen wäre aus Ihrer Sicht für eine Inode sinnvoll und warum? 156 Byte 256 Byte 356 Byte

- Wie kann über eine Inode fester Größe eine Datei mit variabler Größe verwaltet werden?

- Eine 2 TiB große Festplatte soll mit diesem Dateisystem formatiert werden. Wie viel
  Speicherplatz muss man für die anfallenden Meta-Daten (D-Map, I-Map und Inodes) etwa reservieren, wenn man von einer typischen Dateigröße von 8 KiB ausgehen darf? Geben Sie sinnvolle Abschätzungen an und begründen Sie Ihre Antworten

- Offset einer virtuellen Adresse

- Welchen Einfluss haben die Größe eines Page Frames, die Größe eines PTEs und die Anzahl
  an Hierarchieebenen auf die effektiv nutzbaren Bits einer virtuellen Adresse?

- Wie viele Bits einer virtuellen 64 Bit-Adresse werden in einem Szenario effektiv genutzt? Was könnte man mit den verbleibenden Bits tun?

- Lotterie-Scheduler

- Offensichtlich kann es bei parallelen Zugriffen auf ein und denselben Scheduler zu Problemen kommen. Beschreiben Sie mindestens ein konkretes Szenario, bei dem es zu einem Laufzeitfehler kommt. Zum Beispiel durch den Zugriff auf ein nicht mehr vorhandenes Objekt.

- Was unterscheidet einen Reader von einem Writer?

- Welche der öffentlichen Methoden des Schedulers dienen im Sinne des Readers-andWriters-Pattern dem Lesen und welche dem Schreiben? Begründen Sie Ihre Antwort.
