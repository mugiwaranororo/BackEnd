from django.test import TestCase, Client
from django.urls import reverse
from .models import Sunglasses, Brand, Color, Type
from django.contrib.auth.models import User


#This is a negative test to check if you can access the home page without being logged in
class MyViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('home')

    def test_requires_authentication(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/sunglasses/')

#This is a negative test to check if a typical user can access the admin page
class AdminViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('admin:index')

    def test_requires_authentication(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/admin/')

class BrandModelTest(TestCase):
    #This is a positive test to check if the brand is created
    def test_brand_string_representation(self):
        brand = Brand(name='Ray-Ban')
        self.assertEqual(str(brand), 'Ray-Ban')

    #This is a positive test to check if the price is created
    def test_brand_price(self):
        brand = Brand.objects.create(name='Ray-Ban', price=10.00)
        self.assertEqual(brand.price, 10.00)

class TypeModelTest(TestCase):
    #This is a positive test to check if the type is created
    def test_type_string_representation(self):
        sunglass_type = Type(name='Round')
        self.assertEqual(str(sunglass_type), 'Round')

    #This is a positive test to check if the price is created
    def test_type_price(self):
        sunglass_type = Type.objects.create(name='Round', price=10.00)
        self.assertEqual(sunglass_type.price, 10.00)

class ColorModelTest(TestCase):
    #This is a positive test to check if the color is created
    def test_color_string_representation(self):
        color = Color(name='Black')
        self.assertEqual(str(color), 'Black')

    #This is a positive test to check if the price is created
    def test_color_price(self):
        color = Color.objects.create(name='Black', price=10.00)
        self.assertEqual(color.price, 10.00)

class SunglassesModelTest(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name='Ray-Ban', price=10.00)
        self.type = Type.objects.create(name='Round', price=10.00)
        self.color = Color.objects.create(name='Black', price=10.00)
        self.user = User.objects.create_user(username='test', password='test')
        self.sunglasses = Sunglasses.objects.create(
            name='RayOne',
            price=200.00,
            brand=self.brand,
            type=self.type,
            color=self.color,
            id=1,
            user=self.user
        )

    #This is a positive test to check if the sunglasses are created
    def test_sunglasses_string_representation(self):
        self.assertEqual(str(self.sunglasses), 'RayOne')

    #This is a positive test to check if the brand of the sunglasses is created
    def test_sunglasses_brand(self):
        self.assertEqual(self.sunglasses.brand, self.brand)

    #This is a positive test to check if the type of the sunglasses is created
    def test_sunglasses_type(self):
        self.assertEqual(self.sunglasses.type, self.type)

    #This is a positive test to check if the color of the sunglasses is created
    def test_sunglasses_color(self):
        self.assertEqual(self.sunglasses.color, self.color)

    #This is a positive test to check if the price of the sunglasses is created
    def test_sunglasses_price(self):
        self.assertEqual(self.sunglasses.price, 200.00)

    #This is a positive test to check if the id of the sunglasses is created
    def test_sunglasses_id(self):
        self.assertEqual(self.sunglasses.id, 1)

    #This is a positive test to check if the user of the sunglasses is created
    def test_sunglasses_user(self):
        self.assertEqual(self.sunglasses.user, self.user)

