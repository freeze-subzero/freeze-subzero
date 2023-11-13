from datetime import datetime

month = datetime.now().month
day = datetime.now().day
year = datetime.now().year
calculation = round(((((month-1)*30.416666667) + day)/365)* 100)

progress_bar = []

for i in range(1,21):
    percentage = i * 5
    if percentage <= calculation:
        progress_bar.append("🟩")
    if percentage > calculation:
        progress_bar.append("⬜")

print(f"{year} is {calculation}% complete!{''.join(progress_bar)}")