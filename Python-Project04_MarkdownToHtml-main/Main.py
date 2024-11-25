import markdown
import os

def markdown_to_html(input_file, output_file):
    # Check if the file exists
    if not os.path.exists(input_file):
        print(f"The file {input_file} was not found.")
        return

    # Read the Markdown content
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            markdown_content = file.read()
        
        # Convert Markdown to HTML
        html_content = markdown.markdown(markdown_content)
        
        # Write the HTML content to an output file
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(html_content)
        
        print(f"Conversion successful! HTML output saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the exact path to your input Markdown file
input_markdown_file = os.path.abspath("Project04_MarkdownToHtml/Hello.md")  # Use an absolute path
output_html_file = "Hello.html"

# Run the conversion
markdown_to_html(input_markdown_file, output_html_file)
