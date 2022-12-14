0. Open dir
```
cd django
```

1. Test Django
```
python manage.py test
```

2. Build Container
```
docker build \
    -t registry.digitalocean.com/aks-dj-k8s/django_kubernetes:latest \
    -t registry.digitalocean.com/aks-dj-k8s/django_kubernetes:v1 \
    -f Dockerfile .
```

3. Push container to Digital Ocean Container Registry
```
docker push registry.digitalocean.com/aks-dj-k8s/django_kubernetes --all-tags
```

4. Update secrets
```
k delete secret django-k8s-prod-env
k create secret generic django-k8s-prod-env --from-env-file=.env.prod
```

4.1. How to get secret for accessing private image
```
k get serviceaccount default -o YAML
```
and copy `imagePullSecrets` into Deployment manifest file to access private image

5. Update deployment
```
cd ..
k apply -f k8s/apps/dj-k8-app.yaml
```
force update
```
k rollout restart deployment/django-deployment
```
6. Wait for rollout to finish
```
k rollout status deployment/django-deployment
```

7. Migrate db
```
k exec -it <pod_name> -- bash /app/migrate.sh 
export SINGLE_POD_NAME=$(k get pod -l app=django-deployment -o jsonpath="{.items[0].metadata.name}")
k exec -it $SINGLE_POD_NAME -- bash /app/migrate.sh 
```

8. to run a different image
```
k set image deployment/django-deployment django-deployment=registry.digitalocean.com/aks-dj-k8s/django_kubernetes:<image_id>
```