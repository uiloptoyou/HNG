from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)


def get_current_day():
    current_datetime = datetime.datetime.now()
    day_name = current_datetime.strftime("%A")

    return day_name


def get_utc_time():
    current_utc_time = datetime.datetime.utcnow()
    formatted_utc_time = current_utc_time.strftime("%Y-%m-%dT%H:%M:%SZ")

    return formatted_utc_time


@app.route('/')
def api():
    data = {
        "current_day": get_current_day(),
        "utc_time": get_utc_time(),
        "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
        "github_repo_url": "https://github.com/TolulopeJoel/HNG",
        "status_code": 200,
    }

    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    if slack_name:
        data['slack_name'] = slack_name

    if track:
        data['track'] = track

    return jsonify(data), 200


if __name__ == '__main__':
    app.run(debug=True)
