import ldapdb.models
from ldapdb.models.fields import CharField, ImageField, IntegerField, ListField


class inetOrgPerson(ldapdb.models.Model):
    base_dn = "dc=at"
    object_classes = ['inetOrgPerson']

    given_name = CharField(db_column='givenName')
    surname = CharField("surname", db_column='sn')
    cn = CharField(db_column='cn', primary_key=True)
    email = CharField(db_column='mail')
    uid = CharField(db_column='uid')

    def __str__(self):
        return self.cn

    def __repr__(self):
        return self.dn


class tstPerson(ldapdb.models.Model):
    base_dn = "dc=at"
    object_classes = ['tstPerson', 'inetOrgPerson']

    given_name = CharField(db_column='givenName')
    surname = CharField("surname", db_column='sn')
    cn = CharField(db_column='cn')
    email = CharField(db_column='mail')
    uid = CharField(db_column='uid')
    tstgid = CharField(db_column='tstgid', primary_key=True)

    def __str__(self):
        return self.cn

    def __repr__(self):
        return self.dn


class tstPerson2(tstPerson):
    object_classes = ['tstPerson2', ]
    otherid = CharField(db_column='otherid')

