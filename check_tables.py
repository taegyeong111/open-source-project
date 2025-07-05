import sqlite3

conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

print("🔍 테이블 이름들 중 'auth_user__old' 유사한 거 찾기...")
cursor.execute("SELECT name, sql FROM sqlite_master WHERE sql LIKE '%auth_user__old%';")
rows = cursor.fetchall()

for row in rows:
    print(f"\n📄 Table: {row[0]}")
    print(row[1])

conn.close()