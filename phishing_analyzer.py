# ================================
# Phishing Awareness Analyzer
# DecodeLabs - Project 3
# SOC Analyst Track
# ================================

# Red flags database
RED_FLAGS = {
    "urgent_keywords": [
        "urgent", "immediate", "act now", "limited time",
        "account suspended", "verify now", "click here",
        "confirm your account", "unusual activity", "locked"
    ],
    "suspicious_domains": [
        "gmail.com", "yahoo.com", "hotmail.com",
        "outlook.com", "protonmail.com"
    ],
    "dangerous_attachments": [
        ".exe", ".js", ".bat", ".cmd", ".vbs",
        ".scr", ".zip", ".rar", ".html"
    ],
    "sensitive_requests": [
        "password", "credit card", "ssn", "social security",
        "bank account", "pin", "otp", "verification code",
        "login credentials", "username"
    ]
}

def analyze_email(sender, subject, body, attachments=""):
    red_flags = []
    score = 0

    # Check 1: Sender domain
    if any(domain in sender.lower() 
           for domain in RED_FLAGS["suspicious_domains"]):
        red_flags.append("🚨 Red Flag 1: Suspicious sender domain detected")
        score += 2

    # Check 2: Urgent keywords in subject
    if any(word in subject.lower() 
           for word in RED_FLAGS["urgent_keywords"]):
        red_flags.append("🚨 Red Flag 2: Urgency trigger in subject line")
        score += 2

    # Check 3: Urgent keywords in body
    urgent_found = [word for word in RED_FLAGS["urgent_keywords"] 
                   if word in body.lower()]
    if urgent_found:
        red_flags.append(f"🚨 Red Flag 3: Urgency keywords in body: {', '.join(urgent_found)}")
        score += 2

    # Check 4: Sensitive info requests
    sensitive_found = [word for word in RED_FLAGS["sensitive_requests"] 
                      if word in body.lower()]
    if sensitive_found:
        red_flags.append(f"🚨 Red Flag 4: Requests sensitive info: {', '.join(sensitive_found)}")
        score += 3

    # Check 5: Dangerous attachments
    if attachments:
        dangerous = [ext for ext in RED_FLAGS["dangerous_attachments"] 
                    if ext in attachments.lower()]
        if dangerous:
            red_flags.append(f"🚨 Red Flag 5: Dangerous attachment: {', '.join(dangerous)}")
            score += 3

    # Check 6: Suspicious links
    if "http://" in body.lower():
        red_flags.append("🚨 Red Flag 6: Unencrypted HTTP link detected")
        score += 2

    # Check 7: Domain spoofing patterns
    spoofing_patterns = ["amaz0n", "paypa1", "g00gle", 
                        "micros0ft", "app1e", "faceb00k"]
    if any(pattern in body.lower() for pattern in spoofing_patterns):
        red_flags.append("🚨 Red Flag 7: Domain spoofing pattern detected!")
        score += 4

    # Classify threat level
    if score == 0:
        verdict = "✅ SAFE"
        action = "Close — No threats detected"
    elif score <= 3:
        verdict = "⚠️ SUSPICIOUS"
        action = "Warn User — Proceed with caution"
    else:
        verdict = "🔴 MALICIOUS"
        action = "Block & Escalate — Report immediately!"

    return {
        "verdict": verdict,
        "action": action,
        "score": score,
        "red_flags": red_flags
    }

# Main Program
while True:
    print("\n")
    print("=" * 50)
    print("   🔵 DECODELABS PHISHING TRIAGE ANALYZER")
    print("         SOC Analyst Toolkit — Project 3")
    print("=" * 50)
    print("  1. Analyze a suspicious email")
    print("  2. Quit")
    print("=" * 50)

    choice = input("Choose option (1-2): ")

    if choice == "1":
        print("\n--- EMAIL DETAILS ---")
        sender = input("Sender email: ")
        subject = input("Subject line: ")
        body = input("Email body: ")
        attachments = input("Attachments (or press Enter to skip): ")

        result = analyze_email(sender, subject, body, attachments)

        print("\n" + "=" * 50)
        print("   📊 TRIAGE ANALYSIS REPORT")
        print("=" * 50)
        print(f"Threat Score : {result['score']}/16")
        print(f"Verdict      : {result['verdict']}")
        print(f"Action       : {result['action']}")
        print("-" * 50)

        if result["red_flags"]:
            print("RED FLAGS DETECTED:")
            for flag in result["red_flags"]:
                print(f"  {flag}")
        else:
            print("✅ No red flags detected!")

        print("=" * 50)

    elif choice == "2":
        print("\n🔵 Stay vigilant! Goodbye!")1
        break

    else:
        print("❌ Invalid option!")