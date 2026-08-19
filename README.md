# Password Complexity Checker

## Project Overview

Password Complexity Checker is a Python-based cybersecurity project designed to evaluate the strength and security level of a password.

The application analyzes the entered password based on multiple security criteria such as password length, uppercase letters, lowercase letters, numbers, and special characters. Based on these conditions, it determines whether the password is Weak, Medium, or Strong.

This project helps users understand the importance of creating strong passwords and following basic password security practices.

## Objectives

- To check the complexity of a password.
- To identify weak and easily guessable passwords.
- To encourage users to create stronger passwords.
- To demonstrate basic cybersecurity and password security concepts.
- To provide quick feedback about password strength.

## Features

- Checks minimum password length.
- Detects uppercase letters.
- Detects lowercase letters.
- Checks for numeric characters.
- Checks for special characters.
- Evaluates overall password strength.
- Displays the result in an easy-to-understand format.
- Simple and beginner-friendly implementation.

## Password Strength Criteria

The password is evaluated using the following criteria:

| Criteria | Description |
|---|---|
| Length | Checks whether the password has sufficient characters |
| Uppercase | Checks for uppercase letters (A-Z) |
| Lowercase | Checks for lowercase letters (a-z) |
| Numbers | Checks for numeric characters (0-9) |
| Special Characters | Checks for symbols such as @, #, $, %, etc. |

## Strength Levels

- **Weak** – Password does not satisfy enough security requirements.
- **Medium** – Password satisfies some security requirements but can be improved.
- **Strong** – Password satisfies most or all security requirements.

## Technologies Used

- Python
- Regular Expressions (`re` module)

## How It Works

1. The user enters a password.
2. The program analyzes the password.
3. It checks the password against different complexity criteria.
4. Each satisfied criterion contributes to the overall strength.
5. The program displays the final password strength.

## Example

**Input:**

`Hello@123`

**Output:**

`Password Strength: Strong`

## Output

![Password Complexity Checker Output](output.png)

## Applications

- Basic password security assessment.
- Cybersecurity learning projects.
- User awareness about password security.
- Beginner Python and cybersecurity demonstrations.

## Future Improvements

- Add a graphical user interface (GUI).
- Add a password generator.
- Provide detailed suggestions for improving weak passwords.
- Add a password strength meter.
- Include additional security checks.

## Conclusion

The Password Complexity Checker is a simple cybersecurity project that demonstrates how password complexity can be evaluated using Python. It helps users understand the characteristics of a strong password while providing practical implementation of basic security concepts.