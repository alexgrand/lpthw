def read_file(file_name):
    fl = open(file_name, encoding='utf-8')
    quest_text = fl.read().split('\n')
    fl.close()

    return quest_text

def get_data(line, data_name):
    data = []
    index = 0
    lines_list = line.split(data_name)

    for string in lines_list:
        index += 1
        if index % 2 == 0:
            data.append(string)

    return data

def convert_file_to_steps(quest_name):
    q_steps = {}
    lines = read_file(quest_name)
    index = 0

    for line in lines:
        if line:
            name = get_data(line, '[name]')[0]
            text = get_data(line, '[text]')[0]
            options = get_data(line, '[option]')
            steps = get_data(line, '[next_step]')

            q_steps[name] = {'text': text, 'decisions': options, 'next_steps': steps}
    
    return q_steps
