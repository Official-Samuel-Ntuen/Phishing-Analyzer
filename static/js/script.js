// ================================
// DecodeLabs - Phishing Analyzer
// Blue SOC Analyst Theme
// ================================

async function analyzeEmail() {
    const sender = document.getElementById('sender').value;
    const subject = document.getElementById('subject').value;
    const body = document.getElementById('body').value;
    const attachments = document.getElementById('attachments').value;

    // Validate input
    if (!sender && !subject && !body) {
        showError('ERROR: Please fill in at least sender, subject and body!');
        return;
    }

    // Show loading state
    const btn = document.querySelector('.btn-analyze');
    btn.textContent = '🔍 ANALYZING...';
    btn.disabled = true;

    try {
        const response = await fetch('/analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ sender, subject, body, attachments })
        });

        const data = await response.json();
        displayResults(data);

    } catch (error) {
        showError('ERROR: Analysis failed. Check server connection!');
    }

    // Reset button
    btn.textContent = '🔍 RUN TRIAGE ANALYSIS';
    btn.disabled = false;
}

function displayResults(data) {
    const verdictDisplay = document.getElementById('verdictDisplay');
    const verdictIcon = document.getElementById('verdictIcon');
    const verdictText = document.getElementById('verdictText');
    const verdictAction = document.getElementById('verdictAction');
    const scoreBar = document.getElementById('scoreBar');
    const scoreText = document.getElementById('scoreText');
    const flagsList = document.getElementById('flagsList');

    // Reset verdict classes
    verdictDisplay.className = 'verdict-display';

    // Update verdict
    if (data.verdict === 'SAFE') {
        verdictDisplay.classList.add('verdict-safe');
        verdictIcon.textContent = '✅';
        scoreBar.style.background = '#00ff88';

    } else if (data.verdict === 'SUSPICIOUS') {
        verdictDisplay.classList.add('verdict-suspicious');
        verdictIcon.textContent = '⚠️';
        scoreBar.style.background = '#ffaa00';

    } else {
        verdictDisplay.classList.add('verdict-malicious');
        verdictIcon.textContent = '🚨';
        scoreBar.style.background = 
            'linear-gradient(90deg, #ff3333, #ff0000)';
    }

    verdictText.textContent = data.verdict;
    verdictAction.textContent = data.action;

    // Update score bar
    const percentage = (data.score / data.max_score) * 100;
    scoreBar.style.width = percentage + '%';
    scoreText.textContent = data.score;

    // Update red flags
    flagsList.innerHTML = '';

    if (data.red_flags.length === 0) {
        flagsList.innerHTML = 
            '<p class="no-flags">✅ No red flags detected!</p>';
    } else {
        data.red_flags.forEach((flag, index) => {
            const div = document.createElement('div');
            div.className = 'flag-item';
            div.innerHTML = `
                <span class="flag-number">RF${index + 1}</span>
                <span>${flag}</span>
            `;
            flagsList.appendChild(div);
        });
    }
}

function showError(message) {
    const flagsList = document.getElementById('flagsList');
    flagsList.innerHTML = `
        <div class="flag-item">
            <span class="flag-number">ERR</span>
            <span>${message}</span>
        </div>
    `;
}

function clearAll() {
    document.getElementById('sender').value = '';
    document.getElementById('subject').value = '';
    document.getElementById('body').value = '';
    document.getElementById('attachments').value = '';

    // Reset verdict display
    document.getElementById('verdictDisplay').className = 'verdict-display';
    document.getElementById('verdictIcon').textContent = '🛡️';
    document.getElementById('verdictText').textContent = 'AWAITING ANALYSIS';
    document.getElementById('verdictAction').textContent = 
        'Submit an email to begin triage';
    document.getElementById('scoreBar').style.width = '0%';
    document.getElementById('scoreText').textContent = '0';
    document.getElementById('flagsList').innerHTML = 
        '<p class="no-flags">No analysis run yet</p>';
}

// Allow Enter key to trigger analysis
document.addEventListener('keydown', (e) => {
    if (e.ctrlKey && e.key === 'Enter') {
        analyzeEmail();
    }
});
