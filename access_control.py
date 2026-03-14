SEED_NUM = 5
FAVORITE_ARTIST = "KESHI"

def control_num():
    CONTROL_NUM = max(1, SEED_NUM)
    return CONTROL_NUM

def compute_access_level():
    CONTROL_NUM = control_num()
    ACCESS_LEVEL = CONTROL_NUM * 3 + len(FAVORITE_ARTIST)
    return ACCESS_LEVEL

def audit_log(func):
    def wrapper():
        print("Authorization Started.")
        result = func()
        print("Authorization Completed.")
        return result
    return wrapper

@audit_log
def threshold_check():
    CONTROL_NUM = control_num()
    ACCESS_LEVEL = compute_access_level()
    THRESHOLD = CONTROL_NUM * 5
    if ACCESS_LEVEL < THRESHOLD:
        return "ACCESS GRANTED"
    else:
        return "ACCESS DENIED"