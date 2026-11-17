import requests

res_parse_list = []
response = requests.get("http://books.toscrape.com/")
response.encoding = "utf-8"

response_text = response.text

response_parse = response_text.split('title="')

for parse_elem_1 in response_parse:
  for parse_elem_2 in parse_elem_1.split('"'):

    if len(parse_elem_2) > 2 and "</a>" not in parse_elem_2 and ">" not in parse_elem_2:
      if not parse_elem_2.startswith("http") and not parse_elem_2.startswith("index"):
        if parse_elem_2 not in res_parse_list:
          res_parse_list.append(parse_elem_2)

for title in res_parse_list:
  print(title)