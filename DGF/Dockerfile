FROM alang/django:1.11-python2

ENV DGF_APP=/DGF  

RUN mkdir -p /var/log/gunicorn   
RUN mkdir $DGF_APP

WORKDIR $DGF_APP

ADD requirements.txt $DGF_APP

RUN pip install --upgrade pip && pip install -r requirements.txt
RUN apt-get install -y freecad
RUN apt-get update
RUN apt-get install -y build-essential cmake git libqt4-dev libxslt1-dev  libqtwebkit-dev
#RUN apt-get install git cmake libqt4-dev libphonon-dev python2.7-dev libxml2-dev libxslt1-dev qtmobility-dev libqtwebkit-dev
#RUN apt-get install g++ qtmobility-dev libprotobuf-dev protobuf-compiler libqt4-dev
RUN pip install -U pyside

ADD . $DGF_APP

RUN python manage.py collectstatic --no-input

RUN echo "sys.path.append('/usr/lib/freecad/lib')" >> /usr/local/lib/python2.7/site.py

#RUN touch /usr/local/lib/python2.7/site-packages/example.pth
#RUN echo "/usr/lib/freecad/lib" >> /usr/local/lib/python2.7/site-packages/example.pth
RUN touch /usr/lib/freecad/lib/__init__.py