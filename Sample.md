# Play with Code

## Random instructions

Stick this code in the right panel.

```python
import requests

url = "https://httpbin.org/get"

r = requests.get(url)

print(r.status_code)
print(r.headers)
print(r.text)
```