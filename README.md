# 🛡️ Phishing Awareness Analyzer

> A real-time phishing triage web application that analyzes suspicious emails and classifies them as Safe, Suspicious, or Malicious using 7 red flag detection algorithms.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-black?style=flat-square&logo=flask)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Skill](https://img.shields.io/badge/Skill-Cybersecurity-red)
![Kali](https://img.shields.io/badge/Kali_Linux-v2026.1-purple)
![Skill](https://img.shields.io/badge/Penetration_Testing-Skill-red)
![GitHub](https://img.shields.io/badge/GitHub-Official--Samuel--Ntuen-black?logo=github)
![Ethical](https://img.shields.io/badge/Ethical_Hacking-darkgreen)
![Waqas](https://img.shields.io/badge/-Samuel_M._Ntuen-red)
---

## 🎯 About The Project

This project was built as part of my **Cybersecurity Internship at DecodeLabs (Batch 2026)**.

Project 3 focuses on building the **Human Firewall** — the most critical layer of cybersecurity defense. According to the Verizon DBIR, 80% of security breaches involve phishing and it only takes 82 seconds for an attacker to get their first click.

> *\"The modern cybersecurity perimeter is no longer the network firewall. It is the user.\"* — DecodeLabs

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| 🔍 Real-time Triage | Analyze emails instantly for phishing indicators |
| 🚨 7 Red Flag Detectors | Domain, urgency, sensitive info, attachments and more |
| 📊 Threat Scoring | CVSS-based scoring system (0-16) |
| 🟢 Safe Detection | Identifies clean legitimate emails |
| 🟡 Suspicious Classification | Warns about potentially dangerous emails |
| 🔴 Malicious Classification | Blocks and escalates confirmed phishing attempts |
| 💡 SOC Dashboard | Professional blue SOC analyst interface |

---

## 🚩 Red Flags Detected

| # | Red Flag | Risk Level |
|---|----------|------------|
| RF1 | Suspicious Sender Domain | HIGH |
| RF2 | Urgency Triggers in Subject | HIGH |
| RF3 | Urgency Keywords in Body | HIGH |
| RF4 | Sensitive Information Requests | CRITICAL |
| RF5 | Dangerous Attachments (.exe, .js, .bat) | CRITICAL |
| RF6 | Unencrypted HTTP Links | MEDIUM |
| RF7 | Domain Spoofing Patterns | CRITICAL |

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3, JavaScript
- **Security Logic:** Pattern matching, keyword analysis, domain validation
- **Theme:** Blue SOC Analyst Dashboard

---

## 📁 Project Structure

Phishing-Analyzer/
│
├── app.py # Flask backend & detection logic
├── phishing_analyzer.py # Terminal version
│
├── templates/
│ └── index.html # SOC dashboard HTML
│
├── static/
│ ├── css/
│ │ └── style.css # Blue SOC analyst styling
│ └── js/
│ └── script.js # Real-time analysis logic
│
└── README.md


---

## ▶️ How To Run

```bash
git clone https://github.com/Official-Samuel-Ntuen/Phishing-Analyzer.git
cd Phishing-Analyzer
pip3 install flask
python3 app.py
```

Then open your browser and go to:

http://127.0.0.1:5000


---

## 🧪 Test Cases

**Test 1 — Malicious Email:**
- Sender: security@gmail.com
- Subject: URGENT: Your account has been suspended
- Body: Click here to verify your password immediately
- Attachment: invoice.exe
- Expected: 🔴 MALICIOUS

**Test 2 — Safe Email:**
- Sender: colleague@company.com
- Subject: Team meeting tomorrow
- Body: Hi, just a reminder about our meeting at 10am
- Expected: ✅ SAFE

---

## 🧠 What I Learned

- Phishing attack anatomy and detection techniques
- Social engineering tactics and cognitive triggers
- Pattern matching and keyword analysis in Python
- SOC analyst triage workflows
- CVSS scoring methodology
- Flask REST API development
- Real-world threat classification systems

---

## 🔐 Security Concepts Covered

- **Phishing Types** — Mass phishing, Spear phishing, Whaling
- **Domain Spoofing** — Typosquatting, Homoglyph attacks
- **Social Engineering** — Authority, Urgency, Fear/Greed triggers
- **The Golden Rule** — Pause, Verify, Report

---

## 👨‍💻 Author

**Samuel Ntuen**
Junior Cybersecurity Analyst | DecodeLabs Intern 2026

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin)](https://linkedin.com/in/yourprofile)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat-square&logo=github)](https://github.com/Official-Samuel-Ntuen)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> *\"Technical firewalls cannot compensate for human error.\"* — DecodeLabs
'''
with open('README.md', 'w') as f:
    f.write(content)
print('README created!')
"
