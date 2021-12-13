import time
import os
import shutil
import mysql.connector

def createFile():
    i = 0

    while True:
        i += 1
        filename = "test" + str(i) + ".txt"
        filepath = "Processing/" + filename
        with open(filepath, "w") as file:
            time.sleep(1)

def moveFile():
    # Specify the path for Processing folder
    for files in os.listdir("~/Desktop/AdarshAssnML/Processing"):
        shutil.move(os.path.join("~/Desktop/AdarshAssnML/Processing", files), "~/Desktop/AdarshAssnML/queue")
    time.sleep(5)

def AddToDataBase(data):
    # establishing the connection
    conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='mydb')
    cursor = conn.cursor()

    insert_statement = (
        "INSERT INTO FILETABLE(FILENAME, VALUE)"
        "VALUES (%s, %s)"
    )

    try:
        cursor.execute(insert_statement, data)
        conn.commit()
    except:
        conn.rollback()


if __name__ == "__main__":
    createFile()
    moveFile()

    for files in os.listdir("~/Desktop/AdarshAssnML/queue"):
        data = (files, '1')
        AddToDataBase(data)
        shutil.move(os.path.join("~/Desktop/AdarshAssnML/queue", files), "~/Desktop/AdarshAssnML/processed")

