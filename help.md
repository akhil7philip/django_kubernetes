# saving K8 config file

* for local use: save path in a workspace folder as done here to call the config file

* for production use: open/create `~/.kube/config` file and save `config.yaml` contents inside it, which makes it a global file that kubectl can access

#
# create private container registry in digital ocean

* `docker login registry.digitalocean.com` in the command line
* `username` and `password` is the api token that you copy from access token sub-section in API section
* once login succeeds, `docker build -t registry.digitalocean.com/aks-dj-k8s/django_kubernetes -f Dockerfile .`
* then, `docker push registry.digitalocean.com/aks-dj-k8s/django_kubernetes --all-tags`