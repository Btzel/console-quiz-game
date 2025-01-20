# Console Quiz Game

A Python-based console quiz application featuring various categories and difficulty levels with an OOP approach.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Console](https://img.shields.io/badge/Console-Application-green)
![OOP](https://img.shields.io/badge/OOP-Principles-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🎯 Overview

This project implements a console-based quiz game that:
1. Offers questions from multiple categories
2. Features different difficulty levels
3. Tracks player scores
4. Provides immediate feedback

## 🎮 Quiz Features

### Categories
- Video Games
- History
- Geography
- Science
- Entertainment
- Sports
- And more...

### Difficulty Levels
- Easy
- Medium
- Hard

## 🔧 Technical Components

### Question Model
```python
class Question:
    def __init__(self, category, difficulty, text, answer):
        self.category = category
        self.difficulty = difficulty
        self.text = text
        self.answer = answer
```

### Quiz Brain
- Score tracking
- Question management
- Answer validation
- Progress monitoring

### Data Management
- Question bank creation
- Category organization
- Answer verification
- Score calculation

## 💻 Implementation Details

### Core Classes

#### QuizBrain
```python
class QuizBrain:
    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list
```

### Key Features
1. **Question Processing**
   - Category-based organization
   - Difficulty level sorting
   - Answer validation

2. **Score System**
   - Real-time score tracking
   - Progress monitoring
   - Final score calculation

## 🚀 Usage

1. Run the program:
```bash
python main.py
```

2. Answer questions when prompted:
```
The next question is from 'Geography', the difficulty is 'Easy'.
Q.1: Ottawa is the capital of Canada (True/False)?: 
```

3. View your progress:
```
You got it right!
Your current score is: 1/1
```

## 📊 Sample Output

```
Q.10: Tokyo is the capital of Japan (True/False)?: True
You got it right!
Your current score is: 7/10

The quiz is completed.
Your final score is: 7/10
```

## 🛠️ Project Structure

```
quiz_game/
├── main.py             # Main application entry
├── question_model.py   # Question class definition
├── quiz_brain.py       # Quiz logic implementation
└── data.py            # Question database
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Author

Burak TÜZEL