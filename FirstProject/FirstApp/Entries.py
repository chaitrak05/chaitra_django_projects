from FirstProject.FirstApp.models import Student

#event1 = Event(name="Test Event1", event_date="2018-12-17",
#  venue="test venue", manager="Bob")
#
# StudentID = models.CharField(max_length=30)
#     First_name = models.CharField(max_length=30)
#     Last_name = models.CharField(max_length=30)
#     Contact = models.CharField(max_length=30)
#     Address = models.CharField(max_length=30)

student1 = Student(Studentid="1", First_name="Chaitra" , Last_name="Krishnamurthy", Contact= "201-283-4710", Address=" 51 S 47th Street")
student1.save()