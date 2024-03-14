# Generated by Django 4.2.1 on 2024-03-14 10:57

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('professions', '0002_skill_professionskill'),
        ('languages', '0001_initial'),
        ('citizenships', '0001_initial'),
        ('applications', '0003_remove_application_description_jobinfo_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='salary',
            new_name='max_salary',
        ),
        migrations.AddField(
            model_name='application',
            name='min_salary',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='recruit_requirements',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='applications.recruitrequirements'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='start_working',
            field=models.CharField(blank=True, choices=[('tomorrow', 'Сможет приступить завтра'), ('in_week', 'В течение недели'), ('in_month', 'В течение месяца'), ('not_hurry', 'Не спешу с поиском')], null=True),
        ),
        migrations.AlterField(
            model_name='candidaterequirements',
            name='citizenship',
            field=models.ManyToManyField(blank=True, to='citizenships.citizenship'),
        ),
        migrations.RemoveField(
            model_name='candidaterequirements',
            name='core_skills',
        ),
        migrations.AlterField(
            model_name='candidaterequirements',
            name='driving_skills',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('B', 'Категория B, легковые автомобили'), ('C', 'Категория C, грузовые автомобили'), ('D', 'Категория D, автобусы'), ('M', 'Категория M, мопеды'), ('A', 'Категория A, мотоциклы')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='candidaterequirements',
            name='education',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('not_required', 'Не имеет значения'), ('higher', 'Высшее'), ('vocational', 'Среднее профессиональное')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='candidaterequirements',
            name='experience',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('not_required', 'Не имеет значения'), ('no_experience', 'Нет опыта'), ('1-3_years', 'От 1 года до 3 лет'), ('3-6_years', 'От 3 до 6 лет'), ('over_6_years', 'Более 6 лет')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='candidaterequirements',
            name='has_medical_sertificate',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='candidaterequirements',
            name='has_photo',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='candidaterequirements',
            name='language_skills',
            field=models.ManyToManyField(blank=True, to='languages.languageproficiency'),
        ),
        migrations.AlterField(
            model_name='jobinfo',
            name='contract_type',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('contract', 'Трудовой договор'), ('civil-personal_contract', 'ГПХ'), ('individual_entrepreneurship', 'ИП'), ('self-employed', 'Самозанятый'), ('holding_multiple_positions', 'Совместительство')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='jobinfo',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='jobinfo',
            name='employment_type',
            field=models.CharField(blank=True, choices=[('full-time', 'Полная занятость'), ('part-time', 'Частичная занятость'), ('project', 'Проект'), ('shift_work', 'Вахта'), ('traineeship', 'Стажировка')], null=True),
        ),
        migrations.AlterField(
            model_name='jobinfo',
            name='schedule',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('full-day', 'Полный день'), ('part-time', 'Неполный день'), ('5_on_2_off', '5/2'), ('2_on_2_off', 'Два через два'), ('24_h_on_72_h_off', 'Сутки / трое'), ('flexible', 'Свободный'), ('shift_work', 'Вахта')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='jobinfo',
            name='work_model',
            field=models.CharField(blank=True, choices=[('office', 'Офис'), ('remote', 'Удаленный'), ('hybrid', 'Гибрид')], null=True),
        ),
        migrations.AlterField(
            model_name='jobinfo',
            name='working_conditions',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('VMI', 'ДМС'), ('fitness', 'Фитнес'), ('meal_compensation', 'Оплата питания'), ('free_parking', 'Бесплатная парковка'), ('mobile_phone_compensation', 'Оплата мобильной связи'), ('transportation_compensation', 'Оплата проезда'), ('language_training', 'Языковые курсы'), ('professional_training', 'Профессиональные курсы'), ('from_age_14', 'Подходит подросткам с 14 лет'), ('for_people_with_disabilities', 'Подходит людям с ограниченными возможностями')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='recruitrequirements',
            name='rating',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(4.9, '4.9 и выше'), (4.5, '4.5 и выше'), (4, '4 и выше'), (3, '3 и выше'), (0, 'Не имеет значения')], max_length=1000),
        ),
        migrations.AddField(
            model_name='candidaterequirements',
            name='core_skills',
            field=models.ManyToManyField(blank=True, to='professions.professionskill'),
        ),
    ]
