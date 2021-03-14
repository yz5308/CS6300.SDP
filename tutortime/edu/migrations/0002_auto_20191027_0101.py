# Generated by Django 2.1.3 on 2019-10-27 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('edu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('year', models.CharField(max_length=4, verbose_name='School Year')),
                ('grade', models.CharField(choices=[('K', 'Kindergarten'), ('1', 'First'), ('2', 'Second'), ('3', 'Third'), ('4', 'Fourth'), ('5', 'Fifth'), ('6', 'Sixth'), ('7', 'Seventh'), ('8', 'Eight'), ('9', 'Ninth'), ('10', 'Tenth'), ('11', 'Eleventh'), ('12', 'Twelth')], max_length=2, verbose_name='Grade')),
                ('active', models.BooleanField(default=False, verbose_name='Active Course?')),
                ('done', models.BooleanField(default=False, verbose_name='Course Complete?')),
                ('info', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Course Information')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CoursesTeached',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_started', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edu.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Educator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last Name')),
                ('bc_addr', models.CharField(max_length=255, unique=True, verbose_name='Blockchain Address')),
                ('email', models.EmailField(max_length=255, verbose_name='Email Address')),
                ('phone_number', models.CharField(blank=True, max_length=30, null=True, verbose_name='Phone Number')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Prefer not to say')], max_length=1, verbose_name='Gender')),
                ('bio', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Bio')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('courses_teached', models.ManyToManyField(related_name='Courses_Teached', through='edu.CoursesTeached', to='edu.Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='coursesteached',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edu.Educator'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Course_Teacher', to='edu.Educator'),
        ),
    ]
