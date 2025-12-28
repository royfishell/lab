import requests
import sys


def main():
	try:
		response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q": sys.argv[1]}
        )
		response.raise_for_status()
	except requests.HTTPError:
		print("Couldn't complete request!")
		return
		
	content = response.json()
	for artwork in content["data"]:
		print(f"* {artwork['title']}")

main()
