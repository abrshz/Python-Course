# def format_name(fname , lname):
#     print(fname.title())
#     print(lname.title())


# format_name("mike", "abrsh")

# Leap year formula 
# def is_leap_year(year):
#     # Write your code here. 
#     # Don't change the function name.

    
#       if year % 4 == 0:
#          if year % 100 == 0:
#              if year % 400 == 0:
#                 return True
#              else: 
#                  return False
#          else:
#              return True
#       else: 
#           return False
        

def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)  

def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))





# Three create database tables 
# CREATE TABLE users(
#      userid INT(20) NOT NULL AUTO_INCREMENT,
#      username VARCHAR(20) NOT NULL,
#      firstname VARCHAR(20) NOT NULL,
#      lastname VARCHAR(20) NOT NULL,
#      email VARCHAR(40) NOT NULL,
#      password VARCHAR(100) NOT NULL,
#      PRIMARY KEY(userid) 
#  );
 
#  CREATE TABLE questions(
#      id INT(20) NOT NULL AUTO_INCREMENT,
#      questionid VARCHAR(100) NOT NULL UNIQUE,
#      userid INT(20) NOT NULL,
#      title VARCHAR(50) NOT NULL,
#      description VARCHAR(200) NOT NULL,
#      tag VARCHAR(20),
#      PRIMARY KEY(id , questionid),
#      FOREIGN KEY(userid) REFERENCES users(userid)
#  );
 
#  CREATE TABLE answers(
#      answerid INT(20) NOT NULL AUTO_INCREMENT,
#      userid INT(20) NOT NULL,
#      questionid VARCHAR(100) NOT NULL,
#      answer VARCHAR(200) NOT NULL,
#      PRIMARY KEY(answerid),
#      FOREIGN KEY(questionid) REFERENCES questions(questionid),
#      FOREIGN KEY(userid) REFERENCES users(userid)
#  );

    
            