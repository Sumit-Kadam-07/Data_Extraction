import pandas as pd

def extract_coursera(ocr_result):
  name=""
  string = ocr_result
  start = "2023\n"
  end = "\nhas"
  start_index = string.index(start) + len(start)
  end_index = string.index(end)
  cropped_string = string[start_index:end_index].strip()
  name=""
  for i in cropped_string:
    name+=i

  date_ = ""
  for i in ocr_result:
    date_+=i
    if i=="\n":
      break
  new_date = str(date_.split())

  special_char = ["'",",","[","]"]
  x= new_date.replace("'",'')
  normal_string = x
  for i in special_char:
    normal_string = normal_string.replace(i,"")

  string = ocr_result
  start = "completed\n"
  end = "\nan"
  start_index = string.index(start) + len(start)
  end_index = string.index(end)
  cropped_string = string[start_index:end_index].strip()
  course=""
  for i in cropped_string:
    course+=i

  return [name, date_[:len(date_)-1], course]