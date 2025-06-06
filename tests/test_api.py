"""Tests for API functionality."""

import tempfile
from pathlib import Path
from unittest.mock import Mock, patch
from inaturalist_to_ankivalenz.api import INaturalistAPI


def test_download_observation_image_skips_existing_file():
    """Test that download_observation_image skips downloading if file already exists."""
    api = INaturalistAPI()
    
    # Sample observation data
    observation = {
        "id": 123,
        "photos": [{"url": "http://example.com/photo-square.jpg"}]
    }
    
    with tempfile.TemporaryDirectory() as temp_dir:
        output_dir = Path(temp_dir)
        image_path = output_dir / "observation-123.jpg"
        
        # Create the image file to simulate it already exists
        image_path.write_text("existing image content")
        original_content = image_path.read_text()
        
        # Mock requests.get to ensure it's not called
        with patch('inaturalist_to_ankivalenz.api.requests.get') as mock_get:
            result = api.download_observation_image(observation, output_dir)
            
            # Verify the existing file is returned
            assert result == image_path
            # Verify the content wasn't changed
            assert image_path.read_text() == original_content
            # Verify requests.get was not called
            mock_get.assert_not_called()


def test_download_observation_image_downloads_new_file():
    """Test that download_observation_image downloads when file doesn't exist."""
    api = INaturalistAPI()
    
    # Sample observation data
    observation = {
        "id": 456,
        "photos": [{"url": "http://example.com/photo-square.jpg"}]
    }
    
    with tempfile.TemporaryDirectory() as temp_dir:
        output_dir = Path(temp_dir)
        image_path = output_dir / "observation-456.jpg"
        
        # Ensure file doesn't exist
        assert not image_path.exists()
        
        # Mock requests.get to simulate successful download
        mock_response = Mock()
        mock_response.content = b"downloaded image content"
        mock_response.raise_for_status = Mock()
        
        with patch('inaturalist_to_ankivalenz.api.requests.get', return_value=mock_response) as mock_get:
            result = api.download_observation_image(observation, output_dir)
            
            # Verify the file was created and returned
            assert result == image_path
            assert image_path.exists()
            assert image_path.read_bytes() == b"downloaded image content"
            # Verify requests.get was called with the medium URL
            mock_get.assert_called_once_with("http://example.com/photo-medium.jpg")