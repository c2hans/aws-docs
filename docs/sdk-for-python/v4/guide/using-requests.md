---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/using-requests.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Making requests and handling responses

Each service package of the AWS SDK for Python v4 provides a generated client with one method for each service operation. You call an operation with keyword arguments. It returns a typed output object. Type checkers use the generated types to check arguments and response members before the application runs.

The examples on this page use the synchronous DynamoDB client. The asynchronous client takes the same arguments and returns the same output types, but you `await` each call. For the differences between the two clients, see [Synchronous and asynchronous clients](using-sync-async.md).

## Creating a service client
<a name="using-requests-client"></a>

Create the client with a configuration object that you resolve for the service. The following example resolves a DynamoDB configuration that sets the Region. The client gets credentials from the default credential resolver chain.

```
from aws_sdk_dynamodb import DynamoDBClient, DynamoDBConfig

config = DynamoDBConfig.resolve(region="us-east-1")
client = DynamoDBClient(config=config)
```

If you create a client without a configuration object, the client resolves one from the environment the first time you use it. For other client options and credential configuration, see [Configuration](configuring.md).

Reuse a client for operations that use the same client-wide configuration. Create a separate client when you need different client-wide configuration.

The client holds network resources, such as HTTP connections. The client is a *context manager*, an object that a `with` statement opens and closes. Leaving the `with` block closes the client and releases those resources.

```
with DynamoDBClient(config=config) as client:
    response = client.list_tables(limit=25)
```

When the client's lifetime doesn't match a single block, such as a client that the application creates at startup and shares across functions, call `client.close()` after the last operation. The following example closes the client in a `finally` block.

```
client = DynamoDBClient(config=config)
try:
    response = client.list_tables(limit=25)
finally:
    client.close()
```

Calling an operation on a closed client raises a `RuntimeError`. Create a new client instead.

## Passing keyword arguments
<a name="using-requests-inputs"></a>

