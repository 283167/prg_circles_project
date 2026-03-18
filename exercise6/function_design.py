def analyze_password(password, require_upper=True, require_symbol=False):
    contains_upper = False
    contains_symbol = False
    symbols = "!@#$%^&*()-_=+[]{};:,.?"
    requirements = []
    if require_upper:
        for i in password:
            if i.isupper():
                contains_upper = True
                break
        requirements.append(contains_upper)
    if require_symbol:
        for i in password:
            if i in symbols:
                contains_symbol = True
                break
        requirements.append(contains_symbol)
    is_strong = True
    count_true = 0
    for i in requirements:
        if i == True:
            count_true += 1
        else:
            is_strong = False


    missing_rules = []
    if contains_upper:
        count_true += 1
    else:
        is_strong = False
        missing_rules.append("upper")
    if contains_symbol:
        count_true += 1
    else:
        is_strong = False
        missing_rules.append("symbol")
    score_percent = int(count_true/len(requirements) * 100)
    return is_strong, score_percent, missing_rules

print(analyze_password(password="Heslo123?"))