password = 'a123456'
i=1 #第幾次輸入密碼
while i<4:
	password1 = input('請輸入密碼:')
	if password1 == password:
		print('登入成功!')
		break
	else:
		print('密碼錯誤!,你還有', 3-i ,'次機會。')
		i = i+1
