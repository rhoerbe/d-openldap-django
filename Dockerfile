FROM  centos:7

RUN yum -y update \
 && yum -y install curl iproute lsof net-tools \
 && yum -y install https://centos7.iuscommunity.org/ius-release.rpm \
 && yum -y install python36u python36u-pip \
 && ln -s /usr/bin/python3.6 /usr/bin/python3 \
 && ln -s /usr/bin/pip3.6 /usr/bin/pip3 \
 && yum -y install openldap openldap-servers openldap-clients \
 && yum clean all

# OpenLDAP: Extend configuration, prepare tests
COPY install/etc/openldap/*.conf /etc/openldap/
COPY install/etc/openldap/schema/* /etc/openldap/schema/
COPY install/etc/openldap/DB_CONFIG /var/db/
COPY install/scripts/* /scripts/
COPY install/tests /tests
RUN chmod -R +x /scripts/* /tests/*
RUN chown -R ldap:root /etc/openldap /tests /var/db \
 && chmod 600 $(find   /etc/openldap -type f) \
 && chmod 700 $(find   /etc/openldap -type d)
VOLUME /etc/openldap/ /var/db/


# Django application
COPY install/djangoldap /opt/djangoldap
RUN pip3 install ldap3 virtualenv \
 && mkdir -p /opt/venv \
 && virtualenv --python=/usr/bin/python3.6 /opt/venv/djangoldap \
 && source /opt/venv/djangoldap/bin/activate \
 && pip install -r /opt/djangoldap/requirements.txt
COPY install/scripts/* /scripts/
COPY install/etc/profile.d/pythonenv.sh /etc/profile.d/pythonenv.sh
RUN chmod +x /scripts/*


CMD /scripts/start.sh
