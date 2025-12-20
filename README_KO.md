# noka.moe
just url 구현체

# 설치
레포를 클론.   
data.example.json을 data.json으로 바꾸세요  
files 폴더 만드세요.  
아무 파일이나 위에서 만든 폴더에 넣으세요  
data.json 항목에 따라 data.json을 수정하세요  
Dockerfile 실행 ㄱㄱ.

## data.json
```
{
    "justurl": { # "example.com/justurl"를 의미
        "redirect": "example.net" # example.net로 리디렉트함
        # path 또는 redirect 하나만 넣으세요. 짜피 하나만 작동함.
    },
    "justfile": {
        "path": "test.html" # files/test.html
    }
}
```

## update
레포 pull하면 업뎃됩니다.

## use
example.com/url?download=false  
다운로드 안돼요 
이거 써서 스태틱 파일정도는 배포 가능 ㅇㅇ
example.com/url?download=true  
파일이 다운로드됩니다. html이든 뭐든 일단 다운로드시킴. 옵션 지정 안하면 이걸로 작동함

# License
Source Code is LICENSE

Image is static/image/LICENSE