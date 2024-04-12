# Generated by Django 3.2.20 on 2023-10-06 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0016_auto_20231004_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backgroundbenefit',
            name='type',
            field=models.CharField(blank=True, choices=[('ability_score_increase', 'Ability Score Increase'), ('skill_proficiency', 'Skill Proficiency'), ('tool_proficiency', 'Tool Proficiency'), ('language', 'Language'), ('equipment', 'Equipment'), ('feature', 'Feature'), ('suggested_characteristics', 'Suggested Characteristics'), ('adventures_and_advancement', 'Adventures and Advancement'), ('connection_and_memento', 'Connection and Memento')], help_text='Benefit type.', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='featbenefit',
            name='type',
            field=models.CharField(blank=True, choices=[('ability_score_increase', 'Ability Score Increase'), ('skill_proficiency', 'Skill Proficiency'), ('tool_proficiency', 'Tool Proficiency'), ('language', 'Language'), ('equipment', 'Equipment'), ('feature', 'Feature'), ('suggested_characteristics', 'Suggested Characteristics'), ('adventures_and_advancement', 'Adventures and Advancement'), ('connection_and_memento', 'Connection and Memento')], help_text='Benefit type.', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='trait',
            name='type',
            field=models.CharField(blank=True, choices=[('ability_score_increase', 'Ability Score Increase'), ('skill_proficiency', 'Skill Proficiency'), ('tool_proficiency', 'Tool Proficiency'), ('language', 'Language'), ('equipment', 'Equipment'), ('feature', 'Feature'), ('suggested_characteristics', 'Suggested Characteristics'), ('adventures_and_advancement', 'Adventures and Advancement'), ('connection_and_memento', 'Connection and Memento')], help_text='Benefit type.', max_length=200, null=True),
        ),
    ]