# Time2Code
A portable scaleable web code editor to integrate into your sites and learning experiences.

##Tech Overview
* The Code execution backend is built off of the serverless [FaaS](http://docs.get-faas.com/) Framework for scalability and ability to support many languages.  Although support for [k8s](https://kubernetes.io/) is currently being tested on [faas-netes](https://github.com/alexellis/faas-netes) and this project and appears to be fairly successful, currently primary support is on Docker Swarm.

* Web site is being driven by the [Flask](http://flask.pocoo.org/) Framework as a Swarm service.

* Code editor is built from [Ace Editor](https://ace.c9.io/) project.

* Terminal is built from [XTermJS](https://xtermjs.org/).

## Up and Running


