import shutil
from sys import exit
from read import convert_file_to_steps

quest_steps = convert_file_to_steps('quest_text.txt')
# terminal_size = list(shutil.get_terminal_size((80, 20)))[0]
max_line_size = 70

def print_line(words_list):
    line = ''

    while len(line) < max_line_size and len(words_list) > 0:
        line += words_list.pop(0)
        line += ' '
    
    print('\t', line)
    if len(words_list) > 0:
        print_line(words_list)

def print_step(step_name):
    step = quest_steps.get(step_name)
    text = step.get('text').split(' ')
    
    print_line(text)
    
    
def start_quest():
    print_step('Begining')

start_quest()