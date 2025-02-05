# How to run Streamlit Localy
## Setup Environment - Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run steamlit app
```
streamlit run dashboard.py
```

## Setup localtunnel
```
npm install localtunnel
```

## Run localtunnel 
```
npx localtunnel --port 8502 --subdomain analisisdatakualitasudara-joshuams04-streamlit
```
