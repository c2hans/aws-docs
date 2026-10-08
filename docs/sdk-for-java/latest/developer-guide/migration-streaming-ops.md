---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-streaming-ops.html
---

# Streaming operation differences between 1.x and 2.x of the AWS SDK for Java
<a name="migration-streaming-ops"></a>

Streaming operations, such as Amazon S3 `getObject` and `putObject` methods, support non-blocking I/O in version 2.x of the SDK. As a result, the request and response model objects no longer take an `InputStream` as a parameter. Instead, for synchronous requests the request object accepts `RequestBody`, which is a stream of bytes. The asynchronous equivalent accepts an `AsyncRequestBody`.

**Example of Amazon S3 `putObject` operation in 1.x**

```
s3client.putObject(BUCKET, KEY, new File(file_path));
```

**Example of Amazon S3 `putObject` operation in 2.x**

```
s3client.putObject(PutObjectRequest.builder()
                                 .bucket(BUCKET)
                                 .key(KEY)
                                 .build(),
                 RequestBody.of(Paths.get("myfile.in")));
```

A streaming response object accepts a `ResponseTransformer` for synchronous clients and a `AsyncResponseTransformer` for asynchronous clients in V2.

**Example of Amazon S3 `getObject` operation in 1.x**

```
S3Object o = s3.getObject(bucket, key);
S3ObjectInputStream s3is = o.getObjectContent();
FileOutputStream fos = new FileOutputStream(new File(key));
```

**Example of Amazon S3 `getObject` operation in 2.x**

```
s3client.getObject(GetObjectRequest.builder().bucket(bucket).key(key).build(),
		ResponseTransformer.toFile(Paths.get("key")));
```

In the SDK for Java 2.x, streaming response operations have an `AsBytes` method to load the response into memory and simplify common type conversions in-memory.

## Migrate concatenated GZIP response handling
<a name="migration-streaming-gzip"></a>

When migrating from SDK for Java 1.x, manually update code that wraps an S3 response stream in `GZIPInputStream`. Make this change if the response can contain multiple concatenated GZIP members. Select `ResponseTransformer.toGzipCompatibleInputStream()` or, for an asynchronous client, `AsyncResponseTransformer.toGzipCompatibleBlockingInputStream()`.

Consider the following when you migrate this code:
+ The migration tool does not select these transformers automatically.
+ On some JDK versions, your `GZIPInputStream` can stop after one member of a concatenated GZIP response. This can happen if the next network chunk has not arrived. The result can be truncated decompressed data without an exception.
+ These transformers do not decompress the response content. Use them only when you wrap the returned stream in `GZIPInputStream`. Otherwise, use `ResponseTransformer.toInputStream()` or `AsyncResponseTransformer.toBlockingInputStream()`.

For a synchronous client:

```
ResponseInputStream<GetObjectResponse> response =
    s3Client.getObject(
        request,
        ResponseTransformer.toGzipCompatibleInputStream());

try (GZIPInputStream gzipInputStream = new GZIPInputStream(response)) {
    // Read the decompressed response.
}
```

You can use `ResponseTransformer.toGzipCompatibleInputStream(Duration)` to configure the timeout for the first read operation.

For an asynchronous client:

```
CompletableFuture<ResponseInputStream<GetObjectResponse>> responseFuture =
    s3AsyncClient.getObject(
        request,
        AsyncResponseTransformer.toGzipCompatibleBlockingInputStream());

try (ResponseInputStream<GetObjectResponse> response = responseFuture.join();
     GZIPInputStream gzipInputStream = new GZIPInputStream(response)) {
    // Read the decompressed response. Reads block the calling thread.
}
```
