FROM alang/django:1.11-python2

ENV DGF_APP=/DGF  

RUN mkdir -p /var/log/gunicorn   
RUN mkdir $DGF_APP

WORKDIR $DGF_APP

ADD requirements.txt $DGF_APP

RUN pip install -r requirements.txt

ADD . $DGF_APP

RUN python manage.py collectstatic --no-input