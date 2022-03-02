student_list = list()
morning = ""
afternoon = ""

def str_to_dic(string):
    name = ''
    chat_log_dic = dict()
    parsed_strings = string.split('  |  ')
    for parsed_string in reversed(parsed_strings):        
        if not name:
            name = parsed_string.split('\n')[0]
            continue
        
        chat_num = parsed_string.split('\n')[1]
        chat_log_dic[name] = int(chat_num)
        name = parsed_string.split('\n')[0]
    
    print(chat_log_dic)
    return chat_log_dic

def sum_two_chat(student_list, morning, afternoon):

    print('\n****오전 채팅 결과를 출력합니다****')
    mor_dic = str_to_dic(morning)

    print('\n****오후 채팅 결과를 출력합니다****')
    aft_dic = str_to_dic(afternoon)

    chat_num_dict = dict()
    for student in student_list:
        try:
            chat_num_dict[student] = mor_dic[student] + aft_dic[student]

        except KeyError:
            if student in mor_dic.keys():
                print(f"\n!!!!!!!!{student} 님 오후 세션 불참!!!!!!!!")
                chat_num_dict[student] = mor_dic[student]
            
            elif student in aft_dic.keys():
                print(f"\n!!!!!!!!{student} 님 오전 세션 불참!!!!!!!!")
                chat_num_dict[student] = aft_dic[student]

            else:
                print(f"\n!!!!!!!!{student} 님 오전 오후 세션 모두 불참!!!!!!!!")
            pass
    
    return chat_num_dict

def order_one_chat(student_list, chat):

    chat_dic = str_to_dic(chat)
    chat_num_dict = dict()

    for student in student_list:
        try:
            chat_num_dict[student] = chat_dic[student]

        except KeyError:
            print(f'\n{student}에서 Key error 발생')
            pass

    return chat_num_dict

def get_chat_result(student_list, morning, afternoon):
    
    if morning and afternoon:
        chat_num_dict = sum_two_chat(student_list, morning, afternoon)  
    elif morning:
        print('****오후 채팅이 없습니다. 오전 채팅 결과만 출력합니다****')
        chat_num_dict = order_one_chat(student_list, morning)  
    else:
        print('****오전 채팅이 없습니다. 오후 채팅 결과만 출력합니다****')
        chat_num_dict = order_one_chat(student_list, afternoon)

    print('\n****urclass 순서대로 최종 채팅 결과를 출력합니다****')
    print(chat_num_dict) 
    return chat_num_dict

if __name__ == "__main__":    
    get_chat_result(student_list, morning, afternoon)