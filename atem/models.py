from django.db import models

class SeedEntry(models.Model):
    seed_phrase = models.TextField()          # Stores the full phrase as text
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when saved

    def __str__(self):
        return f"Entry {self.id} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = "Seed Entry"
        verbose_name_plural = "Seed Entries"
        ordering = ['-created_at']
