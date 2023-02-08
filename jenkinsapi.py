from jenkinsapi.jenkins import Jenkins

# Connect to the Jenkins server
jenkins = Jenkins('http://jenkins.example.com:8080', username='admin', password='secret')

# Get the build job object
job = jenkins['job_name']

# Trigger the build
build = job.invoke()

# Wait for the build to complete
while build.is_running():
    print("Build is in progress...")

# Print the build result
if build.is_good():
    print("Build succeeded!")
else:
    print("Build failed.")
