# Create your models here.

# models.py

from django.db import models


class GPT3Conversation(models.Model):
    user_input = models.TextField()
    openai_response = models.TextField()



