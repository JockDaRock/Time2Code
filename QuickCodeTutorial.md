## Code Tutorial

This is a quick tutorial to highlight the tutorial page feature of Time2Code.  It is generated from MarkDown pages on GitHub.

I will do a few quick HTTP Request code examples you can try in a few languages.

If you are viewing this on GitHub you will need to get Time2Code started before you can do anything else.

First click the **Try in PWD** Button.

[![Try in PWD](https://cdn.rawgit.com/play-with-docker/stacks/cff22438/assets/images/button.png)](http://play-with-docker.com?stack=https://raw.githubusercontent.com/JockDaRock/Time2Code/master/time2code-swarm-deploy.yml&stack_name=time2code)

Once Time2Code is started up click the 5555 tab at the top of the Play-With-Docker site.

![](https://raw.githubusercontent.com/JockDaRock/Time2Code/master/images/PWD-5555.png)

Add `/tutorial?tut=https://github.com/JockDaRock/Time2Code/blob/master/QuickCodeTutorial.md` to the URL in the browser.

Continue with the instructions below...

### Golang

Select the Golang code language from the menu button on the bottom navbar.

![](https://raw.githubusercontent.com/JockDaRock/Time2Code/master/images/lang_sel.png)

Then enter the Code below in the **IDE** on the **right**.

```Golang
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

Repeat the same steps as above for the NodeJS and Python examples.

**AND Dont forget to select the appropriate code langauge when running the different code snippets.

### NodeJS

```NodeJS
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


```Python
import requests

url = "http://api.open-notify.org/iss-now.json"

r = requests.get(url)

print(r.text)
```