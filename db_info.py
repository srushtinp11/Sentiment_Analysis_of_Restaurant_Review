# import pymysql
# conn=pymysql.connect(user='root',password='root',host='localhost')
# qur='create database rest_review_db'
# mycur=conn.cursor()
# mycur.execute(qur)
# mycur.close()
# conn.close()


#create table
# import pymysql
# conn=pymysql.connect(user='root',password='root',host='localhost',
#                              database='rest_review_db')
# qur=('create table food_data(food VARCHAR(40) PRIMARY KEY,good_review INT,'
#      'bad_review INT,customer INT)')
# mycur=conn.cursor()
# mycur.execute(qur)
# mycur.close()
# conn.close()


# insert food
# foods = ["Idly", "Dosa", "Vada", "Roti", "Meals", "Veg Biryani",
#          "Egg Biryani", "Chicken Biryani", "Mutton Biryani",
#          "Ice Cream", "Noodles", "Manchooriya", "Orange juice",
#          "Apple Juice", "Pineapple juice", "Banana juice"]

# import pymysql
# for i in foods:
#     conn = pymysql.connect(user='root', password='root', host='localhost',
#                                    database='rest_review_db')
#     qur = f'INSERT INTO food_data VALUES("{i}",{0},{0},{0})'
#     mycur = conn.cursor()
#     mycur.execute(qur)
#     conn.commit()
#     mycur.close()
#     conn.close()