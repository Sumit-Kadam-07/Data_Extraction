import pandas as pd

def extract_coretechtive(ocr_result):
    """Code for Name"""
    name=""
    string = ocr_result
    start = "that "
    end = " has"
    start_index = string.index(start) + len(start)
    end_index = string.index(end)
    cropped_string = string[start_index:end_index].strip()
    name=""
    for i in cropped_string:
      name+=i
    # print("Name:",name)
    """Code for Date"""
    date_=""
    for i in ocr_result:
      date_+=i
      if i=="\n":
        break
    date_ = date_.strip()
    # print("Date: ",date_)

    words = date_.split()

    # print("words: ",words[-1])
    # """Code for Week"""
    # res = []
    # for i in str(words):
    #   if i.isdigit():
    #       res.append(i)

    # """Code for Course Name"""
    string = str(ocr_result)
    start = "Completed "
    end = " Training"
    start_index = string.index(start) + len(start)
    end_index = string.index(end)
    cropped_string = string[start_index:end_index].strip()
    course = ""
    for i in cropped_string:
      course+=i
    special_char = ["'",",","\n"]
    x= course.replace("'",'')
    normal_string = x
    for i in special_char:
      normal_string = normal_string.replace(i," ")
    # print("Normal String: ",normal_string)

    """Attributes"""
    # fname = list(name)
    # certificate = list(word)
    course = normal_string

    return [name, words[-1], course]

    # l1=['Name','Date of Certification','Course Name']
    # l2=[name, words[-1], course]

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