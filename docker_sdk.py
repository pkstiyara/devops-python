import docker

# Connect to Docker daemon
client = docker.from_env()

# Pull an image from a Docker registry
image = client.images.pull("alpine:latest")

# Create a container from the image
container = client.containers.create("alpine:latest", command="ping 8.8.8.8")

# Start the container
container.start()

# Wait for the container to finish and get its logs
output = container.wait()
print(container.logs().decode("utf-8"))

# Clean up the container
container.remove()