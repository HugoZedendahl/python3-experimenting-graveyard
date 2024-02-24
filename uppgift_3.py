namn = "Hugo Zedendahl"

print(namn[0:4])
print(namn[5:14])

aktivitet = "träna"
print("mitt namn är "+namn+" jag gillar att "+aktivitet)

minSträng = "Detta är ent Sträng"

minRättadeSträng = minSträng.replace("ent", "en")
print(minRättadeSträng)

minStoraRättadeSträng = minRättadeSträng.upper()
minLillaRättadeSträng = minRättadeSträng.lower()

print(minStoraRättadeSträng)
print(minLillaRättadeSträng)

tidOchDatum = ("1990:02:14 13:33")
tidOchDatumLista = tidOchDatum.split()

print("datument är "+tidOchDatumLista[0])
print("tiden är "+tidOchDatumLista[1])

var1 = "sträng"
var2 = "f-sträng"

print(f"detta är en {var1} som har blivit modifierad med en {var2}")