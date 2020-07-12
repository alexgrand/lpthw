from sys import exit
from read import convert_file_to_data

def change_scene(quest_data):
    scene_names_list = list(quest_data.keys())
    print('\nВыберите сцену которую хотите изменить: ')
    print(f"{scene_names_list}")
    scene_to_change = input("> ")

    if not scene_names_list.__contains__(scene_to_change):
        print("\nТакой сцены не существует. Введите данные правильно.")
        return change_scene(quest_data)
    
    edit_scene(quest_data, scene_to_change)

    return quest_data

def edit_scene(data, scene_name):
    print("\nВыберите вариант, который нужно исправить:\n")
    print("1. Название сцены.")
    print('2. Текст сцены.')
    print('3. Варианты ответов.')
    print('4. Название сцен куда ведут варианты ответов.')
    choice = input("> ")

    if choice == '1':
        new_scene_name = write_scene_name(data)
        scene_data = data.pop(scene_name)
        data[new_scene_name] = scene_data
        return check_mistakes(data, new_scene_name)

    elif choice == '2':
        new_text = write_scene_text()
        data[scene_name]['text'] = new_text
        return check_mistakes(data, scene_name)
    
    elif choice == '3' or choice == '4':
        options = write_quest_options()
        data[scene_name]['decisions'] = options.get('decisions')
        data[scene_name]['next_scenes'] = options.get('next_scenes')
        return check_mistakes(data, scene_name)
    
    else:
        print("\n--- ВВЕДИТЕ ПРАВИЛЬНЫЙ ОТВЕТ ---")
        return check_mistakes(data, scene_name)

def check_mistakes(data, scene_name):
    print(f"\n{'-'*10}")
    print("\nПРОВЕРЬТЕ ПРАВИЛЬНОСТЬ ВВЕДЕННЫХ ДАННЫХ СЦЕНЫ:")
    print(f"\n{'-'*10}")
    print(f"\n>>>Название сцены<<<\n{scene_name}")
    print(f"\n>>>Текст сцены<<<\n{data.get(scene_name).get('text')}")
    print(f"\n>>>Варианты ответов<<<\n{data.get(scene_name).get('decisions')}")
    print(f"\n>>>Сцены куда ведут указанные выше шаги<<<\n{data.get(scene_name).get('next_scenes')}")
    print("\nДанные этой сцены введены правильно?")
    print("1. Да")
    print("2. Нет, изменить.")
    is_correct = input("> ")

    if is_correct == '1':
        return True
    elif is_correct == '2':
        return edit_scene(data, scene_name)
    else:
        print("\n--- ВВЕДИТЕ ПРАВИЛЬНЫЙ ОТВЕТ ---")
        return check_mistakes(data, scene_name)

def write_scene_name(quest_data):
    print("\nНапишите название для сцены квеста")
    scene_name = input("> ")
    all_scene_names = quest_data.keys()

    if all_scene_names.__contains__(scene_name):
        print(f"\nТакое имя сцены ** {scene_name} ** уже существует.")
        print("Введите другое имя сцены.")
        return write_scene_name(quest_data)

    return scene_name

def write_scene_text():
    print("\nВведите текст сцены квеста.")
    return input("> ")

def write_scene_option():
    print("\nВпишите вариант ответа")
    return input("> ")

def write_next_scene():
    print("\nВпишите название следующей сцены куда ведет этот вариант.")
    return input("> ")

def write_more_options():
    print("\nЕсть ли еще варианты ответа?")
    print("1. Да")
    print("2. Нет")
    more_options = input("> ")

    if more_options == '1':
        return True
    elif more_options == '2':
        return
    else:
        print("\n--- ВВЕДИТЕ ПРАВИЛЬНЫЙ ОТВЕТ ---")
        return write_more_options()

def write_quest_options():
    options = {}
    decisions = []
    next_scenes = []

    decisions.append(write_scene_option())
    next_scenes.append(write_next_scene())

    while write_more_options():
        decisions.append(write_scene_option())
        next_scenes.append(write_next_scene())

    options['decisions'] = decisions
    options['next_scenes'] = next_scenes

    return options

def has_another_scene(quest_data, scene_name):
    scene_data = quest_data.get(scene_name)
    print("\nЕсть ли еще сцены в этом квесте?")
    print("1. Да.")
    print("2. Нет.")
    has_scene = input("> ")

    if has_scene == '1':
        return True
    elif has_scene == '2':
        i = 0
        decisions = scene_data.get('decisions')
        next_scenes = scene_data.get('next_scenes')

        for option in next_scenes:
            if not list(quest_data.keys()).__contains__(option) and not option == '':
                print("\n\t\t\tВНИМАНИЕ!\n")
                print("\t", f"У вас отсутствует сцена [{option}] для варианта ответа [{decisions[i]}]")
                print("\tНапишите соответствующую сцену.")
                write_scene(quest_data)
            
            i += 1

        return
    else:
        print("\n--- ВВЕДИТЕ ПРАВИЛЬНЫЙ ОТВЕТ ---")
        return has_another_scene(quest_data, scene_name)

