from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Shoe


# Create your tests here.

class ShoeTests(APITestCase):
    # In Python, the @classmethod decorator is used to declare a method in the class as a class method that can be called using ClassName.MethodName()
    # click the blue circle, this overrides a particular method
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_shoe = Shoe.objects.create(
            name="Jordan III",
            owner=testuser1,
            description="A classic early Jordan sneaker",
            laces=True,
            brand="Jordan",
            color="True Blue",
        )
        test_shoe.save()

    def test_shoes_model(self):
        shoe = Shoe.objects.get(id=1)
        actual_owner = str(shoe.owner)
        actual_name = str(shoe.name)
        actual_description = str(shoe.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "Jordan III")
        self.assertEqual(
            actual_description, "A classic early Jordan sneaker"
        )

    def test_get_shoe_list(self):
        url = reverse("shoe_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        shoes = response.data
        self.assertEqual(len(shoes), 1)
        self.assertEqual(shoes[0]["name"], "Jordan III")

    def test_get_shoe_by_id(self):
        url = reverse("shoe_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        thing = response.data
        self.assertEqual(thing["name"], "Jordan III")

    def test_create_shoe(self):
        url = reverse("shoe_list")
        data = {"owner": 1, "name": "Ultraboost", "description": "Comfy and looks good"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        shoes = Shoe.objects.all()
        self.assertEqual(len(shoes), 2)
        self.assertEqual(Shoe.objects.get(id=2).name, "Ultraboost")

    def test_update_thing(self):
        url = reverse("thing_detail", args=(1,))
        data = {
            "owner": 1,
            "name": "Jordan III",
            "description": "One of my favorite pairs of sneakers",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        shoe = Shoe.objects.get(id=1)
        self.assertEqual(shoe.name, data["name"])
        self.assertEqual(shoe.owner.id, data["owner"])
        self.assertEqual(shoe.description, data["description"])


    def test_delete_shoe(self):
        url = reverse("shoe_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        shoes = Shoe.objects.all()
        self.assertEqual(len(shoes), 0)

