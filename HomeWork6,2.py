user_num = int(input("Введіть число від 0 до 8640000: "))

days, remainder = divmod(user_num, 86400)
hours, remainder = divmod(remainder, 3600)
minutes, sec = divmod(remainder, 60)

if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif days % 10 in (2, 3, 4) and not (12 <= days % 100 <= 14):
    day_word = "дні"
else:
    day_word = "днів"

print(f" {days} {day_word}, {hours:02}:{minutes:02}:{sec:02}")
