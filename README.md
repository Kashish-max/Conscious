# Conscious
<i>This repository is for our team's project for hackathon at HACKDAVIS2021</i>

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=shields)](http://makeapullrequest.com)

Conscious is a utility web app that serves the people with special needs and helps make the access of data easier and safer manner.Our platform provides a simple yet efficient user experience with a straightforward and easy-to-use interface. We have made the web application to integrate different aspects of it into one platform, each part intricately connected to others, each dedicated to solving issues that people with special needs might encounter.

We provide various functionalities listed below:
<ul>
<li>Trigger warnings to understand the context *of the news/data/text and provide *insights, keywords and summary of said data. This helps people with anxiety, stress, or other mental illnesses like PTSD to avoid certain common triggers.</li>
<li>Ability to convert Text data(in form of link, text) to convert to Embosser Ready File(.brf) and allow downloading it in this format. This can also be done for texts a big as the Bible itself. This will be help blind people (or people working with them) to convert input data to braille fast and without any worry of huge pay walls as this functionality is built using liblouis which is open-sourced. As a additional functionality, we have also provided a braille visualizer for sighted people who wish to learn more about braille.
</li>
<li>Ability to convert Text data (in form of link, text) to a font friendly to those with dyslexia(Open Dyslexic) and allow downloading the same in a pdf format. People with dyslexia are often left feeling inadequate while simple yet eloquent solutions such as this one could go lengths in making them achieve their best.
</li>
<li>Ability to extract text data from images using OCR and then do any of the above processes on it. We used tesseract.js for this.
</li>
</ul>

Link to Video Presentation:
[![IMAGE ALT TEXT HERE](https://i.imgur.com/IjCpYC4.png)](https://youtu.be/0UxPH3suLbg)

## Setup
Let's get you started with this interesting project of ours:

To run this project locally, follow the steps:

Solves general chemical problems
Ubuntu 20.04 focal fossa with python.3.8
- Install Anaconda
```
wget -P /tmp https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
bash /tmp/Anaconda3-2020.02-Linux-x86_64.sh
source ~/.bashrc
```

 Accept the conda init prompt and this should install conda
 
- Create a environment with 
```
conda create --name consciousapp
conda activate consciousapp
```

- Install Django and some dependencies
```
pip install django
https://github.com/Kashish-max/Conscious.git
cd Conscious/
pip3 install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
References:
## Important Links:
<li>1)[Tesseract.js](https://tesseract.projectnaptha.com/)</li>
<li>2)[Liblouis Library](http://liblouis.org/)</li>
<li>3)[Braille-Tools](https://evoluteur.github.io/braille-tools/index.html)</li>
<li>4)[Open Dyslexic](https://opendyslexic.org/)
<li>5)[HACKDAVIS2021](https://hackdavis2021.devpost.com/)</li>

## License: MIT LICENSE


