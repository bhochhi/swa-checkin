# vim:set ft=dockerfile:

FROM kennethreitz/pipenv as pipenv
#WORKDIR ./app

COPY . ./
#RUN pip install --upgrade pip
RUN pipenv install


#ENTRYPOINT [ "python" ]
#
#CMD [ "app.py" ]

#CMD ["python", "app.py"]

#CMD ["pipenv", "run", "gunicorn", "app:app", "-b", "0.0.0.0:8000", "--max-requests 30", "--preload"]
#

CMD ["pipenv", "run", "gunicorn", "--workers=0", "-b", "0.0.0.0:5000","app:app"]

EXPOSE 5000
EXPOSE 27017
#EXPOSE 8000
