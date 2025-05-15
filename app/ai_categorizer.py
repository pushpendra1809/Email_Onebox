def categorize_email(text):
    if "meeting" in text.lower():
        return "Meeting Booked"
    elif "interested" in text.lower():
        return "Interested"
    elif "spam" in text.lower():
        return "Spam"
    elif "out of office" in text.lower():
        return "Out of Office"
    return "Not Interested"
