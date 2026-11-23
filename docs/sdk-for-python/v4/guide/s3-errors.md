---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/s3-errors.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Handle Amazon S3 errors

Amazon S3 operations raise a generated exception class for each error that the operation models. Import the classes from `aws_sdk_s3.models`. Each class is a subclass of `ServiceError`. Each exception has a `message` and a `response_metadata` field with the request IDs. For example, the modeled errors include `NoSuchKey` for `get_object` and `NoSuchBucket` for `list_objects_v2`. For general guidance, see [Handling errors](using-errors.md).

## Before you begin
<a name="s3-errors-before"></a>

The examples on this page require the following:
+ A `client` created from the snippet in [Set up the examples](services-s3.md#s3-shared-setup).
+ An identity that allows `s3:GetObject` and `s3:ListBucket` on the bucket that you read from.

## Handle a missing object
<a name="s3-errors-no-such-key"></a>

For request and response details, see the [get\_object()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/s3/operations/get_object/) API reference.

`get_object` raises `NoSuchKey` when the bucket has no object with the key. Amazon S3 returns this error only to an identity that has the `s3:ListBucket` permission on the bucket. For any other identity, Amazon S3 returns an access denied error instead.

 **Imports**

```python
from aws_sdk_s3 import S3Client
from aws_sdk_s3.models import NoSuchKey
```

 **Code**

```python
def read_object_if_exists(
    client: S3Client, bucket_name: str, key: str
) -> bytes | None:
    """Return an object's contents, or None if the key doesn't exist."""
    try:
        response = client.get_object(bucket=bucket_name, key=key)
    except NoSuchKey:
        return None
    with response.body as body:
        return body.read()
```

## Handle a missing bucket
<a name="s3-errors-no-such-bucket"></a>

For request and response details, see the [list\_objects\_v2()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/s3/operations/list_objects_v2/) API reference.

`list_objects_v2` raises `NoSuchBucket` when the bucket doesn't exist.

 **Imports**

```python
from aws_sdk_s3 import S3Client
from aws_sdk_s3.models import NoSuchBucket
```

 **Code**

```python
def first_keys(client: S3Client, bucket_name: str) -> list[str] | None:
    """Return up to 10 keys, or None if the bucket doesn't exist."""
    try:
        response = client.list_objects_v2(bucket=bucket_name, max_keys=10)
    except NoSuchBucket:
        return None
    return [obj.key for obj in response.contents or [] if obj.key]
```

Errors that an operation doesn't model, such as access denied errors, don't have their own class. To handle them, catch `SmithyError` at an application boundary, as described in [Handling errors at an application boundary](using-errors.md#using-errors-sdk).

## More information
<a name="s3-errors-more-info"></a>
+ [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) in the Amazon Simple Storage Service API Reference
+ [ListObjectsV2](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html) in the Amazon Simple Storage Service API Reference
