---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/services-s3.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Amazon S3

[Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) (Amazon S3) is an object storage service. You store data as *objects* in containers called *buckets*. The pages in this section provide runnable examples for common Amazon S3 tasks. They show how to create and delete buckets, upload and download objects, list and delete objects, use the asynchronous client, handle errors, and verify data with checksums.

The AWS SDK for Python v4 doesn't provide presigned URLs, paginators, waiters, or the Amazon S3 Transfer Manager yet.

Install the Amazon S3 client package.

```bash
python -m pip install aws-sdk-s3
```

## Set up the examples
<a name="s3-shared-setup"></a>

The following examples use a `client` that you create by calling the `create_client()` function in the following snippet. Use the client in a `with` statement, or call `client.close()` after the last operation, as described in [Creating a service client](using-requests.md#using-requests-client).

Configure an AWS Region and credentials before you run the examples. For more information, see [Configuration variables](configuration-variables.md) and [Credential providers](credential-providers.md).

For Amazon S3-specific endpoint settings, such as `force_path_style`, see [Amazon S3 endpoint settings](config-endpoints.md#endpoints-s3).

 **Imports**

```python
from aws_sdk_s3 import S3Client, S3Config
```

 **Code**

```python
def create_client() -> S3Client:
    config = S3Config.resolve()
    return S3Client(config=config)
```

**Topics**
+ [Set up the examples](#s3-shared-setup)
+ [Work with Amazon S3 buckets](s3-bucket-operations.md)
+ [Work with Amazon S3 objects](s3-object-operations.md)
+ [Use the asynchronous Amazon S3 client](s3-async-streaming.md)
+ [Handle Amazon S3 errors](s3-errors.md)
+ [Verify data integrity with checksums](s3-checksums.md)
