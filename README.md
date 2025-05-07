# iNaturalist to Ankivalenz

A Python CLI tool to export iNaturalist observations to [Ankivalenz](https://github.com/vangberg/ankivalenz/)-formatted Markdown for creating flashcards.

## Features

- Fetch user's observations from iNaturalist API
- Download observation images to a local directory
- Generate Ankivalenz-compatible Markdown flashcards
- Support for multiple observations
- Preserve observation metadata

## Installation

```bash
pip install inaturalist-to-ankivalenz
```

## Usage

Export observations for any iNaturalist user:

```bash
inaturalist-to-ankivalenz --username <username> [--limit <number>] [--output-dir <directory>] [--common-name-lang <language>]
```

Options:
- `--username`: iNaturalist username (required)
- `--limit`: Maximum number of observations to fetch (default: 100)
- `--output-dir`: Output directory for images and markdown (default: current directory)
- `--common-name-lang`: Language for common names (e.g., 'en', 'da', 'sv') (default: 'en')

## Output

The tool will:
1. Create an `iNaturalist/` directory to store downloaded images
2. Generate an `iNaturalist.md` file with Ankivalenz-formatted flashcards

Example output format:

```markdown
# iNaturalist

- ![iNaturalist/observation-1.jpg] ?:: Monarch Butterfly (Danaus plexippus)
- ![iNaturalist/observation-2.jpg] ?:: California Poppy (Eschscholzia californica)
```

## Development

To set up the development environment:

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

## License

MIT License 