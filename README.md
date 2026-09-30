# auto-typer

Reads text from a .txt file and types it out with random delays between characters, simulating a human typing. Random typos and more are coming soon.

## Usage
```
python3 typer.py test.txt --delay 0.05 0.09
```
- `path`: a .txt file
- `--delay MIN MAX`: random per-character delay range in seconds (default 0.05 0.09)

Pauses are longer after punctuation and line breaks and shorter after spaces. Bad paths, non-.txt files, and invalid delay ranges give an error.