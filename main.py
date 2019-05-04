import docker

client = docker.from_env()
res = client.images.search("foxcris/docker-apacheproxy:dev")
print(res)
