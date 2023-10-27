import re

markdown_text = 'Make the World a *Better Place*'
bold_pattern = r'\*(.*?)\*'
replacement = r'<b>\1<\\b>'
html_text = re.sub(bold_pattern, replacement, markdown_text)

print(html_text)

'''
https://www.pythontutorial.net/python-regex/python-regex-sub/


markdown_text = "This is **bold** text."
bold_pattern = r"\*\*(.*?)\*\*"
html_text = re.sub(bold_pattern, r"<b>\1</b>", markdown_text)
print(html_text)
'''



'''
#Heading
^#(\w+)#$

**Bold**
\*\*([\w\s,\.]+)\*\*

parrafo (se busca un espacio)
^ (\w+)
'''


'''

  #header rules
  [/#{6}\s?([^\n]+)/g, "<h6>$1</h6>"],
  [/#{5}\s?([^\n]+)/g, "<h5>$1</h5>"],
  [/#{4}\s?([^\n]+)/g, "<h4>$1</h4>"],
  [/#{3}\s?([^\n]+)/g, "<h3>$1</h3>"],
  [/#{2}\s?([^\n]+)/g, "<h2>$1</h2>"],
  [/#{1}\s?([^\n]+)/g, "<h1>$1</h1>"],
   ^#(\w+)#$
  
  #bold, italics and paragragh rules
  [/\*\*\s?([^\n]+)\*\*/g, "<b>$1</b>"],
  [/\*\s?([^\n]+)\*/g, "<i>$1</i>"],
  [/__([^_]+)__/g, "<b>$1</b>"],
  [/_([^_`]+)_/g, "<i>$1</i>"],
  [/([^\n]+\n?)/g, "<p>$1</p>"],
  
  #links
  [
    /\[([^\]]+)\]\(([^)]+)\)/g,
    '<a href="$2" style="color:#2A5DB0;text-decoration: none;">$1</a>',
  ],
  
  //highlights
  [
    /(`)(\s?[^\n,]+\s?)(`)/g,
    '<a style="background-color:grey;color:black;text-decoration: none;border-radius: 3px;padding:0 2px;">$2</a>',
  ],
 
  //Lists
  [/([^\n]+)(\+)([^\n]+)/g, "<ul><li>$3</li></ul>"],
  [/([^\n]+)(\*)([^\n]+)/g, "<ul><li>$3</li></ul>"],
  '''