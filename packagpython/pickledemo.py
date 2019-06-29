import pickle

arr = ['x', 'y', 'z']
fp = open("pickle1", "wb")
pickle.dump(arr, fp)
print("Data Saved")
fp.close()

fp1 = open("pickle1", "rb")
x = pickle.load(fp1)
print(x)
fp1.close()