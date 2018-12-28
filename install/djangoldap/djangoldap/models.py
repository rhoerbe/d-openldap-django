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

class LdapUser(ldapdb.models.Model):
    base_dn = "dc=at"
    object_classes = ['inetOrgPerson']

    first_name = CharField(db_column='givenName')
    last_name = CharField("surname", db_column='sn')
    full_name = CharField(db_column='cn', primary_key=True)
    email = CharField(db_column='mail')

    def __str__(self):
        return self.full_name
