from django.db import models

# Create your models here.
class Room(models.Model):
    room_name = models.CharField(max_length=20)
    room_id = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return self.room_name
class Student(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    RFID = models.CharField(primary_key=True, max_length=16)
    group = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} {self.surname}"
    
class Attendance(models.Model):
    RFID = models.ForeignKey(Student,
                             on_delete=models.CASCADE
                             )
    room_id = models.ForeignKey(Room,
                                on_delete=models.CASCADE
                                )
    time_in = models.DateTimeField()

    class Meta:
        ordering = ["-time_in"]


