def game_play(self) :

        Baek_kyung_a_skill = [1,2,3] 
        Baek_kyung_d_skill = [1,2,3] 

        self.game_difficulty()

        while True:
           
            Baek_kyung_attack = rd.choice(Baek_kyung_a_skill) 
            if Baek_kyung_attack == 1:
                print('\n 백경이가 물을 뿜으려고 합니다. 어떻게 하시겠습니까?')
                self.defense()
                user_d = self.defense()
                if self.defense() == 1:
                    print('\n 백경이의 공격을 피하셨습니다!')
                    break
                else:
                    self.user_hp -= 10
                    print('\n 백경이에게 공격 받았습니다!, 유저 hp {}'.format(self.user_hp))
                    break
            elif Baek_kyung_attack == 2:
                print('\n 백경이가 꼬리를 흔들고 있습니다. 어떻게 하시겠습니까?')
                self.defense()
                if self.defense() == 2:
                    print('\n 백경이의 공격을 피하셨습니다!')
                else:
                    self.user_hp -= 20
                    print('\n 백경이에게 공격 받았습니다!, 유저 hp {}'.format(self.user_hp))
            else:
                print('\n 백경이가 달려들 준비를 하고 있습니다. 어떻게 하시겠습니까?')
                self.defense()
                if self.defense() == 3:
                    print('\n 백경이의 공격을 피하셨습니다!')
                else:
                    self.user_hp -= 30
                    print('\n 백경이에게 공격 받았습니다!, 유저 hp {}'.format(self.user_hp))

        
            Baek_kyung_defense = rd.choice(Baek_kyung_d_skill) 
            if Baek_kyung_defense == 1:
                print()
            elif Baek_kyung_defense == 2:
                print()
            else:
                print()
            user.attack()
            if self.user_hp == 0:
               print('패배')
               break    
            elif self.Baek_kyung_hp == 0:
                print('승리')
                break
            else:
                continue