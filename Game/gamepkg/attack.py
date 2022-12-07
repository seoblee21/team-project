    def attack(self):
        if self.user_input_j == '전사':
            print('\n공격 스킬은 3가지가 있습니다. 첫번째 스킬은 \'찌르기\' 두번째 스킬은 \'가로 베기\' 세번째 스킬은 \'난도질\' 입니다.')
            attack_style = input('\n어떻게 공격 하시겠습니까? 숫자로 입력하세요 (1 : 찌르기 , 2 : 가로 베기 , 3 : 난도질) = ')
            if int(attack_style) == 1:
                damage = 10
                self.Baek_kyung_hp -= 10
                print('\n-----백경이에게 {}만큼의 데미지가 들어갔습니다!, 백경이 hp {}-----'.format(damage, self.Baek_kyung_hp))
            elif int(attack_style) == 2:
                damage = 20
                self.Baek_kyung_hp -= 20
                print('\n-----백경이에게 {}만큼의 데미지가 들어갔습니다!, 백경이 hp {}-----'.format(damage, self.Baek_kyung_hp))
            elif int(attack_style) == 3:
                damage = 40
                self.Baek_kyung_hp -= 40
                print('\n-----백경이에게 {}만큼의 데미지가 들어갔습니다!, 백경이 hp {}-----'.format(damage, self.Baek_kyung_hp))
            elif int(attack_style) not in [1,2,3]:
                print('머뭇거리다 허공에 공격하셨습니다!')

        if self.user_input_j == '궁수': 
            print('\n공격 스킬은 3가지가 있습니다. 첫번째 스킬은 \'활로 내려찍기\' 두번째 스킬은 \'더블샷\' 세번째 스킬은 \'파이어샷\' 입니다.')
            attack_style = input('\n어떻게 공격 하시겠습니까? 숫자로 입력하세요 (1 : 활로 내려찍기 , 2 : 더블샷 , 3 : 난도질) = ')
            if attack_style == 1:
                damage = 5
                self.Baek_kyung_hp -= 5
                print('\n-----백경이에게 {}만큼의 데미지가 들어갔습니다!, 백경이 hp {}-----'.format(damage, self.Baek_kyung_hp))
            elif attack_style == 2:
                damage = 35
                self.Baek_kyung_hp -= 35
                print('\n-----백경이에게 {}만큼의 데미지가 들어갔습니다!, 백경이 hp {}-----'.format(damage, self.Baek_kyung_hp))
            elif attack_style == 3:
                damage = 30
                self.Baek_kyung_hp -= 30
                print('\n-----백경이에게 {}만큼의 데미지가 들어갔습니다!, 백경이 hp {}-----'.format(damage, self.Baek_kyung_hp))
            elif int(attack_style) not in [1,2,3]:
                print('머뭇거리다 허공에 공격하셨습니다!')

        if self.user_input_j == '마법사': 
            print('\n공격 스킬은 3가지가 있습니다. 첫번째 스킬은 \'지팡이로 내려찍기\' 두번째 스킬은 \'파이어볼\' 세번째 스킬은 \'아이스빔\' 입니다.')
            attack_style = input('\n어떻게 공격 하시겠습니까? 숫자로 입력하세요 (1 : 지팡이로 내려찍기 , 2 : 파이어볼 , 3 : 아이스빔) = ')
            if attack_style == 1:
                damage = 30
                self.Baek_kyung_hp -= 30
                print('\n-----백경이에게 {}만큼의 데미지가 들어갔습니다!, 백경이 hp {}-----'.format(damage, self.Baek_kyung_hp))
            elif attack_style == 2:
                damage = 20
                self.Baek_kyung_hp -= 20
                print('\n-----백경이에게 {}만큼의 데미지가 들어갔습니다!, 백경이 hp {}-----'.format(damage, self.Baek_kyung_hp))
            elif attack_style == 3:
                damage = 20
                self.Baek_kyung_hp -= 20
                print('\n-----백경이에게 {}만큼의 데미지가 들어갔습니다!, 백경이 hp {}-----'.format(damage, self.Baek_kyung_hp))
            elif int(attack_style) not in [1,2,3]:
                print('머뭇거리다 허공에 공격하셨습니다!')