import csv

data = []

with open('final.csv') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)

headers = data[0]
data_rows = data[1:]
del data_rows[9]

star_masses = []
star_radiuses = []
star_gravities = []
star_names = []
star_distances = []
for star_data in data_rows:
    try:
        star_masses.append(float(star_data[2]))
    except: pass
    try:
        star_radiuses.append(float(star_data[3]))
    except: pass
    try:
        star_gravities.append(float(star_data[8]))
    except: pass
    star_names.append(star_data[0])
        
    splitted_dist = [*star_data[1]]
    for i in range(0, (len(splitted_dist)-1)):
        if splitted_dist[i] == ',':
            dist = star_data[1].split(',')
            dist_1 = dist[0].lstrip('0')
            dist_2 = dist[1]
            final_dist = dist_1 + dist_2
            star_distances.append(float(final_dist))
            break
        else:
            try:
                star_distances.append(float(star_data[1]))
                break
            except: pass
print(len(star_masses))
print(len(star_names))
print(len(star_radiuses))
print(len(star_gravities))
print(len(star_distances))

new_list = []
for index, data_row in enumerate(data_rows):
    if float(star_distances[index]) <= 100 and float(star_gravities[index]) >= 150 and float(star_gravities[index]) <= 350:
        new_list.append(data_row)
print(len(new_list))

#Appropriate data is not given hence not new csv file can be created.