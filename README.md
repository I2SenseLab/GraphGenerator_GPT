Automatically Generates the needed png files for spider graphs. 

categories = data['categories']
    values = data['values']

Call with an array of categories and an array of values in the json

https://graph-generator-3yvuhaorjq-uc.a.run.app

Test Web Request
Invoke-WebRequest -Method POST -Uri https://graph-generator-3yvuhaorjq-uw.a.run.app/spider_plot -ContentType 'application/json' -Body '{ "categories": ["Able to Assess market needs", "Bias Aware & Adaptive", "Fosters Creative thinking", "IP knowledgeable", "Good Communicator", "Presenter/Self promoter", "Good Negotiator", "Resilient", "Strategic Planner", "Alliance Builder"], "values": [1, 2, 3, 4, 5, 4, 3, 2, 1, 0] }' -OutFile output.png



https://graph-generator-3yvuhaorjq-uw.a.run.app/bar_graph

Invoke-WebRequest -Method POST -Uri https://graph-generator-3yvuhaorjq-uw.a.run.app/bar_graph -ContentType 'application/json' -Body '{ "categories": ["Able to Assess market needs", "Bias Aware & Adaptive", "Fosters Creative thinking", "IP knowledgeable", "Good Communicator", "Presenter/Self promoter", "Good Negotiator", "Resilient", "Strategic Planner", "Alliance Builder"], "values": [1, 2, 3, 4, 5, 4, 3, 2, 1, 0], "title":"TEST DATA STUFF, "xlabel":"X VALUES", "ylabel":"VERTICLE" }' -OutFile output.png

    categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5']
    values = [50, 60, 70, 80, 90]
    filename = "bar_plot.png"
    title = "THE TITLE"
    xlabel = "XCATS"
    ylabel = "YVALS"

Gunicorn is used as the web server