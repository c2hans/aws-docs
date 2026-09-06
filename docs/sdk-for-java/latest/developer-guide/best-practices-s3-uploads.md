---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/best-practices-s3-uploads.html
---

# Uploading streams to Amazon S3 using the AWS SDK for Java 2.x
<a name="best-practices-s3-uploads"></a>

When you use a stream to upload content to S3 using [`putObject`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3Client.html#putObject(software.amazon.awssdk.services.s3.model.PutObjectRequest,software.amazon.awssdk.core.sync.RequestBody)) or [`uploadPart`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3Client.html#uploadPart(software.amazon.awssdk.services.s3.model.UploadPartRequest,software.amazon.awssdk.core.sync.RequestBody)), you use a `RequestBody` factory class for the synchronous API to supply the stream. For the asynchronous API, the `AsyncRequestBody` is the equivalent factory class.

## Which methods upload streams?
<a name="s3-stream-upload-methods"></a>

For the synchronous API, you can use the following factory methods of `RequestBody` to supply the stream:
+ `[fromInputStream](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/sync/RequestBody.html#fromInputStream(java.io.InputStream,long))(InputStream inputStream, long contentLength)`

  `[fromContentProvider](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/sync/RequestBody.html#fromContentProvider(software.amazon.awssdk.http.ContentStreamProvider,long,java.lang.String))(ContentStreamProvider provider, long contentLength, String mimeType)`
  + The `ContentStreamProvider` has the `fromInputStream(InputStream inputStream)` factory method
+ `[fromContentProvider](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/sync/RequestBody.html#fromContentProvider(software.amazon.awssdk.http.ContentStreamProvider,java.lang.String))(ContentStreamProvider provider, String mimeType)`

For the asynchronous API, you can use the following factory methods of `AsyncRequestBody`:
+ `[fromInputStream](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/async/AsyncRequestBody.html#fromInputStream(java.io.InputStream,java.lang.Long,java.util.concurrent.ExecutorService))(InputStream inputStream, Long contentLength, ExecutorService executor)`
+ `[fromInputStream](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/async/AsyncRequestBody.html#fromInputStream(software.amazon.awssdk.core.async.AsyncRequestBodyFromInputStreamConfiguration))(AsyncRequestBodyFromInputStreamConfiguration configuration)`
  + You use the AsyncRequestBodyFromInputStreamConfiguration.Builder to supply the stream
+ `[fromInputStream](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/async/AsyncRequestBody.html#fromInputStream(java.util.function.Consumer))(Consumer<AsyncRequestBodyFromInputStreamConfiguration.Builder> configuration)`
+ `[forBlockingInputStream](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/async/AsyncRequestBody.html#forBlockingInputStream(java.lang.Long))(Long contentLength)`
  + The resulting `[BlockingInputStreamAsyncRequestBody](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/async/BlockingInputStreamAsyncRequestBody.html)` contains the method `writeInputStream(InputStream inputStream)` that you can use to provide the stream

## Performing the upload
<a name="s3-upload-stream-perform"></a>

### If you know the length of the stream
<a name="s3-stream-upload-supply-content-length"></a>

As you can see from the signature of the methods shown previously, most methods accept a content length parameter.

If you know the content length in bytes, provide the exact value:

```
// Always provide the exact content length when it's available.
long contentLength = 1024; // Exact size in bytes.
s3Client.putObject(req -> req
    .bucket("amzn-s3-demo-bucket")
    .key("my-key"),
RequestBody.fromInputStream(inputStream, contentLength));
```

**Warning**
 When you upload from an input stream, if your specified content length doesn't match the actual byte count, you might experience:
Truncated objects if your specified length is too small
Failed uploads or hanging connections if your specified length is too large

### If you don't know the length of the stream
<a name="s3-stream-upload-unknown-length"></a>

#### Using the synchronous API
<a name="s3-upload-unknown-sync-client"></a>

Use the `fromContentProvider(ContentStreamProvider provider, String mimeType)`:

```
public PutObjectResponse syncClient_stream_unknown_size(String bucketName, String key, InputStream inputStream) {

    S3Client s3Client = S3Client.create();

    RequestBody body = RequestBody.fromContentProvider(ContentStreamProvider.fromInputStream(inputStream), "text/plain");
    PutObjectResponse putObjectResponse = s3Client.putObject(b -> b.bucket(BUCKET_NAME).key(KEY_NAME), body);
    return putObjectResponse;
}
```

Because the SDK buffers the entire stream in memory to calculate the content length, you can run into memory issues with large streams. If you need to upload large streams with the synchronous client, consider using the multipart API:

##### Upload a stream using the synchronous client API and multipart API
<a name="sync-multipart-upload-stream"></a>

```
public static void uploadStreamToS3(String bucketName, String key, InputStream inputStream) {
    // Create S3 client
    S3Client s3Client = S3Client.create();
    try {
        // Step 1: Initiate the multipart upload
        CreateMultipartUploadRequest createMultipartUploadRequest = CreateMultipartUploadRequest.builder()
                .bucket(bucketName)
                .key(key)
                .build();

        CreateMultipartUploadResponse createResponse = s3Client.createMultipartUpload(createMultipartUploadRequest);
        String uploadId = createResponse.uploadId();
        System.out.println("Started multipart upload with ID: " + uploadId);

        // Step 2: Upload parts
        List<CompletedPart> completedParts = new ArrayList<>();
        int partNumber = 1;
        byte[] buffer = new byte[PART_SIZE];
        int bytesRead;

        try {
            while ((bytesRead = readFullyOrToEnd(inputStream, buffer)) > 0) {
                // Create request to upload a part
                UploadPartRequest uploadPartRequest = UploadPartRequest.builder()
                        .bucket(bucketName)
                        .key(key)
                        .uploadId(uploadId)
                        .partNumber(partNumber)
                        .build();

                // If we didn't read a full buffer, create a properly sized byte array
                RequestBody requestBody;
                if (bytesRead < PART_SIZE) {
                    byte[] lastPartBuffer = new byte[bytesRead];
                    System.arraycopy(buffer, 0, lastPartBuffer, 0, bytesRead);
                    requestBody = RequestBody.fromBytes(lastPartBuffer);
                } else {
                    requestBody = RequestBody.fromBytes(buffer);
                }

                // Upload the part and save the response's ETag
                UploadPartResponse uploadPartResponse = s3Client.uploadPart(uploadPartRequest, requestBody);
                CompletedPart part = CompletedPart.builder()
                        .partNumber(partNumber)
                        .eTag(uploadPartResponse.eTag())
                        .build();
                completedParts.add(part);

                System.out.println("Uploaded part " + partNumber + " with size " + bytesRead + " bytes");
                partNumber++;
            }

            // Step 3: Complete the multipart upload
            CompletedMultipartUpload completedMultipartUpload = CompletedMultipartUpload.builder()
                    .parts(completedParts)
                    .build();

            CompleteMultipartUploadRequest completeRequest = CompleteMultipartUploadRequest.builder()
                    .bucket(bucketName)
                    .key(key)
                    .uploadId(uploadId)
                    .multipartUpload(completedMultipartUpload)
                    .build();

            CompleteMultipartUploadResponse completeResponse = s3Client.completeMultipartUpload(completeRequest);
            System.out.println("Multipart upload completed. Object URL: " + completeResponse.location());

        } catch (Exception e) {
            // If an error occurs, abort the multipart upload
            System.err.println("Error during multipart upload: " + e.getMessage());
            AbortMultipartUploadRequest abortRequest = AbortMultipartUploadRequest.builder()
                    .bucket(bucketName)
                    .key(key)
                    .uploadId(uploadId)
                    .build();
            s3Client.abortMultipartUpload(abortRequest);
            System.err.println("Multipart upload aborted");
        } finally {
            try {
                inputStream.close();
            } catch (IOException e) {
                System.err.println("Error closing input stream: " + e.getMessage());
            }
        }
    } finally {
        s3Client.close();
    }
}

/**
 * Reads from the input stream into the buffer, attempting to fill the buffer completely
 * or until the end of the stream is reached.
 *
 * @param inputStream the input stream to read from
 * @param buffer      the buffer to fill
 * @return the number of bytes read, or -1 if the end of the stream is reached before any bytes are read
 * @throws IOException if an I/O error occurs
 */
private static int readFullyOrToEnd(InputStream inputStream, byte[] buffer) throws IOException {
    int totalBytesRead = 0;
    int bytesRead;

    while (totalBytesRead < buffer.length) {
        bytesRead = inputStream.read(buffer, totalBytesRead, buffer.length - totalBytesRead);
        if (bytesRead == -1) {
            break; // End of stream
        }
        totalBytesRead += bytesRead;
    }

    return totalBytesRead > 0 ? totalBytesRead : -1;
}
```

**Note**
For most use cases, we recommend using the asynchronous client API for streams of unknown size. This approach enables parallel transfers and offers a simpler programming interface, because the SDK handles the stream segmentation into multipart chunks if the stream is large.
Both the standard S3 asynchronous client with multipart enabled and the AWS CRT-based S3 client implement this approach. We show examples of this approach in the following section.

#### Using the asynchronous API
<a name="s3-stream-upload-unknown-async-client"></a>

You can provide `null` for the `contentLength` argument to the `fromInputStream(InputStream inputStream, Long contentLength, ExecutorService executor)`

**Example using the AWS CRT-based asynchronous client:**

```
public PutObjectResponse crtClient_stream_unknown_size(String bucketName, String key, InputStream inputStream) {

    S3AsyncClient s3AsyncClient = S3AsyncClient.crtCreate();
    ExecutorService executor = Executors.newSingleThreadExecutor();
    AsyncRequestBody body = AsyncRequestBody.fromInputStream(inputStream, null, executor);  // 'null' indicates that the
                                                                                            // content length is unknown.
    CompletableFuture<PutObjectResponse> responseFuture =
            s3AsyncClient.putObject(r -> r.bucket(bucketName).key(key), body)
                    .exceptionally(e -> {
                        if (e != null){
                            logger.error(e.getMessage(), e);
                        }
                        return null;
                    });

    PutObjectResponse response = responseFuture.join(); // Wait for the response.
    executor.shutdown();
    return response;
}
```

**Example using the standard asynchronous client with multipart enabled:**

```
public PutObjectResponse asyncClient_multipart_stream_unknown_size(String bucketName, String key, InputStream inputStream) {

    S3AsyncClient s3AsyncClient = S3AsyncClient.builder().multipartEnabled(true).build();
    ExecutorService executor = Executors.newSingleThreadExecutor();
    AsyncRequestBody body = AsyncRequestBody.fromInputStream(inputStream, null, executor); // 'null' indicates that the
                                                                                           // content length is unknown.
    CompletableFuture<PutObjectResponse> responseFuture =
            s3AsyncClient.putObject(r -> r.bucket(bucketName).key(key), body)
                    .exceptionally(e -> {
                        if (e != null) {
                            logger.error(e.getMessage(), e);
                        }
                        return null;
                    });

    PutObjectResponse response = responseFuture.join(); // Wait for the response.
    executor.shutdown();
    return response;
}
```
