Automatically Generates the needed png files for spider graphs. 

categories = data['categories']
    values = data['values']

Call with an array of categories and an array of values in the json

https://graph-generator-3yvuhaorjq-uc.a.run.app

Test Web Request

https://graph-generator-3yvuhaorjq-uw.a.run.app/spider_plot

"$uri = "https://graphgen-plugin-geearsjixq-uc.a.run.app/spider_plot"
$headers = @{
    "Content-Type" = "application/json"
}
$body = @{
    categories = @("Able to Assess market needs", "Bias Aware & Adaptive", "Fosters Creative thinking", "IP knowledgeable", "Good Communicator", "Presenter/Self promoter", "Good Negotiator", "Resilient", "Strategic Planner", "Alliance Builder")
    data_sets = @(
        @{
            values = @(1, 2, 3, 4, 5, 4, 3, 2, 1, 0)
            legend = "Pre Workshop"
        },
        @{
            values = @(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
            legend = "Post Workshop"
        }
    )
    max_value = 5
    response_type = "bucketurl"
}
$jsonBody = $body | ConvertTo-Json

Invoke-WebRequest -Method Post -Uri $uri -Headers $headers -Body $jsonBody"



https://graph-generator-3yvuhaorjq-uw.a.run.app/bar_graph

Invoke-WebRequest -Method POST -Uri https://graph-generator-3yvuhaorjq-uw.a.run.app/bar_graph -ContentType 'application/json' -Body '{ "categories": ["Able to Assess market needs", "Bias Aware & Adaptive", "Fosters Creative thinking", "IP knowledgeable", "Good Communicator", "Presenter/Self promoter", "Good Negotiator", "Resilient", "Strategic Planner", "Alliance Builder"], "values": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "title":"TEST DATA STUFF", "xlabel":"X VALUES", "ylabel":"VERTICLE" }' -OutFile output.png


Gunicorn is used as the web server