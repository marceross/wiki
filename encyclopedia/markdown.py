import re

'''
markdown_text = "This is **bold** text."
bold_pattern = r"\*\*(.*?)\*\*"
html_text = re.sub(bold_pattern, r"<b>\1</b>", markdown_text)
print(html_text)
'''

markdown_text = 'Make the World a *Better Place*'
bold_pattern = r'\*(.*?)\*'
replacement = r'<b>\1<\\b>'
html_text = re.sub(bold_pattern, replacement, markdown_text)

print(html_text)


