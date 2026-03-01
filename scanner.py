import requests

# Define variables
my_url = "http://10.10.230.135"
dir_list = "common.txt"

# Status code meanings
status_meaning = {
    200: "OK (Page exists)",
    301: "Moved Permanently (Redirect)",
    302: "Found (Temporary redirect)",
    403: "Forbidden (Exists but no access)"
}

# Create list of full urls
full_urls = []
dir_content = open(dir_list, 'r')

for directory in dir_content:
    url = my_url + "/" + directory.strip()
    full_urls.append(url)

dir_content.close()

# Send get requests to urls
print("Started scanning...\n")

for url in full_urls:
    try:
        url_request = requests.get(url, timeout=3)
        code = url_request.status_code

        if code in status_meaning:
            print("Found:", url)
            print("Status:", code, "-", status_meaning[code])
            print()

    except:
        print("Error accessing:", url)

print("\nScan completed!")
