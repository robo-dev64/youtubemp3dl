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