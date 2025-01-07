# Workout Recommendations Dataset
This repository contains a synthetic dataset designed for building personalized workout recommendation models. The data is generated for educational and experimental purposes, allowing users to practice machine learning techniques such as classification, k-NN, and clustering, as well as explore fitness-related data analysis.
![image](https://github.com/user-attachments/assets/770cac1f-1adc-438d-8588-2f69601351f3)

Overview

The dataset contains user profiles with features such as age, fitness level, goal, workout type, and recommended workouts. It was created to mimic real-world data in the context of personalized fitness plans.
Features

    Age: Age of the user (integer from 18 to 60).
    Fitness Level: A categorical variable indicating the user's fitness level:
        Beginner
        Intermediate
        Advanced
    Goal: The user's fitness goal, one of:
        Weight Loss
        Muscle Gain
        Endurance
        Flexibility
    Workout Type: The type of workout the user prefers, one of:
        Cardio
        Strength
        Flexibility
    Recommended Workouts: A comma-separated list of recommended workouts (three workouts selected based on the user's goal and workout type).

Workout Categories

    Cardio: Treadmill, Cycling, Jogging, Rowing, Swimming, HIIT, Jump Rope, Stair Climbing
    Strength: Squats, Deadlifts, Push-ups, Bench Press, Pull-ups, Dumbbell Rows, Overhead Press, Bicep Curls, Plank Holds
    Flexibility: Yoga, Pilates, Stretching, Tai Chi, Foam Rolling, Barre Workouts, Dynamic Stretches, Mobility Drills
How to Use This Dataset

   1) Download the dataset: You can download the expanded_workout_data.csv file from the repository.
   2) Import into your project: Use your preferred data analysis tools (e.g., Pandas, Numpy, etc.) to load the dataset into your project.
   3) Preprocessing: Clean the dataset (if necessary), handle categorical data, and normalize numerical features.
   4) Model Training: Use this dataset to train machine learning models (e.g., k-NN, Decision Trees) to recommend workouts or classify fitness goals.
