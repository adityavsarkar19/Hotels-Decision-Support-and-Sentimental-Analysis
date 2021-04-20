import json
from statistics import mean

def hotel_comment_avg(data):
    for i in data.keys():
        print(i)
        ratings = []
        for r in data[i]['reviews'].items():
            # print(r[1]['rating'], "\n")
            ratings.append(int(r[1]['rating']))
        print(ratings)
        data[i]['comment_rating'] = mean(ratings)
    return data

if __name__=="__main__":
    filename = "Singapore.json"
    with open(filename) as f:
        data = json.load(f)

    data = hotel_comment_avg(data)

    with open(f'{filename}', 'w') as outfile:
            json.dump(data, outfile, indent=4)