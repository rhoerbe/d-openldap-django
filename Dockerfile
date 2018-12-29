FROM  centos:7

RUN yum -y update \
 && yum -y install curl iproute lsof net-tools \
 && yum -y install https://centos7.iuscommunity.org/ius-release.rpm \
 && yum -y install openldap openldap-servers openldap-clients \
 && yum -y install gcc python36u-devel python36u-pip openldap-devel \
 && pip3.6 install --upgrade pip \
 && yum clean all

# OpenLDAP: Extend configuration, prepare tests
COPY install/etc/openldap/*.conf /etc/openldap/
COPY install/etc/openldap/schema/* /etc/openldap/schema/
COPY install/etc/openldap/DB_CONFIG /var/db/
COPY install/bin/* /opt/bin/
COPY tests /tests
RUN chmod -R +x /opt/bin/* /tests/* \
 && chown -R ldap:ldap /etc/openldap /var/db \
 && chmod 600 $(find /var/db -type f) \
 && chmod 700 $(find /var/db -type d)
VOLUME /etc/openldap/ /var/db/


# Django application
COPY manage.py requirements.txt /opt/djangoldap/
COPY djangoldap /opt/djangoldap/djangoldap
RUN pip3.6 install virtualenv \
 && mkdir -p /opt/venv \
 && virtualenv --python=/usr/bin/python3.6 /opt/venv/djangoldap \
 && source /opt/venv/djangoldap/bin/activate \
 && pip install ldap3 \
 && pip install -r /opt/djangoldap/requirements.txt
COPY install/etc/profile.d/pythonenv.sh /etc/profile.d/pythonenv.sh


CMD /opt/bin/start.sh