def write_scene(quest_data):
    if not quest_data:
        scene_name = 'Begining'
    else:
        scene_name = write_scene_name(quest_data)
        
    scene_text = write_scene_text()
    
    options = write_quest_options()
    decisions = options.get('decisions')
    next_scenes = options.get('next_scenes')
    
    quest_data[scene_name] = {'text': scene_text, 'decisions': decisions, 'next_scenes': next_scenes}

    check_mistakes(quest_data, scene_name)

    if has_another_scene(quest_data, scene_name):
        quest_data = write_scene(quest_data)

    return quest_data

def write_quest_data():
    data = {}
    write_scene(data)

    return data

def write_quest_name():
    print("\nВведите название квеста.")
    quest_name = input("> ")
    print(f"\nНазвание квеста ** {quest_name} **. Правильно?")
    print("1. Правильно")
    print("2. Изменить название")
    correct = input("> ")

    if correct == '1':
        return quest_name
    elif correct == '2':
        return write_quest_name()
    else:
        print("\n--- ВВЕДИТЕ ПРАВИЛЬНЫЙ ОТВЕТ ---")
        return write_quest_name()

def convert_data_to_str(quest_data):
    str_data = ''
    
    for name in quest_data:
        str_data += f"[name]{name}[name]"
        str_data += f"[text]{quest_data[name]['text']}[text]"
        
        decisions = quest_data[name]['decisions']
        next_scenes = quest_data[name]['next_scenes']
        str_data += "[decisions]"

        for i in range(0, len(decisions)):
            str_data += f"[option]{decisions[i]}[option]"
            str_data += f"[next_scene]{next_scenes[i]}[next_scene]"
        
        str_data += "[decisions]\n"
    
    return str_data
        
def write_to_file(fl_name, fl_data):
    str_data = convert_data_to_str(fl_data)
    fl = open(f"{fl_name}.txt", 'w', encoding='utf-8')
    fl.write(str_data)
    fl.close()

def write_new_quest():
    quest_name = write_quest_name()
    quest_data = write_quest_data()

    write_to_file(quest_name, quest_data)

def open_quest_file(fl_name):
    try:
        fl_raw_data = convert_file_to_data(f"{fl_name}.txt")

        return fl_raw_data
    except:
        print(f"\n\tОШИБКА! Квест с именем ** {fl_name} ** не существует.\n")
        exit(0)

def edit_or_change_scene(quest_name, quest_data):
    scene_names_list = list(quest_data.keys())
    print('\nВ квесте уже есть следующие сцены:\n')
    print(f"{scene_names_list}")
    print("\nВы хотите изменить какую то сцену квеста или добавить новую?")
    print("1. Изменить сцену квеста")
    print("2. Добавить сцену квеста")
    edit_or_add = input("> ")

    if edit_or_add == '1':
        quest_data = change_scene(quest_data)
        write_to_file(quest_name, quest_data)
    elif edit_or_add == '2':
        quest_data = write_scene(quest_data)
        write_to_file(quest_name, quest_data)
    else:
        print("\n--- ВВЕДИТЕ ПРАВИЛЬНЫЙ ОТВЕТ ---")
        edit_or_change_scene(quest_name, quest_data)

def edit_quest_data():
    print("\nКакой квест вы хотите изменить? Введите название.")
    quest_name = input("> ")
    data = open_quest_file(quest_name)

    edit_or_change_scene(quest_name, data)

def get_scene(quest_data):
    print("\nКакую сцену Вы хотите просмотреть?")
    choice = input("> ")
    
    try:
        choice = int(choice)
        scene_name = list(quest_data.keys())[choice]

        check_mistakes(quest_data, scene_name)
    except:
        print("\n\t\t---ОШИБКА. ВВЕДИТЕ ПРАВИЛЬНЫЙ НОМЕР СЦЕНЫ---")
        get_scene(quest_data)
        exit(0)

def check_scenes():
    print("\nКакой квест вы хотите просмотреть? Введите название.")
    quest_name = input("> ")
    data = open_quest_file(quest_name)

    print("\nВ указанном Вами квесте существуют следующие сцены: \n")
    
    scenes_list = list(data.keys())
    i = 0

    for scene_name in scenes_list:
        print(f"\t{i}. {scene_name}")
        i += 1
    
    get_scene(data)
    write_to_file(quest_name, data)
    
def start():
    print("\nЧто Вы хотите сделать?\n")
    print("1. Написать новый квест.")
    print("2. Изменить существующий квест.")
    print("3. Прочитать сцены квеста")
    choice = input(">> ")

    if choice == '1':
        write_new_quest()
    elif choice == '2':
        edit_quest_data()
    elif choice == '3':
        check_scenes()
    else:
        print("\n---ВВЕДИТЕ ПРАВИЛЬНЫЙ ОТВЕТ. ЕСЛИ ХОТИТЕ ВЫЙТИ НАЖМИТЕ ctrl-z")
        return start()

start()