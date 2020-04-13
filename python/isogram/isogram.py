def is_isogram(string):
    let = []
    for x in string.lower():
        if x in let:
            return False
        if x.isalpha():
            let.append(x)
    return True
