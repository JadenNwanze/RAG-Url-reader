# pipeline.py

from src.vectordb_manager import load_or_create_vectorstore
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from langchain.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA

def EmbeddingLogic(docs=None):
    # Load existing vectorstore or create if docs are passed
    vectorstore = load_or_create_vectorstore(docs)
    model_name = "google/flan-t5-small"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to("cpu")  # or .to("cuda") if you have a GPU

    pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer, max_length=512, device=0)
    llm = HuggingFacePipeline(pipeline=pipe)

    retriever = vectorstore.as_retriever(search_type="similarity", k=4)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain
