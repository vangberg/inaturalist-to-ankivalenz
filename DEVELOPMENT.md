# Development Guide

## Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/inaturalist-to-ankivalenz.git
cd inaturalist-to-ankivalenz

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .

# Run tests
pytest
```

## Architecture

The codebase is organized into 3 main modules:

- `api.py` - `INaturalistAPI` class handles API communication and image downloads
- `markdown.py` - Functions for generating Ankivalenz-compatible Markdown format
- `cli.py` - Click-based command-line interface that orchestrates the workflow

The CLI workflow: fetch observations → download images to `iNaturalist/` directory → generate `iNaturalist.md` with flashcard format

## Testing

Run tests with:
```bash
pytest
```

## Creating New Releases

To create a new release:

1. Update version in `pyproject.toml`
2. Commit changes:
   ```bash
   git add .
   git commit -m "bump version to X.Y.Z"
   ```
3. Create and push a git tag:
   ```bash
   git tag vX.Y.Z
   git push origin vX.Y.Z
   ```
4. Build and publish to PyPI:
   ```bash
   python -m build
   python -m twine upload dist/*
   ```

## Dependencies

- `requests` for API calls and image downloads
- `click` for CLI interface
- Uses `pathlib` for file system operations

## Output Format

The tool generates Ankivalenz flashcards in this format:
```markdown
- ![Common Name (Scientific Name)](iNaturalist/observation-ID.jpg) ?:: Common Name (Scientific Name)
```