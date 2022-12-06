### THIS IS WHERE YOU MANIPULATE USER DATA IN THE DATABASE ###


from StudenDiri import mysql

class UserRepo:
    @staticmethod
    def login(username, password):
        cur = mysql.connection.cursor()
        
        try:
            cur.execute(f"""
                        SELECT * FROM users
                        WHERE username = '{username}'
                        """)
            user = cur.fetchone()
            print(user)
        
        except Exception as e:
            return {
                'code' : -1,
                'message' : f'{e}'
            }
            
        # if user:
        #     password = 