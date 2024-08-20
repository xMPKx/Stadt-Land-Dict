Stadt-Land-Dictionary
Dieses Python-Skript erstellt ein Dictionary, in dem Städte ihren entsprechenden Ländern zugeordnet sind. Es bietet Funktionen zur Erstellung des Dictionaries, zur Hinzufügung neuer Stadt-Land-Kombinationen und zur Löschung vorhandener Einträge.

Funktionen:

create_city_country_dict(cities, countries):
Erstellt ein Dictionary d, das Städte aus der Liste cities mit den entsprechenden Ländern aus der Liste countries verknüpft.
Beispiel: { "Berlin": "Germany", "Paris": "France" }
Rückgabewert: Das erstellte Dictionary d.

new_combinations():
Fügt eine neue Stadt-Land-Kombination ("Tokyo": "Japan") in das bestehende Dictionary d ein.
Rückgabewert: Das aktualisierte Dictionary d.

del_eintrag(city, country):
Löscht eine Stadt-Land-Kombination aus dem Dictionary d, wenn diese existiert.
Parameter: city (die Stadt) und country (das Land), die gelöscht werden sollen.
Gibt eine Bestätigung aus, ob die Kombination gelöscht wurde oder nicht gefunden werden konnte.
Rückgabewert: Das aktualisierte Dictionary d.

Verwendung:
Das Skript beginnt mit der Definition von zwei Listen: cities und countries.
Mit der Funktion create_city_country_dict(cities, countries) wird ein Dictionary erstellt, das die Städte den Ländern zuordnet.
Die Funktion new_combinations() fügt eine neue Stadt-Land-Kombination ("Tokyo": "Japan") hinzu.
Mit del_eintrag(city, country) kann eine bestimmte Stadt-Land-Kombination gelöscht werden.
