from constants import *


def decode_dictionary(dictionary, depth=0):
    result = ""
    for key, value in dictionary.items():
        if type(value) == dict:
            if len(result) >= 2 and result[-2] == "}":
                result += "\n"
            result += "\t" * depth + key + " = " + "{" + "\n"
            result += decode_dictionary(value, depth + 1)
        elif type(value) == list:
            for element in value:
                result += "\t" * depth + key + " = " + "{" + "\n"
                result += decode_dictionary(element, depth + 1)
        elif type(value) == str:
            result += "\t" * depth + key + " = " + value + "\n"
        elif type(value) == bool:
            result += "\t" * depth + key + "\n"
        elif type(key) == int:
            if value[3] == Constants.PART_LINE_COMMENT_TYPE:
                result = result[:-1] + " " + value[2] + "\n"
            if value[3] == Constants.FULL_LINE_COMMENT_TYPE:
                result += value[2] + "\n"
    if depth > 0:
        result += "\t" * (depth - 1) + "}" + "\n"
    return result
