from bs4 import BeautifulSoup
from typing import List

def get_soup_from_html_text(file_path:str="IFrameRight.aspx_files/IFrameSub.html"):
    """
    Open the html file in file_path
    Change its text to soup and return it
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'lxml')
    return soup

def get_table_information(soup:BeautifulSoup):
    table = soup.select("#Table1>tbody>tr")#直接獲取表格資訊
    return table[1:]

def split_information_from_line(text:str):
    """
    這邊送入的字串格式會是: NO 學年期 選別 課號 班別 課名 期中評量 學分 成績
    """
    parts = text.split()
    if parts[-1].isdigit() and parts[-2].isdigit():
        course_name = parts[5] # 第6個元素為課程名稱 第7個是英文名稱
        credit = parts[-2] # 倒數第2個元素為學分
        score = parts[-1] # 倒數第1個元素為分數
        #print(f"學分: {credit}, 分數: {score}, 課程名稱: {course_name}")
        return course_name, int(credit), int(score)
    return None, None, None

def get_course_and_score(table_tags:List):
    course_and_score = dict() #課程，學分以及分數對應關係
    for table_row in table_tags:
        line = str()
        for td in table_row:
            line = line + td.text + ' '
        course, credit, score = split_information_from_line(line)#函數中得出的資訊
        if not (course is None and credit is None and score is None):
            course_and_score[course] = {'credit':credit, 'score':score}
    return course_and_score

def run():
    soup = get_soup_from_html_text()
    table_tags = get_table_information(soup)
    return get_course_and_score(table_tags)
    
if __name__ == '__main__':
    soup = get_soup_from_html_text()
    table_tags = get_table_information(soup)
    get_course_and_score(table_tags)