with open("dna.txt") as DNA_file:
    DNA_sequence = DNA_file.read()

DNA_marker ={
'hair_black': 'CCAGCAATCGC',
'hair_brown': 'GCCAGTGCCG',
'hair_blonde': 'TTAGCTATCGC',
'face_square': 'GCCACGG',
'face_round': 'ACCACAA',
'face_oval': 'AGGCCTCA',
'eye_blue': 'TTGTGGTGGC',
'eye_green': 'GGGAGGTGGC',
'eye_brown': 'AAGTAGTGAC',
'gender_female': 'TGAAGGACCTTC',
'gender_male': 'TGCAGGAACTTC',
'race_white': 'AAAACCTCA',
'race_black': 'CGACTACAG',
'race_asian': 'CGCGGGCCG'
}

DNA_marker_list = DNA_marker.items()
suspect_charateristics = []

#Collecting characteristics

for key, value in DNA_marker_list:
    if DNA_sequence.find(value) != -1:
        suspect_charateristics.append(key)

suspect_charateristics.sort()

print(f"Suspect characteristics: {suspect_charateristics}\n")

#Build models from suspects

peoples = [
    {'Name': 'Eva', 'Gender': 'female', 'Race': 'white', 'Hair color': 'blonde', 'Eye color': 'blue', 'Face shape': 'oval'},
    {'Name': 'Larisa', 'Gender': 'female', 'Race': 'white', 'Hair color': 'brown', 'Eye color': 'brown', 'Face shape': 'oval'},
    {'Name': 'Matej', 'Gender': 'male', 'Race': 'white', 'Hair color': 'black', 'Eye color': 'blue', 'Face shape': 'oval'},
    {'Name': 'Miha', 'Gender': 'male', 'Race': 'white', 'Hair color': 'brown', 'Eye color': 'green', 'Face shape': 'square'}
]

people_model = []
char=[0,1,2,3,4]

for i in range(0, len(peoples)):
    x = peoples[i].values()
    k=0
    for j in x:
        match k:
            case 1:  # Gender
                if str(j) == 'male':
                    char[0] = 'gender_male'
                else:
                    char[0] = "gender_female"

            case 2:  # Race
                if j == 'white':
                    char[1] = 'race_white'
                elif j == 'asian':
                    char[1] = 'race_asian'
                else:
                    char[1] = 'race_black'

            case 3:  # Hair color
                if j == 'brown':
                    char[2] = 'hair_brown'
                elif j == 'black':
                    char[2] = 'hair_black'
                else:
                    char[2] = 'hair_blonde'

            case 4:  # Eye color
                if j == 'blue':
                    char[3] = 'eye_blue'
                elif j == 'green':
                    char[3] = 'eye_green'
                else:
                    char[3] = 'eye_brown'

            case 5:  # Face shape
                if j == 'oval':
                    char[4] = 'face_oval'
                elif j == 'round':
                    char[4] = 'face_round'
                else:
                    char[4] = 'face_square'
        k += 1

    char.sort()
    people_model.append(char[:]) #ha [:] nélkül írnám a char-t, akkor minden tömbelemet ugyanazzal az új értkkel töltene fel

for i in range(0, len(people_model)):
    print(f"Suspect {i+1} characteristics {people_model[i]}")

#Find match between charateristics and suspects

match_nr = -1

while True:
    match_nr = match_nr + 1
    if people_model[match_nr] == suspect_charateristics:
        break

print(f"\nThe guilty is: {peoples[match_nr]['Name']}")


