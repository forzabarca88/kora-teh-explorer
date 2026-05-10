git pull; git checkout -f main

uv run ./main.py

git add *.md; git commit -m "updated by Kora"

# Construct the URL with credentials
#$RemoteUrl = "https://forzabarca88:$($Env:GITHUB_TOKEN)@github.com/forzabarca88/kora-teh-explorer.git"

git push