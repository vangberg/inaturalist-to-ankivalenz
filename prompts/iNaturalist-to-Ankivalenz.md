# iNaturalist to Ankivalenz

A Python CLI tool to export iNaturalist observations to Ankivalenz-formatted Markdown for creating flashcards.

## Features

- Fetch user's observations from iNaturalist API
- Download observation images to a local directory
- Generate Ankivalenz-compatible Markdown flashcards
- Support for multiple observations
- Preserve observation metadata

## Requirements

- Python 3.8+
- iNaturalist API access
- User authentication for accessing private observations

## Authentication

The tool uses OAuth 2.0 for secure, browser-based authentication:

1. First run will open your default browser
2. Log in to iNaturalist and authorize the application
3. The tool will automatically receive and store the access token
4. Subsequent runs will use the stored token

```bash
# First run - initiates OAuth flow
python inaturalist_to_ankivalenz.py --auth

# Subsequent runs - uses stored token
python inaturalist_to_ankivalenz.py
```

## Security

- OAuth tokens are stored securely in the user's home directory
- All API requests use HTTPS

## Usage

```bash
python inaturalist_to_ankivalenz.py --username <username> [--limit <number>]
```

## Output Format

The tool will:
1. Create an `iNaturalist/` directory to store downloaded images
2. Generate an `iNaturalist.md` file with Ankivalenz-formatted flashcards

Example output format:

```markdown
# iNaturalist Observations

- ![iNaturalist/observation-1.jpg] ?:: Monarch Butterfly (Danaus plexippus)
- ![iNaturalist/observation-2.jpg] ?:: California Poppy (Eschscholzia californica)
```

## Configuration

The tool can be configured through:
- Command line arguments
- Environment variables
- Configuration file

## Dependencies

- `requests` - For API communication
- `python-dotenv` - For environment variable management
- `click` - For CLI interface

## Installation

```bash
pip install inaturalist-to-ankivalenz
```

## Package Structure

```
inaturalist-to-ankivalenz/
├── pyproject.toml
├── README.md
├── src/
│   └── inaturalist_to_ankivalenz/
│       ├── __init__.py
│       ├── cli.py
│       ├── auth.py
│       ├── api.py
│       └── markdown.py
└── tests/
    └── __init__.py
```

## Development

To set up the development environment:

```bash
# Clone the repository
git clone https://github.com/yourusername/inaturalist-to-ankivalenz.git
cd inaturalist-to-ankivalenz

# Install in development mode
pip install -e .

# Run tests
pytest
```

## Building and Publishing

```bash
# Build the package
python -m build

# Publish to PyPI
python -m twine upload dist/*
```

## License

MIT License