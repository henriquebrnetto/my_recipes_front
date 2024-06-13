def validate_email(str):
    for var in ['@', '.com']:
        if var not in str:
            return False
    if len(str.replace('.com', '').split('@')) < 2 or str[:4] == '.com':
        return False
    for part in str.replace('.com', '').split('@'):
        if not part:
            return False
    return True