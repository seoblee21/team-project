def defense(self):  
    print('\n방어 스킬은 3가지가 있습니다. 첫번째 스킬은 \'고개 숙이기\' 두번째 스킬은 \'옆으로 구르기\' 세번째 스킬은 \'점프\' 입니다.')
    user_input_d = input('\n어떻게 방어 하시겠습니까? (1 : 고개 숙이기 , 2 : 옆으로 구르기 , 3 : 점프) = ')

    if int(user_input_d) not in [1,2,3]:
      self.user_hp -= 50
      print('\n방어 스킬을 고르지 못하고 머뭇거리다 백경이에게 치명타를 당했습니다! 유저 hp {}'.format(self.user_hp))
            

    elif user_input_d.isdigit() == False:
      user_input_d = input('\n숫자로 입력하세요 = ')

    self.user_input_d = user_input_d