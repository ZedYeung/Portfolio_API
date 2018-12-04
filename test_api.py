from api import app
import unittest
import json
from datetime import datetime

# unittest.TestLoader.sortTestMethodsUsing = None


class TestApi(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_homepage(self):
        resp = self.app.get('/')

        assert json.loads(resp.get_data())["Create new investments"] == "POST /investments"

    def test_empty(self):
        resp = self.app.get('/investments')
        res = json.loads(resp.get_data())

        assert resp.status_code == 200
        assert res == []

    def test_post(self):
        resp1 = self.app.post('/investments', data=json.dumps({
            "company": "Meetly",
            "quantity": 1000,
            "cost": 1000
        }), content_type='application/json')

        resp2 = self.app.post('/investments', data=json.dumps({
            "company": "Meet",
            "quantity": 100,
            "cost": 100,
            "creation_date": "2018-06-06"
        }), content_type='application/json')

        res1 = json.loads(resp1.get_data())
        res2 = json.loads(resp2.get_data())

        assert resp1.status_code == 201
        assert resp2.status_code == 201
        assert res1['company'] == 'Meetly'
        assert res1['quantity'] == 1000
        assert res1['cost'] == 1000
        assert res1['creation_date'] == datetime.today().strftime('%Y-%m-%d')

        assert res2['creation_date'] == "2018-06-06"

    def test_put(self):
        post_resp = self.app.post('/investments', data=json.dumps({
            "company": "IMIM",
            "quantity": 100,
            "cost": 100
        }), content_type='application/json')

        id = json.loads(post_resp.get_data())['id']

        resp = self.app.put('/investments/{}'.format(id), data=json.dumps({
            "company": "IMIM",
            "quantity": 200,
            "cost": 300,
            "creation_date": "2018-06-07"
        }), content_type='application/json')

        res = json.loads(resp.get_data())

        assert resp.status_code == 201
        assert res['id'] == id
        assert res['company'] == 'IMIM'
        assert res['quantity'] == 200
        assert res['cost'] == 300
        assert res['creation_date'] == "2018-06-07"

    def test_get_by_date(self):
        for i in range(1, 13):
            resp = self.app.post('/investments', data=json.dumps({
                "company": "Meetly{}".format(i),
                "quantity": 1000,
                "cost": 1000,
                "creation_date": "2017-{:02d}-01".format(i)
            }), content_type='application/json')

        get_resp = self.app.get('/investments?date=2017-08-11')

        res = json.loads(get_resp.get_data())

        eighth = res[7]

        assert len(res) == 8
        assert eighth["company"] == "Meetly8"

    def test_update_stock(self):
        for i in range(1, 13):
            resp = self.app.post('/investments', data=json.dumps({
                "company": "test",
                "quantity": i * (1 if i % 2 else - 1),
                "cost": i * i * (1 if i % 2 else - 1),
                "creation_date": "2018-{:02d}-02".format(i)
            }), content_type='application/json')

        resp = self.app.get('/investments?date=2019-01-01')

        investments = json.loads(resp.get_data())
        test = [i for i in investments if i["company"] == "test"][0]

        assert test["quantity"] == sum([i * (1 if i % 2 else - 1) for i in range(1, 13)])
        assert test["cost"] == sum([i * i * (1 if i % 2 else - 1) for i in range(1, 13)])


if __name__ == '__main__':
    unittest.main()
