import pytest


class TestAccount:

    @pytest.mark.django_db(transaction=True)
    def test_create_user(self, django_user_model):
        user = django_user_model.objects.create_user(username='user',
                                                     email='user@user.com',
                                                     password='user',
                                                     )
        assert user.is_active, 'user not active'

    @pytest.mark.django_db(transaction=True)
    def test_email(self, django_user_model):
        with pytest.raises(ValueError):
            assert django_user_model.objects.create_user(username='user',
                                                         password='user'
                                                         ),\
                'Email is not required'


