def game_difficulty(self) : 
        input_game_difficulty = input('\n게임 난이도를 숫자로 설정해주세요 (1 : 애기 백경이 , 2 : 사춘기 백경이 , 3 : 전투병기 백경이) = ')
        while input_game_difficulty.isdigit() == False : 
            input_game_difficulty = input('\n숫자로 입력해주세요 = ')
        while int(input_game_difficulty) not in [1,2,3]:
            input_game_difficulty = input('\n똑바로 입력하세요 = ')

        if int(input_game_difficulty) == 1 : 
            print('\n애기 백경이 모드를 선택하셨습니다.')
            self.Baek_kyung_hp = 120
            self.Baek_kyung_dam = 15

        elif int(input_game_difficulty) == 2 :
            print('\n사춘기 백경이 모드를 선택하셨습니다.')
            self.Baek_kyung_hp = 200
            self.Baek_kyung_dam = 20

        else: 
            print('\n전투병기 백경이 모드를 선택하셨습니다.')
            self.Baek_kyung_hp = 360
            self.Baek_kyung_dam = 40
