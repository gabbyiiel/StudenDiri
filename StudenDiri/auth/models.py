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
        
    @staticmethod
    def signup(username,idnumber, firstname, lastname, email, course, college, password, gender,):
        cur = mysql.connection.cursor()
        
        try:
            cur.execute(f""" INSERT INTO users
                        (`userID`,`username`, `idnumber`, `firstname`, `lastname`, `email`, `college`, `course`, `password`, 'gender') 
                        VALUES (5,'{username}','{idnumber}','{firstname}','{lastname}','{email}','{college}','{course}','{password}','{gender}')
                        """)
            mysql.connection.commit()
            return print('Hatdog')
        except Exception as e:
            print(e)    