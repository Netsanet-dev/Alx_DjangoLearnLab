bookUpdate = Book.objects.get(title='1984')
bookUpdate.title = 'Nineteen Eighty-Four'
bookUpdate.save()
