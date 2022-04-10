class Metadate:
    def __init__(self,identifier,publisher,date,author,title,language,source,uploader,description = "test"):
        self.identifier = identifier
        self.publisher = publisher
        self.date = date
        self.author = author
        self.title = title
        self.language = language
        self.source = source
        self.uploader = uploader
        self.description = description
class Translated_metadate(Metadate):
    def __init__(self,identifier,publisher,date,author,title,language,source,uploader,translator):
        super().__init__(identifier,publisher,date,author,title,source,language,uploader)
        self.translator = translator

if __name__ == '__main__':
    adam = Translated_metadate('DAV-018','ワニマガジン社','2021-04-15','米奇王','主僕狂熱','zh-TW','SCAN','K4W1H0R53','台北原動力視覺有限公司')
    print(adam.identifier)
    print(adam.publisher)
    print(adam.date)
    print(adam.author)
    print(adam.title)
    print(adam.language)
    print(adam.source)
    print(adam.uploader)
    print(adam.translator)