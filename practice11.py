#pickle
import pickle
profile_file = open("profile.pickle", "wb")
profile={"이름:박명수"}
print(profile)
pickle.dump(profile, profile_file)
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

