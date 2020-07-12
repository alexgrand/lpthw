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
            word = words_list.pop(0)
            word = word.replace('\\t', '\t')

            if word.__contains__('\\n'):
                words = word.split('\\n')
                new_line += words.pop(0)
                line += f"\n\t{new_line}"
                new_line = '\n\t'.join(words)
                new_line += ' '
            else:
                new_line += word
                new_line += ' '

        else:
            line += f"\n\t{new_line}"
            new_line = ''
    
    line += f"\n\t{new_line}\n"        

    return line

def print_text(scene_data):
    text = scene_data.get('text').split(' ')
    print(format_line(text))

def print_decisions(scene_data):
    decisions = scene_data.get('decisions')
    index = 0

    for decision in decisions:
        if decision:
            index += 1
            decision = f"{index}. {decision}"
            string = decision.split(' ')
            print(format_line(string))

def print_scene(scene_name, quest_data):
    scene_data = quest_data.get(scene_name)    
    print_text(scene_data)
    print_decisions(scene_data)

def print_quest_name(quest_name):
    name_len = len(quest_name)
    middle_point = int((max_line_size - name_len) / 2)
    print(f"\t{'-' * (max_line_size + 3)}")
    print(f"\t|{' ' * middle_point} {quest_name} {middle_point * ' '}|")
    print(f"\t{'-' * (max_line_size + 3)}")
    
def play(quest_data, scene_name):
    scene_data = quest_data.get(scene_name)
    decisions = scene_data.get('decisions')
    next_scenes = scene_data.get('next_scenes')

    if not decisions.count(''):
        choice = input("\t> ")

        try:
            choice = int(choice)
            next_scene_name = next_scenes[choice - 1]

            print_scene(next_scene_name, quest_data)
            play(quest_data, next_scene_name)        
        except:
            print("\n\n\t\t---ВВЕДИТЕ ПРАВИЛЬНЫЙ ОТВЕТ---\n")
            play(quest_data, scene_name)
    
    else:
        return

def start_quest():
    print('Введите название квеста, который хотите пройти.')
    quest_name = input("> ")

    try:
        quest_data = convert_file_to_data(f"{quest_name}.txt")
    except:
        print("\nТакого квеста нет.")
        exit(0)
    
    print_quest_name(quest_name)
    print_scene('Begining', quest_data)
    play(quest_data, 'Begining')
    print_quest_name('END')

start_quest()