# Password Complexity Checker

## Project Overview

The Password Complexity Checker is a Python-based application that analyzes the strength of a password by checking multiple security parameters. The application helps users create stronger passwords by identifying weak passwords and providing real-time feedback based on predefined complexity rules.

## Features

- Checks password length
- Detects uppercase letters
- Detects lowercase letters
- Detects numbers
- Detects special characters
- Calculates password strength
- Provides real-time feedback
- User-friendly interface

## Technologies Used

- Python
- Tkinter
- Regular Expressions (Regex)

## Password Strength Criteria

| Requirement | Status |
| --- | --- |
| Minimum 8 characters | ✓ |
| Uppercase letter | ✓ |
| Lowercase letter | ✓ |
| Number | ✓ |
| Special character | ✓ |

## Output

### Example 1: Weak Password

```text
Password: hello123

Strength: Weak

Suggestions:
- Add uppercase letters
- Add special characters
- Increase password length
```

### Example 2: Strong Password

```text
Password: Hello@123

Strength: Strong

All security requirements satisfied.
```


#### Weak Password Detection

![Weak Password](screenshots/weak_password.png)

#### Strong Password Detection

![Strong Password](screenshots/strong_password.png)

## How to Run the Project

```bash
git clone <repository-url>
cd Password-Complexity-Checker
python password_checker.py
```

## Future Improvements

- Password history checking
- Password generation feature
- Dark mode
- Advanced security analysis


