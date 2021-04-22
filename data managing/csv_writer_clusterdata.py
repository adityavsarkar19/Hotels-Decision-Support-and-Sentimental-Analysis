import csv
import json

def numbers_to_csv(data):
    row_list = [["avg_rating", "comment_avg_rating"]]
    for i in data.keys():
        row = []
        row.append(data[i]['avg_rating'])
        row.append(data[i]['comment_rating'])
        row_list.append(row)
    return row_list

filename = "Bangkok"
with open(f"{filename}.json") as f:
        data = json.load(f)

row_list = numbers_to_csv(data)

with open(f'clustering/{filename}_cluster.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)