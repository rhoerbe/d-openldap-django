import ldapdb.models
from ldapdb.models.fields import CharField, ImageField, IntegerField, ListField


class gvOrganisation(ldapdb.models.Model):
    # LDAP meta-data
    base_dn = "dc=at"
    object_classes = ['gvOrganisation']

    #ordering = ['last_name']
    gvOuId = CharField(db_column='gvOuId',primary_key=True)
    gvOuVKZ = CharField(db_column='gvOuVKZ')
    o = CharField("surname", db_column='o')
    cn = CharField(db_column='cn')
    gvOuCn = CharField(db_column='gvOuCn')
    gvStatus = CharField(db_column='gvStatus')
    gvSource = CharField(db_column='gvSource')

    def __str__(self):
        return self.cn

    def __repr__(self):
        return self.dn


class gvOrgPerson(ldapdb.models.Model):
    base_dn = "dc=at"
    object_classes = ['gvOrgPerson']

    gvGid = CharField(db_column='gvGid', primary_key=True),
    cn = CharField(db_column='cn', )
    displayName = CharField(db_column='displayName', ),
    email = CharField(db_column='email', ),
    givenname = CharField(db_column='givenname', ),
    surname = CharField(db_column='surname', )
    uid = CharField(db_column='uid', ),
    gvScope = CharField(db_column='gvScope', ),
    gvSource = CharField(db_column='gvSource', ),
    gvStatus = CharField(db_column='gvStatus', ),

    def __str__(self):
        return self.cn

    def __repr__(self):
        return self.dn


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
