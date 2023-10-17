from datetime import datetime

# first_name = "joseph"
# last_name = "joestar"
# full_name = f"{first_name} {last_name}"
# print(full_name)

today = datetime.now()
date_time = today.strftime("%Y-%m-%d %H:%M:%S")
print(date_time)