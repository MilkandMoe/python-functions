activities = ['Dancing', 'Swimming', 'Biking']
duration = [10, 20, 15]

def calories_burned(activities, duration):
    total_calories_burned = (duration * 3)
    return total_calories_burned



calories = calories_burned(activities, duration)
print(f"Calories burned during {activities} for sometime {duration}")