status_code=$(curl --write-out %{http_code} --silent --output /dev/null http://127.0.0.1:5000/)

if [[ "$status_code" == 200 ]] ; then
    echo "Site status code $status_code"

    echo "Launching API localhost..."

    start "" chrome.exe --kiosk --fullscreen "http://127.0.0.1:5000/"

else
    echo "You need to run the './py.sh' or 'python main.py' first"
    echo "Closing.."
    exit 0
fi
