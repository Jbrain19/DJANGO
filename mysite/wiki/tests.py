from django.test import TestCase
from django.utils import timezone

from django.urls import reverse


def create_question(question_text, days):
        """
        Create a question with the given `question_text` and published the
        given number of `days` offset to now (negative for questions published
        in the past, positive for questions that have yet to be published).
        """
        time = timezone.now() + datetime.timedelta(days=days)
        return Question.objects.create(question_text=question_text, pub_date=time)

def test_login (user):
    

def test_logout ():
# Create your tests here.
