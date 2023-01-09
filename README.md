Automatically Generates the needed png files for spider graphs. 

categories = data['categories']
    values = data['values']

Call with an array of categories and an array of values in the json

https://graph-generator-3yvuhaorjq-uc.a.run.app

Test Web Request
Invoke-WebRequest -Method POST -Uri https://graph-generator-3yvuhaorjq-uw.a.run.app/spider_plot -ContentType 'application/json' -Body '{ "categories": ["Able to Assess market needs", "Bias Aware & Adaptive", "Fosters Creative thinking", "IP knowledgeable", "Good Communicator", "Presenter/Self promoter", "Good Negotiator", "Resilient", "Strategic Planner", "Alliance Builder"], "values": [1, 2, 3, 4, 5, 4, 3, 2, 1, 0] }' -OutFile output.png


Gunicorn is used as the web server