from django.db import models

STATUS_CHOICES = [
    ('inprogress', 'In Progress'),
    ('completed', 'Completed'),
    ('pending', 'Pending'),
]
class Item(models.Model):

    title = models.CharField(max_length=400)
    description = models.CharField(max_length=700)
    expired_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("item_detail", kwargs={"pk": self.pk})
