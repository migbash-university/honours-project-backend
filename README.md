![image](https://user-images.githubusercontent.com/20924663/149317090-2482101c-87f2-4fdc-aecc-80e088b66f30.png)

---

## 📜 Description

This is an Edinburgh Napier University Honours Project for (BSc.) Computer Science Degree. 

This Honours Project revolves around Conversational A.I. Agents to be used in the Educational System for the correct interaction with humans to pass across knowledge. However, due to the lack of existing real-world literature and research on `multi-modal` learning approaches, such as: visual - audio and interactive charts methods of learning, this honours project aims to understand the imapct of the use of a Conversational A.I. Agent to pass across knowledge to the user on a scientific topic and companre it with standard and more common methods of learning.

This repository is only half-of the project. It focuses on the development of the `conversational AI` agent and the outline of its development. The `UI/UX` in a web-app format can be accessed on the following link -> [insert-link-here] and for the open-source code for it can be found here -> [insert-link-here]

This project is a `conversational-agent` tailored on the builing of a `space-education` website.

## 📊 Project Graph [ChatBot]

[insert-project-chart-here]

## 📃 Data

The data used for the project comes from the main source -> `NASA`. Using the correct links and [data](https://solarsystem.nasa.gov/moons/saturn-moons/titan/overview/)

## 🔭 In-depth technologies

Diving deeper in the understanding of the project technology stack and design decisions:

**📌 Implementation #1 [w/ `BERT`]**

This implementation project is a use of `BERT` technology by `HuggingFace` with their `transformers` library for the users to use. The model is a `pre-trained` model that by `HuggingFace` obtained from the list of existing models [here.](https://huggingface.co/models)

The project has also been implemented as a `GoogleCollab` Notebook, [here.](https://colab.research.google.com/drive/1BkZXC41xG9hDmCmkJHKnHr3bu_RH0gAO?usp=sharing)

**Why `PyTorch` vs. `Tensorflow`?**

The main reason for the use of [`PyTorch`](https://pytorch.org/) instead that of `Tensorflow` is the use: _PyTorch has long been the preferred deep-learning library for researchers, while TensorFlow is much more widely used in production. PyTorch's ease of use makes it convenient for fast, hacky solutions and smaller-scale models._ - [ref](https://www.udacity.com/blog/2020/05/pytorch-vs-tensorflow-what-you-need-to-know.html)

**What is Question Answering (QA) ?**

Question-answering is the ability for a conversational agent to answer a particular question a user may have, based on a `context` (or a _passage_). This can be further explored and has been explained by the following article [1](https://blog.marketmuse.com/glossary/question-answering-definition/)

**Why not use `RASA` ?**

The use of `RASA` has been omitted in the development cycle of this project, due to the use of a simpler approach to a `Question-Answering` model, using solely `BERT` for question-answering model. However, examples of the `integration` of `RASA -> BERT` exist and can be found [here.](https://rasa.com/blog/how-to-benchmark-bert/)

**Why `pipenv` and `pyenv-win` ?**

1. Pipenv: To learn more about how to use the `pipenv` python module for better module management and versioning of the python libraries, please consult the following guide [here](https://pipenv-fork.readthedocs.io/en/latest/basics.html).

2. Pyenv: Learn more about how to manage different python versions in one instance evironment of python usong `pyenv`. [tutorial](https://switowski.com/blog/pyenv) [tutorial-2](https://realpython.com/intro-to-pyenv/). Useful `pynev` commands -> [commands](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md)

**Why `Flask-API` ?**

The use of a `Flask-API` is used for the correct interaction over the web-api with the `Conversational A.I.` agent with the correct method. To validate the correct use of the flask and the methods used, the `pytest` module is used -> (https://flask.palletsprojects.com/en/2.0.x/testing/)

## 🚀 Get Started

**Guides**

Getting started as another video or alternative(s):

- [guide-1](https://www.machinelearningplus.com/nlp/chatbot-with-rasa-and-spacy/)
- [guide-2](https://towardsdatascience.com/create-chatbot-using-rasa-part-1-67f68e89ddad)
- [guide-3](https://medium.com/co-learning-lounge/step-by-step-guide-to-install-rasa-x-in-windows-without-docker-85da8502bce)
- [guide-4](https://medium.com/analytics-vidhya/deploying-rasa-chatbot-on-heroku-using-docker-7199bf16c219)

---

- ⭐[v-guide-2](https://www.youtube.com/watch?v=Nk9K4s8g9yQ)
- ⭐[v-guide-3](https://www.youtube.com/watch?v=sazsWmP2d3o)

---

- [guide-6-bert](https://github.com/allenai/scibert)
- [guide-7-bert](https://github.com/rsvp-ai/bertserini)
- [guide-8-bert](https://huggingface.co/models)
- [guide-9-bert](https://aclanthology.org/N19-4013/)
- [guide-10-bert](https://towardsdatascience.com/how-to-train-a-bert-model-from-scratch-72cfce554fc6)

### 📌 Dependecies

This project has been built and developed using the following `libraries` and `modules`

- [pipenv](https://pypi.org/project/pipenv/)
- [pyenv *linux-only](https://github.com/pyenv/pyenv) | [pyenv-win](https://github.com/pyenv-win/pyenv-win#installation)
- [rasa](https://pypi.org/project/rasa/)
- [python](https://www.python.org/downloads/)
- [pipenv_and_pyenv](https://hackernoon.com/reaching-python-development-nirvana-bb5692adf30c)
- [rasa_and_flask](https://www.skcript.com/svr/rasa-flask-together-forever/)

### 📂 Project Structure

This project is broken down into the following structure and components:

- `.python-version` - contains the `pyenv-win` version that is used for this project.
- `app.py` - contains the main project entry for the project and the necessary endpoints to make the application run and work.
- `Pipfile` + `Pipfile.lock` - are the main files essential for the interaction with the `pipenv` and the further interaction of the `virtualenv`.
- `bert_env` - contains the data for the `BERT` development and the necessary data for its operation.