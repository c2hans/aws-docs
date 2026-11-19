---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/using-errors.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Handling errors

AWS service calls can fail for reasons that your application must anticipate. For example, a resource doesn't exist, a request is throttled, or the network is unreachable. The AWS SDK for Python v4 raises a typed exception for each failure instead of returning an error code, so you can handle each kind of failure in its own `except` clause. Synchronous and asynchronous clients raise the same exception types. This page shows how to catch modeled service errors, handle SDK runtime exceptions, and understand the retries that the SDK makes before an error reaches your code.

## Handling a modeled service error
<a name="using-errors-modeled"></a>

Modeled exceptions describe failures that a service operation can return. The following example catches `ResourceNotFoundException` because a missing DynamoDB table is an expected result for this application. It lets every other failure propagate.

```
from aws_sdk_dynamodb import DynamoDBClient
from aws_sdk_dynamodb.models import ResourceNotFoundException

def table_exists(client: DynamoDBClient, table_name: str) -> bool:
    try:
        client.describe_table(table_name=table_name)
    except ResourceNotFoundException:
        return False
    return True
```

Avoid catching a broad exception near an operation when the application doesn't know how to recover from it.

## Handling errors at an application boundary
<a name="using-errors-sdk"></a>

An application boundary is a place where unhandled failures receive one common response, such as a command-line entry point, job handler, or web request handler. `SmithyError` is the base class for exceptions raised by the SDK, including modeled service exceptions and SDK runtime exceptions.

The following example catches `SmithyError` after `table_exists` has handled the specific failure that it understands. The boundary translates any remaining SDK failure into an application error.

```
from smithy_core.exceptions import SmithyError

def safely_check_table(client: DynamoDBClient, table_name: str) -> bool:
    try:
        return table_exists(client, table_name)
    except SmithyError as error:
        raise RuntimeError(
            "The SDK could not complete the DynamoDB request"
        ) from error
```

Exceptions don't expose a common response dictionary. Read fields only from the concrete generated exception type that defines them.

If you omit a required keyword argument, pass an unknown keyword argument, or pass an invalid nested value, the operation raises `TypeError` before it sends a request. A `TypeError` isn't a service error and isn't a `SmithyError`, so the preceding `except` clause doesn't catch it. Treat it as a bug in the calling code. For how operations take arguments, see [Making requests and handling responses](using-requests.md).

## Understanding retry behavior
<a name="using-errors-retries"></a>

The SDK retry strategy can repeat a request after a failure that it classifies as retryable. It stops after a bounded number of attempts. An exception that reaches the application can mean that the SDK has already attempted the request more than once and couldn't complete it. For which errors the SDK retries and how to configure retries, see [Retries](config-retries.md).

An application-level retry starts a new operation invocation. Add one only for a transient failure and only when repeating the operation is safe. An operation is *idempotent* when sending the same request again doesn't cause an additional change after the first successful request. Always limit retry attempts so that a persistent failure doesn't cause an unbounded retry loop or add sustained load to the service.

Some operations provide an idempotency token to identify repeated requests. Others can partially succeed, so retrying the entire request might repeat work that already completed. These behaviors are service specific. Check the operation API reference before you add an application retry. For DynamoDB examples, see [Use DynamoDB batch operations and transactions](dynamodb-grouped-operations.md).
