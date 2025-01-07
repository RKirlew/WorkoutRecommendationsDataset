import pandas as pd
import random

#Define possible values for features
fitness_levels = ['Beginner', 'Intermediate', 'Advanced']
goals = ['Weight Loss', 'Muscle Gain', 'Endurance', 'Flexibility']
workout_types = ['Cardio', 'Strength', 'Flexibility']

workout_recommendations = {
    'Cardio': ['Treadmill', 'Cycling', 'Jogging', 'Rowing', 'Swimming', 'HIIT', 'Jump Rope', 'Stair Climbing'],
    'Strength': ['Squats', 'Deadlifts', 'Push-ups', 'Bench Press', 'Pull-ups', 'Dumbbell Rows', 'Overhead Press', 'Bicep Curls', 'Plank Holds'],
    'Flexibility': ['Yoga', 'Pilates', 'Stretching', 'Tai Chi', 'Foam Rolling', 'Barre Workouts', 'Dynamic Stretches', 'Mobility Drills']
}

#Function to generate the synthetic data
def generate_data(num_entries=200):
    data = []
    for _ in range(num_entries):
        age = random.randint(18, 60)
        fitness_level = random.choice(fitness_levels)
        goal = random.choice(goals)
        workout_type = random.choice(workout_types)
        recommended_workouts = random.sample(workout_recommendations[workout_type], 3)  # Pick 3 workouts
        data.append([age, fitness_level, goal, workout_type, ", ".join(recommended_workouts)])

    # Return as DataFrame
    return pd.DataFrame(data, columns=['Age', 'Fitness Level', 'Goal', 'Workout Type', 'Recommended Workouts'])

#Generate and save to CSV
df = generate_data(num_entries=500)  # Generate 500 new entries
df.to_csv('generated_workout_data.csv', index=False)
print("New dataset generated and saved as 'generated_workout_data.csv'")
