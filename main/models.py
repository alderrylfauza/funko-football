from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)  # nama FunkoPop
    price = models.IntegerField()            # harga FunkoPop
    description = models.TextField()         # deskripsi item
    thumbnail = models.URLField()            # link gambar FunkoPop
    category = models.CharField(max_length=50)  # kategori (contoh: "Football Player")
    stock = models.PositiveIntegerField(default=0) # contoh stok
    is_featured = models.BooleanField(default=False)  # produk unggulan
    
    def __str__(self):
        return self.name