import csv
import os

def write_csv(file_name, student_dict:dict):
    with open(f'./result/{file_name}.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        for key, value in student_dict.items():
            writer.writerow([key,value])
    return None          

def extract_student_list(student_csv_name:str) -> dict:
    """
    file_name = urclass admin에서 다운로드한 수강생 정보 csv 파일명
    return = 수강생 이름이 key로 들어간 딕셔너리
    """

    student_dict = dict()
    with open(f'{student_csv_name}.csv', 'r', encoding='utf-8') as f:
        lines = csv.reader(f)
        cnt = 0
        for rec in lines:
            if cnt == 0:
                cnt+=1
                continue
            student_dict[rec[1]] = 0
    
    print(student_dict)
    return student_dict

def count_chat(chat_txt_name:str, student_dict:dict) -> dict:
    with open(f'chat/{chat_txt_name}.txt', 'r') as f:
        lines = f.readlines()
        for i in range(0,len(lines),2):
            line = lines[i]
            for key in student_dict.keys():
                if key not in line:
                    continue
                student_dict[key]+=1
    return student_dict
      
def extract_chat_cnt(student_csv_name:str, mor_txt_name=None, aft_txt_name=None) -> dict:
    """
    student_csv_name: urclass admin에서 다운로드한 수강생 정보 csv 파일명
    chat_mor_txt_name: 오전 채팅 txt 파일명, 없으면 None
    chat_aft_txt_name: 오후 채팅 txt 파일명, 없으면 None
    """
    student_dict = extract_student_list(student_csv_name)

    if mor_txt_name:
        student_dict = count_chat(mor_txt_name, student_dict)
        print('\n****오전 채팅 결과를 출력합니다****')
        print(student_dict)
        result_file_name = f'{mor_txt_name}'
    
    elif aft_txt_name:
        student_dict = count_chat(aft_txt_name, student_dict)
        print('\n****오전 채팅 결과를 출력합니다****')
        print(student_dict)
        result_file_name = f'{aft_txt_name}'
    
    if mor_txt_name and aft_txt_name:
        print('\n****오전과 오후 채팅을 더한 결과를 출력합니다****')
        student_dict = count_chat(aft_txt_name, student_dict)
        print(student_dict)
    
    os.makedirs('./result', exist_ok=True)
    write_csv(result_file_name, student_dict)
    
    return student_dict



if __name__ == "__main__":
    file_list = ['n322','n323','n324','n32x','n331','n332','n333','n334','n33x','n3xx','project']

    for file_name in file_list:
        print(f'------------{file_name}------------')
        extract_chat_cnt('10_list',file_name)
