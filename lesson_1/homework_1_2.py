time = int(input("time in seconds: "))
hours = time // 3600
minutes = (time // 60) - (hours * 60)
sec = time % 60
print(f'{hours:00}: {minutes:00}: {sec:00}')