# Check for a env file
$envPath = "./.env"
if (!(Test-Path -Path $envPath)){
  Write-Warning "ENV file not found, please refer to the README for how to get and include this item."
}
else {
    # Start and enter the Virtual Environment
    python -m venv venv
    ./venv/bin/activate

    # Install dependencies
    pip install -r requirements.txt
}

