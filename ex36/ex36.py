import shutil
from sys import exit
from read import convert_file_to_data

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

def print_text(scene_data):
    text = scene_data.get('text').split(' ')
    print(format_line(text))

def print_decisions(scene_data):
    decisions = scene_data.get('decisions')
    index = 0

    for decision in decisions:
        index += 1
        decision = f"{index}. {decision}"
        string = decision.split(' ')
        print(format_line(string))

def print_scene(scene_name, quest_data):
    scene_data = quest_data.get(scene_name)    
    print_text(scene_data)
    print_decisions(scene_data)
    
    
def start_quest():
    print('Введите название квеста, который хотите пройти.')
    quest_name = input("> ")

    try:
        quest_data = convert_file_to_data(f"{quest_name}.txt")
        print_scene('Begining', quest_data)
    except:
        print("\nТакого квеста нет.")

start_quest()