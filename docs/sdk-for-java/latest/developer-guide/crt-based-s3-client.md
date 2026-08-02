---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/crt-based-s3-client.html
---

# Use a performant S3 client: AWS CRT-based S3 client
<a name="crt-based-s3-client"></a>

The AWS CRT-based S3 client—built on top of the [AWS Common Runtime (CRT)](https://docs.aws.amazon.com/sdkref/latest/guide/common-runtime.html)—is an alternative S3 asynchronous client. It transfers objects to and from Amazon Simple Storage Service (Amazon S3) with enhanced performance and reliability by automatically using Amazon S3's [multipart upload API](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html) and [byte-range fetches](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance-guidelines.html#optimizing-performance-guidelines-get-range).

The AWS CRT-based S3 client improves transfer reliability in case there is a network failure. Reliability is improved by retrying individual failed parts of a file transfer without restarting the transfer from the beginning.

In addition, the AWS CRT-based S3 client offers enhanced connection pooling and Domain Name System (DNS) load balancing, which also improves throughput.

You can use the AWS CRT-based S3 client in place of the SDK's standard S3 asynchronous client and take advantage of its improved throughput right away.

**Important**
The AWS CRT-based S3 client does not currently support [SDK metrics collection](metrics.md) at the client level nor at the request level.

**AWS CRT-based components in the SDK**

The AWS CRT-based* S3* client, described in this topic, and the AWS CRT-based *HTTP* client are different components in the SDK.

The **AWS CRT-based S3 client** is an implementation of the [S3AsyncClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3AsyncClient.html) interface and is used for working with the Amazon S3 service. It is an alternative to the Java-based implementation of the `S3AsyncClient` interface and offers several benefits.

The [AWS CRT-based HTTP client](http-configuration-crt.md) is an implementation of the [SdkAsyncHttpClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/async/SdkAsyncHttpClient.html) interface and is used for general HTTP communication. It is an alternative to the Netty implementation of the `SdkAsyncHttpClient` interface and offers several advantages.

Although both components use libraries from the [AWS Common Runtime](https://docs.aws.amazon.com/sdkref/latest/guide/common-runtime.html), the AWS CRT-based S3 client uses the [aws-c-s3 library](https://github.com/awslabs/aws-c-s3) and supports the [S3 multipart upload API](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html) features. Since the AWS CRT-based HTTP client is meant for general purpose use, it does not support the S3 multipart upload API features.

## Add dependencies to use the AWS CRT-based S3 client
<a name="crt-based-s3-client-depend"></a>

To use the AWS CRT-based S3 client, add the following two dependencies to your Maven project file. The example shows the minimum versions to use. Search the Maven central repository for the most recent versions of the [s3](https://central.sonatype.com/artifact/software.amazon.awssdk/s3) and [aws-crt](https://central.sonatype.com/artifact/software.amazon.awssdk.crt/aws-crt) artifacts.

```
<dependency>
  <groupId>software.amazon.awssdk</groupId>
  <artifactId>s3</artifactId>
  <version>{{2.27.21}}</version>
</dependency>
<dependency>
  <groupId>software.amazon.awssdk.crt</groupId>
  <artifactId>aws-crt</artifactId>
  <version>{{0.30.11}}</version>
</dependency>
```

## Create an instance of the AWS CRT-based S3 client
<a name="crt-based-s3-client-create"></a>

 Create an instance of the AWS CRT-based S3 client with default settings as shown in the following code snippet.

```
S3AsyncClient s3AsyncClient = S3AsyncClient.crtCreate();
```

To configure the client, use the AWS CRT client builder. You can switch from the standard S3 asynchronous client to AWS CRT-based client by changing the builder method.

```
import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3AsyncClient;

S3AsyncClient s3AsyncClient =
        S3AsyncClient.crtBuilder()
                     .credentialsProvider(DefaultCredentialsProvider.create())
                     .region(Region.US_WEST_2)
                     .targetThroughputInGbps(20.0)
                     .minimumPartSizeInBytes(8 * 1025 * 1024L)
                     .build();
```

**Note**
Some of the settings in the standard builder might not be currently supported in the AWS CRT client builder. Get the standard builder by calling `S3AsyncClient#builder()`.

## Use the AWS CRT-based S3 client
<a name="crt-based-s3-client-use"></a>

Use the AWS CRT-based S3 client to call Amazon S3 API operations. The following example demonstrates the [PutObject](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3AsyncClient.html#putObject(java.util.function.Consumer,software.amazon.awssdk.core.async.AsyncRequestBody)) and [GetObject](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3AsyncClient.html#getObject(java.util.function.Consumer,software.amazon.awssdk.core.async.AsyncResponseTransformer)) operations available through the AWS SDK for Java.

```
import software.amazon.awssdk.core.async.AsyncRequestBody;
import software.amazon.awssdk.core.async.AsyncResponseTransformer;
import software.amazon.awssdk.services.s3.S3AsyncClient;
import software.amazon.awssdk.services.s3.model.GetObjectResponse;
import software.amazon.awssdk.services.s3.model.PutObjectResponse;

S3AsyncClient s3Client = S3AsyncClient.crtCreate();

// Upload a local file to Amazon S3.
PutObjectResponse putObjectResponse =
      s3Client.putObject(req -> req.bucket({{<BUCKET_NAME>}})
                                   .key({{<KEY_NAME>}}),
                        AsyncRequestBody.fromFile(Paths.get({{<FILE_NAME>}})))
              .join();

// Download an object from Amazon S3 to a local file.
GetObjectResponse getObjectResponse =
      s3Client.getObject(req -> req.bucket({{<BUCKET_NAME>}})
                                   .key({{<KEY_NAME>}}),
                        AsyncResponseTransformer.toFile(Paths.get({{<FILE_NAME>}})))
              .join();
```

## Uploading streams of unknown size
<a name="crt-stream-unknown-size"></a>

One significant advantage of the AWS AWS CRT-based S3 client is its ability to handle input streams of unknown size efficiently. This is particularly useful when you need to upload data from a source where the total size cannot be determined in advance.

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

This capability helps avoid common issues with traditional uploads where an incorrect content length specification can lead to truncated objects or failed uploads.

## Configuration limitations
<a name="crt-based-s3-client-limitations"></a>

The AWS CRT-based S3 client and Java-based S3 async client [provide comparable features](examples-s3.md#s3-clients), with the AWS CRT-based S3 client offering a performance edge. However, the AWS CRT-based S3 client lacks configuration settings that the Java-based S3 async client has. These settings include:
+ *Client-level configuration:* API call attempt timeout, compression execution interceptors, metric publishers, custom execution attributes, custom advanced options, custom scheduled executor service, custom headers
+ *Request-level configuration:* custom signers, API call attempt timeout

For a full listing of the configuration differences, see the API reference.

| Java-based S3 async client | AWS CRT-based S3 client |
| --- | --- |
| Client-level configurations[See the AWS documentation website for more details](http://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/crt-based-s3-client.html)Request-level configurations[See the AWS documentation website for more details](http://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/crt-based-s3-client.html) | Client-level configurations[See the AWS documentation website for more details](http://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/crt-based-s3-client.html)Request-level configurations[See the AWS documentation website for more details](http://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/crt-based-s3-client.html) |
