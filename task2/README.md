# Password Generator (Web Application)

This project is a web-based Password Generator developed using Python and Flask as part of my internship work.  
The application allows users to generate secure passwords by selecting the desired password length and character options through a clean and interactive user interface.

## Features
- User-defined password length
- Option to include:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Symbols
- Guaranteed inclusion of selected character types
- 🔄 Regenerate password using the same selected settings
- ⧉ One-click copy password to clipboard
- Clean and modern user interface

## Project Structure
task2/
- main.py  
- templates/  
  - index.html  
- static/  
  - style.css  
- README.md  

## How to Run
1. Ensure Python 3.x is installed on your system
2. Open a terminal or command prompt
3. Navigate to the project directory
4. Install Flask:
   pip install flask
5. Run the following command:
   python main.py
6. Open a browser and visit:
   http://127.0.0.1:5000/

## Working
- The user enters the desired password length
- The user selects character options (uppercase, lowercase, numbers, symbols)
- Clicking **Generate Password** creates a secure password
- Clicking **🔄 Regenerate** generates a new password using the same options
- Clicking **⧉ Copy** copies the password to the clipboard

## Technologies Used
- Python
- Flask
- HTML
- CSS
- JavaScript

## Learning Outcome
This project helped me improve my understanding of Flask framework, backend and frontend integration, secure password generation logic, and UI/UX design principles. It also enhanced my skills in building interactive web applications using Python.

## Conclusion
The Password Generator is a practical and user-friendly web application that demonstrates core Python and Flask concepts. It can be further enhanced with additional features such as a password strength indicator or deployment on a cloud platform.
