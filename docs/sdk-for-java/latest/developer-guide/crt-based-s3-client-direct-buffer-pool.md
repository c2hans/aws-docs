---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/crt-based-s3-client-direct-buffer-pool.html
---

# Download objects through a direct buffer pool with the AWS CRT-based S3 client
<a name="crt-based-s3-client-direct-buffer-pool"></a>

When you download an object into memory with the AWS CRT-based S3 client, response transformers such as `AsyncResponseTransformer.toBytes()`, `toPublisher()`, and `toBlockingInputStream()` copy each downloaded part into a new Java heap array. A *direct buffer pool* stores transfer parts in client-wide direct memory (off-heap). A blocking input stream can read each part from that memory instead of from a heap copy. This eliminates SDK-created per-part heap arrays, reducing heap allocation and garbage collection during high-throughput downloads. Downloads to a file with `getObject(GetObjectRequest, Path)` don't make this copy, because the client writes the file directly.

A direct buffer pool is client-wide. Multipart uploads and downloads other than `GetObject` requests that set `partNumber` use it. If this client uploads objects, see [How a direct buffer pool affects uploads](#crt-based-s3-client-direct-buffer-pool-uploads).

**Important**
Read or close each stream promptly. An open stream retains pool memory.
Size the pool for concurrent downloads. When free pool capacity runs out, new download data waits until another request releases memory. See [Configure pool capacity](#crt-based-s3-client-direct-buffer-pool-size).

## Create a direct buffer pool
<a name="crt-based-s3-client-direct-buffer-pool-configure"></a>

Use version 2.59.0 or later of the SDK and version 0.50.0 or later of `aws-crt`. Then pass an [S3CrtDirectBufferPoolConfiguration](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/crt/S3CrtDirectBufferPoolConfiguration.html) to the client builder.

```
import software.amazon.awssdk.services.s3.S3AsyncClient;
import software.amazon.awssdk.services.s3.crt.S3CrtDirectBufferPoolConfiguration;

S3AsyncClient s3AsyncClient =
        S3AsyncClient.crtBuilder()
                     .directBufferPoolConfiguration(S3CrtDirectBufferPoolConfiguration.auto())
                     .build();
```

Start with `auto()`. Use `elastic()` when you want to size the pool yourself: it sets the ceiling, and its floor sets how much memory the pool keeps allocated while idle.
+ `auto()`: By default, the client derives the ceiling from its throughput target. A ceiling that you set through `maxNativeMemoryLimitInBytes` or the `AWS_CRT_S3_MEMORY_LIMIT_IN_MB` / `AWS_CRT_S3_MEMORY_LIMIT_IN_GIB` environment variables overrides that default. The pool starts with a baseline (128 MiB with the default 8 MiB part size, capped at the ceiling), grows with demand, and releases unused memory down to that baseline when the client is idle.
+ `elastic(minimumSizeInBytes, memoryLimitInBytes)`: The pool keeps its floor allocated, grows to its ceiling on demand, and releases unused memory down to the floor when the client is idle. With the default part size, the floor is rounded down to a multiple of 128 MiB, so a floor below 128 MiB keeps nothing allocated. The exception is a floor equal to the ceiling, which keeps the whole pool allocated.

When the pool grows, other requests on the client are briefly delayed. A larger `elastic()` floor makes this happen less often, and a floor equal to the ceiling prevents it.

## Download an object
<a name="crt-based-s3-client-direct-buffer-pool-getobject"></a>

To download from the pool, use the transformer returned by [S3CrtResponseTransformerProvider.toBlockingInputStreamFromDirectBufferPool()](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/crt/S3CrtResponseTransformerProvider.html#toBlockingInputStreamFromDirectBufferPool()). Pass it directly to `getObject`. This returns a `ResponseInputStream` that reads the object from pool memory.

```
import software.amazon.awssdk.core.ResponseInputStream;
import software.amazon.awssdk.services.s3.crt.S3CrtResponseTransformerProvider;
import software.amazon.awssdk.services.s3.model.GetObjectResponse;

try (ResponseInputStream<GetObjectResponse> stream =
             s3AsyncClient.getObject(req -> req.bucket("{{amzn-s3-demo-bucket}}").key("{{object-key}}"),
                                     S3CrtResponseTransformerProvider.toBlockingInputStreamFromDirectBufferPool())
                          .join()) {
    byte[] buffer = new byte[64 * 1024];
    int bytesRead;
    while ((bytesRead = stream.read(buffer)) != -1) {
        // Process bytesRead bytes of buffer.
    }
}
```
+ The future completes when the stream is ready. The rest of the object downloads as you read.
+ Read until `read()` returns `-1` (EOF). A failure after the stream is returned, including a full-object checksum mismatch, is thrown by `read()`.
+ Always close the stream (use try-with-resources). Closing releases its pool memory and cancels the rest of the download. The SDK doesn't time out a stalled stream, so close it to end the download. Interrupting a blocked `read` also closes the stream.
+ The request fails before it's sent if the client isn't an AWS CRT-based S3 client with a direct buffer pool, or if you wrap the transformer in another `AsyncResponseTransformer`, such as a custom transformer that delegates to it.
+ `ExecutionInterceptor.modifyAsyncHttpResponseContent` isn't applied to the object body. If you rely on an interceptor to transform object bytes, don't use a pool for those downloads.

## Download an object with the Amazon S3 Transfer Manager
<a name="crt-based-s3-client-direct-buffer-pool-tm"></a>

Build the [Transfer Manager](transfer-manager.md) with a client that has a pool configured, then call `download()` with a request that holds a transformer from `S3CrtResponseTransformerProvider`.

```
import software.amazon.awssdk.core.ResponseInputStream;
import software.amazon.awssdk.services.s3.crt.S3CrtResponseTransformerProvider;
import software.amazon.awssdk.services.s3.model.GetObjectResponse;
import software.amazon.awssdk.transfer.s3.S3TransferManager;
import software.amazon.awssdk.transfer.s3.model.DownloadRequest;
import software.amazon.awssdk.transfer.s3.progress.LoggingTransferListener;

S3TransferManager transferManager = S3TransferManager.builder().s3Client(s3AsyncClient).build();

DownloadRequest<ResponseInputStream<GetObjectResponse>> request =
        DownloadRequest.builder()
                       .getObjectRequest(req -> req.bucket("{{amzn-s3-demo-bucket}}").key("{{object-key}}"))
                       .addTransferListener(LoggingTransferListener.create())
                       .responseTransformer(S3CrtResponseTransformerProvider.toBlockingInputStreamFromDirectBufferPool())
                       .build();

try (ResponseInputStream<GetObjectResponse> stream =
             transferManager.download(request).completionFuture().join().result()) {
    byte[] buffer = new byte[64 * 1024];
    int bytesRead;
    while ((bytesRead = stream.read(buffer)) != -1) {
        // Process bytesRead bytes of buffer.
    }
}
```

The stream behaves as described in [Download an object](#crt-based-s3-client-direct-buffer-pool-getobject). In addition:
+ `completionFuture()` completes when the stream is ready, not when the object has downloaded. To track progress and to know when the transfer finishes or fails, use a `TransferListener`.
+ Progress counts bytes the client has received, which your application might not have read yet.
+ Closing the stream before the client has received the whole object fails the transfer, and the `TransferListener` receives `transferFailed`.

## Configure pool capacity
<a name="crt-based-s3-client-direct-buffer-pool-size"></a>

Each download can hold up to its read window plus one part. The read window is `initialReadBufferSizeInBytes`, which defaults to 10 times `minimumPartSizeInBytes` (80 MiB with the default 8 MiB part size).

Pool memory counts against the JVM direct-memory limit (`-XX:MaxDirectMemorySize`, which defaults to the maximum heap size on OpenJDK). A ceiling that you set, through `elastic()`, `maxNativeMemoryLimitInBytes`, or a memory-limit environment variable, must fit within 80% of that limit, or client creation fails. If you don't set a ceiling, `auto()` lowers its default ceiling to fit and logs a warning. A smaller ceiling can limit throughput. If you set both `elastic()` and `maxNativeMemoryLimitInBytes`, the `elastic()` ceiling can't exceed `maxNativeMemoryLimitInBytes`, or client creation fails.

As a starting estimate, size the pool to:

```
concurrent downloads × (initialReadBufferSizeInBytes + part size) + headroom for other requests
```

For example, 16 concurrent downloads with an explicit 8 MiB part size and an 80 MiB read window need 16 × (80 MiB \+ 8 MiB) = 1,408 MiB, so a 1.5 GiB ceiling with `-XX:MaxDirectMemorySize=2g` fits. Test with your workload, because a pool that's too small stalls downloads.

```
long mib = 1024L * 1024;
S3AsyncClient s3AsyncClient =
        S3AsyncClient.crtBuilder()
                     .minimumPartSizeInBytes(8 * mib)
                     .directBufferPoolConfiguration(
                             S3CrtDirectBufferPoolConfiguration.elastic(256 * mib, 1536 * mib))
                     .build();
```

Keep the following in mind:
+ Each request that uses the pool holds a full part, even for a small object. Pool capacity therefore scales with concurrent requests.
+ If the read window limits download throughput, increase `initialReadBufferSizeInBytes` and raise the pool ceiling to match. Each download then holds more pool memory, so the same ceiling supports fewer concurrent downloads.

## How a direct buffer pool affects uploads
<a name="crt-based-s3-client-direct-buffer-pool-uploads"></a>

A direct buffer pool bounds multipart-upload memory as well as download memory. It can also limit the size of multipart uploads with a known content length.
+ With an explicit `minimumPartSizeInBytes`, that value is the exact upload part size and CRT does not raise it. Amazon S3 limits multipart uploads to 10,000 parts. See [Amazon S3 multipart limits](https://docs.aws.amazon.com/AmazonS3/latest/userguide/qfacts.html). An 8 MiB part size limits an upload to 78 GiB and a 64 MiB part size limits an upload to 625 GiB. To upload beyond these limits, increase `minimumPartSizeInBytes` and the pool ceiling.
+ Without an explicit part size, CRT selects the part size needed for a known-size multipart upload. The maximum part size is half the pool ceiling, capped at 5 GiB. An upload that needs a part size above that maximum fails before it sends data. Increase the pool ceiling to upload beyond that limit.
+ Uploads from a file path, such as `putObject(PutObjectRequest, Path)` or Transfer Manager `uploadFile`, skip the SDK's up-front validation because CRT can stream the body rather than buffer whole parts. Amazon S3 multipart limits still apply. If CRT does not stream the body and the part size cannot cover the object, the upload can fail after it starts.
