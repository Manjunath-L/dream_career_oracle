from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dreams", "0003_remove_dream_user_delete_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="dream",
            name="likes",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
