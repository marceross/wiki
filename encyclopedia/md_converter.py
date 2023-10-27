import re

patterns = [
    # heading
    (r'######\s?(.*)', r'<h6>\1</h6>'),
    (r'#####\s?(.*)', r'<h5>\1</h5>'),
    (r'####\s?(.*)', r'<h4>\1</h4>'),
    (r'###\s?(.*)', r'<h3>\1</h3>'),
    (r'##\s?(.*)', r'<h2>\1</h2>'),
    (r'#\s?(.*)', r'<h1>\1</h1>'),

    # bold
    (r'\*\*(.*)\*\*', r'<b>\1</b>'),

    # links
    (r'\[(.*)\]\s?\((.*)\)', r'<a href="\2">\1</a>'),

    # list
    (r'(?m)^\s?(?:\*|-)\s?(.*)$', r'<li>\1</li>'),

    # paragraph
    (r'(?m)^(?!<(?:h))((?:[^\n][\n]?)+)', r'<p>\n\1</p>\n'),
]

def to_html(markdown):
    html = markdown
    for pattern in patterns:
        html = re.sub(pattern[0], pattern[1], html)
    return html