def check_password_strength(password, username, min_length, require_uppercase, require_numbers, require_special):
    result = {
        "length_ok": False,
        "no_username_ok": False,
        "uppercase_ok": False,
        "numbers_ok": False,
        "special_ok": False,
        "overall_valid": False,
        "strength": "weak"
    }
    
    if len(password) >= min_length:
        result["length_ok"] = True
    
    if username.lower() not in password.lower():
        result["no_username_ok"] = True
    
    if require_uppercase:
        if any(c.isupper() for c in password):
            result["uppercase_ok"] = True
    else:
        result["uppercase_ok"] = True
    
    if require_numbers:
        if any(c.isdigit() for c in password):
            result["numbers_ok"] = True
    else:
        result["numbers_ok"] = False
    
    special_chars = "!@#$%^&*"
    if require_special:
        if any(c in special_chars for c in password):
            result["special_ok"] = True
    else:
        result["special_ok"] = True
    
    if result["length_ok"] and result["no_username_ok"] and result["uppercase_ok"] and result["numbers_ok"] and result["special_ok"]:
        result["overall_valid"] = True
    
    criteria_met = sum([result["length_ok"], result["uppercase_ok"], result["numbers_ok"], result["special_ok"]])
    if criteria_met >= 4:
        result["strength"] = "strong"
    elif criteria_met >= 2:
        result["strength"] = "medium"
    
    return result