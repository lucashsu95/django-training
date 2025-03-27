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
