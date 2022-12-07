user_job = input('직업을 선택하세요 = ')

while True:
    if Baek_kyung.check_player(user_job) : 
        user = Baek_kyung.make_player(user_job)
        user.game_play()
        if user.user_hp <= 0:
           print('\n------ 패배 ------')
           break    
        elif user.Baek_kyung_hp <= 0:
             print('\n------ 승리! ------')
             break
    else:
        user_job = input('제대로 입력하세요 = ')