from flask import Flask, render_template, request
import re

app = Flask(__name__,template_folder='demo')

def parse_log(log_text):
    # Define regular expression patterns for parsing log entries
    log_entry_pattern = r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (?P<level>\w+): (?P<message>.*)'

    # List to store parsed log entries
    parsed_logs = []

    # Parse each log entry using regular expressions
    for line in log_text.split('\n'):
        match = re.match(log_entry_pattern, line)
        if match:
            parsed_logs.append({
                'timestamp': match.group('timestamp'),
                'level': match.group('level'),
                'message': match.group('message')
            })

    return parsed_logs

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/parse_log', methods=['POST'])
def parse_log_endpoint():
    log_text = request.form['log_text']
    parsed_logs = parse_log(log_text)
    return render_template('result.html', parsed_logs=parsed_logs)

if __name__ == '__main__':
    app.run(debug=True)