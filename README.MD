# install pre-requisites
pip3 install -r requirements.txt


# add insecure for microk8s 
clusters:
- cluster:
    insecure-skip-tls-verify: true