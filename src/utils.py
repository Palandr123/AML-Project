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
                    json_string = json_string[:idx - 1] + "]" + json_string[idx - 1:]
                else:
                    json_string = json_string[:idx - 1] + "}" + json_string[idx - 1:]
    return json_string
