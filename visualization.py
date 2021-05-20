import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt

def dict_replace(string, table):
   temp_str = string
   for old, new in table.items():
      temp_str = temp_str.replace(old, new)

   return temp_str

replace_table = {
   ",": " ",
   ".": " ",
   "-": " ",
   "$": " ",
   "%": " ",
   "%p": " ",
}

def extract_num(string):
   return [int(dict_replace(s, replace_table)) for s in string.split() if dict_replace(s, replace_table).replace("%p", " ").isnumeric()]

def crawl_text(url):
   html = requests.get(url)
   soup = BeautifulSoup(html.text, features="html.parser")

   script_tag = soup.find_all(['script', 'style', 'header', 'footer', 'form'])

   for script in script_tag:
      script.extract()

   content = soup.get_text('\n', strip=True)

   return content

def get_frequency(numlist):
   freq = {}
   for i in range(1, 9 + 1):
      freq[i] = round(numlist.count(i) / len(numlist) * 100)

   return freq

urls = []
nums = []

with open("urls.txt") as f:
   lines = f.readlines()
   for line in lines:
      urls.append(line.replace("\n", ""))

for url in urls:
   print(f"URL: {url}")
   print("Crawling...")
   string = crawl_text(url)
   print("Extracting Numbers...")
   for num in extract_num(string):
      firstdigit = int(str(num)[0])
      nums.append(firstdigit)

   print("Done.\n")

freqdict = get_frequency(nums)

print("Plotting...")

plt.plot(list(freqdict.keys()), list(freqdict.values()))

plt.xlabel("First Digit")
plt.ylabel("Frequency (%)")

plt.show()
plt.clf()

print("Done.")
