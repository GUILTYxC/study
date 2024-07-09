import openpyxl
import pymysql

# 连接到数据库
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',
                             database='myxuexi',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # 准备插入数据的SQL语句
        sql = """
            INSERT INTO cet6data (year, section_type, text_content, question_1, answer_1, question_2, answer_2, question_3, answer_3, question_4, answer_4, question_5, answer_5, question_6, answer_6, question_7, answer_7, question_8, answer_8, question_9, answer_9, question_10, answer_10, question_11, answer_11, question_12, answer_12, question_13, answer_13, question_14, answer_14, question_15, answer_15, question_16, answer_16, question_17, answer_17, question_18, answer_18, question_19, answer_19, question_20, answer_20)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # 加载Excel文件
        workbook = openpyxl.load_workbook('cet6.xlsx')
        sheet = workbook.active

        # 遍历Excel文件中的每一行
        for row in sheet.iter_rows(min_row=2, values_only=True):
            # 将 row 转换为列表，并截断或填充到 43 个元素
            processed_row = list(row)[:43] + [None] * (43 - len(row))

            # 确保处理后的行有 43 个元素
            if len(processed_row) == 43:
                cursor.execute(sql, processed_row)
            else:
                print(f"处理后的行有 {len(processed_row)} 个元素，预期为 43: {processed_row}")

        # 提交事务
        connection.commit()

except Exception as e:
    print(f"错误: {e}")
    connection.rollback()  # 回滚事务

finally:
    connection.close()
