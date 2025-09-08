import csv
import parser
from typing import Dict, List, Tuple

def formalize(d:Dict)->List[Tuple]:
    for k,v in d.items():
        d[k] = v['score']
    sorted_items_by_value = sorted(d.items(), key=lambda item: item[1], reverse=True)
    return sorted_items_by_value

def save_to_csv(l:List):
    with open('grade.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Course', 'Score'])
        for item in l:
            row = [item[0], item[1]]
            writer.writerow(row)
    print("Save is Done.")



if __name__ == '__main__':
    d = parser.run()
    l = formalize(d)
    save_to_csv(l)