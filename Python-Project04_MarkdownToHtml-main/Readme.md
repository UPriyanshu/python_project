
# Markdown to HTML Converter (Python)

## Project Overview
This project is a simple Markdown to HTML converter script written in Python. The program reads a Markdown file and converts its content to HTML, making it easier to render Markdown files in a web-compatible format.

## Features
- **Markdown to HTML Conversion**: Converts any Markdown file to an HTML file.
- **Simple and Fast**: Leverages the `markdown` library to ensure quick conversion.

## Requirements
- **Python** (version 3.x)
- **markdown** library (install via pip)

## Installation and Usage
1. Install the `markdown` library:
   ```bash
   pip install markdown
   ```
2. Place the Markdown file (e.g., `Hello.md`) that you want to convert in the same directory as `Main.py` is Being Placed.
3. Run the following command to start the script:
   ```bash
   python Main.py
   ```
4. The HTML file (e.g., `README.html`) will be generated in the same directory.

## Code Explanation
- The script uses the `markdown` library's `markdown()` function to convert the Markdown content to HTML.
- **Functionality**:
  - **`markdown_to_html(input_file, output_file)`**: Reads the Markdown file, converts its content to HTML, and writes the HTML content to a new file.

## Project Structure
```
.
├── Main.py                   # Main script for converting Markdown to HTML
├── README.md                 # Project documentation
├── Hello.md                  # File for Project Use
└── ProjectScreenshots/
    └── image.png             # Screenshot of the application
```

## Screenshot
![Markdown to HTML Converter](ProjectScreenshots/image.png)

## License
This project is open-source and available under the MIT License.

## Resources
For more information on the `markdown` library, refer to the [Python Markdown documentation](https://python-markdown.github.io/).
