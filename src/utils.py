def fix_json(json_string):
    stack = []

    for idx, ch in enumerate(json_string):
        if ch in ["[", "{"]:
            stack.append(ch)
        if ch in ["]", "}"]:
            if (stack[-1] == '[' and ch == ']') or (stack[-1] == '{' and ch == '}'):
                del stack[-1]
            else:
                if ch == '}':
                    json_string = json_string[:idx] + "]" + json_string[idx:]
                else:
                    json_string = json_string[:idx] + "}" + json_string[idx:]
    return json_string


def dict_to_markdown(input_data, depth, prev_list=False):
    if isinstance(input_data, str):
        if prev_list:
            return "* " + input_data + '\n'
        return input_data + '\n'

    if isinstance(input_data, list):
        out_str = ''
        for list_item in input_data:
            out_str += dict_to_markdown(list_item, depth, prev_list=True)
        return out_str

    if isinstance(input_data, dict):
        out_str = ''
        for idx, key in enumerate(input_data.keys()):
            if isinstance(input_data[key], dict) or isinstance(input_data[key], list):
                out_str += "#" * depth + " " + str(key) + "\n"
            if not isinstance(input_data[key], list) and idx == 0:
                out_str += "#" * depth + " "
            out_str += dict_to_markdown(input_data[key], depth + 1)
        return out_str


def cut_to_json(string):
    start_idx = 0
    end_idx = -1
    for idx, ch in enumerate(string):
        if ch in ['[', '{']:
            start_idx = idx
            break
    for idx, ch in enumerate(string[::-1]):
        if ch in [']', '}']:
            end_idx = -1 * idx
            break
    return str(string[start_idx:end_idx])