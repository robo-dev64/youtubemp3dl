import random
import string

class FileRenaming:
    # symbol to replace any flagged characters with
    REPLACEMENT_SYMBOL = "-"
    # flagged characters for files
    FILE_REPLACE_CHARS = {
        "\\":   REPLACEMENT_SYMBOL,
        "/":    REPLACEMENT_SYMBOL,
        ":":    REPLACEMENT_SYMBOL,
        "*":    REPLACEMENT_SYMBOL,
        "\"":   REPLACEMENT_SYMBOL,
        "<":    REPLACEMENT_SYMBOL,
        ">":    REPLACEMENT_SYMBOL,
        "|":    REPLACEMENT_SYMBOL,        
        }

class Cookies:
    @staticmethod
    def create_cookie(length=11):
        acceptable_chars = string.ascii_letters + string.digits
        return ''.join(random.choice(acceptable_chars) for i in range(length))