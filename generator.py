from html.parser import HTMLParser
import webbrowser
import json


class htmlParser(HTMLParser):
    html = ""
    indent = 0
    tags = {}
    nonendindent = {
        "a",
        "b",
        "p",
        "h1",
        "h2",
        "li",
        "title",
        "script",
        "strong",
        "span",
        "td",
        "br",
        "th",
        "tr"
    }
    nonstartindent = {
        "b",
        "a",
        "span",
        "strong",
        "th",
        "td"
    }

    def clear(self):
        self.html = ""
        self.reset()

    def save(self, path):
        test = open(path, "w+")
        test.write(self.html)
        test.close()

    def indenting(self, name, tag):
        if name == "data":
            return
        if name == "start":
            if tag in self.nonstartindent:
                return
        if name == "end" or name == "startend":
            if tag in self.nonendindent:
                return
        self.html += "\n"
        for _ in range(self.indent):
            self.html += "  "

    def handle_startendtag(self, tag, attrs):
        text = ''
        for i in attrs:
            text += ' %s="%s\"' % (i[0], i[1])
        self.indenting("startend", tag)
        self.html += "<%s%s/>" % (tag, text)

    def handle_starttag(self, tag, attrs):
        text = ''
        for i in attrs:
            text += ' %s=\"%s\"' % (i[0], i[1])
        self.indenting("start", tag)
        self.html += "<%s%s>" % (tag, text)
        self.indent += 1

    def handle_endtag(self, tag):
        self.indent -= 1
        self.indenting("end", tag)
        self.html += "</%s>" % (tag)

    def handle_data(self, data):
        text = data.replace("\n", "").replace("  ", "")
        if text == "":
            return
        self.indenting("data", "")
        self.html += "%s" % (text)

    def handle_decl(self, data):
        self.indenting("decl", data)
        self.html += "<!%s>" % (data)

    def unknown_decl(self, data):
        print("Unknown declaration tag: ", data)

    def handle_pi(self, data):
        print("Processing tag: ", data)

    def handle_comment(self, data):
        print("Comment tag: ", data)


class jsonData():
    def __init__(self, path="resources/resources.json"):
        self.path = path
        content = open(path)
        self.beatifiy = htmlParser()
        self.JSON = json.load(content)

    def parser(self):
        def getStyle(styleName):
            for style in self.JSON["styles"]:
                if style["name"] == styleName:
                    return style
            return self.JSON["styles"][0]
        for site in self.JSON["sites"]:
            style = getStyle(site["style"])
            self.build(site, style)

    def build(self, site, style):
        def openfile(path):
            try:
                bestand = open(path)
                content = bestand.read()
                bestand.close()
            except:
                print("Exception opening file")
                content = ""
            return content
        def add(key, text):
            # print("//%s//" %key, text)
            pass
        for s in style:
            add(s, style[s])
        article = openfile(site["articles"][0])
        html    = openfile(style["build"])
        head    = openfile(style["head"])
        nav     = openfile(style["navigation"])
        header  = openfile(style["header"])
        footer  = openfile(style["footer"])
        script  = openfile(style["script"])
        html = html.replace("//head//",       head)
        html = html.replace("//title//",      site["title"])
        html = html.replace("//navigation//", nav)
        html = html.replace("//header//",     header)
        html = html.replace("//content//",    article)
        html = html.replace("//footer//",     footer)
        html = html.replace("//script//",     script)
        self.beatifiy.clear()
        self.beatifiy.feed(html)
        self.beatifiy.save(site["path"])

    def open(self):
        bestand = open(self.path)
        content = bestand.read()
        bestand.close()
        return content

    def write(self):
        bestand = open(self.path, "w+")
        bestand.saveJSON(json.dumps(self.JSON, indent=2))
        bestand.close()

    def rename(self, name, pathOld, pathNew):
        for i in self.JSON["sites"]:
            try:
                if i[name] == pathOld:
                    i[name] = pathNew
            except:
                print("%s does not exist!" % pathOld)


def main():
    j = jsonData()
    j.parser()

def pretty(path):
    with open(path) as text:
        gen = htmlParser()
        gen.feed(text.read())
        gen.save(path)

if __name__ == "__main__":
    pretty("articles/eerstejaar.html")
    main()