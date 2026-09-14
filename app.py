# ================================
# Phishing Awareness Analyzer
# DecodeLabs - Project 3
# Flask Web Application
# ================================

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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

    if any(domain in sender.lower()
           for domain in RED_FLAGS["suspicious_domains"]):
        red_flags.append("Suspicious sender domain detected")
        score += 2

    if any(word in subject.lower()
           for word in RED_FLAGS["urgent_keywords"]):
        red_flags.append("Urgency trigger in subject line")
        score += 2

    urgent_found = [word for word in RED_FLAGS["urgent_keywords"]
                   if word in body.lower()]
    if urgent_found:
        red_flags.append(f"Urgency keywords in body: {', '.join(urgent_found)}")
        score += 2

    sensitive_found = [word for word in RED_FLAGS["sensitive_requests"]
                      if word in body.lower()]
    if sensitive_found:
        red_flags.append(f"Requests sensitive info: {', '.join(sensitive_found)}")
        score += 3

    if attachments:
        dangerous = [ext for ext in RED_FLAGS["dangerous_attachments"]
                    if ext in attachments.lower()]
        if dangerous:
            red_flags.append(f"Dangerous attachment detected: {', '.join(dangerous)}")
            score += 3

    if "http://" in body.lower():
        red_flags.append("Unencrypted HTTP link detected")
        score += 2

    spoofing_patterns = ["amaz0n", "paypa1", "g00gle",
                        "micros0ft", "app1e", "faceb00k"]
    if any(pattern in body.lower() for pattern in spoofing_patterns):
        red_flags.append("Domain spoofing pattern detected!")
        score += 4

    if score == 0:
        verdict = "SAFE"
        action = "Close — No threats detected"
    elif score <= 3:
        verdict = "SUSPICIOUS"
        action = "Warn User — Proceed with caution"
    else:
        verdict = "MALICIOUS"
        action = "Block & Escalate — Report immediately!"

    return {
        "verdict": verdict,
        "action": action,
        "score": score,
        "max_score": 16,
        "red_flags": red_flags
    }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    sender = data.get('sender', '')
    subject = data.get('subject', '')
    body = data.get('body', '')
    attachments = data.get('attachments', '')
    result = analyze_email(sender, subject, body, attachments)
    return jsonify(result)

if __name__ == '__main__':
    import webbrowser
    webbrowser.open('http://127.0.0.1:5000')
    app.run(debug=True)