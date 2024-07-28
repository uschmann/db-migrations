from datetime import datetime

now = datetime.now()
formatted = now.strftime("%Y_%m_%d_%H%M%S")
print(formatted)