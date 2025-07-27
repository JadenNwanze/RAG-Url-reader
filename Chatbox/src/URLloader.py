def UrlLoader(Urls):
    from langchain.document_loaders import WebBaseLoader

    loader = WebBaseLoader(Urls)
    docs = loader.load()
    return docs