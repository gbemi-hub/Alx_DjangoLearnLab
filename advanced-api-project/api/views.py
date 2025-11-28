from rest_framework import filters
from rest_framework import generics
from django_filters import rest_framework
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

# --------------------------
# List all books (read-only)
# --------------------------
class BookListView(generics.ListAPIView):
    """
    List all books with filtering, search, and ordering capabilities:
    - Filtering by title, author, publication_year
    - Search in title and author fields
    - Ordering by title or publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # Everyone can read

    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering

# --------------------------
# Retrieve a single book
# --------------------------
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # Everyone can read

# --------------------------
# Create a new book
# --------------------------
class BookCreateView(generics.CreateAPIView):
    """
    Create a new book. Only authenticated users can create.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only logged-in users can create

# --------------------------
# Update an existing book
# --------------------------
class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book. Only authenticated users can update.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# --------------------------
# Delete a book
# --------------------------
class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book. Only authenticated users can delete.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
