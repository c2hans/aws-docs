---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/s3-checksums.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Verify data integrity with checksums

Amazon S3 uses checksums to confirm that the data it stores is the data that you sent, and that the data you download is the data that it stores. The SDK calculates and validates these checksums by default. For more information, see [Checking object integrity in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the Amazon Simple Storage Service User Guide.

## Before you begin
<a name="s3-checksums-before"></a>

The examples on this page require the following:
+ A `client` created from the snippet in [Set up the examples](services-s3.md#s3-shared-setup).
+ A bucket that you can write to, such as one created with the example in [Create a bucket](s3-bucket-operations.md#s3-create-bucket).
+ An identity that allows `s3:PutObject` and `s3:GetObject` on the bucket.

## Checksums for uploads
<a name="s3-checksums-upload"></a>

For request and response details, see the [put\_object()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/s3/operations/put_object/) API reference.

When you upload an object, the SDK calculates a CRC64NVME checksum of the body and sends it with the request. Amazon S3 calculates the checksum of the data that it receives and rejects the upload if the two values don't match. To use a different algorithm, set `checksum_algorithm`, for example to `"SHA256"`. The `ChecksumAlgorithm` class in `aws_sdk_s3.models` lists the algorithm names. The response contains the checksum that Amazon S3 stored, such as `checksum_sha256`.

 **Imports**

```python
from aws_sdk_s3 import S3Client
```

 **Code**

```python
def upload_with_sha256(
    client: S3Client, bucket_name: str, key: str, data: bytes
) -> str | None:
    """Upload bytes with a SHA-256 checksum and return the stored checksum."""
    response = client.put_object(
        bucket=bucket_name,
        key=key,
        body=data,
        checksum_algorithm="SHA256",
    )
    return response.checksum_sha256
```

## Checksum validation for downloads
<a name="s3-checksums-download"></a>

For request and response details, see the [get\_object()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/s3/operations/get_object/) API reference.

When you call `get_object`, the SDK sets `checksum_mode` to `ENABLED`, so Amazon S3 returns the checksum that it stored for the object. The SDK calculates a checksum of the body as you read it. When you read the body to the end, the SDK compares the two values. If they don't match, the last read raises `ChecksumMismatchError` from `smithy_aws_core.checksums`. The earlier reads have already returned their data. If you stop reading before the end, the SDK doesn't validate the data. The SDK also doesn't validate the composite checksums of objects that were uploaded in multiple parts.

Because the SDK detects a mismatch only at the end of the body, the following example removes a partly written file when validation fails.

 **Imports**

```python
import os

from aws_sdk_s3 import S3Client
from smithy_aws_core.checksums import ChecksumMismatchError
```

 **Code**

```python
def download_file_verified(
    client: S3Client, bucket_name: str, key: str, file_path: str
) -> None:
    """Stream an object to a file, and remove the file if validation fails."""
    response = client.get_object(bucket=bucket_name, key=key)
    try:
        with response.body as body, open(file_path, "wb") as file:
            for chunk in body:
                file.write(chunk)
    except ChecksumMismatchError:
        os.remove(file_path)
        raise
```

## Configure checksum behavior
<a name="s3-checksums-config"></a>

Two configuration fields control when the SDK uses checksums. Both accept `"when_supported"`, which is the default, and `"when_required"`.
+ `request_checksum_calculation` applies to uploads. With `"when_required"`, the SDK calculates a checksum only when the operation requires one, such as `delete_objects`, or when you set `checksum_algorithm`.
+ `response_checksum_validation` applies to downloads. With `"when_required"`, the SDK validates a response only when you set `checksum_mode="ENABLED"` on the request.

Use `"when_required"` if you send requests to a storage service that implements the Amazon S3 API but doesn't support these checksums. The following example sets both fields when it resolves the configuration.

```python
config = S3Config.resolve(
    request_checksum_calculation="when_required",
    response_checksum_validation="when_required",
)
```

You can also set the values with the `AWS_REQUEST_CHECKSUM_CALCULATION` and `AWS_RESPONSE_CHECKSUM_VALIDATION` environment variables, or with settings of the same names as the fields in the shared AWS `config` file.

```ini
# ~/.aws/config
[default]
request_checksum_calculation = when_required
response_checksum_validation = when_required
```

## More information
<a name="s3-checksums-more-info"></a>
+ [Checking object integrity in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the Amazon Simple Storage Service User Guide
+ [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html) in the Amazon Simple Storage Service API Reference
+ [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) in the Amazon Simple Storage Service API Reference
