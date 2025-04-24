# Django Day1

## 初始化專案
```bash
python -m django startproject <name>
```

## 新增網頁應用專案
```bash
python -m django startapp <name>
```

## How to Run
```bash
python manage.py runserver
```

## 介紹

### urls.py
`urls.py`就是路由，`path(路徑, 你的視圖函數(通常放在views裡)`

### 設定 settings.py

在`INSTALLED_APPS`加入你剛剛新增的**網頁應用專案**(可能是web_app)
在`TEMPLATES`的`DIRS`加入你的路徑 範例:`os.path.join(BASE_DIR, 'templates')`

### 設定 tempaltes

#### lang mode
用vscode打html的格式可能是Django HTML這樣會沒有提示，要記得改成HTML。

接下來就會發現你每次新增一個html檔案就要改一次lang mode 所以可以直接在設定檔裡`settings.json`
```json
"files.associations": {
    "*.html": "html"
}
```

#### 設定路徑
`setting.py`裡的`TEMPLATES` -> `DIRS` <br>然後在裡面打`os.path.join(BASE_DIR,'templates')` ~~記得import os~~
