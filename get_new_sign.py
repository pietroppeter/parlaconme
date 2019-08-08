# pythonista script to get text to update index.md with a new sign
import appex
import clipboard
from bs4 import BeautifulSoup

req = appex.get_web_page_info()
soup = BeautifulSoup(req['html'])
src = soup.find("video").get("src")
# print("src:\n", src, '\n')
h2 = soup.find("h2")
# print("h2:\n", h2, '\n')

keyword = h2.get_text().strip()
video_id = '/'.join(src.split('/')[-2:])[:-4]

text = f"""
## {keyword}

{{% include signVideo.html id="{video_id}" %}}
"""
print("text:\n", text)
clipboard.set(text)
print("text pasted to clipboard!")
