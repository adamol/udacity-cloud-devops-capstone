help create helloapp

->
    helloapp/
    |
    |- .helmignore # Contains patterns to ignore when packaging Helm charts.
    |
    |- Chart.yaml # Information about your chart
    |
    |- values.yaml # The default values for your templates
    |
    |- charts/ # Charts that this chart depends on
    |
    |- templates/ # The template files

# delete charts
# move deployment.yaml and service.yaml to templates
# move values.yaml to subfolder
