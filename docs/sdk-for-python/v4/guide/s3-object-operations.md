---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/s3-object-operations.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Work with Amazon S3 objects

An object is a file and any metadata that describes the file. A *key* identifies each object in a bucket. Keys often use slash-separated prefixes, such as `reports/2026/summary.csv`, so that you can list related objects together. For more information, see [Amazon S3 objects overview](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingObjects.html) in the Amazon Simple Storage Service User Guide.

## Before you begin
<a name="s3-objects-before"></a>

The examples on this page require the following:
+ A `client` created from the snippet in [Set up the examples](services-s3.md#s3-shared-setup).
+ A bucket that you can write to, such as one created with the example in [Create a bucket](s3-bucket-operations.md#s3-create-bucket).
+ An identity that allows `s3:PutObject`, `s3:GetObject`, `s3:ListBucket`, and `s3:DeleteObject` on the bucket. The cleanup example also requires `s3:DeleteBucket`.

**Note**
Storing objects in Amazon S3 incurs charges. When you finish, delete the example bucket and its objects, as shown in [Clean up the example bucket](#s3-cleanup).

## Upload an object
<a name="s3-upload-object"></a>

For request and response details, see the [put\_object()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/s3/operations/put_object/) API reference.

Use `put_object` to upload an object of up to 5 GB in a single request. Pass the data as the `body` keyword argument. The body can be `bytes` or a file opened in binary mode.

The following example uploads a string as UTF-8 encoded text.

 **Imports**

```
from aws_sdk_s3 import S3Client
```

 **Code**

```
def upload_text(client: S3Client, bucket_name: str, key: str, text: str) -> None:
    """Upload a string as a UTF-8 text object."""
    client.put_object(
        bucket=bucket_name,
        key=key,
        body=text.encode("utf-8"),
        content_type="text/plain; charset=utf-8",
    )
```

To upload a local file, open it in binary mode and pass the file object as the body.

```
def upload_file(
    client: S3Client, bucket_name: str, key: str, file_path: str
) -> None:
    """Upload a local file as an object."""
    with open(file_path, "rb") as file:
        client.put_object(bucket=bucket_name, key=key, body=file)
```

The SDK calculates a checksum of each upload by default. For more information, see [Verify data integrity with checksums](s3-checksums.md).

## Download an object
<a name="s3-download-object"></a>

For request and response details, see the [get\_object()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/s3/operations/get_object/) API reference.

Use `get_object` to download an object. The response's `body` is a stream that holds an HTTP connection until you read the body to the end or close it. Open the body in a `with` block, which closes the body and releases the connection even if your code stops reading early. The response also has the object's metadata, such as `content_type`, `content_length`, and `last_modified`.

The following example reads a whole object into memory.

 **Imports**

```
from aws_sdk_s3 import S3Client
```

 **Code**

```
def download_bytes(client: S3Client, bucket_name: str, key: str) -> bytes:
    """Read an entire object into memory."""
    response = client.get_object(bucket=bucket_name, key=key)
    with response.body as body:
        return body.read()
```

For a large object, iterate over the body to process the data in chunks instead of holding all of it in memory. The following example writes each chunk to a local file.

```
def download_file(
    client: S3Client, bucket_name: str, key: str, file_path: str
) -> None:
    """Stream an object to a local file in chunks."""
    response = client.get_object(bucket=bucket_name, key=key)
    with response.body as body, open(file_path, "wb") as file:
        for chunk in body:
            file.write(chunk)
```

When you read the body to the end, the SDK also validates the object's checksum. For more information, see [Checksum validation for downloads](s3-checksums.md#s3-checksums-download).

## List objects
<a name="s3-list-objects"></a>

For request and response details, see the [list\_objects\_v2()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/s3/operations/list_objects_v2/) API reference.

Use `list_objects_v2` to list the objects in a bucket. Set `prefix` to list only the objects whose keys start with that value. Each response contains up to 1,000 objects. While `is_truncated` is true, pass the response's `next_continuation_token` as `continuation_token` to get the next page.

 **Imports**

```
from aws_sdk_s3 import S3Client
from aws_sdk_s3.models import Object
```

 **Code**

```
def list_objects(
    client: S3Client, bucket_name: str, prefix: str = ""
) -> list[Object]:
    """Return every object whose key starts with the prefix."""
    objects: list[Object] = []
    continuation_token = None
    while True:
        response = client.list_objects_v2(
            bucket=bucket_name,
            prefix=prefix,
            continuation_token=continuation_token,
        )
        objects.extend(response.contents or [])
        if not response.is_truncated:
            return objects
        continuation_token = response.next_continuation_token
```

Each `Object` model has the object's `key`, `size`, and `last_modified` time.

```
for obj in list_objects(client, bucket_name, prefix="reports/"):
    print(obj.key, obj.size, obj.last_modified)
```

## Delete an object
<a name="s3-delete-object"></a>

For request and response details, see the [delete\_object()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/s3/operations/delete_object/) API reference.

Use `delete_object` to delete one object. In a bucket that doesn't use versioning, the request succeeds even if no object has the key. In a bucket that uses versioning, Amazon S3 adds a delete marker instead of removing the object's data.

 **Imports**

```
from aws_sdk_s3 import S3Client
```

 **Code**

```
def delete_object(client: S3Client, bucket_name: str, key: str) -> None:
    """Delete one object."""
    client.delete_object(bucket=bucket_name, key=key)
```

## Delete multiple objects
<a name="s3-delete-objects"></a>

For request and response details, see the [delete\_objects()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/s3/operations/delete_objects/) API reference.

Use `delete_objects` to delete up to 1,000 objects in one request. Pass a `delete` dictionary whose `objects` list contains one `{"key": ...}` dictionary for each object. With `quiet=True`, the response lists only the objects that Amazon S3 couldn't delete. A successful request can still contain errors for individual objects, so check the response's `errors`.

 **Imports**

```
from aws_sdk_s3 import S3Client
```

 **Code**

```
def delete_objects(client: S3Client, bucket_name: str, keys: list[str]) -> None:
    """Delete up to 1,000 objects and raise if any deletion fails."""
    if not 1 <= len(keys) <= 1000:
        raise ValueError("A delete request must contain between 1 and 1,000 keys")
    response = client.delete_objects(
        bucket=bucket_name,
        delete={
            "objects": [{"key": key} for key in keys],
            "quiet": True,
        },
    )
    if response.errors:
        details = ", ".join(
            f"{error.key}: {error.code}" for error in response.errors
        )
        raise RuntimeError(f"S3 couldn't delete every object: {details}")
```

## Clean up the example bucket
<a name="s3-cleanup"></a>

Delete the bucket that you created for the examples, together with its objects. The following function lists the objects one page at a time and deletes each page with the `delete_objects` function from [Delete multiple objects](#s3-delete-objects). A page contains at most 1,000 keys, which is also the most that `delete_objects` accepts. After the last page, the function deletes the empty bucket.

 **Imports**

```
from aws_sdk_s3 import S3Client
```

 **Code**

```
def delete_bucket_and_objects(client: S3Client, bucket_name: str) -> None:
    """Delete every object in an unversioned bucket, then the bucket."""
    continuation_token = None
    while True:
        response = client.list_objects_v2(
            bucket=bucket_name, continuation_token=continuation_token
        )
        keys = [obj.key for obj in response.contents or [] if obj.key]
        if keys:
            delete_objects(client, bucket_name, keys)
        if not response.is_truncated:
            break
        continuation_token = response.next_continuation_token
    client.delete_bucket(bucket=bucket_name)
```

Call the cleanup function in a `finally` block, so that it runs even if an earlier step fails.

```
config = S3Config.resolve()
if config.region is None:
    raise ValueError("No AWS Region is configured")
with S3Client(config=config) as client:
    bucket_name = create_bucket(client, config.region)
    try:
        upload_text(client, bucket_name, "greetings/hello.txt", "Hello, Amazon S3")
        print(download_bytes(client, bucket_name, "greetings/hello.txt"))
    finally:
        delete_bucket_and_objects(client, bucket_name)
```

The function doesn't delete earlier versions of objects. To empty a bucket that uses versioning, see [Emptying a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/empty-bucket.html) in the Amazon Simple Storage Service User Guide.

## More information
<a name="s3-objects-more-info"></a>
+ [Uploading objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html) in the Amazon Simple Storage Service User Guide
+ [Downloading objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/download-objects.html) in the Amazon Simple Storage Service User Guide
+ [Listing object keys programmatically](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ListingKeysUsingAPIs.html) in the Amazon Simple Storage Service User Guide
+ [Deleting Amazon S3 objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjects.html) in the Amazon Simple Storage Service User Guide
+ [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html) in the Amazon Simple Storage Service API Reference
+ [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) in the Amazon Simple Storage Service API Reference
+ [ListObjectsV2](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html) in the Amazon Simple Storage Service API Reference
+ [DeleteObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html) in the Amazon Simple Storage Service API Reference
+ [DeleteObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjects.html) in the Amazon Simple Storage Service API Reference
