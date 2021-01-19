from pytest import fail


class TestBaseApplication:
    def test_factory_function_exists(self):
        try:
            __import__('app').create_app
        except AttributeError:
            fail('Make sure create_app function is defined')


    def test_factory_function_return_flask_instance(self):
        given = __import__('app').create_app()
        expected = __import__('flask').Flask

        assert isinstance(given, expected), \
            'The function create_app does not return an instance of Flask'


    def test_flask_routes(self):
        ...
