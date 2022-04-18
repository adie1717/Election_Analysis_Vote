counties = ["Arapahoe","Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or EL Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")
for county in counties:
    print(county)
for num in range(5):
    print(num)
for i in range(len(counties)):
    print(counties[i])
counties_dict = {'Arapahoe':422829,'Denver':463353,'Jefferson':432438}