Operations take keyword arguments that are named after the members of the operation's input. The names use Python snake case, such as `table_name` and `exclusive_start_table_name`. You can't pass individual members by position. To pass the whole request as one object instead, see [Passing a request object](#using-requests-request-object).

```
from aws_sdk_dynamodb import DynamoDBClient
from aws_sdk_dynamodb.models import ListTablesOutput

def list_table_page(
    client: DynamoDBClient,
    start_name: str | None = None,
) -> ListTablesOutput:
    return client.list_tables(
        exclusive_start_table_name=start_name,
        limit=25,
    )
```

The client checks the arguments before it sends a request:
+ Each required input member is a required keyword argument. If you omit one, the client raises a `TypeError` that names the missing argument.
+ An argument name that the operation doesn't define also raises a `TypeError`.
+ Passing `None` for an optional argument is the same as omitting it.

An operation with no required input members can be called with no arguments, such as `client.list_tables()`.

The generated types for a service are in the service package's `models` module, such as `aws_sdk_dynamodb.models`. This module includes the input and output class of each operation. You can use these classes in type annotations, as the preceding example does with `ListTablesOutput`.

Every operation also accepts a `plugins` keyword argument. The plugins customize a copy of the client's configuration for that call only. For details, see [Customizing SDK behavior with plugins and interceptors](using-extensions.md).

## Passing nested values
<a name="using-requests-nested"></a>

Some arguments take structures, unions, or lists and maps of them. For these values, you can pass generated model objects or plain dictionaries. Before the client sends the request, it converts each dictionary to its model class. A dictionary can contain model objects at any depth. Inside a model object, nested structures and unions must also be model objects. The client doesn't convert dictionaries inside a model object, so it raises a `TypeError`.

A dictionary for a structure uses the structure's member names as keys. A dictionary for a union must have exactly one key, which is the Python name of the union member that it sets. For a DynamoDB attribute value, the key is `"s"` for a string, `"n"` for a number, `"bool_"` for a Boolean, and `"null"` for a null value. Other attribute types follow the same pattern, such as `"m"` for a map and `"l"` for a list. If a union dictionary sets no member, more than one member, or an unknown member, the client raises a `TypeError`. This includes the uppercase keys that Boto3 uses, such as `"S"`.

The following two calls send the same request.

```
from aws_sdk_dynamodb.models import AttributeValueS

# Generated model objects
response = client.get_item(
    table_name="Books",
    key={"id": AttributeValueS(value="book-123")},
)

# Plain dictionaries
response = client.get_item(
    table_name="Books",
    key={"id": {"s": "book-123"}},
)
```

The following call mixes a model object with dictionaries in one item.

```
client.put_item(
    table_name="Books",
    item={
        "id": AttributeValueS(value="book-123"),
        "pages": {"n": "320"},
        "in_print": {"bool_": True},
    },
)
```

The client doesn't need to convert model objects, so they're the faster choice for large requests and frequent calls. The examples in this guide use model objects.

## Passing a request object
<a name="using-requests-request-object"></a>

Instead of keyword arguments, you can pass the whole request as a single positional argument. The request is either the operation's input model, such as `PutItemInput`, or a dictionary with the same members. Import the input model from the service's `models` module.

```
from aws_sdk_dynamodb.models import AttributeValueS, PutItemInput

request = PutItemInput(
    table_name="Books",
    item={"id": AttributeValueS(value="book-123")},
)
client.put_item(request)
```

To type-check a request dictionary, annotate it with the operation's generated `TypedDict`. Its name is the input class name with a `Dict` suffix, such as `PutItemInputDict`. A type checker reports missing required keys and values of the wrong type. At runtime, the value is a plain `dict`.

```
from aws_sdk_dynamodb.models import PutItemInputDict

params: PutItemInputDict = {
    "table_name": "Books",
    "item": {
        "id": {"s": "book-123"},
        "title": {"s": "Example Book"},
    },
}
client.put_item(params)
```

The client checks a request object the same way that it checks keyword arguments. Pass the request or keyword arguments, not both. The only keyword argument that you can add to a request object is `plugins`. Passing both, or more than one positional argument, raises a `TypeError`.

## Reading optional response members
<a name="using-requests-outputs"></a>

Each operation returns an instance of its generated output class. You read response members as attributes. A member is optional when the service can omit it. Check for `None`, or use an appropriate empty value, before you process the result.

```
page = list_table_page(client)
for table_name in page.table_names or []:
    print(table_name)

if page.last_evaluated_table_name is not None:
    print(f"continue after: {page.last_evaluated_table_name}")
```

## Handling paginated responses
<a name="using-requests-pagination"></a>

The AWS SDK for Python v4 doesn't provide paginators yet, so you request each page yourself. When a response includes a continuation member, pass it to the next call as the matching start argument. Continue until the response omits the continuation member.

```
from collections.abc import Iterator

from aws_sdk_dynamodb import DynamoDBClient

def iter_table_names(client: DynamoDBClient) -> Iterator[str]:
    start_name: str | None = None

    while True:
        page = client.list_tables(
            exclusive_start_table_name=start_name,
            limit=25,
        )
        for table_name in page.table_names or []:
            yield table_name

        start_name = page.last_evaluated_table_name
        if start_name is None:
            return
```

Requests and responses use the same generated types, so you can pass an output member directly to the next call. For example, a DynamoDB `query` response has a `last_evaluated_key` member that you can pass to the next `query` call as `exclusive_start_key=page.last_evaluated_key`.

Continuation member names and page-size limits are operation-specific. Process each page as it arrives, because the complete result set might be too large to keep in memory.

## Following the modeled shape
<a name="using-requests-model-shapes"></a>

Operation responses are instances of generated Python classes, not untyped dictionaries. Each member corresponds to a field in the service API. The API model sets the member's type. For example, the SDK returns a map field as a typed Python dictionary. It returns a document field as a `Document` object, which can hold object, array, scalar, or null data.

DynamoDB items are one example of a modeled map. Each item is a dictionary whose keys are attribute names. Each value is a generated class that identifies the DynamoDB attribute type, such as `AttributeValueS` for a string. The following example checks the value's class before it reads the value.

```
from aws_sdk_dynamodb.models import AttributeValueS

response = client.get_item(
    table_name="Books",
    key={"id": AttributeValueS(value="book-123")},
)

if response.item is not None:
    title = response.item.get("title")
    if isinstance(title, AttributeValueS):
        print(title.value)
```

## Narrowing union members
<a name="using-requests-unions"></a>

A union is a model member that holds exactly one of several possible variants. The SDK represents each variant with a different generated Python class. Use `isinstance()` or pattern matching to identify the class before you access its `value`. The DynamoDB attribute value in the preceding section is a union. Each `AttributeValue` class is one of its variants. Responses always contain variant classes, even if you passed dictionaries in the request.

Some responses nest unions inside unions. In the following Amazon Bedrock Runtime example, `response.output` can be one of several output variants. The function first checks for the message variant and then checks each content block for the text variant.

```
from aws_sdk_bedrock_runtime.models import (
    ContentBlockText,
    ConverseOperationOutput,
    ConverseOutputMessage,
)

def print_converse_text(response: ConverseOperationOutput) -> None:
    if not isinstance(response.output, ConverseOutputMessage):
        raise RuntimeError(
            f"Unexpected output type: {type(response.output).__name__}"
        )

    for block in response.output.value.content:
        if isinstance(block, ContentBlockText):
            print(block.value)
```
