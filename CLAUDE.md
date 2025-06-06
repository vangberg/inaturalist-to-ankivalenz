# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python CLI tool that exports iNaturalist observations to Ankivalenz-formatted Markdown flashcards. The tool fetches observations from the iNaturalist API, downloads images, and generates flashcard files for spaced repetition learning.

## Architecture

The codebase is organized into 3 main modules:

- `api.py` - `INaturalistAPI` class handles API communication and image downloads
- `markdown.py` - Functions for generating Ankivalenz-compatible Markdown format
- `cli.py` - Click-based command-line interface that orchestrates the workflow

The CLI workflow: fetch observations → download images to `iNaturalist/` directory → generate `iNaturalist.md` with flashcard format

## Development Commands

```bash
# Set up development environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e .

# Run tests
pytest

# Run the CLI tool
inaturalist-to-ankivalenz --username <username> [--limit <number>] [--output-dir <directory>] [--common-name-lang <language>]
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