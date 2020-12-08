# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Coach(models.Model):
    coach_id = models.CharField(db_column='coach_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    name = models.CharField(max_length=20)
    cert = models.CharField(max_length=20)
    salary = models.FloatField()
    phone = models.CharField(max_length=10)
    team_id_fk = models.ForeignKey('Team', models.DO_NOTHING, db_column='team_ID_FK')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Coach'


class Coachcheckout(models.Model):
    coach_id_fk = models.ForeignKey(Coach, models.DO_NOTHING, db_column='coach_ID_FK')  # Field name made lowercase.
    itemnum_fk = models.ForeignKey('Inventory', models.DO_NOTHING, db_column='itemNum_FK')  # Field name made lowercase.
    checknum = models.AutoField(db_column='checkNum', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CoachCheckOut'


class Inventory(models.Model):
    itemnum = models.AutoField(db_column='itemNum', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=20)
    decription = models.CharField(max_length=40)
    price = models.FloatField()
    quantity = models.IntegerField()
    player_id_fk = models.ForeignKey('Player', models.DO_NOTHING, db_column='player_ID_FK', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Inventory'


class Parent(models.Model):
    parent_id = models.CharField(db_column='parent_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    first = models.CharField(max_length=20)
    last = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'Parent'


class Player(models.Model):
    player_id = models.CharField(db_column='player_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    first = models.CharField(max_length=20)
    last = models.CharField(max_length=20)
    percentage = models.FloatField()
    age = models.IntegerField()
    team_id_fk = models.ForeignKey('Team', models.DO_NOTHING, db_column='team_ID_FK')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Player'


class Relatedto(models.Model):
    player_id_fk = models.OneToOneField(Player, models.DO_NOTHING, db_column='player_ID_FK', primary_key=True)  # Field name made lowercase.
    parent_id_fk = models.ForeignKey(Parent, models.DO_NOTHING, db_column='parent_ID_FK')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RelatedTo'
        unique_together = (('player_id_fk', 'parent_id_fk'),)


class Team(models.Model):
    team_id = models.CharField(db_column='team_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'Team'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class SnippetsSnippet(models.Model):
    created = models.DateTimeField()
    title = models.CharField(max_length=100)
    code = models.TextField()
    linenos = models.IntegerField()
    language = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    highlighted = models.TextField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'snippets_snippet'
