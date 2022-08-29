"""
Author: Kartushov Danil

"""
import os
from pylint.lint import Run

def get_pylint_score()->float:
    """
    Get pylint score
    """
    filedir = os.getcwd() + '/user_input/solution.py'
    return Run([filedir], do_exit=False).linter.stats.global_note

def rename_solution_file():
    """
    Rename student file`s to solution.py
    """
    curdir = os.getcwd() + '/user_input'
    student_sol_file = os.listdir(curdir)[0]
    old_file_path = os.path.join(curdir, student_sol_file)
    new_file_path = os.path.join(curdir, 'solution.py')
    #print(old_file_path)
    #print(new_file_path)
    os.rename(old_file_path, new_file_path)

def main(task_type:int=-1):
    """
    Main function

    Parameters
    ----------
    task_type:  int
        1 - First case
        2 - Second case
        3 - Third case
        4 - Four case
        other - All cases
    """
    rename_solution_file()

    if task_type==1:
        print('='*10 + 'First case' + '='*10 )
        print(os.system('python first_case_test.py -v'))
    elif task_type==2:
        print('='*10 + 'Second case' + '='*10 )
        print(os.system('python second_case_test.py -v'))
    elif task_type==3:
        print('='*10 + 'Third case' + '='*10 )
        print(os.system('python third_case_test.py -v'))
    elif task_type==4:
        print('='*10 + 'Four case' + '='*10 )
        print(os.system('python four_case_test.py -v'))
    else:
        print('='*10 + 'First case' + '='*10 )
        print(os.system('python first_case_test.py -v'))
        print('='*10 + 'Second case' + '='*10 )
        print(os.system('python second_case_test.py -v'))
        print('='*10 + 'Third case' + '='*10 )
        print(os.system('python third_case_test.py -v'))
        print('='*10 + 'Four case' + '='*10 )
        print(os.system('python four_case_test.py -v'))

    print('='*10 + 'PyLint' + '='*10)
    print(f'Your pylint score: {get_pylint_score():.4f}')

if __name__ == "__main__":
    main(task_type=-1)
