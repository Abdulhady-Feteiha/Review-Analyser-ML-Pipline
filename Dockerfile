
FROM ubuntu:latest
         # Install latest updates
         RUN apt-get update -y
         # Install Python and build libraries
         RUN apt-get install -y python3-pip python-dev-is-python3 build-essential
         # Copy all files from current folder (.) to container's folder (.)
# Copy all files from current folder (.) to container's folder (.)
COPY . .
# Set working directory container's default folder (.)
WORKDIR .
# Install the dependencies specified in requirements file
RUN pip install -r requirements.txt
# Define which program to run when container starts
ENTRYPOINT [ "python" ]
# Pass file as parameter to the entry command to start your app
CMD [ "app.py" ]