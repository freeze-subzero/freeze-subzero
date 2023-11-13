from datetime import datetime
from pathlib import Path

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
        progress_bar.append("⬛")

print(f"{year} is {calculation}% complete! {''.join(progress_bar)}")


with open('README.md', 'w') as file:
    file.write(f"# Hello there! 👋\n\n⌨️ I'm currently learning Python, HTML, CSS and Javascript.\n\n## Year progress bar\n\n📅 {year} is {calculation}% complete!\n\n{''.join(progress_bar)}")