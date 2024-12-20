def extract_techedu(ocr_result):
  name=""
  string = ocr_result
  start = "TO\n"
  end = "\nFOR"
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
  start = "\nIN"
  end = " BY"
  start_index = string.index(start) + len(start)
  end_index = string.index(end)
  cropped_string = string[start_index:end_index].strip()
  course=""
  for i in cropped_string:
    course+=i

  # fname = list(name)
  # certificate = list(course)
  date = normal_string

  return [name, date, course]

  # l1=['Name','Date of Certification','Course Name']
  # l2=[name, date, course]

  # d1=zip(l1,l2)
  # d2 = dict(d1)

  # import pandas as pd
  # file_path = 'certificate.xlsx'
  # try:
  #     df_existing = pd.read_excel(file_path)
  # except FileNotFoundError:
  #     data_dict = d2
  #     df_new = pd.DataFrame(data_dict, index=[0])
  #     df_new.to_excel(file_path, index=False)
  # else:
  #     data_dict = d2
  #     df_new = pd.DataFrame(data_dict, index=[0])
  #     df_updated = pd.concat([df_existing, df_new], ignore_index=True)
  #     df_updated.to_excel(file_path, index=False)