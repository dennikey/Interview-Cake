def ajv_to_joi(input_str):
    str_array = input_str.split(',')
    answer = ""

    for i  in str_array:
        word = i.replace('\n', '').replace(' ', '').replace('{', '').replace('}', '').replace('"', '')
        words = word.split(":")
        answer += words[0]
        answer += ": "
        answer += "Joi."
        if len(words) == 3:
            answer += words[2]
        answer += "(),"
        answer += "\n"

    return answer

print(ajv_to_joi(""" 	
"label": {
            "type": "string"
        },
        "placeholder": {
            "type": "string"
        },
        "tabindex": {
            "type": "string"
        },
        "hidden": {
            "type": "boolean"
        },
        "disabled": {
            "type": "boolean"
        },
        "autofocus": {
            "type": "boolean"
        },
        "type": {
            "const": "textfield"
        },
        "key": {
            "type": "string"
        },
        "input": {
            "type": "boolean"
        },
        "tableView": {
            "type": "boolean"
        },
        "conditional": {
            "$ref": "#conditional"
        },
        "validate": {
            "$ref": "#validate"
        },
        "reorder": {
            "type": "boolean"
        }
 """
))

