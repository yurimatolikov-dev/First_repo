def add_habit(data, habit_name):
    if "habits" not in data:
        data["habits"] = {}
    if habit_name in data["habits"]:
        print(f"Привычка \"{habit_name}\" уже существует.")
        return
    data["habits"][habit_name] = {"streak": 0, "last_done": None}
    print(f"Привычка \"{habit_name}\" добавлена.")

def mark_done(data, habit_name):
    from datetime import date
    today = date.today().isoformat()

    habit = data.get("habits", {}).get(habit_name)
    if not habit:
        print(f"Привычка \"{habit_name}\" не найдена.")
        return
    
    if habit["last_done"] != today:
        habit["streak"] += 1
        habit["last_done"] = today
        print(f"Привычка \"{habit_name}\" отмечена как выполненная сегодня. Текущая серия: {habit['streak']}.")
    else: 
        print(f"Привычка \"{habit_name}\" уже была выполнена сегодня.")
    
def show_stats(data):
    for name, habit in data.get("habits", {}).items():
        print(f"{name} - {habit['streak']} дней подряд, последний раз выполнена: {habit['last_done']}")
    