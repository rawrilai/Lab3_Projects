CONTROL_NUM = 5
FAVORITE_ARTIST = "KESHI"

def signal_shutdown(power):
    if power == 0:
        return 1
    return 1 + signal_shutdown(power - 1)

def play_count_stream(limit):
    for i in range(limit):
        if i % 2 == 0:
            yield i ** 2

def monitor(func):
    def wrapper(limit):
        print("Processing Started")
        result = func(limit)
        print("Processing Completed")
        return result
    return wrapper

@monitor
def run_stream(limit):

    total = 0
    count = 0

    for value in play_count_stream(limit):
        print("Play Count:", value)
        total += value
        count += 1

    return total, count