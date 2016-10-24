import random

i = 0;

while(i < 10):
	print("가위(1), 바위(2), 보(3)를 입력하세요. ")
	my_finger = int(input())
	com_finger = random.randint(0,2)


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

	i = i + 1


