import requests

res_parse_list = []
response = requests.get("http://books.toscrape.com/")
response.encoding = "utf-8"

response_text = response.text
response_parse = response_text.split('<p class="price_color">')

for parse_elem_1 in response_parse:
  for parse_elem_2 in parse_elem_1.split("</p>"):
    if parse_elem_2.startswith("£"):
      res_parse_list.append(parse_elem_2)

for price in res_parse_list:
  print(price)