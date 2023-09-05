# PDF to Summarized PDF Converter

This Python program allows you to convert a regular PDF document into a summarized PDF using language processing techniques. It leverages the [langchain](https://langchain.io) library and [PyPDF2](https://pythonhosted.org/PyPDF2/) for text extraction and manipulation. With this tool, you can condense lengthy PDFs into shorter, more digestible versions.

## Prerequisites

Before you can use this program, make sure you have the required dependencies installed. You can find them listed in the `requirements.txt` file. To install them, run:

---bash
pip install -r requirements.txt

Make sure to replace 'YOUR_API_KEY' with your actual OpenAI API key in the code.
import os
os.environ['OPENAI_API_KEY'] = 'YOUR_API_KEY'

Make sure to replace 'YOUR_API_KEY' with your actual OpenAI API key in the code.

This approach allows you to securely store and use your API key without hardcoding it directly into your code. It's a best practice for managing sensitive information like API keys.






Additionally, ensure you have the appropriate Python version specified in the runtime.txt file.

#Usage
Place the PDF file you want to summarize in the same directory as app.py.

Modify the app.py file if necessary to customize the summarization process according to your preferences.

Run the app.py script:

---bash
python app.py

The program will extract text from the PDF, generate a summary, and create a new summarized PDF in the same directory.

#Customization
You can customize the summarization process by modifying the app.py file. Some possible customizations include:

Adjusting the length of the summary.
Choosing the language model or summarization algorithm.
Fine-tuning the summarization parameters.


#License
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to contribute, report issues, or suggest improvements. Happy summarizing!


You can copy and paste this code into your GitHub repository's README.md file, and don't forget to replace placeholders like `"your_pdf.pdf"` with actual file paths or relevant information.




