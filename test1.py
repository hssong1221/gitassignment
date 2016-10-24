"""
==========================
Descroption here
==========================

 * Author : Song hyun soo
 * Created : rock scissors paper program
 * version : 1.0 
"""
# **랜덤함수를 사용하기위해 import**

import random

 
# **반복문을 위한 변수 i**

i = 0;

# **가위바위보를 10번 반복하는 반복문(1. 가위 2. 바위 3. 보)**

while(i < 10):
	print("가위(1), 바위(2), 보(3)를 입력하세요. ")
	my_finger = int(input())
	com_finger = random.randint(0,2)

	# **내가 가위를 냈을때 컴퓨터와의 승패계산**

	if(my_finger == 1):
		if(com_finger == 1):
			print("컴퓨터가 낸 것은 가위입니다.")
			print(" -----> 비김~!\n")
		elif(com_finger == 2):
			print("컴퓨터가 낸 것은 바위입니다.")
			print(" -----> 컴퓨터 승\n")
		else:
			print("컴퓨터가 낸 것은 보입니다.");
			print(" -----> 사용자 승\n");

	# **내가 바위를 냈을때 컴퓨터와의 승패계산**

	elif(my_finger == 2):
		if(com_finger == 1):
			print("컴퓨터가 낸 것은 가위입니다.");
			print(" -----> 사용자 승\n");
		elif(com_finger == 2):
			print("컴퓨터가 낸 것은 바위입니다.");
			print(" -----> 비김~!\n");
		else:
			print("컴퓨터가 낸 것은 보입니다.");
			print(" -----> 컴퓨터 승\n");

	# **내가 보를 냈을때 컴퓨터와의 승패계산**

	else:
		if(com_finger == 1):
			print("컴퓨터가 낸 것은 가위입니다.");
			print(" -----> 컴퓨터 승\n");
		elif(com_finger == 2):
			print("컴퓨터가 낸 것은 바위입니다.");
			print(" -----> 사용자 승\n");
		else:
			print("컴퓨터가 낸 것은 보입니다.");
			print(" -----> 비김~!\n");

	# **반복문을 끝내기 위한 조건**

	i = i + 1


