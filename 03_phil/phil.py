import sys
import re
from urllib.request import urlopen
from urllib.parse import quote

def get_content(name):
    try:
        with urlopen(f"https://ru.wikipedia.org/wiki/{quote(name)}") as response:
            html = response.read().decode()
        return html
    except:
        return None

def extract_content(page):
    begin = page.find('<p>')
    end = page.rfind('</p>')
    return (begin, end)

def extract_links(page, begin, end):
    links = re.findall(r'href="/wiki/([^:#]*?)"', page[begin:end])
    return list(set(links))

def find_chain(start, finish):
    visited = {start}
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == finish:
            return path
        page = get_content(node)
        if page is None:
            continue
        begin, end = extract_content(page)
        for link in extract_links(page, begin, end):
            if link not in visited:
                visited.add(link)
                queue.append(path + [link])
    return None

def main():
    if len(sys.argv) > 1:
        start = sys.argv[1]
        finish = 'Философия'
        chain = find_chain(start, finish)
        if chain is not None:
            print(' -> '.join(chain))
    else:
        print("Please provide a start word as a command line argument.")
        
if __name__ == '__main__':
    main()
