# noka.moe
just url implementation

# how to install???
clone the repo.  
rename data.example.json to data.json  
create a file direcoty.  
add file to the files directory.  
edit data.json
build and run the Dockerfile.

## data.json
```
{
    "justurl": { # this is "example.com/justurl"
        "redirect": "example.net" # redirect to example.net
        # you can use only one option.
    },
    "justfile": {
        "path": "test.html" # files/test.html
    }
}
```

## update
pull the repo.

## use
example.com/url?download=false  
no download  
you can use this option to static file deploy.
example.com/url?download=true  
download file. default

# License
Source Code is LICENSE

Image is static/image/LICENSE