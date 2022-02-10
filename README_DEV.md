**Personal Local Development Guides**

This is a personal `README.md` file, used for `local-development` for the `backend-API`, as a reminder and useful links to sources:

Getting started as another video or alternative(s):

---

**`RASA` Bot Development useful guides:**
- [guide-1](https://www.machinelearningplus.com/nlp/chatbot-with-rasa-and-spacy/)
- [guide-2](https://towardsdatascience.com/create-chatbot-using-rasa-part-1-67f68e89ddad)
- [guide-3](https://medium.com/co-learning-lounge/step-by-step-guide-to-install-rasa-x-in-windows-without-docker-85da8502bce)
- [guide-4](https://medium.com/analytics-vidhya/deploying-rasa-chatbot-on-heroku-using-docker-7199bf16c219)
- [guide-5](https://thepathforward.io/building-your-first-ai-chatbot/)
- ⭐[How to Create Conversational AI Chatbot using RASA (Python) by Cisco Data Scientist](https://www.youtube.com/watch?v=Nk9K4s8g9yQ)
- ⭐[An Open-Source Chatbot Made With Rasa](https://www.youtube.com/watch?v=sazsWmP2d3o)

---

- https://datahive.ai/conversational-chatbot-part-1/
- https://towardsdatascience.com/question-answering-with-a-fine-tuned-bert-bc4dafd45626
- https://datahive.ai/deploying-rasa-chatbot-on-google-cloud-with-docker/

---

- [guide-6-bert](https://github.com/allenai/scibert)
- [guide-7-bert](https://github.com/rsvp-ai/bertserini)
- [guide-8-bert](https://huggingface.co/models)
- [guide-9-bert](https://aclanthology.org/N19-4013/)
- [guide-10-bert](https://towardsdatascience.com/how-to-train-a-bert-model-from-scratch-72cfce554fc6)

---

**`Dockerize` a Flask (Python) App:**
- [deploy-flask-app-via-docker](https://runnable.com/docker/python/dockerize-your-flask-application)
- [create-python-docker-container-1](https://www.youtube.com/watch?v=bi0cKgmRuiA)
- [create-python-docker-container-2](https://www.docker.com/blog/containerized-python-development-part-1/)

**Standard Dockerfile Python Development**

```
# FROM ubuntu:16.04
FROM python:3.8.0

# MAINTANER Your Name "youremail@domain.tld"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
```

---

### 🚀 Hosting Deployment Options / Guides

Potential [options.](https://geekflare.com/python-hosting-platform/)

**Deployment to `GoogleCloud` for Python:**
- [free-credit](https://console.cloud.google.com/freetrial)
- [pre-eliminary-step-google-cloud-deployment-with-gcloud](https://cloud.google.com/sdk/docs/quickstart)
- [different-ways-to-deploy-to-google-cloud](https://www.youtube.com/watch?v=jh0fPT-AWwM)
- [Deploying Python App to GoogleCloud](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python)
- [Deploying Python App GoogleCloud `Transformers` and `PyTorch`](https://huggingface.co/blog/how-to-deploy-a-pipeline-to-google-clouds)

![image](https://user-images.githubusercontent.com/20924663/153281199-98fcf597-ff9c-46fa-bc92-22510d4d92e1.png)

**Deployment to `Heroku`:**

Due to the `RAM` and `storage` limitations, _this_ application cannot be deployed to `Heroku`, as it is only limited to `512 MB` in size, with the other `tiers` costing of upwards-to `$50 / month` , and the reduction of the critical `python-modules`, such that as the `PyTorch` is not viable, as presented in silutions, such as:
- [solution-1](https://discuss.pytorch.org/t/is-there-a-slimmed-down-pytorch-for-computation/78771/3),
- [solution-2](https://stackoverflow.com/questions/59122308/heroku-slug-size-too-large-after-installing-pytorch),
- [solution-3](https://medium.com/analytics-vidhya/deploying-bert-on-heroku-7df1d23f9c43)

For the deployment of the `heroku` for the `backend` as a `Docker-container` the following useful link-articles have been used:
- [link](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml)
- [link-2](https://devcenter.heroku.com/articles/container-registry-and-runtime)

![image](https://user-images.githubusercontent.com/20924663/153280702-6465adca-c517-4d1b-b160-8eea2dd4839e.png)
![image](https://user-images.githubusercontent.com/20924663/153280738-ecf93a46-a17c-4a04-9805-32dea03e468c.png)
^ https://www.heroku.com/pricing

**Deployment to `PythonAnyWhere`:**
- [service-link](https://www.pythonanywhere.com/pricing/)

**Alternative Deployment Options:**
- [Deploying BERT Question Answering System as web application using Streamlit](https://www.youtube.com/watch?v=ki84YCluXBk)