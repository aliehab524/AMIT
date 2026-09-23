def is_not_empty(text):

    return len(str(text).strip()) > 0


def is_number(text):
    try:
        int(text)
        return True
    except ValueError:
        return False


def is_valid_id(text):
    if not is_not_empty(text) or not is_number(text):
        return False
    return True


def is_valid_title(text):
     
    cleaned_text = str(text).strip()
    return len(cleaned_text) >= 2


def is_in_range(text,low,high):
    if not is_number(text):
        return False
    num = int(text)
    return low <= num <= high


