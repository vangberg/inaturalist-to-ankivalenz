"""Command-line interface for iNaturalist to Ankivalenz."""

import click
from pathlib import Path
from .api import INaturalistAPI
from .markdown import generate_markdown, save_markdown


@click.command()
@click.option("--username", required=True, help="iNaturalist username")
@click.option("--limit", default=100, help="Maximum number of observations to fetch")
@click.option(
    "--output-dir", default=".", help="Output directory for images and markdown"
)
@click.option(
    "--common-name-lang",
    default="en",
    help="Language for common names (e.g., 'en', 'da', 'sv')",
)
def main(username, limit, output_dir, common_name_lang):
    """Export iNaturalist observations to Ankivalenz-formatted Markdown."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    image_dir = output_dir / "iNaturalist"

    # Initialize API client
    api = INaturalistAPI()

    # Fetch observations
    click.echo(f"Fetching observations for user {username}...")
    observations = api.get_user_observations(username, limit, locale=common_name_lang)

    # Download images
    click.echo("Downloading observation images...")
    for obs in observations:
        if obs.get("photos"):
            api.download_observation_image(obs, image_dir)

    # Generate markdown
    click.echo("Generating Ankivalenz markdown...")
    markdown = generate_markdown(observations, image_dir)

    # Save markdown
    output_file = output_dir / "iNaturalist.md"
    save_markdown(markdown, output_file)

    click.echo(f"Export complete! Output saved to {output_file}")
