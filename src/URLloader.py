def UrlLoader(Urls):
    from langchain.document_loaders import UnstructuredURLLoader

    loader = UnstructuredURLLoader(Urls)
    docs = loader.load()
    return docs
