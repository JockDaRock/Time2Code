# Time2Code
A portable, scalable web based code editor to integrate into your code learning experiences.

The goal is to make deploying your own web based code editor easier and more fun.

![](/images/code_gif.gif)

## Tech Overview
* The Code execution backend is built off of the serverless [FaaS](http://docs.get-faas.com/) Framework for scalability and ability to support many languages.  Support for [k8s](https://kubernetes.io/) is ready through [faas-netes](https://github.com/alexellis/faas-netes) and appears to be working well.

* UI Modelled after the wonderful [Play-with-Moby Site](http://play-with-moby.com) and the wonderful work the guys at [Play-With-Docker](https://github.com/play-with-docker/play-with-docker) do to make our Docker Learning Experiences Better.

* Function handling and code execution are being handled by Python processes.  Python handles the STDIN of all of the function requests and then passes it to the desired language for interpretation and execution or compilation and execution.

* Web site is being driven by the [Flask](http://flask.pocoo.org/) Framework as a Swarm service.

* Code editor is built from [Ace Editor](https://ace.c9.io/) project.

* Terminal is built from [XTermJS](https://xtermjs.org/).

## Up and Running

### Docker Swarm

The following snippet will initialize your swarm, Time2Code, FaaS and Time2code functions.

```sh
$ docker swarm init --advertise-addr eth0 && \
  git clone https://github.com/JockDaRock/Time2Code && \
  cd Time2Code && \
  bash time2deploy.sh && \
  docker service ls
```

If you are on your laptop navigate to http://127.0.0.1:5555 and start coding.

### Play-with-Docker

[![Try in PWD](https://cdn.rawgit.com/play-with-docker/stacks/cff22438/assets/images/button.png)](http://play-with-docker.com?stack=https://raw.githubusercontent.com/JockDaRock/Time2Code/master/time2code-swarm-deploy.yml&stack_name=time2code)

Click the **Try in PWD** and get started with Time2Code quickly.  Once your PWD instance is up and running click on the 5555 tag and start coding.

![](/images/PWD-5555.png)



### Kubernetes (minikube)

You will need to have [minikube installed](https://kubernetes.io/docs/tasks/tools/install-minikube/) before you begin.

Type the following snippets will get minikube started and faas-netes loaded into the kube cluster.

`$ git clone https://github.com/JockDaRock/Time2Code`

`$ minikube start` or `$ minikube start --vm-driver=xhyve`

Then run the following bash script to load FaaS and Time2Code...

`$ bash ./minikube.sh'

Once the script is complete it will provide you with the url, like this http://192.168.99.100:31114/, to reach the Time2Code web editor.  **BEFORE** you start using it, you will need to deploy the code execution functions after the FaaS services have started.  It might take a minute or two for all of the necessary Kube pods to be Running.  Keep checking the pods with `kubectl get pods`.  

To deploy the functions use the following command in your terminal.

`$ faas-cli -action deploy -f ./time2code-faas-cli-minikube.yml`

Once the kube pods for the code execution are running you can get to coding :)!

![](images/python_sample0.png)

## Latest News

[Time2Code: Functions as Service and Code as a Function](https://medium.com/@JockDaRock/time2code-functions-as-service-and-code-as-a-function-3d9125fc49fb)



## Coding Languages Currently Supported

* Python, Golang, Powershell, NodeJS, ... more coming very soon.

* Currently working on... I am currently working C# code execution. Most of my tests are running well, but need to iron out some necessary dependencies and other issues.

#### Repos for language specific code execution handlers
* [Python](https://github.com/JockDaRock/Time2Py)
* [Golang](https://github.com/JockDaRock/Time2Go)
* [NodeJS](https://github.com/JockDaRock/Time2NodeJS)
* [Powershell](https://github.com/JockDaRock/Time2Powershell)
* [C#](https://github.com/JockDaRock/Time2CSharp)


## Roadmap and Contributing

Currently in progress:

* Adding markdown and instruction functionality to accompany code execution. - check and check

* Add language dependency builder for code execution functions.

* Kubernetes Support - check and check

Time2Code is written mostly in HTML and Javascript on the FrontEnd, Python and Flask to handle the WebIDE pages, and Python on the backend to handle code language execution on the OpenFaaS framework. This project is MIT licensed - contributions are welcomed whether that means providing feedback, testing existing and new features or hacking on the source. This project is still in early stages so I need to people to generally try functionality and provide feedback. I need help building new code execution handlers for different languages or suggestions for languages to add. I also need help reducing the image sizes for the Microsoft languages handlers ([Powershell](https://github.com/JockDaRock/Time2Powershell) and [C#](https://github.com/JockDaRock/Time2CSharp)).

