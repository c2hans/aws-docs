---
source_url: https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-performance.html
---

Version 4 (V4) of the AWS SDK for .NET has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html).

 [![Orange button with text "Click here for details".](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html)

# Performance best practices for the AWS SDK for .NET
<a name="net-dg-performance"></a>

How you create clients, handle responses, and configure your application has a large effect on throughput, latency, and memory use. This topic describes usage and configuration patterns that help your applications run efficiently and reliably. These patterns matter most under high load or in resource-constrained environments such as containers and serverless functions. Following these practices can improve performance and prevent common problems such as slow responses, hangs, and high memory use.

The most impactful practices are the following:
+ [Reuse a single, long-lived service client](#net-dg-performance-reuse-clients) instead of creating one per request.
+ [Dispose responses and streams](#net-dg-performance-dispose) so that network connections are released back to the connection pool.
+ [Use `async`/`await` correctly](#net-dg-performance-async) and never block on asynchronous SDK calls.
+ [Configure .NET garbage collection](#net-dg-performance-gc) for constrained environments such as AWS Lambda and Amazon ECS.
+ [Manage HTTP connections](#net-dg-performance-connections) and connection limits under high throughput.

Before you begin, be sure you have [set up your environment](net-dg-config.md) and [configured your project](configuring-the-sdk.md).

## Reuse a single, long-lived service client
<a name="net-dg-performance-reuse-clients"></a>

Service clients such as [AmazonS3Client](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/S3/TS3Client.html) and [AmazonDynamoDBClient](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/DynamoDBv2/TDynamoDBClient.html) are *thread-safe*, relatively *expensive* to construct, and *long-lived*. Constructing a client resolves Region and endpoint information and establishes the underlying HTTP infrastructure. Create one client per service and reuse it for the lifetime of your application. If you call more than one Region, create a separate client for each Region.

**Warning**
Do not create a new service client for each request or inside a loop. Creating clients repeatedly churns the underlying HTTP infrastructure, which adds measurable latency. It can also exhaust sockets or handles and cause requests to fail or hang under load.

In applications that use dependency injection, register the client as a singleton. The `AddAWSService` extension method from the `AWSSDK.Extensions.NETCore.Setup` NuGet package registers the client with a default lifetime of `ServiceLifetime.Singleton`. The client is created the first time it's requested, and the same instance is reused for the lifetime of the process. For more information about registering AWS services with dependency injection and reading options from configuration, see [AWSSDK.Extensions.NETCore.Setup and IConfiguration](net-dg-config-netcore.md).

You can also register a client as a singleton manually.

```
builder.Services.AddSingleton<IAmazonS3>(_ => new AmazonS3Client());
```

**Note**
Because `AddAWSService` registers the client as a singleton by default, do not dispose the client that it provides. If you need a non-default lifetime, pass a different `ServiceLifetime` value to the optional `lifetime` parameter of `AddAWSService`.

Reusing the client does **not** mean you should stop disposing per-operation responses. Reuse the client for the life of the application, but continue to dispose the responses and streams that individual operations return, as described in [Dispose responses and streams](#net-dg-performance-dispose).

## Dispose responses and streams to release connections
<a name="net-dg-performance-dispose"></a>

Some SDK response objects carry a live network stream. The most common example is [GetObjectResponse](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/S3/TGetObjectResponse.html), which implements `IDisposable` and exposes the object's content through its `ResponseStream` property. The response holds an open HTTP connection until the stream is fully read or the response is disposed. If you leak these responses (for example, by calling `GetObject` in a loop without disposing each result), open connections accumulate until the connection pool is exhausted, and the next call blocks. This is the cause behind reports of downloads that "hang randomly" or stall on the Nth object.

Always wrap a streaming response in a `using` statement and read or copy its stream promptly.

```
using Amazon.S3;
using Amazon.S3.Model;

// s3Client is a reused, long-lived client.
var request = new GetObjectRequest { BucketName = bucketName, Key = key };

using var response = await s3Client.GetObjectAsync(request);
await response.WriteResponseStreamToFileAsync(filePath, append: false, CancellationToken.None);
```

Disposing the response and disposing its `ResponseStream` are equivalent; either one closes the underlying network stream and returns the connection to the pool.

**Tip**
If you only need object metadata, such as size, last-modified time, content type, or ETag, call `GetObjectMetadata` or `GetObjectMetadataAsync` instead of `GetObject`. The metadata operation issues an HTTP `HEAD` request and transfers no object body, so there's no content stream to manage.

```
var metadata = await s3Client.GetObjectMetadataAsync(bucketName, key);
Console.WriteLine($"Size: {metadata.ContentLength} bytes");
```

**Warning**
Response and stream types such as `GetObjectResponse` don't implement a finalizer, so you can't rely on garbage collection to release their connections for you. You must dispose responses and streams deterministically with `using` or an explicit `Dispose` call.

## Use async/await correctly
<a name="net-dg-performance-async"></a>

On modern .NET, the service operations in the AWS SDK for .NET are asynchronous and return a `Task`. On .NET Framework, synchronous methods also exist, but asynchronous calls scale better and are recommended. Consume operations with `await`, and propagate `async` through every layer of your code up to the entry point. For more information about asynchronous programming with the SDK, see [Asynchronous programming](sdk-net-async-api.md).

**Warning**
Do not block on an asynchronous SDK call with `.Result`, `.Wait()`, or `.GetAwaiter().GetResult()`. This *sync-over-async* pattern is a common cause of applications that hang:
Under load, blocking calls consume threads faster than the thread pool can grow, so continuations can't run. This *thread-pool starvation* appears as an indefinite hang and is the dominant failure mode on modern .NET (where ASP.NET Core has no default `SynchronizationContext`).
Some contexts capture a `SynchronizationContext`, such as classic ASP.NET, Windows Forms, WPF, Blazor WebAssembly, and .NET Framework applications. In these contexts, blocking the calling thread while a continuation needs that same thread produces a *deadlock*. Operations in the SDK use `ConfigureAwait(false)` internally, so they don't post their continuations back to the captured context. The deadlock arises from `async` code elsewhere in your call chain that does capture it. Consuming SDK calls with `await` throughout avoids the problem entirely.

The following method blocks on the asynchronous call and can deadlock or starve the thread pool.

```
// Anti-pattern: do not do this.
public GetObjectResponse Get(GetObjectRequest request)
{
    return s3Client.GetObjectAsync(request).Result;
}
```

Instead, make the method `async` and `await` the call.

```
public async Task<GetObjectResponse> GetAsync(GetObjectRequest request)
{
    return await s3Client.GetObjectAsync(request);
}
```

Additional recommendations for asynchronous code:
+ Pass a `CancellationToken` to every operation so a slow or stalled call can be canceled instead of hanging. For more information, see [Using the `CancellationToken` parameter for timeouts](retries-timeouts.md#timeouts-async).
+ Don't swallow exceptions in an empty `catch` block. Doing so hides the real failure and makes a hang indistinguishable from an error. Catch specific exceptions and log them.
+ When rethrowing a caught exception, use `throw;` rather than `throw ex;` so that the original stack trace is preserved.
+ If you must call from a synchronous boundary, treat it as a last resort and isolate the work from the captured context rather than making blocking calls the default pattern.

## Configure .NET garbage collection for AWS Lambda and Amazon ECS
<a name="net-dg-performance-gc"></a>

When a container appears to have a "memory leak," the .NET garbage collector (GC) might be retaining reclaimed memory for reuse. As a result, process memory can appear high and stable even when the managed heap is not growing. In addition, the GC doesn't automatically detect a container's memory limit (its cgroup limit). In a constrained environment, the heap might then grow toward the host's memory rather than the container's limit. This can lead to `OutOfMemoryException` or the container being terminated.

To help the GC work well in constrained environments:
+ Set an explicit memory limit on the container so the GC honors the cgroup limit, and/or set the `DOTNET_GCHeapHardLimit` (an absolute byte value, in hexadecimal) or `DOTNET_GCHeapHardLimitPercent` environment variable to cap the managed heap. In several reported Amazon ECS out-of-memory cases, setting a hard memory limit resolved the crashes.
+ On small AWS Lambda and Amazon ECS hosts, consider disabling concurrent (background) garbage collection so the collector doesn't reserve additional memory; for example, set the `DOTNET_gcConcurrent` environment variable to `0`, or set `<ConcurrentGarbageCollection>false</ConcurrentGarbageCollection>` in the project file.
+ Bound your concurrency. Launching many operations at once, such as calling `Task.WhenAll` over a large collection, inflates process memory and can starve the connection pool. Cap the degree of parallelism instead. For example, avoid this unbounded pattern:

  ```
  // Anti-pattern: starts one task per item with no limit.
  await Task.WhenAll(keys.Select(key => s3Client.GetObjectMetadataAsync(bucket, key)));
  ```

  Instead, cap concurrency with `Parallel.ForEachAsync`:

  ```
  var options = new ParallelOptions { MaxDegreeOfParallelism = 10 };
  await Parallel.ForEachAsync(keys, options, async (key, token) =>
  {
      await s3Client.GetObjectMetadataAsync(bucket, key, token);
  });
  ```

For more information about these settings, see [Runtime configuration options for garbage collection](https://learn.microsoft.com/en-us/dotnet/core/runtime-config/garbage-collector) on learn.microsoft.com. For guidance specific to AWS compute, see the AWS Developer Tools Blog post [ Configuring .NET Garbage Collection for Amazon ECS and AWS Lambda](https://aws.amazon.com/blogs/developer/configuring-net-garbage-collection-for-amazon-ecs-and-aws-lambda).

## Manage HTTP connections and connection limits
<a name="net-dg-performance-connections"></a>

Under high throughput, two connection-related problems are common. The first is opening too many short-lived connections. This exhausts ephemeral ports, leaves sockets in `TIME_WAIT`, and adds TCP and TLS handshake latency. The second is having too few connections available, which bottlenecks parallelism. Reusing a single, long-lived client (see [Reuse service clients](#net-dg-performance-reuse-clients)) is the foundation for healthy connection pooling, because pooling depends on the client being reused.

To tune the number of concurrent connections per endpoint, set the `MaxConnectionsPerServer` property on the client configuration. When this property is `null` (the default), the underlying `HttpClientHandler` default applies, which is effectively unlimited on modern .NET. Raise it only when many concurrent requests to the same endpoint are bottlenecked on connections. A good starting point is the peak number of concurrent requests you expect per endpoint. Setting it far higher than your workload needs wastes sockets without improving throughput.

```
using Amazon.S3;

var config = new AmazonS3Config
{
    MaxConnectionsPerServer = 50
};

var s3Client = new AmazonS3Client(config);
```

If you already use dependency injection, configure your clients through `AWSSDK.Extensions.NETCore.Setup`. This is the recommended approach when you use DI or register several service clients. It centralizes configuration and makes clients easy to inject and test. You can set configuration values from your application's configuration instead of in code. For more information, see [AWSSDK.Extensions.NETCore.Setup and IConfiguration](net-dg-config-netcore.md).

Finally, bound your own parallelism so that you don't start more concurrent operations than your connection limit allows. For example, gate calls with a `SemaphoreSlim` sized to your connection limit:

```
var throttle = new SemaphoreSlim(50); // match MaxConnectionsPerServer
await throttle.WaitAsync(token);
try
{
    await s3Client.GetObjectAsync(request, token);
}
finally
{
    throttle.Release();
}
```

## Configure timeouts and retries
<a name="net-dg-performance-timeouts"></a>

Timeouts and retries have a direct effect on perceived performance. A `Timeout` value that is too high lets a stalled request block for a long time. When a service is already returning throttling errors, an aggressive retry policy adds more requests and can make the throttling worse. Choose a retry policy that fits your application's tolerance for latency versus failure, and let genuine exceptions propagate rather than retrying in a way that masks a hang.

**Note**
The `Timeout` property does not affect asynchronous calls. If you are using asynchronous calls, see [Using the `CancellationToken` parameter for timeouts](retries-timeouts.md#timeouts-async) instead.

For more information about the retry modes, `MaxErrorRetry`, and the `Timeout` property (`ReadWriteTimeout` applies only to .NET Framework), along with examples of how to set them, see [Retries and timeouts](retries-timeouts.md).

## Optimize streaming and large-object transfers (Amazon S3)
<a name="net-dg-performance-streaming"></a>

To upload and download large objects, or many objects, use the [TransferUtility](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/S3/TTransferUtility.html) class in the `Amazon.S3.Transfer` namespace. It uploads and downloads in parallel using multipart transfers, and manages streams, parts, and connections for you. This is faster than a single-stream transfer and is the recommended way to move large objects.
+ **Parallel multipart download.** Earlier versions of the SDK downloaded an object as a single stream, rather than downloading parts in parallel. Starting with `AWSSDK.S3` version 4.0.17, `TransferUtility` provides multipart (parallel) download through the `DownloadWithResponseAsync`, `OpenStreamWithResponseAsync`, and `DownloadDirectoryWithResponseAsync` methods. When you use `OpenStreamWithResponseAsync`, the object's parts are buffered in memory while you consume the returned stream. Control how many parts are buffered with the `MaxInMemoryParts` property of [TransferUtilityOpenStreamRequest](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/S3/TTransferUtilityOpenStreamRequest.html). For most transfers, prefer `TransferUtility`. Download byte ranges yourself with the `ByteRange` property of [GetObjectRequest](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/S3/TGetObjectRequest.html) only when you need a specific range or a custom parallelism scheme. For more information, see [Introducing multipart download support for AWS SDK for .NET Transfer Manager](https://aws.amazon.com/blogs/developer/introducing-multipart-download-support-for-aws-sdk-for-net-transfer-manager/) on the AWS Developer Tools Blog.
+ **Content length for uploads.** An Amazon S3 `PUT` requires a known content length, and by default the SDK computes a checksum over the request body. When the length is known and the stream is seekable, the SDK can do this without buffering the whole object in memory. The `TransferUtility` handles non-seekable streams for you by buffering as needed. If you instead call `PutObjectAsync` directly with a non-seekable stream (such as a raw request body in ASP.NET Core), the request can fail. Provide a seekable stream, set the content length explicitly, or configure how the SDK calculates checksums. For more information, see [Data integrity protections](https://docs.aws.amazon.com/sdkref/latest/guide/feature-dataintegrity.html) in the AWS SDKs and Tools Reference Guide.
+ **Part sizing.** Amazon S3 allows a maximum of 10,000 parts per multipart upload. When the total length is known, the SDK computes a part size that stays within this limit automatically. You mainly need to set `PartSize` yourself for streams whose length isn't known in advance. Otherwise, small default parts can exceed the limit on a very large upload. A larger part size also reduces per-part overhead, at the cost of more memory per part.

## Diagnose performance problems
<a name="net-dg-performance-diagnose"></a>

When you investigate a slowdown, hang, or apparent leak, the following signals help you find the cause quickly:
+ A growing number of sockets in the `CLOSE_WAIT` or `TIME_WAIT` state (visible with `netstat`) is the fingerprint of undisposed responses or of clients being created and discarded per request. See [Dispose responses and streams](#net-dg-performance-dispose) and [Reuse service clients](#net-dg-performance-reuse-clients).
+ Enable request metrics and response logging to confirm that requests are actually being dispatched and to measure latency. Set the properties of the [LoggingConfig](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Util/TLoggingConfig.html) object on [AWSConfigs](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Amazon/TAWSConfigs.html) before you create your service clients. A client captures settings such as `LogMetrics` when it is constructed.

  ```
  using Amazon;

  AWSConfigs.LoggingConfig.LogMetrics = true;
  AWSConfigs.LoggingConfig.LogResponses = ResponseLoggingOption.OnError;
  ```
+ When investigating memory, distinguish whole-process memory from the managed heap. High but stable process memory is often the GC holding reclaimed memory rather than a leak. See [Configure garbage collection](#net-dg-performance-gc).
