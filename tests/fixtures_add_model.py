from flask_restful import fields

from flask_restful_swagger import swagger

###############################################################################
# Copy setup objects from examples/basic.py
###############################################################################


class MockBasicObject:
    pass


class MockBasicWithSwaggerMetadata1:
    swagger_metadata = {"an_enum": {"enum": ["one", "two", "three"]}}


class MockBasicWithSwaggerMetadata2:
    def __init__(self, arg1, an_enum):
        pass

    swagger_metadata = {"an_enum": {"enum": ["one", "two", "three"]}}


class MockTodoItem:
    """This is an example of a model class that has parameters in its constructor
    and the fields in the swagger spec are derived from the parameters
    to __init__.
    In this case we would have args, arg2 as required parameters and arg3 as
    optional parameter.
    """

    def __init__(self, arg1, arg2, arg3="123"):
        pass


class MockModelWithResourceFieldsNoRequired:
    resource_fields = {"a_string": fields.String()}


class MockModelWithResourceFieldsWithRequired:
    resource_fields = {"a_string": fields.String()}

    required = ["a_string"]


@swagger.nested(
    a_nested_attribute=MockModelWithResourceFieldsNoRequired.__name__,
    a_list_of_nested_types=MockModelWithResourceFieldsNoRequired.__name__,
)
class MockModelWithResourceFieldsWithRequiredWithSwaggerMetadata:
    resource_fields = {
        "a_string": fields.String(),
        "an_enum": fields.String,
    }
    required = ["a_string"]
    swagger_metadata = {"an_enum": {"enum": ["one", "two", "three"]}}


@swagger.nested(
    a_nested_attribute=MockModelWithResourceFieldsNoRequired.__name__,
    a_list_of_nested_types=MockModelWithResourceFieldsNoRequired.__name__,
)
class MockTodoItemWithResourceFields:
    """This is an example of how Output Fields work
      (http://flask-restful.readthedocs.org/en/latest/fields.html).
      Output Fields lets you add resource_fields to your model in which you
      specify the output of the model when it gets sent as an HTTP response.
      flask-restful-swagger takes advantage of this to specify the fields in
      the model
    """

    resource_fields = {
        "a_string": fields.String(attribute="a_string_field_name"),
        "a_formatted_string": fields.FormattedString,
        "an_enum": fields.String,
        "an_int": fields.Integer,
        "a_bool": fields.Boolean,
        "a_url": fields.Url,
        "a_float": fields.Float,
        "an_float_with_arbitrary_precision": fields.Arbitrary,
        "a_fixed_point_decimal": fields.Fixed,
        "a_datetime": fields.DateTime,
        "a_list_of_strings": fields.List(fields.String),
        "a_nested_attribute": fields.Nested(
            MockModelWithResourceFieldsNoRequired.resource_fields
        ),
        "a_list_of_nested_types": fields.List(
            fields.Nested(MockModelWithResourceFieldsNoRequired.resource_fields)
        ),
    }

    # Specify which of the resource fields are required
    required = ["a_string"]


###############################################################################
# Tests Fixtures
###############################################################################

fixtures_integration_test_add_model = [
    (MockBasicObject, [], [], []),
    (MockTodoItem, ["arg1", "arg2", "arg3"], ["arg1", "arg2"], ["arg3"]),
    (MockModelWithResourceFieldsNoRequired, ["a_string"], [], []),
    (
        MockTodoItemWithResourceFields,
        [
            "a_string",
            "a_formatted_string",
            "an_enum",
            "an_int",
            "a_bool",
            "a_url",
            "a_float",
            "an_float_with_arbitrary_precision",
            "a_fixed_point_decimal",
            "a_datetime",
            "a_list_of_strings",
            "a_nested_attribute",
            "a_list_of_nested_types",
        ],
        ["a_string"],
        [],
    ),
    (MockBasicWithSwaggerMetadata1, [], [], []),
    (MockBasicWithSwaggerMetadata2, [], [], []),
]

fixtures_add_model_get_docs = [
    MockBasicObject,
    MockTodoItem,
    MockModelWithResourceFieldsNoRequired,
    MockTodoItemWithResourceFields,
]

fixtures_add_model_with_resource_fields_without_swagger_metadata = [
    MockModelWithResourceFieldsWithRequired,
]

fixtures_add_model_with_resource_fields_with_nested = [
    MockTodoItemWithResourceFields,
]

fixtures_add_model_with_resource_fields_nested_swagger_metadata = [
    MockModelWithResourceFieldsWithRequiredWithSwaggerMetadata,
]


fixtures_add_model_init = [
    MockBasicObject,
    MockTodoItem,
]

fixtures_add_model_init_parsing_args = [
    [MockTodoItem, ["arg1", "arg2"], [("arg3", "123")]]
]