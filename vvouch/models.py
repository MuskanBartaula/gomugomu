from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # removes email from REQUIRED_FIELDS
    type = models.CharField(
        max_length=30,
        default='user'
    )
    username = models.CharField(
        'username',
        max_length=100,
        blank=True,
        default=''
    )
    email = models.EmailField(unique=True)  # changes email to unique and blank to false
    mobile_number = models.CharField(
        max_length=100,
        blank=True,
    )
    cnic = models.CharField(
        max_length=100,
        blank=True,
    )
    address = models.TextField(
      blank=True,  
      max_length=100,
    )
    message = models.TextField(
      blank=True,  
      max_length=100,
    )
    business_name = models.CharField(
        blank=True,
        max_length=100,
    )
    website = models.CharField(
        blank=True,
        max_length=100,
    )
    insta_page = models.CharField(
        blank=True,
        max_length=100,
    )
    fb_page = models.CharField(
        blank=True,
        max_length=100,
    )
    courier = models.CharField(
        blank=True,
        max_length=100,
    )
    business_category = models.CharField(
        blank=True,
        max_length=100,
    )
    is_secp_registered = models.BooleanField(
        default=False,
    )
    payment_mode = models.CharField(
        blank=True,
        max_length=100,
    )
    is_cod = models.CharField(
        blank=True,
        max_length=100,
    )
    
    def get_full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)


class Activation(models.Model):

    user = models.CharField(
        'activation',
        blank=False,
        null=False,
        max_length=40
    )

    activation_key = models.CharField(
        'activation key',
        max_length=40
    )

    created = models.DateTimeField(
        'created',
        auto_now_add=True
    )

class Products(models.Model):

    product_name = models.CharField(
        max_length=100,
        blank=True,
    )

    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=False,
        null=False,
        related_name='seller_id',
        on_delete=models.CASCADE,
    )

    seller_email = models.CharField(
        max_length=100,
        blank=True,
    )

    product_type = models.CharField(
        max_length=100,
        blank=True,
    )

    product_quantity = models.CharField(
        max_length=100,
        blank=True,
    )
    
    product_reviews = models.CharField(
        max_length=100,
        blank=True,
    )

    product_website = models.CharField(
        max_length=100,
        blank=True,
    )

    product_relevant_page = models.CharField(
        max_length=100,
        blank=True,
    )

    product_status = models.CharField(
        max_length=100,
        default='0'
    )



def ticket_file_path(instance, filename):
    
    if hasattr(instance.product, 'id'):
        head , tail = os.path.split(filename)
        return join('product', str(instance.product.id), tail)
    else:
        return join('product', str(instance.product.id), filename)

class ProductImages(models.Model):
    file = models.CharField(
        max_length=255,
        blank=True,
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='image_added_by',
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    product = models.ForeignKey(
        'Products',
        related_name='product_id',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    is_deleted = models.BooleanField(
        blank=True,
        default=False,
    )

    date_added = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True
    )
