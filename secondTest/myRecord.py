#from models import myBookModel
from secondTest.myTestApp.models import myBookModel

# this is where I demonstrate how to actually create a record, NB: Models simply define the logics, working with them is something else.


record = myBookModel(title= "Chapa Dimba")
# always save after creation.
record.save()
print(f"{record.title}")

# to modify the record's field after creation simply access it via dot notation. and call save
record.title = "Charaza kitabu"
record.save()
print(f"{record.title}")

# to search and print out the whole list of the model in the database,
allBooks = myBookModel.objects.all()
for book in allBooks:
    print(f"book in all the books: {book}")

# to search for a particular group use the filter
# note the space between title and contains. title is a field while contains is the filter match type
wild_books = myBookModel.objects.filter(title__contains="Cha")
#this one below is case insensitive because of the i before the match type
wild_books = myBookModel.objects.filter(title__icontains="Cha")

# to count them there's a count method here
wildBooksNumber = wild_books.count()

# to filter  based on a field that contains a one to many relationship to another field you"ll have to index to the field through the other repeating field like  this below:
books_containing_genre = myBookModel.objects.filter(genre__name__icontains="fiction")

