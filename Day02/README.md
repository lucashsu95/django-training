# Day02 建罝資料庫
create by: 2025/4/23


## 介紹
### 設定settings.py

在`INSTALLED_APPS`加入你剛剛新增的**網頁應用專案**(可能是web_app)
在`TEMPLATES`的`DIRS`加入你的路徑 範例:`os.path.join(BASE_DIR, 'web_app/templates')`

### models.py
class的UserData打完後下
```shell
python manage.py makemigrations web_app
python manage.py migrate
```

### register.html
`csrf_token`要放在`form`表單裡面

# Day03 Django表單教學

### models.py

- 公告
- 