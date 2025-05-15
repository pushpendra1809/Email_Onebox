def store_email(email_data, label):
    print(f"Email stored in Elasticsearch with label: {label} (mocked)")

def search_emails(query):
    return [{"subject": "Demo", "body": "This is a test email with query: " + query}]
