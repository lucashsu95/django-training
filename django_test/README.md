1.安裝django，輸入"pip install django"

2.輸入"python -m django" #列出dajngo功能 (可跳過)

3.輸入"python -m django startproject 「名字」" 建立主專案

4.終端機到專案資料夾，輸入"python -m django startapp 「名字」"建立子網頁專案

5.到"setting.py"，在"INSTALLED_APPS"新增已建立的子網頁專案的名稱

6.輸入"python manage.py runserver"啟動專案

7.建立templates資料夾，存放html

8.在"setting.py"裡的"TEMPLATES"的"DIRS"增加路徑"os.path.join(BASE_DIR, 'web_app/templates'.replace("\\", "/"))"

9.model 建立資料表

*10.設定完資料表輸入"python manage.py makemigrations" 設定資料表，"python manage.py migrate" 同步資料表同步資料表