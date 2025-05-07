"""Generate Ankivalenz-formatted Markdown from iNaturalist observations."""

from pathlib import Path


def generate_markdown(observations, image_dir):
    """Generate Ankivalenz-formatted Markdown for observations."""
    markdown = ["# iNaturalist\n"]

    for obs in observations:
        if not obs.get("photos"):
            continue

        image_path = Path(image_dir) / f"observation-{obs['id']}.jpg"
        if not image_path.exists():
            continue

        # Get the taxon name
        taxon = obs.get("taxon", {})
        common_name = taxon.get("preferred_common_name", "")
        scientific_name = taxon.get("name", "")

        # Format the name
        if common_name and scientific_name:
            name = f"{common_name} ({scientific_name})"
        elif common_name:
            name = common_name
        elif scientific_name:
            name = scientific_name
        else:
            continue

        # Add the markdown line
        markdown.append(f"- ![{name}](iNaturalist/{image_path.name}) ?:: {name}")

    return "\n".join(markdown)


def save_markdown(markdown, output_file):
    """Save markdown content to file."""
    output_path = Path(output_file)
    output_path.write_text(markdown)
