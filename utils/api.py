from utils.http_methods import HttpMethods

base_url = "https://rahulshettyacademy.com"
key = "?key=qaclick123"


class GoogleMapsApi():
    """Класс содержащий методы, для тестирования Google maps api"""

    @staticmethod
    def create_new_place(json):
        """Метод по созданию новой локации"""
        post_resource = "/maps/api/place/add/json"
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = HttpMethods.post(post_url, json)
        print(result_post.json())
        print(result_post.status_code)
        return result_post

    @staticmethod
    def get_new_place(place_id):
        """Метод для проверки новой локации"""
        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        print(result_get.status_code)
        return result_get

    @staticmethod
    def put_new_place(place_id, json):
        """Метод для изменения новой локации"""
        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key
        print(put_url)
        result_put = HttpMethods.put(put_url, json)
        print(result_put.json())
        print(result_put.status_code)
        return result_put

    @staticmethod
    def delete_new_place(place_id):
        """Метод для удаления новой локации"""
        delete_resource = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resource + key
        print(delete_url)
        json_for_delete_new_location = {
            "place_id": place_id
        }
        result_delete = HttpMethods.delete(delete_url, json_for_delete_new_location)
        print(result_delete.json())
        print(result_delete.status_code)
        return result_delete
