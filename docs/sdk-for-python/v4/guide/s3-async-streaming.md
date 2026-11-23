---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/s3-async-streaming.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Use the asynchronous Amazon S3 client

The asynchronous client, `AsyncS3Client`, has the same operations, keyword arguments, and models as the synchronous client. You `await` each operation. For a comparison of the two client types, see [Synchronous and asynchronous clients](using-sync-async.md).

## Before you begin
<a name="s3-async-before"></a>

The example on this page requires the following:
+ A bucket that you can write to. Replace `amzn-s3-demo-bucket` in the example with the name of your bucket.
+ A local file named `summary.csv` in the current directory.
+ An identity that allows `s3:PutObject` and `s3:GetObject` on the bucket.

## Upload and download with an asynchronous client
<a name="s3-async-upload-download"></a>

The following program uploads a local file, streams the object back to a second file in chunks, and then reads the object into memory. Iterate over the body with `async for` for large objects. Use `await response.body.read()` only for objects that fit in memory.

 **Imports**

```python
import asyncio

from aws_sdk_s3 import AsyncS3Client, AsyncS3Config
```

 **Code**

```python
BUCKET_NAME = "amzn-s3-demo-bucket"
KEY = "reports/summary.csv"

async def upload_file(
    client: AsyncS3Client, bucket_name: str, key: str, file_path: str
) -> None:
    """Upload a local file as an object."""
    with open(file_path, "rb") as file:
        await client.put_object(bucket=bucket_name, key=key, body=file)

async def download_file(
    client: AsyncS3Client, bucket_name: str, key: str, file_path: str
) -> None:
    """Stream an object to a local file in chunks."""
    response = await client.get_object(bucket=bucket_name, key=key)
    try:
        with open(file_path, "wb") as file:
            async for chunk in response.body:
                file.write(chunk)
    finally:
        await response.body.close()

async def download_bytes(
    client: AsyncS3Client, bucket_name: str, key: str
) -> bytes:
    """Read an entire object into memory."""
    response = await client.get_object(bucket=bucket_name, key=key)
    return await response.body.read()

async def main() -> None:
    config = await AsyncS3Config.resolve()
    async with AsyncS3Client(config=config) as client:
        await upload_file(client, BUCKET_NAME, KEY, "summary.csv")
        await download_file(client, BUCKET_NAME, KEY, "summary-copy.csv")
        data = await download_bytes(client, BUCKET_NAME, KEY)
        print(f"Downloaded {len(data)} bytes")

if __name__ == "__main__":
    asyncio.run(main())
```

As with the synchronous client, the SDK validates the checksum when you read the body to the end. The asynchronous body isn't a context manager, so `download_file` calls `await response.body.close()` in a `finally` block. Closing the body releases the connection if the function stops reading early.

The example reads and writes local files with blocking calls. For how to keep blocking work off the event loop, see [Keeping blocking work off the event loop](using-async.md#using-async-blocking-work).
