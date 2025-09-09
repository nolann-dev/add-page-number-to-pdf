# PDF Page Number Adder

A Python script that adds page numbers to PDF files in the format "current page / total pages" at the bottom center of each page.

## Features

- Adds page numbers to any PDF file
- Preserves original PDF formatting and content
- Page numbers displayed as "1 / 10", "2 / 10", etc.
- Automatically centers page numbers at the bottom of each page
- Maintains original page dimensions
- Clean, professional appearance using Helvetica font

## Visual Example

### Before (Original PDF)
![Input PDF without page numbers](docs/input.jpg)

### After (With Page Numbers Added)
![Output PDF with page numbers](docs/output.jpg)

As you can see, the script adds clean, professional page numbers at the bottom center of each page without affecting the original content.

## Requirements

- Python 3.6+
- PyPDF2
- reportlab

## Installation

1. Clone or download this repository
2. Install the required dependencies:

```bash
pip install PyPDF2 reportlab
```

## Usage

### Command Line

```bash
python add_page_numbers.py input.pdf output.pdf
```

**Parameters:**
- `input.pdf` - Path to the source PDF file
- `output.pdf` - Path where the numbered PDF will be saved

### Example

```bash
python add_page_numbers.py document.pdf document_numbered.pdf
```

This will create a new file `document_numbered.pdf` with page numbers added to each page.

### As a Python Module

You can also import and use the function in your own Python code:

```python
from add_page_numbers import add_page_numbers

# Add page numbers to a PDF
add_page_numbers("input.pdf", "output.pdf")
```

## How It Works

1. **Read Original PDF**: The script reads the input PDF and determines the number of pages
2. **Create Page Number Overlay**: For each page, it creates a small PDF overlay containing just the page number
3. **Merge Content**: The page number overlay is merged with the original page content
4. **Save Result**: All pages with added numbers are saved to the output file

## Page Number Format

- **Position**: Bottom center of each page
- **Format**: "current / total" (e.g., "5 / 20")
- **Font**: Helvetica, 12pt
- **Distance from bottom**: 20 points

## Error Handling

The script includes basic error handling:
- Validates command line arguments
- Provides usage instructions if incorrect parameters are provided
- Exits gracefully with appropriate error messages

## Limitations

- Page numbers are always placed at the bottom center
- Font and size are fixed (Helvetica, 12pt)
- Page numbers may overlap with existing content if the bottom margin is too small

## License

This project is open source. Feel free to modify and distribute as needed.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## Troubleshooting

**Common Issues:**

1. **Module not found error**: Make sure PyPDF2 and reportlab are installed
   ```bash
   pip install PyPDF2 reportlab
   ```

2. **Permission denied**: Ensure you have write permissions to the output directory

3. **File not found**: Check that the input PDF path is correct and the file exists

4. **Corrupted output**: Some complex PDFs may not merge properly. Try with a simpler PDF first.
