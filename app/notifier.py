import requests

def notify_interested(email_data):
    webhook_url = "https://webhook.site/YOUR_ID"
    slack_url = "https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK"
    
    payload = {
        "text": f"New Interested Email from {email_data['sender']}: {email_data['subject']}"
    }
    
    print("Notifying Slack and Webhook... (mocked)")
    # requests.post(slack_url, json=payload)
    # requests.post(webhook_url, json=email_data)
