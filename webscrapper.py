import streamlit as st
import requests
from requests.exceptions import SSLError

# Set the title and emoji
st.title("🌐 Website Scraper Checker 🕷️")

# Input for the website URL
url = st.text_input("Enter the website URL to check:")

# Function to check if a website can be scraped
def can_scrape(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            st.success(f"👍 Website {url} can be scraped")
            return True
        else:
            st.error(f"❌ Website {url} returned status code {response.status_code}")
            return False
    except SSLError:
        st.error(f"❌ SSL certificate validation failed for {url}")
        return False
    except:
        st.error(f"❌ An error occurred while connecting to {url}")
        return False

# Check if the URL is not empty and trigger the check
if url:
    can_scrape(url)
