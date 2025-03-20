# Growth Mindset Challenge Web App

## Overview
The **Growth Mindset Challenge Web App** is a simple web application built using Streamlit. It provides users with daily challenges, motivational quotes, and a space to reflect on their growth journey.

## Features
- **Daily Challenge:** Receive a new challenge every day to improve your mindset.
- **User Reflection:** Write and submit thoughts on the challenge.
- **Motivational Quotes:** Get inspired by random quotes.
- **Enhanced UI:** Uses icons for a better visual experience.

## Project Structure
```
📂 growth_mindset_app
│── 📄 growth_mindset_app.py  # Main Streamlit application script
│── 📄 README.md              # Project documentation
│── 📄 requirements.txt       # Dependencies list
```

## Installation & Setup

### Prerequisites
Ensure you have **Python 3.7+** installed.

### Step 1: Install Dependencies
```sh
pip install streamlit streamlit-extras
```

### Step 2: Create and Save the Script
1. Open **VS Code**.
2. Create a new file `growth_mindset_app.py`.
3. Copy and paste the provided code.
4. Save the file.

### Step 3: Run the Application
```sh
streamlit run growth_mindset_app.py
```
This will open the web app in your browser.

## How It Works
1. **Daily Challenge:** Fetches a challenge based on the current date.
2. **User Reflection:** Allows users to input and submit responses.
3. **Motivational Quotes:** Displays random quotes for encouragement.
4. **Icons:** UI elements are enhanced using icons.

## Troubleshooting
- **Streamlit not found?** Run `pip install streamlit`.
- **App not opening?** Check if another process is using the same port.
- **Icons not showing?** Ensure an active internet connection.

## Future Improvements
- User authentication for personalized challenges.
- Store reflections in a database.
- AI-based feedback on user inputs.

## Credits
Made with **Muhammad Hasnain**.