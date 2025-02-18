from .models import Author, Book, Library, Librarian

harper = Author.objects.get(name='Harper Lee')
harper.save()
harperbook = Book.objects.create(title='To kill a Mockingbird', author=harper)
harperbook.save()
Book.objects.get(author=1) 

nooklibrary = Library.objects.create(name='Book nook')
nooklibrary.save()

nook = Library.books.add(nooklibrary)
nook.books.all()
Library.objects.get(name='Book nook')