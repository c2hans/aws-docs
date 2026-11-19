---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/s3-bucket-operations.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Work with Amazon S3 buckets

A bucket is a container for objects. You create each general purpose bucket in one AWS Region. Its name must be unique across all AWS accounts in the partition. For the naming rules, see [General purpose bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html) in the Amazon Simple Storage Service User Guide. The examples name each bucket `python-example-bucket-` followed by a random UUID, so that the name is unique.

## Before you begin
<a name="s3-buckets-before"></a>

The examples on this page require the following:
+ A `client` created from the snippet in [Set up the examples](services-s3.md#s3-shared-setup).
+ An identity that allows `s3:CreateBucket`, `s3:ListAllMyBuckets`, and `s3:DeleteBucket`. For the permissions that each Amazon S3 operation requires, see [Required permissions for Amazon S3 API operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-policy-actions.html) in the Amazon Simple Storage Service User Guide.

## Create a bucket
<a name="s3-create-bucket"></a>

For request and response details, see the [create\_bucket()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/s3/operations/create_bucket/) API reference.

Use `create_bucket` to create a bucket in the client's Region. Outside the US East (N. Virginia) Region, pass the Region as the `location_constraint` in the `create_bucket_configuration` dictionary. In `us-east-1`, omit the configuration, because Amazon S3 rejects a `us-east-1` location constraint.

 **Imports**

```
import uuid

from aws_sdk_s3 import S3Client
```

 **Code**

```
def create_bucket(client: S3Client, region: str) -> str:
    """Create a bucket with a unique name and return the name."""
    bucket_name = f"python-example-bucket-{uuid.uuid4()}"
    if region == "us-east-1":
        client.create_bucket(bucket=bucket_name)
    else:
        client.create_bucket(
            bucket=bucket_name,
            create_bucket_configuration={"location_constraint": region},
        )
    return bucket_name
```

Pass the Region that the client uses. When you create the client from a resolved configuration, that Region is `config.region`.

```
config = S3Config.resolve()
if config.region is None:
    raise ValueError("No AWS Region is configured")
with S3Client(config=config) as client:
    bucket_name = create_bucket(client, config.region)
```

## List buckets
<a name="s3-list-buckets"></a>

For request and response details, see the [list\_buckets()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/s3/operations/list_buckets/) API reference.

Use `list_buckets` to list the general purpose buckets that your account owns in all Regions. Set `max_buckets` to request the buckets one page at a time. Continue with `continuation_token` until the response contains no token. Each `Bucket` model in a page has the bucket's `name`, `creation_date`, and `bucket_region`.

 **Imports**

```
from aws_sdk_s3 import S3Client
from aws_sdk_s3.models import Bucket
```

 **Code**

```
def list_buckets(client: S3Client) -> list[Bucket]:
    """Return every general purpose bucket that the account owns."""
    buckets: list[Bucket] = []
    continuation_token = None
    while True:
        response = client.list_buckets(
            max_buckets=1000, continuation_token=continuation_token
        )
        buckets.extend(response.buckets or [])
        continuation_token = response.continuation_token
        if not continuation_token:
            return buckets
```

## Delete a bucket
<a name="s3-delete-bucket"></a>

For request and response details, see the [delete\_bucket()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/s3/operations/delete_bucket/) API reference.

A bucket must be empty before you can delete it. If the bucket still contains objects, Amazon S3 rejects the request with a `BucketNotEmpty` error. To delete the objects and then the bucket, see [Clean up the example bucket](s3-object-operations.md#s3-cleanup).

 **Imports**

```
from aws_sdk_s3 import S3Client
```

 **Code**

```
def delete_bucket(client: S3Client, bucket_name: str) -> None:
    """Delete an empty bucket."""
    client.delete_bucket(bucket=bucket_name)
```

## More information
<a name="s3-buckets-more-info"></a>
+ [General purpose buckets overview](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html) in the Amazon Simple Storage Service User Guide
+ [Creating a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) in the Amazon Simple Storage Service User Guide
+ [Deleting a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-bucket.html) in the Amazon Simple Storage Service User Guide
+ [CreateBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html) in the Amazon Simple Storage Service API Reference
+ [ListBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBuckets.html) in the Amazon Simple Storage Service API Reference
+ [DeleteBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html) in the Amazon Simple Storage Service API Reference
