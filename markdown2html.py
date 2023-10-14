#!/usr/bin/python3
"""Module for converting markdown files to html files"""

from sys import argv, exit

def convert_markdown_to_html(input_file, output_file):
    """
    Converts a Markdown file to HTML and writes the output to a file.
    """
    # Check that the Markdown file exists and is a file
    if not (os.path.exists(input_file) and os.path.isfile(input_file)):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Read the Markdown file and convert it to HTML
    with open(input_file, encoding="utf-8") as f:
        html_lines = []
        for line in f:
            # Check for Markdown headings
            match = re.match(r"^(#+) (.*)$", line)
            if match:
                heading_level = len(match.group(1))
                heading_text = match.group(2)
                html_lines.append(f"<h{heading_level}>{heading_text}</h{heading_level}>")
            else:
                html_lines.append(line.rstrip())

    # Write the HTML output to a file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(html_lines))

if __name__ == "__main__":
    # Check that the correct number of arguments were provided
    if len(argv) < 3:
        exit("Usage: ./markdown2html.py README.md README.html")
    try:
        with open(argv[1], "r") as markdown_file:
            with open(argv[2], "w") as html_file:
                for line in markdown_file:
                    if "###### " in line:
                        line = line.replace("###### ", "<h6>")
                        line = line.replace("\n", "</h6>\n")
                    elif "##### " in line:
                        line = line.replace("##### ", "<h5>")
                        line = line.replace("\n", "</h5>\n")
                    elif "#### " in line:
                        line = line.replace("#### ", "<h4>")
                        line = line.replace("\n", "</h4>\n")
                    elif "### " in line:
                        line = line.replace("### ", "<h3>")
                        line = line.replace("\n", "</h3>\n")
                    elif "## " in line:
                        line = line.replace("## ", "<h2>")
                        line = line.replace("\n", "</h2>\n")
                    elif "# " in line:
                        line = line.replace("# ", "<h1>")
                        line = line.replace("\n", "</h1>\n")
                    html_file.write(line)
    except:
        exit("Missing {}".format(argv[1]))
