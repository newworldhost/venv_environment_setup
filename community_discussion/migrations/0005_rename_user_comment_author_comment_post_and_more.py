# Generated by Django 4.2.18 on 2025-01-31 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community_discussion', '0004_rename_author_comment_user_remove_comment_post_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='author',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=int, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='community_discussion.post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]
