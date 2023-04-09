# Generated by Django 4.1.7 on 2023-03-28 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_rename_2x2 photo submitted_student_goodmorale_done_and_more'),
        ('subjects', '0003_alter_subject_professor_assigned_subjectstudent'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='students_assigned',
            field=models.ManyToManyField(related_name='SubjectProfessor_professor_assigned', through='subjects.SubjectStudent', to='students.student'),
        ),
    ]