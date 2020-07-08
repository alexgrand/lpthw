import shutil
from sys import exit
from read import convert_file_to_data

# quest_scenes = convert_file_to_scenes('quest_text.txt')
quest_scenes = convert_file_to_data('Gobsaur.txt')
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

def print_scene(scene_name):
    scene_data = quest_scenes.get(scene_name)    
    print_text(scene_data)
    print_decisions(scene_data)
    
    
def start_quest():
    print_scene('Begining')

start_quest()