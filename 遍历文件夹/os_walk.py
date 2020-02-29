import os

for root, dirs, files in os.walk(r"E:\本科课件\专业课资料\信息检索\BayesSpam\data\test\Data", topdown=True):
	for name in files:
		#if name.endswith("mp4"):
			print(os.path.join(root, name))
			fileName = os.path.join(root, name)[-13:]
			print(fileName)
			a = open(r"E:\本科课件\专业课资料\信息检索\BayesSpam\data\test" + fileName)
			print(a)
#     for name in dirs:
#         print(os.path.join(root, name))