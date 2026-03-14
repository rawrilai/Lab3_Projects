import access_control

print("CONTROL_NUM Used:", access_control.control_num())
print("FAVORITE_ARTIST Length:", len(access_control.FAVORITE_ARTIST))
print("Computed Access Level:", access_control.compute_access_level())
print("Threshold Applied:", access_control.control_num() * 5)
print(access_control.threshold_check())

import media_engine

CONTROL_NUM = 5
FAVORITE_ARTIST = "KESHI"
limit = CONTROL_NUM + len(FAVORITE_ARTIST)
print("Computed Stream Limit:", limit)

total, records = media_engine.run_stream(limit)
print("Total Plays:", total)
print("Number of Records Processed:", records)

calls = media_engine.signal_shutdown(limit)
print("Total Recursive Calls:", calls)