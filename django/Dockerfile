# what are we using here
FROM python:3.9.13-slim 


# By copying over requirements first, we make sure that Docker will cache
# our installed requirements rather than reinstall them on every build
COPY requirements.txt /app/requirements.txt
# create a venv virtual env inside opt folder and run requirements
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

# copy entire contents into /app (except dockerignore)
COPY . /app
# cd /app, i.e. enter folder
WORKDIR /app 
# permit execution of entrypoint.sh file
RUN chmod +x entrypoint.sh
# command to execute
CMD ["/bin/bash","/app/entrypoint.sh"]