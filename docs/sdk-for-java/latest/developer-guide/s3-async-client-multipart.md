---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/s3-async-client-multipart.html
---

# Configure the Java-based S3 async client to use parallel transfers
<a name="s3-async-client-multipart"></a>

Since version 2.27.5, the standard Java-based S3 async client supports automatic parallel transfers (multipart uploads and downloads). You configure support for parallel transfers when you create the Java-based S3 async client.

This section shows how to enable parallel transfers and how to customize the configuration.

## Create an instance of `S3AsyncClient`
<a name="s3-async-client-multipart-create"></a>

When you create an `S3AsyncClient` instance without calling any of the `multipart*` methods on the [builder](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3AsyncClientBuilder.html), parallel transfers are not enabled. Each of following statements create a Java-based S3 async client without support for multipart uploads and downloads.

### Create *without* multipart support
<a name="s3-async-client-mp-off"></a>

**Example**

```
import software.amazon.awssdk.auth.credentials.ProcessCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3AsyncClient;

S3AsyncClient s3Client = S3AsyncClient.create();

S3AsyncClient s3Client2 = S3AsyncClient.builder().build();

S3AsyncClient s3Client3 = S3AsyncClient.builder()
        .credentialsProvider(ProcessCredentialsProvider.builder().build())
        .region(Region.EU_NORTH_1)
        .build();
```

### Create *with* multipart support
<a name="s3-async-client-mp-on"></a>

To enable parallel transfers with default settings, call the `multipartEnabled` on the builder and pass in `true` as shown in the following example.

**Example**

```
S3AsyncClient s3AsyncClient2 = S3AsyncClient.builder()
        .multipartEnabled(true)
        .build();
```

The default value is 8 MiB for `thresholdInBytes` and `minimumPartSizeInBytes` settings.

If you customize the multipart settings, parallel transfers are automatically enabled as shown in the following.

**Example**

```
import software.amazon.awssdk.services.s3.S3AsyncClient;
import static software.amazon.awssdk.transfer.s3.SizeConstant.MB;

S3AsyncClient s3AsyncClient2 = S3AsyncClient.builder()
        .multipartConfiguration(b -> b
                .thresholdInBytes(16 * MB)
                .minimumPartSizeInBytes(10 * MB))
        .build();
```

## Uploading streams of unknown size
<a name="java-async-client-stream-unknown-size"></a>

The Java-based S3 asynchronous client with multipart enabled can efficiently handle input streams where the total size is not known in advance:

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

This approach prevents issues that can occur when manually specifying an incorrect content length, such as truncated objects or failed uploads.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
