# Deep Learning Project
 

Based on [OpenAI Whisper](https://github.com/openai/whisper)

## How to run Docker image 
I have already built and pushed an Image to [DockerHub](https://hub.docker.com/u/andrewkin77)  

All you need to do is have Docker daemon running  

Then pull my image

```
docker pull andrewkin77/whisper-test
```

And run the container

```
docker run andrewkin77/whisper-test
```

## How to build Docker image

Firstly clone this repository recursively

```
git clone https://github.com/andrewkin77/DL_project.git 
cd DL_project
```
Make sure you have Docker installed and your Docker daemon is running  
Then build an image
```
docker build -t andrewkin77/whisper-test .
```

You can try to run it with 
```
docker run andrewkin77/whisper-test
