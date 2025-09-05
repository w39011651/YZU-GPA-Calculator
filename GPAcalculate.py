import parser
from typing import Dict

def score_gpa_convert(score:int)->float:
    if score >= 90:
        return 4.5
    elif score >= 85:
        return 4.0
    elif score >= 80:
        return 3.7
    elif score >= 77:
        return 3.3
    elif score >= 73:
        return 3.0
    elif score >= 70:
        return 2.7
    elif score >= 67:
        return 2.5
    elif score >= 63:
        return 2.3
    elif score >= 60:
        return 2.0
    elif score >= 50:
        return 1.0
    else:
        return 0.0

def calculate_gpa(d:Dict):
    total_credit = 0
    value = 0
    for k,v in d.items():
        total_credit += v['credit']
        value += v['credit'] * score_gpa_convert(v['score'])
    return value/total_credit

if __name__ == '__main__':
    d = parser.run()
    gpa = calculate_gpa(d)
    print(f"Your GPA is {gpa}")
