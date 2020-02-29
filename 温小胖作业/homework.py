while True:   #整个文件是一个死循环，当达到退出条件时退出循环
	edge1 = float(input("please input the first edg:")) #输入第一条边
	edge2 = float(input("please input the second edg:"))#输入第二条边
	edge3 = float(input("please input the third edg:"))#输入第三条边



	if edge1+edge2>edge3 and edge1+edge3>edge2 and edge2+edge3>edge1: #如果 a+b>c并且b+c>a并且 a+c>b，说明可以构成三角形，执行计算周长面积的语句
		perimeter = edge1+edge2+s-edge3                               #计算周长的语句
		s = perimeter/2                                               #中间变量，就是记一下周长的一半，公式要用
		area = (s*(s-edge1)*(s-edge2)*(s-edge3)) ** 0.5	              #计算面积的语句
		print 'This is a triangle!\n\nArea is '+str(area)+'\n\nPerimeter is ' + str(perimeter) #打印周长面积
		a = input('Exit or Reset(0/1):')                              #输入0/1，如果输入0，退出程序，如果输入1，重新再输入一次
		if a == 0 or a == 0:                                          #如果0
			break                                                     #退出大循环的条件，强行退出循环
		elif a == 1 or a == 1:                                        #如果1
			continue                                                  #结束本轮循环，进入下一轮循环
		else:
			print 'unexpected input! Exiting...'                      #如果输入的又不是0又不是1，输入出错，直接退出  
			break                                                     #强行退出循环
	
	else:                                                             #不满足构成三角形三条边的情况
		print 'This is not a triangle!Please input again!'            #打印提示信息
		                                                        #本轮循环结束，回到第一行继续循环
