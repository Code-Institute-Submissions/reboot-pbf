from django.test import TestCase
from .forms import MakePaymentForm, OrderForm


class TestMakePaymentForm(TestCase):
    """
    Series of tests for MakePaymentForm, checking both validity of form fields
    and check the required attribute for data conditioning.
    """

    def test_form_is_valid(self):
        """Test that our forms is valid with the required fields completed"""
        payment_form = MakePaymentForm({'stripe_id': "123456789"})
        self.assertTrue(payment_form.is_valid())

        order_form = OrderForm({'full_name': 'bob', 'phone_number': '04321',
                                'street_address1': 'house', 'postcode': 'xyz'})
        self.assertTrue(order_form.is_valid())

    def test_form_not_valid(self):
        """Test that our forms are not valid with empty required fields"""
        payment_form = MakePaymentForm({})
        self.assertFalse(payment_form.is_valid())
        self.assertEqual(payment_form.errors['stripe_id'],
                                            ['This field is required.'])

        order_form = OrderForm({})
        self.assertFalse(order_form.is_valid())
        self.assertEqual(order_form.errors['full_name'],
                                          ['This field is required.'])
        self.assertEqual(order_form.errors['phone_number'],
                                          ['This field is required.'])
        self.assertEqual(order_form.errors['street_address1'],
                                          ['This field is required.'])
        self.assertEqual(order_form.errors['postcode'],
                                          ['This field is required.'])
