import sys

from urllib import request

class WebScraper():
    def webScraperFromString(url: str) -> str:
        try:
            with request.urlopen(url) as doc:
                html = doc.read()
        except:
            print("Could not open %s" % doc, file=sys.stderr)

        return html




