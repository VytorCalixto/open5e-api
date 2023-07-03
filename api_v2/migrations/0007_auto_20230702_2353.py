# Generated by Django 3.2.19 on 2023-07-02 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0006_itemset_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='armor',
            options={'verbose_name_plural': 'armor'},
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('staff', 'Staff'), ('rod', 'Rod'), ('scroll', 'Scroll'), ('potion', 'Potion'), ('wand', 'Wand'), ('wondrous-item', 'Wondrous item'), ('ring', 'Ring'), ('ammunition', 'Ammunition'), ('weapon', 'Weapon'), ('armor', 'Armor'), ('gem', 'Gem'), ('jewelry', 'Jewelry'), ('art', 'Art'), ('trade-good', 'Trade Good'), ('shield', 'Shield'), ('poison', 'Poison'), ('adventuring-gear', 'Adventuring gear')], help_text='The category of the magic item.', max_length=100),
        ),
        migrations.AlterField(
            model_name='itemset',
            name='items',
            field=models.ManyToManyField(help_text='The set of items.', related_name='itemsets', to='api_v2.Item'),
        ),
    ]
