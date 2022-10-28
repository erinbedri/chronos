# from django.contrib.auth import get_user_model
# from django.db import models
# from django.db.models import CASCADE
#
# UserModel = get_user_model()
#
#
# class Profile(models.Model):
#     PROFILE_BIO_MAX_LEN = 250
#
#     user = models.ForeignKey(
#         UserModel,
#         primary_key=True,
#         on_delete=CASCADE,
#     )
#
#     bio = models.TextField(
#         blank=True,
#         null=True,
#         max_length=PROFILE_BIO_MAX_LEN,
#     )
#
#     image = models.ImageField(
#         blank=True,
#         null=True,
#         upload_to='profile_image/',
#         default='img/default_profile_img.jpeg',
#     )
