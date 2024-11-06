from utils.api import GoogleMapsApi
from utils.checking import Checking
import allure


@allure.epic("Тестирование локаций в Google Map")
class TestPlace():
    json_for_tests = {
        "location": {
            "lat": -38.383494,
            "lng": 33.427362
        }, "accuracy": 50,
        "name": "Frontline house",
        "phone_number": "(+91) 983 893 3937",
        "address": "29, side layout, cohen 09",
        "types": [
            "shoe park",
            "shop"
        ],
        "website": "http://google.com",
        "language": "French-IN"
    }
    """Класс содержащий тест по работе с локацией"""

    @allure.title("Создание новой локации")
    def test_create_new_location(self):
        """Проверка создания новой локации"""
        result = GoogleMapsApi.create_new_place(self.json_for_tests)
        Checking.check_status_code(result, 200)
        Checking.check_json_fields(result, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result, 'status', 'OK')

    @allure.title("Проверка записанных данных по локации")
    def test_take_location(self):
        """Проверка данных новой локации"""
        result = GoogleMapsApi.create_new_place(self.json_for_tests)
        Checking.check_status_code(result, 200)
        place_id = result.json().get('place_id')
        result = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result, 200)
        json_list = ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language']
        Checking.check_json_fields(result, json_list)
        json_location = {'latitude': str(self.json_for_tests.get('location').get('lat')),
                         'longitude': str(self.json_for_tests.get('location').get('lng'))}
        Checking.check_json_value(result, 'location', json_location)
        Checking.check_json_value(result, 'accuracy', str(self.json_for_tests.get('accuracy')))
        Checking.check_json_value(result, 'name', self.json_for_tests.get('name'))
        Checking.check_json_value(result, 'phone_number', self.json_for_tests.get('phone_number'))
        Checking.check_json_value(result, 'address', self.json_for_tests.get('address'))
        Checking.check_json_value(result, 'types', ','.join(self.json_for_tests.get('types')))
        Checking.check_json_value(result, 'website', self.json_for_tests.get('website'))
        Checking.check_json_value(result, 'language', self.json_for_tests.get('language'))

    @allure.title("Проверка несуществующей локации")
    def test_take_location_not_in_list(self):
        """Проверка данных новой локации"""
        place_id = '0'
        result = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result, 404)
        Checking.check_json_fields(result, ['msg'])
        Checking.check_json_value(result, 'msg', "Get operation failed, looks like place_id  doesn't exists")

    @allure.title("Проверка изменения данных локации")
    def test_update_location(self):
        """Проверка данных новой локации"""
        result = GoogleMapsApi.create_new_place(self.json_for_tests)
        Checking.check_status_code(result, 200)
        place_id = result.json().get('place_id')
        json_put = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result = GoogleMapsApi.put_new_place(place_id, json_put)
        Checking.check_status_code(result, 200)
        Checking.check_json_fields(result, ['msg'])
        Checking.check_json_value(result, 'msg', "Address successfully updated")
        result = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result, 200)
        Checking.check_json_value(result, 'address', json_put.get('address'))

    @allure.title("Проверка изменения данных несуществующей локации")
    def test_update_location(self):
        """Проверка данных новой локации"""
        place_id = '0'
        json_put = {
            "place_id": place_id,
            "address": "34 Turgeneva street, RU",
            "key": "qaclick123"
        }
        result = GoogleMapsApi.put_new_place(place_id, json_put)
        Checking.check_status_code(result, 404)
        Checking.check_json_fields(result, ['msg'])
        Checking.check_json_value(result, 'msg', "Update address operation failed, looks like the data doesn't exists")

    @allure.title("Проверка удаления локации")
    def test_delete_location(self):
        """Проверка данных новой локации"""
        result = GoogleMapsApi.create_new_place(self.json_for_tests)
        Checking.check_status_code(result, 200)
        place_id = result.json().get('place_id')
        result = GoogleMapsApi.delete_new_place(place_id)
        Checking.check_status_code(result, 200)
        Checking.check_json_fields(result, ['status'])
        Checking.check_json_value(result, 'status', "OK")
        result = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result, 404)

    @allure.title("Проверка удаления несуществующей локации")
    def test_delete_location_not_in_list(self):
        """Проверка данных новой локации"""
        place_id = '0'
        result = GoogleMapsApi.delete_new_place(place_id)
        Checking.check_status_code(result, 404)
        Checking.check_json_fields(result, ['msg'])
        Checking.check_json_value(result, 'msg', "Delete operation failed, looks like the data doesn't exists")