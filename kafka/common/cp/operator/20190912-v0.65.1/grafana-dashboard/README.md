# Monitoring

All CP component deployed through Confluent Operator has a capability to scrap metrics through Prometheus Operator.
This folder contains examples metric dashboard for all components except ControlCenter.

## Configure Prometheus and Grafana

### Install Prometheus

    helm install stable/prometheus --set alertmanager.persistentVolume.enabled=false --set server.persistentVolume.enabled=false --name demo-test

#### Run Prometheus

 Read the output of the helm install command when installing prometheus.
    
    1. Run port forwarding on the port 9090 ( information avaiable on the output of helm)


### Install Grafana

    helm install stable/grafana
    
#### Run Grafana
    
    Read the output of the helm install command when installing grafana.
    
    1. First generate admin key
    2. Run port forwarding on the port 3000 ( information avaiable on the output of helm)


## Setup Prometheus Data-source

Name: Prometheus
HTTP:
  URL: http://localhost:9090
  Access: Browser

Make sure, prometheus is port-forwarded to localhost 9090 through kubectl port-forward command and the Click Save & Test
   
## Load Grafana Dashboard

Import grafana-dashboard.json on the Grafana UI.


