from django.urls import reverse
import pytest


@pytest.mark.django_db
class TestViewsCase:

    def test_index_200(self, client):
        url = reverse('catalog:index')
        response = client.get(url)
        assert response.status_code == 200

    def test_authors(self, client):
        url = reverse('catalog:author')
        response = client.get(url)
        assert response.charset == 'utf-8'
        assert response.client == client
        assert 'catalog/author_index.html' in (t.name for t in response.templates)

    def test_add_book_post(self, client):
        url = reverse('catalog:addbook_url')
        response = client.post(url, {'title': 'Python CookBook', 'description': 'Lorem, ipsum dolor \
            sit amet consectetur adipisicing elit. Ratione maxime possimus odio, \
                aliquid in cum corporis vero vitae ullam quia amet molestiae rerum \
                    quos distinctio nemo nostrum. Culpa, fuga. Ipsam? Commodi consectetur\
                         tempora quisquam dolorem laboriosam vero eligendi eius culpa accusantium?\
                              Similique maxime culpa ad eveniet iure natus, porro nemo repudiandae \
                                  praesentium sed illum, unde iste explicabo, dolores vel hic? Pariatur, \
                                      quod exercitationem ipsum illum labore eius velit nobis mol'})
        assert response.status_code == 200

