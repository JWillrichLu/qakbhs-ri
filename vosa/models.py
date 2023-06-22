from django.db import models
from website.settings import LOG_LEVEL, MAIN_LOG, DOMAIN
import logging
import json
from django.urls import reverse
import urllib


class QAKB_KINDS:
    PRODUCT = 'PRODUCT'
    SERVICE = 'SERVICE'
    TOPIC = 'TOPIC'

    CHOICES = (
            (PRODUCT,PRODUCT),
            (SERVICE,SERVICE),
            (TOPIC,TOPIC),
            )

class QAKB(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    tag = models.TextField(editable=False, null=True, blank=True)

    name = models.CharField(max_length=100)
    kind = models.TextField(max_length=20, choices=QAKB_KINDS.CHOICES, default=QAKB_KINDS.TOPIC)

    @property
    def qakb_url(self):
        return 'https://%s/%s' % (DOMAIN, reverse('jqakb',args=(self.id,)))

    def qakbqr_payload(self):
        jkb = {
                'name': self.name,
                'kind': self.kind,
                'url': self.qakb_url
                }

        return urllib.parse.quote_plus(json.dumps(jkb, indent=2))

    def to_json(self):
        jkb = {
                'name': self.name,
                'kind': self.kind,
                'qa': []
                }
        for qa in self.my_qa.all():
            jkb['qa'].append(
                    {
                        'id': qa.id,
                        'q': qa.question,
                        'a': qa.answer,
                        'aq': list(qa.alt_questions.values_list('question', flat=True))
                        })

        return json.dumps(jkb, indent=2)

    def n_qa(self):
        return self.my_qa.count()
    n_qa.verbose_name = '#QA'


    def __str__(self):
        return "%s:%s" % (self.kind, self.name)

    class Meta:
        verbose_name_plural = 'QAKBs'
        verbose_name = 'QAKB'


class QA(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    tag = models.TextField(editable=False, null=True, blank=True)

    question = models.CharField(max_length=200)
    answer = models.TextField(null=True, blank=True)
    qakb = models.ForeignKey(QAKB, on_delete=models.CASCADE, related_name='my_qa')

    def n_aq(self):
        return self.alt_questions.count()
    n_aq.verbose_name = '#AQ'

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = 'QAs'
        verbose_name = 'QA'



class AlternateQ(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    tag = models.TextField(editable=False, null=True, blank=True)

    question = models.CharField(max_length=200, verbose_name='Alternative Question')
    main_qa = models.ForeignKey(QA, on_delete=models.CASCADE, related_name='alt_questions')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = 'aQs'
        verbose_name = 'aQ'

