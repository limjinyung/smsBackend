from django.test import TestCase
from .models import Student, Course
from django.template.defaultfilters import slugify
import datetime

# Create your tests here.
class DumbTestCase(TestCase):

    def dumb_test(self):
        pass


# class CourseModelTest(TestCase):
#
#     def test_create_new_course(self):
#         course1 = Course.objects.create(name="Advance Data Structure and Algorithms")
#         course2 = Course.objects.create(name="Image Processing")
#
#         course1.save()
#         course2.save()
#         self.assertEqual(course1.name, "Advance Data Structure and Algorithms")
#         self.assertEqual(course2.name, "Image Processing")

