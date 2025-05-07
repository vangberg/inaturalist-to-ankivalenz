"""iNaturalist API interaction."""

import requests
from pathlib import Path

INATURALIST_API_URL = "https://api.inaturalist.org/v1"


class INaturalistAPI:
    """Client for interacting with iNaturalist API."""

    def __init__(self):
        self.session = requests.Session()
        self.api_url = INATURALIST_API_URL

    def get_user_observations(self, username, limit=100, locale=None):
        """Fetch observations for a given user."""
        params = {
            "user_login": username,
            "per_page": limit,
            "order_by": "created_at",
            "order": "desc",
        }

        if locale:
            params["locale"] = locale

        response = self.session.get(f"{self.api_url}/observations", params=params)
        response.raise_for_status()

        return response.json()["results"]

    def download_observation_image(self, observation, output_dir):
        """Download observation image to specified directory."""
        if not observation.get("photos"):
            return None

        photo = observation["photos"][0]
        # Replace 'square' with 'medium' in the URL to get a larger image
        image_url = photo["url"].replace("square.jpeg", "medium.jpeg")

        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        response = requests.get(image_url)
        response.raise_for_status()

        image_path = output_dir / f"observation-{observation['id']}.jpg"
        image_path.write_bytes(response.content)

        return image_path
