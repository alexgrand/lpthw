import shutil
from sys import exit
from read import convert_file_to_steps

# quest_steps = convert_file_to_steps('quest_text.txt')
quest_steps = convert_file_to_steps('Gobsaur.txt')
# terminal_size = list(shutil.get_terminal_size((80, 20)))[0]
max_line_size = 70

def format_line(words_list):
    line = ''
    new_line = ''

    while len(words_list) > 0:
        if len(new_line) < max_line_size:
            new_line += words_list.pop(0)
            new_line += ' '
        else:
            line += f"\n\t{new_line}"
            new_line = ''
    
    line += f"\n\t{new_line}"

    return line

def print_text(step_data):
    text = step_data.get('text').split(' ')
    print(format_line(text))

def print_decisions(step_data):
    decisions = step_data.get('decisions')
    index = 0

    for decision in decisions:
        index += 1
        decision = f"{index}. {decision}"
        string = decision.split(' ')
        print(format_line(string))

def print_step(step_name):
    step_data = quest_steps.get(step_name)    
    print_text(step_data)
    print_decisions(step_data)
    
    
def start_quest():
    print_step('Start')

start_quest()