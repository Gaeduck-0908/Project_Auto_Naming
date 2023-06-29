# 파일명 자동 완성

import os
import time

project_name = []
module_name = []
result_name = ''
path =''
file_ex = ''
file_name = ''

module_dict = {
    'Z':'ZM',
    'W':'TAX',
    'S':'SD',
    'J':'SCM',
    'Q':'QM',
    'M':'MM',
    'Y':'PS',
    'P':'PP',
    'U':'PR',
    'H':'HR',
    'B':'MDM',
    'I':'IM',
    'K':'MC',
    'A':'FI',
    'V':'EIS',
    'C':'CO',
    'G':'CO',
    'D':'CFG'}


def setDirLocation():
    global path, file_ex, file_name
    
    path = input('\n사양서가 있는 파일의 경로를 입력해주세요\n> ')
    file_ex = r'.pptx'
    file_name = ''.join(i for i in [file for file in os.listdir(path) if file.endswith(file_ex)])

def makeProjectName():
    global project_name
    
    for i in file_name:
        if i == '(' : break
        project_name.append(str(i))
    
    return_val = ''.join(project_name)
    
    return return_val

def makeProjectModuleName():
    global module_name
    
    if project_name[0].upper() in module_dict:
        module_name.append(module_dict[project_name[0].upper()])
        
    return_val = ''.join(module_name)
    
    return return_val

def runProgram():
    global result_name
    
    name_1 = makeProjectName()
    name_2 = makeProjectModuleName()
    
    result_name = name_2 + '.' + name_1

if __name__ == '__main__' :
    setDirLocation()
    while (True):
        print(f'\n[BIZENTRO UNIERP 프로젝트 이름 생성기]\n사양서 파일이 .pptx 확장자 일때만 인식이 가능합니다.\npath 경로에 사양서가 있어야합니다.\n또한 pptx 파일이 한 개만 존재해야합니다\n현 path 경로 : {path}\n\n1.BL 생성 2.UI 생성 3.종료\n')
        p_input = input('> ')
        
        match p_input:
            case '1':
                runProgram()
                print(f'Bizentro.App.BL.{result_name}')
                print('프로젝트 이름 생성이 완료되었습니다.')
                exit(0)
            case '2':
                runProgram()
                print(f'Bizentro.App.UI.{result_name}')
                print('프로젝트 이름 생성이 완료되었습니다.')
                exit(0)
            case '3':
                print('프로그램을 종료합니다')
                time.sleep(1)
                exit(0)
            case _:
                print('잘못된 입력입니다.')