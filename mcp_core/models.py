from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=150, unique=True)
    github_id = models.CharField(max_length=50, unique=True)
    avatar_url = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    public_repos = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Repository(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='repositories')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    stars = models.IntegerField(default=0)
    forks = models.IntegerField(default=0)
    language = models.CharField(max_length=100, blank=True, null=True)
    repo_url = models.URLField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username}/{self.name}"

class ChatMessage(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='chat_messages')
    message = models.TextField()
    is_bot = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{'Bot' if self.is_bot else self.user.username}: {self.message[:50]}"
