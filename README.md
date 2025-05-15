# Email Onebox Backend

## Features
- Real-time IMAP sync (mocked)
- Email storage & search via Elasticsearch (mocked)
- AI-based email categorization
- Slack and Webhook integration for "Interested" leads

## Setup
```bash
docker-compose up --build
```

## API Endpoints

### Store & Categorize Email
```http
POST /email
Body: {
  "subject": "...",
  "sender": "...",
  "body": "...",
  "folder": "...",
  "account": "..."
}
```

### Search Emails
```http
GET /emails/search?q=term
```
