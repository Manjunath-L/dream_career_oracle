from django.db import models


# Create your models here.
class Dream(models.Model):
    LEVEL_CHOICES = [
        ("Beginner", "Beginner"),
        ("Epic", "Epic"),
        ("Legendary", "Legendary"),
    ]

    # Category Choices
    CATEGORY_CHOICES = [
        ("Tech & AI", "Tech & AI"),
        ("Business & Startup", "Business & Startup"),
        ("Entertainment", "Entertainment"),
        ("Space & Science", "Space & Science"),
        ("Weird Ideas", "Weird & Crazy Ideas"),
        ("Sports & Fitness", "Sports & Fitness"),
        ("Education", "Education"),
        ("Others", "Others"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PathStep(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ]

    dream = models.ForeignKey(
        Dream,
        on_delete=models.CASCADE,
        related_name="steps",
    )

    step_title = models.CharField(max_length=200)
    description = models.TextField()
    estimated_time = models.CharField(max_length=100)  # e.g., "2 months", "45 days"
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.step_title} - {self.dream.title}"
