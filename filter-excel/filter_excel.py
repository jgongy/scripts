import openpyxl, sys
from os.path import exists

SHEET_FILE_DEFAULT = "sheet.xlsx"
KEYWORDS_FILE_DEFAULT = "keywords.txt"
RESULT_FILE_DEFAULT = "results.txt"
CASE_INSENSITIVE = False

def get_keywords(keywords_file):
  # Read a text file of keywords into an array
  keywords = set()
  with open(keywords_file, "r") as f:
    words = f.readlines()
    # Strip the newline and other spaces, then strip surrounding quotes
    words = map(lambda word: word.strip().strip('\"'), words)
    keywords = set(words);

  return keywords

"""
Checks if any of the keywords exist in the text.
"""
def get_trigger_words(text, keywords):
  trigger_words = []
  new_text = text;
  if (CASE_INSENSITIVE):
    new_text = new_text.lower()
  for word in keywords:
    new_word = word
    if (CASE_INSENSITIVE):
      new_word = word.lower()
    if new_word in new_text:
      trigger_words.append(word)
  return trigger_words

"""
Assumes there is only one sheet in the workbook.
"""
def filter_keywords_inclusive(sheet_file, keywords_file, result_file):
  if (not exists(keywords_file)):
    print(f'No valid keywords file "{keywords_file}" could be found in current directory.')
    return
  if (not exists(sheet_file)):
    print(f'No valid Excel file "{sheet_file}" could be found in current directory.')
    return

  keywords = get_keywords(keywords_file)
  workbook = openpyxl.load_workbook(sheet_file)
  worksheet = workbook.active

  # Empties the file
  file = open(result_file, "w")
  file.write("")
  file.close()

  file = open(result_file, "a")

  # Excel sheets are not zero-indexed.
  for row in range(2, num_rows):
    cell = worksheet.cell(row=row, column=col_num)
    text = cell.value
    trigger_words = get_trigger_words(text, keywords)
    if trigger_words:
      # There is at least one trigger word
      file.write(cell.coordinate)
      file.write(" " + ", ".join(trigger_words))
      file.write("\n")

  file.close()

def main():
  args = sys.argv[1:]

  keywords_file = KEYWORDS_FILE_DEFAULT
  sheet_file = SHEET_FILE_DEFAULT
  result_file = RESULT_FILE_DEFAULT
  while (len(args) > 0 and args[0][0] == '-'):
    # Process all flags
    if args[0] == "-k":
      keywords_file = args[1]
      args = args[2:]
    elif args[0] == "-s":
      sheet_file = args[1]
      args = args[2:]
    elif args[0] == "-r":
      result_file = args[1]
      args = args[2:]
    elif args[0] == "--case-insensitive":
      CASE_INSENSITIVE = True
      args = args[1:]
    else:
      print("Invalid flag")
      return

  if (len(args) < 2):
    print("Need the number of rows and the column to read from.")
    return

  filter_keywords_inclusive(sheet_file, keywords_file, result_file, num_rows, col_num)

if __name__ == "__main__":
  main()


