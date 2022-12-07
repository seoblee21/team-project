@staticmethod
   def check_player(user_job) : 
       if user_job in Baek_kyung.job:
          return True
       else:
           return False

@classmethod
   def make_player(cls, user_job) :
      return cls(user_job)