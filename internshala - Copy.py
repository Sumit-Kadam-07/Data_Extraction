import pandas as pd

def extract_internshala(ocr_result):
    """Code for Name"""
    name=""
    for i in ocr_result:
      name+=i
      if i=="\n":
        break
    name = name.strip()

    """Code for Date"""
    date_ = ""
    for i in ocr_result:
      date_+=i
    words = date_.split()
    for word in words:
        if len(word) == 10 and word[4] == "-" and word[7] == "-":
            # print(f"Date of Certification: {word}")
            # new_list2 = list(word)
            break
    """Code for Week"""
    res = []
    for i in str(words):
      if i.isdigit():
          res.append(i)

    """Code for Course Name"""
    string = str(words)
    start = "training', 'on', "
    end = ", 'The"
    start_index = string.index(start) + len(start)
    end_index = string.index(end)
    cropped_string = string[start_index:end_index].strip()
    course = ""
    for i in cropped_string:
      course+=i
    special_char = ["'",","]
    x= course.replace("'",'')
    normal_string = x
    for i in special_char:
      normal_string = normal_string.replace(i,"")

    """Attributes"""
    
    completion_date = word
    weeks = f"{res[0]}-weeks"
    course = normal_string

    
    return [name, completion_date, course]

    # l1=['Name','Date of Certification','Course Name']
    # l2=[name, word, course]

    # d1 = zip(l1,l2)
    # d2 = dict(d1)

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