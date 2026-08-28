---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/using-requests.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Making requests and handling responses
<a name="using-requests"></a>

Before making a request, instantiate the generated client for the service and construct the operation's input object. Each operation returns a service-specific output object. Type checkers and editors can use the generated types to identify available members before the application runs.

The operation examples on this page run inside a coroutine and use `await`. For application entry points and event loop behavior, see [Using the SDK asynchronously](using-async.md).

## Creating a service client
<a name="using-requests-client"></a>

Create the client using the configuration object required by the service. This example uses a DynamoDB client that overrides the Region; credentials come from the default credential chain.

```
from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.config import AsyncDynamoDBConfig

config = await AsyncDynamoDBConfig.resolve(region="us-east-1")
client = AsyncDynamoDBClient(config=config)
```

For other client options and credential configuration, see [Configuration](configuring.md).

Reuse a client for operations that use the same client-wide configuration. Create a separate client when you need different client-wide configuration.

The client owns network resources, such as HTTP connections. The client is an *asynchronous context manager*: an object that an `async with` statement can open and close. Leaving the `async with` block closes the client and releases those resources.

```
from aws_sdk_dynamodb.models import ListTablesInput

async with client:
    response = await client.list_tables(
        input=ListTablesInput(limit=25)
    )
```

When the client's lifetime doesn't match a single block, such as a client that the application creates at startup and shares across functions, call `await client.close()` after the last operation. The following example closes the client in a `finally` block.

```
try:
    response = await client.list_tables(
        input=ListTablesInput(limit=25)
    )
finally:
    await client.close()
```

Don't invoke operations on a closed client; create a new client instead.

## Constructing a typed request
<a name="using-requests-inputs"></a>

Import the operation input object from the service package and pass it as the operation's `input` parameter. All generated types for a service, including operation inputs and outputs, are located in the service package's `models` module, such as `aws_sdk_dynamodb.models`. Model member names use Python snake case.

```
from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.models import ListTablesInput, ListTablesOutput

async def list_table_page(
    client: AsyncDynamoDBClient,
    start_name: str | None = None,
) -> ListTablesOutput:
    request = ListTablesInput(
        exclusive_start_table_name=start_name,
        limit=25,
    )
    return await client.list_tables(input=request)
```

Operations also accept optional plugins that customize configuration for that invocation only. For details, see [Customizing SDK behavior with plugins and interceptors](using-extensions.md).

## Reading optional response members
<a name="using-requests-outputs"></a>

Generated response members are optional when a service can omit them. Check for `None`, or use an appropriate empty value, before processing the result.

```
page = await list_table_page(client)
for table_name in page.table_names or []:
    print(table_name)

if page.last_evaluated_table_name is not None:
    print(f"continue after: {page.last_evaluated_table_name}")
```

## Handling paginated responses
<a name="using-requests-pagination"></a>

The AWS SDK for Python doesn't currently provide paginator objects, so applications must iterate pages explicitly. When an operation returns a continuation token, pass it as the start token member of the next request. Continue until the response omits the token.

```
from collections.abc import AsyncIterator

from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.models import ListTablesInput

async def iter_table_names(
    client: AsyncDynamoDBClient,
) -> AsyncIterator[str]:
    start_name: str | None = None

    while True:
        page = await client.list_tables(input=ListTablesInput(
            exclusive_start_table_name=start_name,
            limit=25,
        ))
        for table_name in page.table_names or []:
            yield table_name

        start_name = page.last_evaluated_table_name
        if start_name is None:
            return
```

Token member names and page-size limits are operation-specific. Process each page as it arrives, since the complete result set might be too large to keep in memory.

## Following the modeled shape
<a name="using-requests-model-shapes"></a>

Most operation responses are instances of generated Python classes rather than untyped response dictionaries. Their members correspond to fields defined by the service API, and each member's type depends on the API model. For example, a field modeled as a map is represented by a typed Python dictionary, while a field modeled as a document is represented by a `Document` object that can contain object, array, scalar, or null data.

DynamoDB items are one example of a modeled map. Each item is a dictionary whose keys are attribute names. Each value is a generated class that identifies the DynamoDB attribute type, such as `AttributeValueS` for a string. The following example checks the value's class before reading it.

```
from aws_sdk_dynamodb.models import AttributeValueS, GetItemInput

response = await client.get_item(
    input=GetItemInput(
        table_name="Books",
        key={"id": AttributeValueS(value="book-123")},
    )
)

if response.item is not None:
    title = response.item.get("title")
    if isinstance(title, AttributeValueS):
        print(title.value)
```

## Narrowing union members
<a name="using-requests-unions"></a>

A union is a model member that can contain one of several possible variants. The SDK represents each variant with a different generated Python class, and only one variant is present in a union value. Use `isinstance()` or pattern matching to identify that class before accessing its `value`. The DynamoDB attribute value in the preceding section is one example of a union: each `AttributeValue` class is a variant of that union.

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Python. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-python` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
