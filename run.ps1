# Set error action to silently continue to avoid error formatting
$ErrorActionPreference = 'SilentlyContinue'

# Create logs directory if it doesn't exist
$logDir = Join-Path (Get-Location) "logs"
if (-not (Test-Path $logDir)) {
    New-Item -ItemType Directory -Path $logDir | Out-Null
}

# Generate timestamped log file name
$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$logFile = Join-Path $logDir "kora_$timestamp.log"

# Run all commands and redirect output to log file (both stdout and stderr as text)
git pull; git checkout -f main 2>&1 | Out-String -Stream | Tee-Object -FilePath $logFile -Append

uv run ./main.py 2>&1 | Out-String -Stream | Tee-Object -FilePath $logFile -Append

git add *.md; git commit -m "updated by Kora" 2>&1 | Out-String -Stream | Tee-Object -FilePath $logFile -Append

# Construct the URL with credentials
#$RemoteUrl = "https://forzabarca88:$($Env:GITHUB_TOKEN)@github.com/forzabarca88/kora-teh-explorer.git"

git push 2>&1 | Out-String -Stream | Tee-Object -FilePath $logFile -Append

Write-Host "Log saved to: $logFile"