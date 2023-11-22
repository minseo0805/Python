#with

import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))


with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬")

with open("study.txt", "r", encoding="utf-8") as study_file:
    print(study_file.read())
    
