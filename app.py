from dotenv import load_dotenv
from langchain.chains.summarize import load_summarize_chain
from langchain.schema import Document
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from utils import create_pdf
load_dotenv()
def main():
    llm = OpenAI(temperature=0)
    summary_ = ""
    pdf_reader = PdfReader('/content/crime-and-punishment.pdf')
    count=0
    i=0
    j=16
    while(count<49):
        text = ""
        for page in pdf_reader.pages[i:j]:
                text += page.extract_text()
        text_splitter = RecursiveCharacterTextSplitter(
                    chunk_size=1000,
                    chunk_overlap=0,
                    length_function=len
                    )
        chunks = text_splitter.split_text(text=text)
        docs = [Document(page_content=t) for t in chunks]
        chain = load_summarize_chain(llm, chain_type="map_reduce")
        summary = chain.run(docs)
        summary_=summary_+summary
        create_pdf(summary_)
if __name__ == "__main__":
      main()

