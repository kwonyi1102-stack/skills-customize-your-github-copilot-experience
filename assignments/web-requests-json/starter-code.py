import json
import urllib.request


API_URL = "https://api.github.com"


def fetch_json(url):
    """Fetch JSON data from a URL and return it as a Python dictionary."""
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
        return json.loads(data.decode("utf-8"))
    except Exception as e:
        print(f"Error: Unable to fetch data: {e}")
        return {}


def main():
    """Fetch and display data from an API."""
    data = fetch_json(API_URL)

    # TODO: Print useful information from the API response.
    # Example: print(data.get("current_user_url"))
    # Example: print(data.get("message"))

    # TODO: Build a short summary using the data you retrieved.


if __name__ == "__main__":
    main()
