"""Tests for markdown generation."""

from pathlib import Path
from inaturalist_to_ankivalenz.markdown import generate_markdown


def test_generate_markdown():
    """Test markdown generation with sample observations."""
    # Sample observation data
    observations = [
        {
            "id": 1,
            "photos": [{"url": "http://example.com/photo1.jpg"}],
            "taxon": {
                "preferred_common_name": "Monarch Butterfly",
                "name": "Danaus plexippus",
            },
        }
    ]

    # Create test image file
    image_dir = Path("inaturalist")
    image_dir.mkdir(exist_ok=True)
    image_path = image_dir / "observation-1.jpg"
    image_path.touch()

    # Generate markdown
    markdown = generate_markdown(observations, image_dir)

    # Clean up
    image_path.unlink()
    image_dir.rmdir()

    # Verify output
    expected = "# iNaturalist\n\n- ![Monarch Butterfly (Danaus plexippus)](iNaturalist/observation-1.jpg) ?:: Monarch Butterfly (Danaus plexippus)"
    assert markdown == expected
