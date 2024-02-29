from django.db import models

# Create your models here.

class libraryEntry(models.Model):
    deckID = models.CharField(max_length=100)
    cardIDs = models.TextField(default='')

    def get_card_ids(self):
        return self.cardIDs.split(',')

    def add_card_id(self, card_id):
        card_ids = self.get_card_ids()
        card_ids.append(card_id)
        self.cardIDs = ','.join(card_ids)

    def remove_card_id(self, card_id):
        card_ids = self.get_card_ids()
        if card_id in card_ids:
            card_ids.remove(card_id)
            self.cardIDs = ','.join(card_ids)
            
