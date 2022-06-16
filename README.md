# workiz_lastartup
Mini local app: scrapped lastartup terms

## Instructions

#### Create python env.
```
python3 -m venv workiz_env
```

#### Install Requirements
```
source workiz_env/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

#### Run App
```
python3 app.py
```

## How to use?
```
lsw = LaStartup_Workiz()

# Insert new Term | True for saving
#data = lsw.insert_new_sample(data, True)

# Remove last inserted Term | True for updating
#data = lsw.remove_last_row(data, True)

# Run App
lsw.run_app(data)
```


<img src="https://raw.githubusercontent.com/vamosUY/workiz_lastartup/main/run_app.gif" width="800" height="400" />
