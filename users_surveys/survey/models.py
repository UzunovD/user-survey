from datetime import timedelta

from django.db import models
from django.utils.timezone import now


def get_date_finish(h=24):
    return now() + timedelta(hours=h)


class Survey(models.Model):
    IN_PROGRESS = 'P'
    FINISHED = 'F'
    EXPIRED = 'E'
    CANCEL = 'C'

    SURVEY_STATUS_CHOICES = (
        (IN_PROGRESS, 'in progress'),
        (FINISHED, 'is finished'),
        (EXPIRED, 'time is over'),
        (CANCEL, 'canceled'),
    )

    user = models.ForeignKey()
    name = models.CharField(verbose_name='Name', max_length=255)
    date_start = models.DateTimeField(verbose_name='Data of start', auto_now_add=True)
    date_finish = models.DateTimeField(verbose_name='Data of finsh', default=get_date_finish)
    description = models.TextField(verbose_name='Description')
    is_active = models.BooleanField(verbose_name='Is_active', default=True)
    status = models.CharField(verbose_name='Status', max_length=1, choices=SURVEY_STATUS_CHOICES, default=IN_PROGRESS)
    is_passed = models.BooleanField(verbose_name='Survey is passed')

    class Meta:
        ordering = ('-date_start',)
        verbose_name = 'survey'
        verbose_name_plural = 'surveys'

    def __str__(self):
        return f'Current survey: {self.id} {self.name}'


class Answer(models.Model):
    pass


class Question(models.Model):
    survey = models.ForeignKey(Survey, related_name="Survey", on_delete=models.CASCADE)
    title = models.TextField(verbose_name='Text of question')
    type_answer = models.ManyToManyField(Answer)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.title
