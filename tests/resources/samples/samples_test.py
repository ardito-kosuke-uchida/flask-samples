from ..resource_test import ResourceTest, skip_auth
from nose.tools import eq_, assert_dict_equal, assert_list_equal



class SamplesTest(ResourceTest):

    @skip_auth
    def test_getone_ok(self):
        response = self.client.get(
            '/samples/1',
            follow_redirects=True,
        )

        eq_(response.status_code, 200)
        assert_dict_equal(
            response.get_json(),
            {'name': 'uchida', 'age': 30},
        )

    def test_getone_failed(self):
        response = self.client.get(
            '/samples/1',
            follow_redirects=True,
        )

        eq_(response.status_code, 400)

    @skip_auth
    def test_getlist_ok(self):
        response = self.client.get(
            '/samples',
            follow_redirects=True,
        )

        eq_(response.status_code, 200)
        assert_list_equal(
            response.get_json(),
            [
                {'name': 'uchida', 'age': 30},
                {'name': 'kosuke', 'age': 40},
            ],
        )

    def test_getlist_failed(self):
        response = self.client.get(
            '/samples',
            follow_redirects=True,
        )

        eq_(response.status_code, 400)
