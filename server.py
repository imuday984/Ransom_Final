from flask import Flask, request, render_template_string, jsonify
import json
import datetime

app = Flask(__name__)

# This list acts as our temporary database
audit_logs = []

# HTML Template for the Dashboard (Dark Mode, Hacker Style)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>🛡️ Ransom-Sentry Dashboard</title>
    <meta http-equiv="refresh" content="2"> <!-- Auto-refresh every 2 seconds -->
    <style>
        body { font-family: 'Consolas', monospace; background: #0d1117; color: #c9d1d9; padding: 20px; }
        h1 { border-bottom: 2px solid #30363d; padding-bottom: 10px; color: #58a6ff; }
        .log-container { background: #161b22; border: 1px solid #30363d; padding: 10px; border-radius: 6px; }
        .log-entry { padding: 8px; border-bottom: 1px solid #21262d; display: flex; justify-content: space-between; }
        .INFO { color: #79c0ff; }
        .WARNING { color: #d29922; }
        .CRITICAL { color: #ff7b72; font-weight: bold; }
        .SAFE { color: #3fb950; }
        .timestamp { color: #8b949e; font-size: 0.9em; }
    </style>
</head>
<body>
    <h1>🛡️ Breach & Attack Simulation: Live Feed</h1>
    <div class="log-container">
        {% for log in logs %}
            <div class="log-entry">
                <span>
                    <strong class="{{ log.status }}">[{{ log.status }}]</strong> 
                    {{ log.message }}
                </span>
                <span class="timestamp">{{ log.time }}</span>
            </div>
        {% endfor %}
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    # Show logs, newest first
    return render_template_string(HTML_TEMPLATE, logs=reversed(audit_logs))

@app.route('/report', methods=['POST'])
def report():
    # This is the endpoint the Agent talks to
    data = request.json
    # Add server-side timestamp
    data['time'] = datetime.datetime.now().strftime("%H:%M:%S")
    audit_logs.append(data)
    print(f"[{data['status']}] {data['message']}") # Also print to terminal
    return jsonify({"status": "received"})

if __name__ == '__main__':
    # Run on all interfaces so other PCs can connect if needed
    app.run(host='0.0.0.0', port=5000, debug=True)