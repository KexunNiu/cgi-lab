import os
import json

#Plain text
# print("Content-Type: text/plain\r\n")
# print(os.environ)

#JSON
# print("Content-Type: application/json\r\n")
# print(json.dumps(dict(os.environ), indent=2))

#Query_String
print("Content-Type: application/html\r\n")
print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")



