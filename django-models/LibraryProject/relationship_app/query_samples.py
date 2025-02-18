from .models import Author, Book, Library, Librarian


# harper.save()
# harperbook = Book.objects.create(title='To kill a Mockingbird', author=harper)
# harperbook.save()
# Book.objects.get(author=1) 

# nooklibrary = Library.objects.create(name='Book nook')
# nooklibrary.save()

Library.objects.get(name=library_name)

nook = Library.books.add(nooklibrary)
nook.books.all()
Author.objects.get(name=author_name)
Book.objects.filter(author=author)
