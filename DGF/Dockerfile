FROM alang/django:1.11-python2

ENV DGF_APP=/DGF  

RUN mkdir -p /var/log/gunicorn   
RUN mkdir $DGF_APP

WORKDIR $DGF_APP

ADD requirements.txt $DGF_APP

RUN pip install --upgrade pip && pip install -r requirements.txt
RUN apt-get install -y freecad

RUN apt-get install -y build-essential git cmake qt5-default libxml2 libxslt1.1 python-dev qtbase5-dev
#RUN apt-get install -y qttools5-dev-tools libqt5clucene5 libqt5concurrent5 libqt5core5a libqt5dbus5 libqt5designer5 libqt5designercomponents5 libqt5feedback5 libqt5gui5 libqt5help5 libqt5multimedia5 libqt5network5 libqt5opengl5 libqt5opengl5-dev libqt5organizer5 libqt5positioning5 libqt5printsupport5 libqt5qml5 libqt5quick5 libqt5quickwidgets5 libqt5script5 libqt5scripttools5 libqt5sql5 libqt5sql5-sqlite libqt5svg5 libqt5test5 libqt5webkit5 libqt5widgets5 libqt5xml5 libqt5xmlpatterns5 libqt5xmlpatterns5-dev 
RUN pip install -U pyside

ADD . $DGF_APP

RUN python manage.py collectstatic --no-input