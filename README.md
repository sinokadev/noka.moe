# noka.moe
just url implementation

Korean: [README_KO.md](README_KO.md)

## Install and Serve

### Requirements
 - Docker

### Steps
1. Clone the repository
```
git clone https://github.com/yourname/your-repo.git
cd your-repo
```

2. Rename the example config file
```
mv data.example.json data.json
```

3. Create the files directory
```
mkdir files
```

4. Add files to the files directory
```
files/
  └─ your_program.exe
```

5. Edit data.json to configure routes
```
{
    "myprogram": {
        "path": "your_program.exe"
    }
}
```

6. Build and run the Docker container:
```
docker build -t justurl .
docker run -p 8080:8080 justurl
```


## data.json emample
```json
{
  "justurl": {
    // This URL will be available at: https://example.com/justurl
    // Redirects the user to an external site
    "redirect": "example.net",

    // Optional: Custom Discord embed (Open Graph)
    // If omitted, Discord will use the destination's own embed
    "embed": {
      "title": "Example Website",
      "description": "You will be redirected to example.net",
      "image": "https://example.com/static/example.png"
    }
  },

  "justfile": {
    // This URL will be available at: https://example.com/justfile
    // Serves a file from BASE_PATH
    "path": "test.html",

    // Custom embeds are NOT supported for file routes.
  }
}

```

## Update

To update the application to the latest version.

1. Pull the repo
```
git pull origin main
```

2. Restart the Docker container.

## Usage
 - Disable download (serve file inline):
https://example.com/url?download=false

 - Force download (default behavior):
https://example.com/url?download=true

 - Redirect routes: The `download` parameter is ignored.

# License
Source Code is LICENSE

Image is static/image/LICENSE