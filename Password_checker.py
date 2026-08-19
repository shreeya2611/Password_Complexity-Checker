import re


def check_password(password):
    score = 0
    feedback = []

    # Length
    if len(password) >= 12:
        score += 25
    elif len(password) >= 8:
        score += 15
        feedback.append("Use at least 12 characters.")
    else:
        feedback.append("Password should be at least 8 characters.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 15
    else:
        feedback.append("Add an uppercase letter.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 15
    else:
        feedback.append("Add a lowercase letter.")

    # Number
    if re.search(r"\d", password):
        score += 15
    else:
        feedback.append("Add a number.")

    # Special character
    if re.search(r"[^A-Za-z0-9]", password):
        score += 20
    else:
        feedback.append("Add a special character.")

    # Strength
    if score >= 80:
        strength = "VERY STRONG"
    elif score >= 60:
        strength = "STRONG"
    elif score >= 40:
        strength = "MEDIUM"
    else:
        strength = "WEAK"

    return score, strength, feedback


# Terminal interface
print("=" * 60)
print("          PASSWORD COMPLEXITY CHECKER")
print("=" * 60)

password = input("\nEnter your password: ")

score, strength, feedback = check_password(password)

print("\nPASSWORD SECURITY REPORT")
print("-" * 60)

print(f"Password Length     : {len(password)} characters")
print(f"Security Score      : {score}/100")
print(f"Password Strength   : {strength}")

print("-" * 60)

if feedback:
    print("\nSECURITY RECOMMENDATIONS:")

    for item in feedback:
        print(f"[!] {item}")
else:
    print("\n[+] Excellent!")
    print("[+] Password satisfies all complexity requirements.")

print("=" * 60)