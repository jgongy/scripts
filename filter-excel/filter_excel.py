import openpyxl, os

SHEET_NAME = "All Courses_CY2021 analysis.xlsx"
KEYWORDS_FILE = "keywords.txt"
RESULTS_FILE = "results.txt"
COL_NUMBER = 15
NUM_ROWS = 1660

def get_keywords():
  # Read a text file of keywords into an array
  keywords = set()
  with open(KEYWORDS_FILE) as f:
    words = f.read()
    # split_words = words.split() # .split() will split on and remove any whitespace
    for word in split_words:
      keywords.add(word)

  print(keywords)
  return keywords

"""
Checks if any of the keywords exist in the paragraph.
"""
def get_trigger_words(paragraph, keywords):
  trigger_words = []
  for word in keywords:
    if word in paragraph:
      trigger_words.append(word)
  return trigger_words
  

"""
Assumes there is only one sheet in the workbook.
"""
def filter_keywords_inclusive(keywords):
  workbook = openpyxl.load_workbook(SHEET_NAME)
  worksheet = workbook.active

  # Empties the file
  file = open(RESULTS_FILE, "w")
  file.write("")
  file.close()

  file = open(RESULTS_FILE, "a")

  for row in range(2, NUM_ROWS + 1): # Excel sheets are not zero-indexed.
    cell = worksheet.cell(row=row, column=COL_NUMBER)
    text = cell.value
    trigger_words = get_trigger_words(text, keywords)
    if trigger_words:
      # There is at least one trigger word
      file.write(cell.coordinate)
      file.write(" " + ", ".join(trigger_words))
      file.write("\n")

  file.close()




if __name__ == "__main__":
  keywords = get_keywords()
  filter_keywords_inclusive(keywords)


