# noka.moe
just url 구현체입니다. 작동하지만, 표준이 변경될 가능성이 높습니다. **하위 호환을 지원하지 않으므로 업데이트 시 리드미를 다시 읽어주세요.**

## 설치와 배포

### 필요한것
 - Docker

### 따라하기
1. 레포지토리를 클론하세요.
```
git clone https://github.com/sinokadev/noka.moe
cd justurl
```

2. `data.example.json`를 `data.json`으로 이름을 변경하세요.
```
mv data.example.json data.json
```

3. `files` 디렉토리를 만드세요.
```
mkdir files
```

4. `files` 디렉토리에 파일을 추가하세요.
```
files/
  └─ your_program.exe
```

5. `data.json`을 알맞게 수정하세요.
```
{
    "myprogram": {
        "path": "your_program.exe"
    }
}
```

6. 빌드하고, 실행하세요.
```
docker build -t justurl .
docker run -p 8080:8080 justurl
```


## data.json 예시
```json
{ // 우리가 호스팅하는 도메인은 example.com이라고 가정합니다.
  "justurl": {
    // example.com/justurl을 방문했을때 example.net으로 리디렉션합니다.
    "redirect": "example.net",

    // 선택: 디스코드 임베드
    // 이 옵션이 있다면 디스코드에서 https://example.com/justurl를 업로드했을때 사용자 지정 임베드가 표시됩니다.
    "embed": {
      "title": "Example Website",
      "description": "You will be redirected to example.net",
      "image": "https://example.com/static/example.png"
    }
  },

  "justfile": {
    // https://example.com/justfile를 방문했을때 files/test.html이 제공됩니다.
    // https://example.com/justfile?download=false를 제공하는 식으로 정적 웹사이트 배포가 가능합니다.
    "path": "test.html",

    // 파일 라우트에서는 커스텀 임베드가 지원되지 않습니다. 원한다면 html 파일에 직접 추가하세요.
  }
}

```

## 업데이트

최신 버전으로 업데이트 하는 방법은 다음과 같습니다.

1. 레포지토리를 pull합니다.
```
git pull origin main
```

2. 도커 컨테이너를 재시작합니다.

## Usage
 - 다운로드 끄기:
https://example.com/url?download=false

 - 모든 파일을 다운로드 시키기 (기본 옵션):
https://example.com/url?download=true

 - 리디렉션 라우트: `download` 파라미터는 적용되지 않습니다.
 - 모든 리디렉션과 파일 목록: https://example.com/index (따라서 index라는 라우팅 이름을 작동하지 않습니다.)

# 라이선스
소스코드는 LICENSE 파일에 따라 제공됩니다.

이미지의 라이선스는 static/image/LICENSE를 참고하세요.