# Securing Docker on the Cheap
## Part 2 - Vulnerabilities - InSpec

### Running the example
From the inspec-example directory:

```
docker build -t inspec-example-asroot:v1 -f Dockerfile-flask-root .
docker build -t inspec-example-asuser:v1 -f Dockerfile-flask-asuser .

docker run -d --rm --name as-root inspec-example-asroot:v1
docker run -d --rm --name as-user inspec-example-asuser:v1

inspec exec inspec-example -t docker://as-root
inspec exec inspec-example -t docker://as-user
```

