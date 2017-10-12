## Code Tutorial

This is a quick tutorial to highlight the tutorial page feature of Time2Code.  It is generated from MarkDown pages on GitHub.

I will do a few quick HTTP Request code examples you can try in a few languages.

### Golang

Select the Golang code language from the menu button on the bottom navbar.

![](https://raw.githubusercontent.com/JockDaRock/Time2Code/master/images/lang_sel.png)

Then enter the Code below in the **IDE** on the **right**.

```golang
package main

import (
	"fmt"
	"net/http"
	"io/ioutil"
)

func main() {

	url := "http://api.open-notify.org/iss-now.json"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("cache-control", "no-cache")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := ioutil.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```
Click the **RUN IT** button and watch as your code is executed quickly.

Click the **CLEAR TERM** button once you are done and Repeat the same steps as above for the NodeJS and Python examples.

**AND Dont forget to select the appropriate code langauge when running the different code snippets.**

### NodeJS

```node
var request = require("request");

var options = { method: 'GET',
  url: 'http://api.open-notify.org/iss-now.json',
  headers: { 'cache-control': 'no-cache' } };

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
```

### Python


```python
import requests

url = "http://api.open-notify.org/iss-now.json"

r = requests.get(url)

print(r.text)
```
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
