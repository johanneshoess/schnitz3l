from django.db import models


class Chain(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=70)
    # chain list wird als JSON gespeichert. Editierbar und möglich eine liste zu speichern.
    chainList = models.TextField(null=True)

    '''
        # encode
        istIWantToStore = [1, 2, 3, 4, 5, 'hello']
        myModel.myList = json.dumps(listIWantToStore)
        myModel.save()
        
        # decode
        jsonDec = json.decoder.JSONDecoder()
        myPythonList = jsonDec.decode(myModel.myList)
        
        #https://stackoverflow.com/questions/1110153/what-is-the-most-efficient-way-to-store-a-list-in-the-django-models
    '''
