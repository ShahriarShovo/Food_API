from django.db import models
from django.conf import settings
import uuid


# User Token Model
class UserToken(models.Model):
    # user token has relation with user model
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #token created with uuid 
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    #create time
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email