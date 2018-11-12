from html.parser import HTMLParser
import webbrowser
import json


class htmlParser(HTMLParser):
    html = ""
    indent = 0
    nonendindent = [
        "a",
        "b",
        "p",
        "h1",
        "h2",
        "li",
        "title",
        "script",
    ]
    nonstartindent = {
        "b",
        "a"
    }

    def __init__(self):
        super().__init__()        

    def indenting(self, name, tag):
        if name == "data":
            return
        if name == "start":
            if tag in self.nonstartindent:
                return
        if name == "end":
            if tag in self.nonendindent:
                return
        self.html += "\n"
        for i in range(self.indent):
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
        self.html += "<!%s>" % (data)

    def unknown_decl(self, data):
        print("Unknown declaration tag: ", data)

    def handle_pi(self, data):
        print("Processing tag: ", data)

    def handle_comment(self, data):
        print("Comment tag: ", data)


class htmlMaker():
    def __init__(self):
        self.html = self.open("resources/html.html")
        self.nav = ""
        self.head = ""
        self.content = ""
        self.header = ""
        self.footer = ""
        self.script = ""

    def make(self):
        html = self.html
        html = html.replace("//head//", self.head)
        html = html.replace("//navigation//", self.nav)
        html = html.replace("//header//", self.header)
        html = html.replace("//content//", self.content)
        html = html.replace("//footer//", self.footer)
        html = html.replace("//script//", self.script)
        self.html = html

    def setHead(self):
        self.head = self.open("resources/head.html")

    def setNav(self):
        self.nav = self.open("resources/navigation.html")

    def setContent(self):
        self.content = self.open("resources/body.html")

    def setHeader(self):
        self.header = self.open("resources/header.html")

    def setFooter(self):
        self.footer = self.open("resources/footer.html")

    def setScript(self):
        self.script = self.open("resources/script.html")

    def open(self, path):
        bestand = open(path)
        content = bestand.read()
        bestand.close()
        return content


h = htmlMaker()
h.setHead()
h.setNav()
h.setFooter()
h.setHeader()
h.setContent()
h.setScript()
h.make()

p = htmlParser()
p.feed(h.html)
# print(p.html)

test = open("test.html", "w+")
test.write(p.html)

# webbrowser.open_new_tab("test.html")
