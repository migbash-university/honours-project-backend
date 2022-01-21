![image](https://user-images.githubusercontent.com/20924663/149317090-2482101c-87f2-4fdc-aecc-80e088b66f30.png)

---

## Description

This is an Edinburgh Napier University Honours Project for (BSc.) Computer Science Degree. 

This Honours Project revolves around Conversational A.I. Agents to be used in the Educational System for the correct interaction with humans to pass across knowledge. However, due to the lack of existing real-world literature and research on `multi-modal` learning approaches, such as: visual - audio and interactive charts methods of learning, this honours project aims to understand the imapct of the use of a Conversational A.I. Agent to pass across knowledge to the user on a scientific topic and companre it with standard and more common methods of learning.

This repository is only half-of the project. It focuses on the development of the `conversational AI` agent and the outline of its development. The `UI/UX` in a web-app format can be accessed on the following link -> [insert-link-here] and for the open-source code for it can be found here -> [insert-link-here]

### Project Graph [ChatBot]

[insert-project-chart-here]

## 🚀 Get Started

**Guides**

Getting started as another video or alternative(s):

- [guide-1](https://www.machinelearningplus.com/nlp/chatbot-with-rasa-and-spacy/)
- [guide-2](https://towardsdatascience.com/create-chatbot-using-rasa-part-1-67f68e89ddad)
- [guide-3](https://medium.com/co-learning-lounge/step-by-step-guide-to-install-rasa-x-in-windows-without-docker-85da8502bce)
- [guide-4](https://medium.com/analytics-vidhya/deploying-rasa-chatbot-on-heroku-using-docker-7199bf16c219)

- ⭐ [v-guide-2](https://www.youtube.com/watch?v=Nk9K4s8g9yQ)
- ⭐ [v-guide-3](https://www.youtube.com/watch?v=sazsWmP2d3o)

### Dependecies

This project has been built and developed using the following `libraries` and `modules`

- [pipenv](https://pypi.org/project/pipenv/)
- [pyenv *linux-only](https://github.com/pyenv/pyenv) | [pyenv-win](https://github.com/pyenv-win/pyenv-win#installation)
- [rasa](https://pypi.org/project/rasa/)
- [python](https://www.python.org/downloads/)
- [pipenv_and_pyenv](https://hackernoon.com/reaching-python-development-nirvana-bb5692adf30c)
- [rasa_and_flask](https://www.skcript.com/svr/rasa-flask-together-forever/)

### Data

The data used for the project comes from the main source -> `NASA`. Using the correct links and [data](https://solarsystem.nasa.gov/moons/saturn-moons/titan/overview/)

### Libraries In-Depth

**Pipenv**

To learn more about how to use the `pipenv` python module for better module management and versioning of the python libraries, please consult the following guide [here](https://pipenv-fork.readthedocs.io/en/latest/basics.html).

**Pyenv**

Learn more about how to manage different python versions in one instance evironment of python usong `pyenv`. [tutorial](https://switowski.com/blog/pyenv) [tutorial-2](https://realpython.com/intro-to-pyenv/)

Useful `pynev` commands -> [commands](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md)

**Flask**

The use of a `Flask-API` is used for the correct interaction over the web-api with the `Conversational A.I.` agent with the correct method. To validate the correct use of the flask and the methods used, the `pytest` module is used -> (https://flask.palletsprojects.com/en/2.0.x/testing/)

**Rasa**

Installing `rasa` using the `pipenv` module has been achieved using the following set of commands:

## 🐛 Common Issues

**Setup & Project Config**

**1**

```
Warning: Your dependencies could not be resolved. You likely have a mismatch in your sub-dependencies.
Soution:pipenv lock --pre --clear
```

- [out-of-disk-space] --> buy more storage (?) - local machine has 15GB of free space...

**Rasa (+ pipenv)**

My issues found with `rasa` & `pipenv` that have been encountered along the way:

- [rasa-pipenv-installation-1](https://stackoverflow.com/questions/70691490/pipenv-install-rasa-incorrect-version)
- [rasa-pipenv-installation-2](https://stackoverflow.com/questions/70727477/rasa-3-0-4-not-installing-due-to-dependency-issues)
- [rasa-pipenv-installation-3](https://stackoverflow.com/questions/70728938/rasa-x-stuck-on-installing)
- [rasa-pipenv-installation-4](https://stackoverflow.com/questions/70645861/rasa-x-takes-too-long-to-install)
 
Questions and Answers from other people and solutions:

- [rasa-pipenv-installation-e-3](https://github.com/RasaHQ/rasa/issues/7962)
- [rasa-pipenv-installation-e-4](https://github.com/RasaHQ/rasa/issues/7124)
- [pipenv-rasa-installation-error-and-taking-forever](https://stackoverflow.com/questions/65806524/pip-install-rasa-x-takes-forever)
- [question](https://stackoverflow.com/questions/70645861/rasa-x-takes-too-long-to-install?noredirect=1#comment124886791_70645861)

**Rasa-X**

```
pipenv install rasa-x -i https://pypi.rasa.com/simple
```

**code-examples**

```
pipenv --no-cache-dir install rasa
```
[link-solution](https://stackoverflow.com/questions/29466663/memory-error-while-using-pip-install-matplotlib)

[build-tools-requirement](https://docs.microsoft.com/en-us/answers/questions/136985/build-tools-for-visual-studio.html)

```
pipenv install aiohttp==3.6.3 multidict==4.7.6 pytz==2020.5 SQLAlchemy==1.3.19
```
