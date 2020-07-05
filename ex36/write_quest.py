from sys import exit

def check_mistakes(data, step_name):
    print(f"\n{'-'*10}")
    print("\nПРОВЕРЬТЕ ПРАВИЛЬНОСТЬ ВВЕДЕННЫХ ДАННЫХ СЦЕНЫ:")
    print(f"\n{'-'*10}")
    print(f"\n>>>Название сцены<<<\n{step_name}")
    print(f"\n>>>Текст сцены<<<\n{data.get(step_name).get('text')}")
    print(f"\n>>>Варианты ответов<<<\n{data.get(step_name).get('decisions')}")
    print(f"\n>>>Сцены куда ведут указанные выше шаги<<<\n{data.get(step_name).get('next_steps')}")
    print("\nДанные этой сцены введены правильно?")
    print("1. Да")
    print("2. Нет, изменить.")
    is_correct = input("> ")

    if is_correct == '1':
        return True
    elif is_correct == '2':
        print("\nВыберите вариант, который нужно исправить:\n")
        print("1. Название сцены.")
        print('2. Текст сцены.')
        print('3. Варианты ответов.')
        print('4. Название сцен куда ведут варианты ответов.')
        choice = input("> ")

        if choice == '1':
            new_step_name = write_step_name()
            step_data = data.pop(step_name)
            data[new_step_name] = step_data
            return check_mistakes(data, new_step_name)

        elif choice == '2':
            new_text = write_step_text()
            data[step_name]['text'] = new_text
            return check_mistakes(data, step_name)
        
        elif choice == '3' or choice == '4':
            options = write_quest_options()
            data[step_name]['decisions'] = options.get('decisions')
            data[step_name]['next_steps'] = options.get('next_steps')
            return check_mistakes(data, step_name)
        
        else:
            print("\n--- ВВЕДИТЕ ПРАВИЛЬНЫЙ ОТВЕТ ---")
            return check_mistakes(data, step_name)

    else:
        print("\n--- ВВЕДИТЕ ПРАВИЛЬНЫЙ ОТВЕТ ---")
        return check_mistakes(data, step_name)

def write_step_name():
    print("\nНапишите название этой сцены квеста")
    return input("> ")

def write_step_text():
    print("\nВведите текст сцены квеста.")
    return input("> ")

def write_step_option():
    print("\nВпишите вариант ответа")
    return input("> ")

def write_next_step():
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
    next_steps = []

    decisions.append(write_step_option())
    next_steps.append(write_next_step())

    while write_more_options():
        decisions.append(write_step_option())
        next_steps.append(write_next_step())

    options['decisions'] = decisions
    options['next_steps'] = next_steps

    return options

def write_quest_step():
    step_data = {}
    step_name = write_step_name()
    step_text = write_step_text()
    
    options = write_quest_options()
    decisions = options.get('decisions')
    next_steps = options.get('next_steps')
    
    step_data[step_name] = {'text': step_text, 'decisions': decisions, 'next_steps': next_steps}

    check_mistakes(step_data, step_name)

    return step_data

def write_quest_data():
    data = {}
    write_quest_step()

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

def write_new_quest():
    quest_name = write_quest_name()
    quest_data = write_quest_data()
    
def new_or_edit():
    print("\nЧто Вы хотите сделать?\n")
    print("1. Написать новый квест.")
    print("2. Изменить существующий квест.")
    new_quest = input(">> ")

    if new_quest == '1':
        return True
    elif new_quest == '2':
        return
    else:
        print("\n---ВВЕДИТЕ ПРАВИЛЬНЫЙ ОТВЕТ. ЕСЛИ ХОТИТЕ ВЫЙТИ НАЖМИТЕ ctrl-z")
        return new_or_edit()

def start():
    new_quest = new_or_edit()
    
    if new_quest:
        write_new_quest()
    else:
        print("Изменим квест")



start()