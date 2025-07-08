# Install required packages
!pip install requests beautifulsoup4 pandas

# Imports
import requests
from bs4 import BeautifulSoup
import random
from datetime import datetime

# Scrape text content from a real estate blog or forum
def scrape_conversation(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    for tag in soup(["script", "style", "img", "noscript", "input"]):
        tag.decompose()

    title = soup.title.string.strip() if soup.title else "Untitled"
    text = soup.get_text(separator="\n", strip=True)
    lines = [line for line in text.split("\n") if 60 < len(line.strip()) < 400]

    return title, random.sample(lines, min(8, len(lines)))

# Generate human-like funding email based on scraped discussion
def create_funding_email(name, insights):
    date_str = datetime.now().strftime("%B %d, %Y")

    real_world_intro = [
        "I was just reading a thread this morning about a guy losing a deal because funding fell through at closing.",
        "One investor mentioned needing 3-day closes because sellers are getting anxious about fallouts.",
        "People are talking about title delays, end buyers ghosting, and capital partners disappearing mid-deal.",
        "Creative deals are getting more competitive—double closes, novations, and hybrids are everywhere now.",
    ]

    value_props = [
        "I specialize in transactional lending and quick bridge funding for flippers, wholesalers, and novation deals.",
        "We close fast. ARV-based, no income docs, and built for active investors doing volume.",
        "This is designed for people moving fast — not W2 borrowers, but real players who need flexibility and certainty.",
    ]

    call_to_actions = [
        "Shoot me a text with the address, and I’ll get you a number in 10 minutes.",
        "I’ve got 2 more slots to fund this week — if you’ve got a deal in motion, let’s lock it in.",
        "Reply back 'Ready' and I’ll reach out with terms by end of day.",
    ]

    insight_line = random.choice(insights) if insights else "Investors are increasingly relying on private capital as traditional lenders slow down."

    email = (
        f"Subject: Fast capital for real deals – {date_str}\n\n"
        f"Hey {name},\n\n"
        f"{random.choice(real_world_intro)}\n\n"
        f"Here’s something I just saw:\n"
        f"\"{insight_line.strip()}\"\n\n"
        f"{random.choice(value_props)}\n\n"
        f"{random.choice(call_to_actions)}\n\n"
        f"- Carlos Ramirez\n"
        f"Private Lending Partner\n"
        f"(Insert phone/email/website)"
    )

    return email

# Example live conversation URLs (you can rotate these daily)
urls = [
    "https://www.biggerpockets.com/blog/how-to-fund-real-estate-deals",
    "https://www.reddit.com/r/realestateinvesting/comments/1cyh4ld/hard_money_lenders_are_becoming_a_red_flag/"
]

# Loop through URLs, scrape content, generate and print professional emails
for url in urls:
    try:
        title, insights = scrape_conversation(url)
        print(f"\nScraped from: {title}\n")

        for i in range(2):  # Create 2 emails per source
            email = create_funding_email("Alex", insights)
            print(f"\n--- EMAIL {i+1} ---\n{email}\n")

    except Exception as e:
        print(f"Error processing {url}: {e}")
