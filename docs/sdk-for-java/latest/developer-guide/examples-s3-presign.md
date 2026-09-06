---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-s3-presign.html
---

# Work with Amazon S3 pre-signed URLs
<a name="examples-s3-presign"></a>

Pre-signed URLs provide temporary access to private S3 objects without requiring users to have AWS credentials or permissions.

For example, assume Alice has access to an S3 object, and she wants to temporarily share access to that object with Bob. Alice can generate a pre-signed GET request to share with Bob so that he can download the object without requiring access to Alice’s credentials. You can generate pre-signed URLs for HTTP GET and for HTTP PUT requests.

## Generate a pre-signed URL for an object, then download it (GET request)
<a name="get-presignedobject"></a>

The following example consists of two parts.
+ Part 1: Alice generates the pre-signed URL for an object.
+ Part 2: Bob downloads the object by using the pre-signed URL.

### Part 1: Generate the URL
<a name="get-presigned-object-part1"></a>

Alice already has an object in an S3 bucket. She uses the following code to generate a URL string that Bob can use in a subsequent GET request.

#### Imports
<a name="get-presigned-example-imports"></a>

```
import com.example.s3.util.PresignUrlUtils;
import org.slf4j.Logger;
import software.amazon.awssdk.http.HttpExecuteRequest;
import software.amazon.awssdk.http.HttpExecuteResponse;
import software.amazon.awssdk.http.SdkHttpClient;
import software.amazon.awssdk.http.SdkHttpMethod;
import software.amazon.awssdk.http.SdkHttpRequest;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.GetObjectRequest;
import software.amazon.awssdk.services.s3.model.S3Exception;
import software.amazon.awssdk.services.s3.presigner.S3Presigner;
import software.amazon.awssdk.services.s3.presigner.model.GetObjectPresignRequest;
import software.amazon.awssdk.services.s3.presigner.model.PresignedGetObjectRequest;
import software.amazon.awssdk.utils.IoUtils;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URISyntaxException;
import java.net.URL;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.file.Paths;
import java.time.Duration;
import java.util.UUID;
```

```
    /* Create a pre-signed URL to download an object in a subsequent GET request. */
    public String createPresignedGetUrl(String bucketName, String keyName) {
        try (S3Presigner presigner = S3Presigner.create()) {

            GetObjectRequest objectRequest = GetObjectRequest.builder()
                    .bucket(bucketName)
                    .key(keyName)
                    .build();

            GetObjectPresignRequest presignRequest = GetObjectPresignRequest.builder()
                    .signatureDuration(Duration.ofMinutes(10))  // The URL will expire in 10 minutes.
                    .getObjectRequest(objectRequest)
                    .build();

            PresignedGetObjectRequest presignedRequest = presigner.presignGetObject(presignRequest);
            logger.info("Presigned URL: [{}]", presignedRequest.url().toString());
            logger.info("HTTP method: [{}]", presignedRequest.httpRequest().method());

            return presignedRequest.url().toExternalForm();
        }
    }
```

### Part 2: Download the object
<a name="get-presigned-object-part2"></a>

Bob uses one of the following code options to download the object. Alternatively, he could use a browser to perform the GET request.

#### Use JDK `HttpURLConnection` (since v1.1)
<a name="get-presigned-example-useHttpUrlConnection"></a>

```
    /* Use the JDK HttpURLConnection (since v1.1) class to do the download. */
    public byte[] useHttpUrlConnectionToGet(String presignedUrlString) {
        ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream(); // Capture the response body to a byte array.

        try {
            URL presignedUrl = new URL(presignedUrlString);
            HttpURLConnection connection = (HttpURLConnection) presignedUrl.openConnection();
            connection.setRequestMethod("GET");
            // Download the result of executing the request.
            try (InputStream content = connection.getInputStream()) {
                IoUtils.copy(content, byteArrayOutputStream);
            }
            logger.info("HTTP response code is " + connection.getResponseCode());

        } catch (S3Exception | IOException e) {
            logger.error(e.getMessage(), e);
        }
        return byteArrayOutputStream.toByteArray();
    }
```

#### Use JDK `HttpClient` (since v11)
<a name="get-presigned-example-useHttpClient"></a>

```
    /* Use the JDK HttpClient (since v11) class to do the download. */
    public byte[] useHttpClientToGet(String presignedUrlString) {
        ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream(); // Capture the response body to a byte array.

        HttpRequest.Builder requestBuilder = HttpRequest.newBuilder();
        HttpClient httpClient = HttpClient.newHttpClient();
        try {
            URL presignedUrl = new URL(presignedUrlString);
            HttpResponse<InputStream> response = httpClient.send(requestBuilder
                            .uri(presignedUrl.toURI())
                            .GET()
                            .build(),
                    HttpResponse.BodyHandlers.ofInputStream());

            IoUtils.copy(response.body(), byteArrayOutputStream);

            logger.info("HTTP response code is " + response.statusCode());

        } catch (URISyntaxException | InterruptedException | IOException e) {
            logger.error(e.getMessage(), e);
        }
        return byteArrayOutputStream.toByteArray();
    }
```

#### Use `SdkHttpClient` from the SDK for Java
<a name="get-presigned-example-useSdkHttpClient"></a>

```
    /* Use the AWS SDK for Java SdkHttpClient class to do the download. */
    public byte[] useSdkHttpClientToGet(String presignedUrlString) {

        ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream(); // Capture the response body to a byte array.
        try {
            URL presignedUrl = new URL(presignedUrlString);
            SdkHttpRequest request = SdkHttpRequest.builder()
                    .method(SdkHttpMethod.GET)
                    .uri(presignedUrl.toURI())
                    .build();

            HttpExecuteRequest executeRequest = HttpExecuteRequest.builder()
                    .request(request)
                    .build();

            try (SdkHttpClient sdkHttpClient = ApacheHttpClient.create()) {
                HttpExecuteResponse response = sdkHttpClient.prepareRequest(executeRequest).call();
                response.responseBody().ifPresentOrElse(
                        abortableInputStream -> {
                            try {
                                IoUtils.copy(abortableInputStream, byteArrayOutputStream);
                            } catch (IOException e) {
                                throw new RuntimeException(e);
                            }
                        },
                        () -> logger.error("No response body."));

                logger.info("HTTP Response code is {}", response.httpResponse().statusCode());
            }
        } catch (URISyntaxException | IOException e) {
            logger.error(e.getMessage(), e);
        }
        return byteArrayOutputStream.toByteArray();
    }
```

#### Use `S3AsyncClient` pre-signed URL extension
<a name="get-presigned-example-useS3AsyncClient"></a>

The AWS SDK for Java 2.x provides a pre-signed URL extension on `S3AsyncClient` that downloads objects using a pre-signed URL through the SDK async pipeline. Access the extension with `S3AsyncClient.presignedUrlExtension()`. This feature is available in SDK version {{2.48.0}} and later.

**CRT client limitation**
The AWS CRT-based S3 client (`S3AsyncClient.crtBuilder()`) does not currently support the pre-signed URL extension. Use `S3AsyncClient.builder()` instead.

**Checksum mode requirement**
To validate data integrity, set `checksumMode(ChecksumMode.ENABLED)` on the `GetObjectRequest` when you generate the pre-signed URL. Specify checksum mode at presign time. You can't add it later when you run the download. When you use the `S3AsyncClient` pre-signed URL extension, the SDK automatically sends the required `x-amz-checksum-mode` header.

##### Imports
<a name="get-presigned-s3async-imports"></a>

```
import java.nio.file.Paths;
import software.amazon.awssdk.core.ResponseBytes;
import software.amazon.awssdk.core.async.AsyncResponseTransformer;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3AsyncClient;
import software.amazon.awssdk.services.s3.model.GetObjectResponse;
import software.amazon.awssdk.services.s3.presignedurl.model.PresignedUrlDownloadRequest;
```

##### Download to a file or to bytes
<a name="get-presigned-s3async-download"></a>

------
#### [ Download to file ]

```
S3AsyncClient s3AsyncClient = S3AsyncClient.builder()
        .region(Region.US_EAST_1)
        .build();

GetObjectResponse response = s3AsyncClient.presignedUrlExtension()
        .getObject(
            PresignedUrlDownloadRequest.builder()
                .presignedUrl(presignedGetObjectRequest.url())
                .build(),
            Paths.get("/tmp/downloaded-file.bin"))
        .join();

// Or use the consumer builder pattern
GetObjectResponse response = s3AsyncClient.presignedUrlExtension()
        .getObject(
            r -> r.presignedUrl(presignedGetObjectRequest.url()),
            Paths.get("/tmp/downloaded-file.bin"))
        .join();
```

------
#### [ Download to bytes ]

```
S3AsyncClient s3AsyncClient = S3AsyncClient.builder()
        .region(Region.US_EAST_1)
        .build();

ResponseBytes<GetObjectResponse> bytes = s3AsyncClient.presignedUrlExtension()
        .getObject(
            PresignedUrlDownloadRequest.builder()
                .presignedUrl(presignedGetObjectRequest.url())
                .build(),
            AsyncResponseTransformer.toBytes())
        .join();

// Or use the consumer builder pattern
ResponseBytes<GetObjectResponse> bytes = s3AsyncClient.presignedUrlExtension()
        .getObject(
            r -> r.presignedUrl(presignedGetObjectRequest.url()),
            AsyncResponseTransformer.toBytes())
        .join();
```

------

##### Multipart download for large files
<a name="get-presigned-s3async-multipart"></a>

To download large objects in parallel, set `multipartEnabled(true)` on the client:

------
#### [ Download to file ]

```
S3AsyncClient multipartClient = S3AsyncClient.builder()
        .region(Region.US_EAST_1)
        .multipartEnabled(true)
        .multipartConfiguration(c -> c.minimumPartSizeInBytes(8 * 1024 * 1024L))
        .build();

GetObjectResponse response = multipartClient.presignedUrlExtension()
        .getObject(
            PresignedUrlDownloadRequest.builder()
                .presignedUrl(presignedGetObjectRequest.url())
                .build(),
            Paths.get("/tmp/large-file.bin"))
        .join();
```

------
#### [ Download to bytes ]

```
S3AsyncClient multipartClient = S3AsyncClient.builder()
        .region(Region.US_EAST_1)
        .multipartEnabled(true)
        .multipartConfiguration(c -> c.minimumPartSizeInBytes(8 * 1024 * 1024L))
        .build();

ResponseBytes<GetObjectResponse> bytes = multipartClient.presignedUrlExtension()
        .getObject(
            PresignedUrlDownloadRequest.builder()
                .presignedUrl(presignedGetObjectRequest.url())
                .build(),
            AsyncResponseTransformer.toBytes())
        .join();
```

------

##### Use the Amazon S3 Transfer Manager
<a name="get-presigned-s3async-transfer-manager"></a>

With the [Amazon S3 Transfer Manager](transfer-manager.md), you can download objects using pre-signed URLs with progress tracking through `TransferListener`.

Add the `s3-transfer-manager` artifact to your project:

```
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>software.amazon.awssdk</groupId>
            <artifactId>bom</artifactId>
            <version>{{2.48.01}}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
<dependencies>
    <dependency>
        <groupId>software.amazon.awssdk</groupId>
        <artifactId>s3-transfer-manager</artifactId>
    </dependency>
</dependencies>
```

1 [Find the latest BOM version on the Maven Central Repository](https://central.sonatype.com/artifact/software.amazon.awssdk/bom).

##### Imports
<a name="get-presigned-tm-imports"></a>

```
import java.nio.file.Paths;
import software.amazon.awssdk.core.ResponseBytes;
import software.amazon.awssdk.core.async.AsyncResponseTransformer;
import software.amazon.awssdk.services.s3.model.GetObjectResponse;
import software.amazon.awssdk.services.s3.presignedurl.model.PresignedUrlDownloadRequest;
import software.amazon.awssdk.transfer.s3.S3TransferManager;
import software.amazon.awssdk.transfer.s3.model.CompletedFileDownload;
import software.amazon.awssdk.transfer.s3.model.Download;
import software.amazon.awssdk.transfer.s3.model.PresignedDownloadFileRequest;
import software.amazon.awssdk.transfer.s3.model.PresignedDownloadRequest;
import software.amazon.awssdk.transfer.s3.model.PresignedFileDownload;
import software.amazon.awssdk.transfer.s3.progress.LoggingTransferListener;
```

------
#### [ Download to file ]

```
S3TransferManager transferManager = S3TransferManager.create();

PresignedFileDownload fileDownload = transferManager.downloadFileWithPresignedUrl(
        PresignedDownloadFileRequest.builder()
            .presignedUrlDownloadRequest(PresignedUrlDownloadRequest.builder()
                .presignedUrl(presignedGetObjectRequest.url())
                .build())
            .destination(Paths.get("/tmp/transfer-download.bin"))
            .addTransferListener(LoggingTransferListener.create())
            .build());

CompletedFileDownload completed = fileDownload.completionFuture().join();
```

------
#### [ Download to bytes ]

```
S3TransferManager transferManager = S3TransferManager.create();

Download<ResponseBytes<GetObjectResponse>> bytesDownload =
        transferManager.downloadWithPresignedUrl(
            PresignedDownloadRequest.<ResponseBytes<GetObjectResponse>>builder()
                .presignedUrlDownloadRequest(PresignedUrlDownloadRequest.builder()
                    .presignedUrl(presignedGetObjectRequest.url())
                    .build())
                .responseTransformer(AsyncResponseTransformer.toBytes())
                .addTransferListener(LoggingTransferListener.create())
                .build());

ResponseBytes<GetObjectResponse> result =
        bytesDownload.completionFuture().join().result();
```

------

**Pause and resume not supported**
Unlike regular `FileDownload`, `PresignedFileDownload` does not support pause and resume because pre-signed URLs can expire during a paused transfer.

For more information about the Amazon S3 Transfer Manager, including configuration options and additional examples, see [Transfer files and directories with the Amazon S3 Transfer Manager](transfer-manager.md).

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/d73001daea05266eaa9e074ccb71b9383832369a/javav2/example_code/s3/src/main/java/com/example/s3/GeneratePresignedGetUrlAndRetrieve.java) and [test](https://github.com/awsdocs/aws-doc-sdk-examples/blob/d73001daea05266eaa9e074ccb71b9383832369a/javav2/example_code/s3/src/test/java/com/example/s3/presignurl/GeneratePresignedGetUrlTests.java) on GitHub.

## Generate a pre-signed URL for an upload, then upload a file (PUT request)
<a name="put-presignedobject"></a>

The following example consists of two parts.
+ Part 1: Alice generates the pre-signed URL to upload an object.
+ Part 2: Bob uploads a file by using the pre-signed URL.

### Part 1: Generate the URL
<a name="put-presigned-object-part1"></a>

Alice already has an S3 bucket. She uses the following code to generate a URL string that Bob can use in a subsequent PUT request.

#### Imports
<a name="put-presigned-example-imports"></a>

```
import com.example.s3.util.PresignUrlUtils;
import org.slf4j.Logger;
import software.amazon.awssdk.core.internal.sync.FileContentStreamProvider;
import software.amazon.awssdk.http.HttpExecuteRequest;
import software.amazon.awssdk.http.HttpExecuteResponse;
import software.amazon.awssdk.http.SdkHttpClient;
import software.amazon.awssdk.http.SdkHttpMethod;
import software.amazon.awssdk.http.SdkHttpRequest;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.PutObjectRequest;
import software.amazon.awssdk.services.s3.model.S3Exception;
import software.amazon.awssdk.services.s3.presigner.S3Presigner;
import software.amazon.awssdk.services.s3.presigner.model.PresignedPutObjectRequest;
import software.amazon.awssdk.services.s3.presigner.model.PutObjectPresignRequest;

import java.io.File;
import java.io.IOException;
import java.io.OutputStream;
import java.io.RandomAccessFile;
import java.net.HttpURLConnection;
import java.net.URISyntaxException;
import java.net.URL;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.Duration;
import java.util.Map;
import java.util.UUID;
```

```
    /* Create a presigned URL to use in a subsequent PUT request */
    public String createPresignedUrl(String bucketName, String keyName, Map<String, String> metadata) {
        try (S3Presigner presigner = S3Presigner.create()) {

            PutObjectRequest objectRequest = PutObjectRequest.builder()
                    .bucket(bucketName)
                    .key(keyName)
                    .metadata(metadata)
                    .build();

            PutObjectPresignRequest presignRequest = PutObjectPresignRequest.builder()
                    .signatureDuration(Duration.ofMinutes(10))  // The URL expires in 10 minutes.
                    .putObjectRequest(objectRequest)
                    .build();

            PresignedPutObjectRequest presignedRequest = presigner.presignPutObject(presignRequest);
            String myURL = presignedRequest.url().toString();
            logger.info("Presigned URL to upload a file to: [{}]", myURL);
            logger.info("HTTP method: [{}]", presignedRequest.httpRequest().method());

            return presignedRequest.url().toExternalForm();
        }
    }
```

### Part 2: Upload a file object
<a name="put-presigned-object-part2"></a>

Bob uses one of the following three code options to upload a file.

#### Use JDK `HttpURLConnection` (since v1.1)
<a name="put-presigned-example-useHttpUrlConnection"></a>

```
    /* Use the JDK HttpURLConnection (since v1.1) class to do the upload. */
    public void useHttpUrlConnectionToPut(String presignedUrlString, File fileToPut, Map<String, String> metadata) {
        logger.info("Begin [{}] upload", fileToPut.toString());
        try {
            URL presignedUrl = new URL(presignedUrlString);
            HttpURLConnection connection = (HttpURLConnection) presignedUrl.openConnection();
            connection.setDoOutput(true);
            metadata.forEach((k, v) -> connection.setRequestProperty("x-amz-meta-" + k, v));
            connection.setRequestMethod("PUT");
            OutputStream out = connection.getOutputStream();

            try (RandomAccessFile file = new RandomAccessFile(fileToPut, "r");
                 FileChannel inChannel = file.getChannel()) {
                ByteBuffer buffer = ByteBuffer.allocate(8192); //Buffer size is 8k

                while (inChannel.read(buffer) > 0) {
                    buffer.flip();
                    for (int i = 0; i < buffer.limit(); i++) {
                        out.write(buffer.get());
                    }
                    buffer.clear();
                }
            } catch (IOException e) {
                logger.error(e.getMessage(), e);
            }

            out.close();
            connection.getResponseCode();
            logger.info("HTTP response code is " + connection.getResponseCode());

        } catch (S3Exception | IOException e) {
            logger.error(e.getMessage(), e);
        }
    }
```

#### Use JDK `HttpClient` (since v11)
<a name="put-presigned-example-useHttpClient"></a>

```
    /* Use the JDK HttpClient (since v11) class to do the upload. */
    public void useHttpClientToPut(String presignedUrlString, File fileToPut, Map<String, String> metadata) {
        logger.info("Begin [{}] upload", fileToPut.toString());

        HttpRequest.Builder requestBuilder = HttpRequest.newBuilder();
        metadata.forEach((k, v) -> requestBuilder.header("x-amz-meta-" + k, v));

        HttpClient httpClient = HttpClient.newHttpClient();
        try {
            final HttpResponse<Void> response = httpClient.send(requestBuilder
                            .uri(new URL(presignedUrlString).toURI())
                            .PUT(HttpRequest.BodyPublishers.ofFile(Path.of(fileToPut.toURI())))
                            .build(),
                    HttpResponse.BodyHandlers.discarding());

            logger.info("HTTP response code is " + response.statusCode());

        } catch (URISyntaxException | InterruptedException | IOException e) {
            logger.error(e.getMessage(), e);
        }
    }
```

#### Use `SdkHttpClient` from the SDK for Java
<a name="put-presigned-example-useSdkHttpClient"></a>

```
    /* Use the AWS SDK for Java V2 SdkHttpClient class to do the upload. */
    public void useSdkHttpClientToPut(String presignedUrlString, File fileToPut, Map<String, String> metadata) {
        logger.info("Begin [{}] upload", fileToPut.toString());

        try {
            URL presignedUrl = new URL(presignedUrlString);

            SdkHttpRequest.Builder requestBuilder = SdkHttpRequest.builder()
                    .method(SdkHttpMethod.PUT)
                    .uri(presignedUrl.toURI());
            // Add headers
            metadata.forEach((k, v) -> requestBuilder.putHeader("x-amz-meta-" + k, v));
            // Finish building the request.
            SdkHttpRequest request = requestBuilder.build();

            HttpExecuteRequest executeRequest = HttpExecuteRequest.builder()
                    .request(request)
                    .contentStreamProvider(new FileContentStreamProvider(fileToPut.toPath()))
                    .build();

            try (SdkHttpClient sdkHttpClient = ApacheHttpClient.create()) {
                HttpExecuteResponse response = sdkHttpClient.prepareRequest(executeRequest).call();
                logger.info("Response code: {}", response.httpResponse().statusCode());
            }
        } catch (URISyntaxException | IOException e) {
            logger.error(e.getMessage(), e);
        }
    }
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/d73001daea05266eaa9e074ccb71b9383832369a/javav2/example_code/s3/src/main/java/com/example/s3/GeneratePresignedUrlAndPutFileWithMetadata.java) and [test](https://github.com/awsdocs/aws-doc-sdk-examples/blob/d73001daea05266eaa9e074ccb71b9383832369a/javav2/example_code/s3/src/test/java/com/example/s3/presignurl/GeneratePresignedPutUrlTests.java) on GitHub.

## Include request fields as URL query parameters
<a name="presign-query-parameters"></a>

Some request fields on [GetObjectRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/model/GetObjectRequest.html) and [PutObjectRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/model/PutObjectRequest.html) map to HTTP headers rather than to URL query parameters. For example, `requestPayer`, `acl`, `metadata`, `serverSideEncryption`, and `storageClass` map to `x-amz-*` headers. When you pre-sign a request that sets one of these fields, the signature covers the headers. However, the pre-signed URL that [S3Presigner](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/presigner/S3Presigner.html) returns does not contain the header values.

The caller of the pre-signed URL must send the same `x-amz-*` headers with the request. Otherwise, Amazon S3 returns `SignatureDoesNotMatch`. HTTP clients that can set custom headers send those headers directly. For example, the `HttpURLConnection`, `HttpClient`, and [SdkHttpClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/SdkHttpClient.html) examples shown earlier all do this. However, if the caller cannot set custom headers, the request fails. Common examples include a web browser opening the URL as a link, an HTML form uploading directly to Amazon S3, and any HTTP client that only receives the URL as input.

To make the URL work without extra headers, pass the value as a signed query parameter instead of setting the typed field. Use [putRawQueryParameter](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/RequestOverrideConfiguration.Builder.html#putRawQueryParameter(java.lang.String,java.lang.String)) on [AwsRequestOverrideConfiguration](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/awscore/AwsRequestOverrideConfiguration.html).

### Pre-sign a GET request with requester-pays
<a name="presign-query-parameters-get-example"></a>

The following example generates a pre-signed URL for a `GetObjectRequest` with the requester-pays setting. Because the value is a query parameter, any caller can use the URL without sending an `x-amz-request-payer` header.

```
try (S3Presigner presigner = S3Presigner.create()) {
    GetObjectRequest getObjectRequest = GetObjectRequest.builder()
            .bucket("amzn-s3-demo-bucket")
            .key("example-key")
            .overrideConfiguration(o -> o.putRawQueryParameter("x-amz-request-payer", "requester"))
            .build();

    GetObjectPresignRequest presignRequest = GetObjectPresignRequest.builder()
            .signatureDuration(Duration.ofMinutes(10))
            .getObjectRequest(getObjectRequest)
            .build();

    PresignedGetObjectRequest presigned = presigner.presignGetObject(presignRequest);
    logger.info("Pre-signed URL: [{}]", presigned.url());

    // Confirm the URL requires no headers at request time:
    logger.info("Signed headers: {}", presigned.signedHeaders().keySet());  // [host]
}
```

### Pre-sign a PUT request with metadata
<a name="presign-query-parameters-put-example"></a>

The following example generates a pre-signed URL for a `PutObjectRequest` with two metadata values as signed query parameters. Because the values are query parameters, any caller can use the URL without sending `x-amz-meta-*` headers.

```
try (S3Presigner presigner = S3Presigner.create()) {
    PutObjectRequest putObjectRequest = PutObjectRequest.builder()
            .bucket("amzn-s3-demo-bucket")
            .key("example-key")
            .overrideConfiguration(o -> o
                    .putRawQueryParameter("x-amz-meta-author", "alice")
                    .putRawQueryParameter("x-amz-meta-purpose", "demo"))
            .build();

    PutObjectPresignRequest presignRequest = PutObjectPresignRequest.builder()
            .signatureDuration(Duration.ofMinutes(10))
            .putObjectRequest(putObjectRequest)
            .build();

    PresignedPutObjectRequest presigned = presigner.presignPutObject(presignRequest);
    logger.info("Pre-signed URL: [{}]", presigned.url());

    // Confirm the URL requires no headers at upload time:
    logger.info("Signed headers: {}", presigned.signedHeaders().keySet());  // [host]
}
```

### Pre-sign a PUT request and upload a file
<a name="presign-query-parameters-helper"></a>

The following example shows the full workflow: a method that pre-signs a PUT request with any `x-amz-*` names and values you supply as a map, and a method that uploads the file with `SdkHttpClient`. Because the values are already part of the signed URL, the upload method does not set any `x-amz-*` headers. In contrast, the earlier upload examples set `x-amz-meta-*` headers explicitly.

#### Imports
<a name="presign-query-parameters-helper-imports"></a>

```
import com.example.s3.util.PresignUrlUtils;
import org.slf4j.Logger;
import software.amazon.awssdk.awscore.AwsRequestOverrideConfiguration;
import software.amazon.awssdk.core.internal.sync.FileContentStreamProvider;
import software.amazon.awssdk.http.HttpExecuteRequest;
import software.amazon.awssdk.http.HttpExecuteResponse;
import software.amazon.awssdk.http.SdkHttpClient;
import software.amazon.awssdk.http.SdkHttpMethod;
import software.amazon.awssdk.http.SdkHttpRequest;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.PutObjectRequest;
import software.amazon.awssdk.services.s3.presigner.S3Presigner;
import software.amazon.awssdk.services.s3.presigner.model.PresignedPutObjectRequest;
import software.amazon.awssdk.services.s3.presigner.model.PutObjectPresignRequest;

import java.io.File;
import java.io.IOException;
import java.net.URISyntaxException;
import java.net.URL;
import java.nio.file.Paths;
import java.time.Duration;
import java.util.Map;
import java.util.UUID;
```

Generate the URL.

```
    /**
     *  Creates a presigned URL to use in a subsequent HTTP PUT request. The code adds query parameters
     *  to the request instead of using headers. By using query parameters, you do not need to add the
     *  the parameters as headers when the PUT request is eventually sent.
     *
     * @param bucketName Bucket name where the object will be uploaded.
     * @param keyName Key name of the object that will be uploaded.
     * @param queryParams Query string parameters to be added to the presigned URL.
     * @return
     */
    public String createPresignedUrl(String bucketName, String keyName, Map<String, String> queryParams) {
        try (S3Presigner presigner = S3Presigner.create()) {
            // Create an override configuration to store the query parameters.
            AwsRequestOverrideConfiguration.Builder overrideConfigurationBuilder = AwsRequestOverrideConfiguration.builder();

            queryParams.forEach(overrideConfigurationBuilder::putRawQueryParameter);

            PutObjectRequest objectRequest = PutObjectRequest.builder()
                    .bucket(bucketName)
                    .key(keyName)
                    .overrideConfiguration(overrideConfigurationBuilder.build()) // Add the override configuration.
                    .build();

            PutObjectPresignRequest presignRequest = PutObjectPresignRequest.builder()
                    .signatureDuration(Duration.ofMinutes(10))  // The URL expires in 10 minutes.
                    .putObjectRequest(objectRequest)
                    .build();

            PresignedPutObjectRequest presignedRequest = presigner.presignPutObject(presignRequest);
            String myURL = presignedRequest.url().toString();
            logger.info("Presigned URL to upload a file to: [{}]", myURL);
            logger.info("HTTP method: [{}]", presignedRequest.httpRequest().method());

            return presignedRequest.url().toExternalForm();
        }
    }
```

Upload the file with `SdkHttpClient`.

```
    /**
     * Use the AWS SDK for Java V2 SdkHttpClient class to execute the PUT request. Since the
     * URL contains the query parameters, no headers are needed for metadata, SSE settings, or ACL settings.
     *
     * @param presignedUrlString The URL for the PUT request.
     * @param fileToPut File to uplaod
     */
    public void useSdkHttpClientToPut(String presignedUrlString, File fileToPut) {
        logger.info("Begin [{}] upload", fileToPut.toString());

        try {
            URL presignedUrl = new URL(presignedUrlString);

            SdkHttpRequest.Builder requestBuilder = SdkHttpRequest.builder()
                    .method(SdkHttpMethod.PUT)
                    .uri(presignedUrl.toURI());

            SdkHttpRequest request = requestBuilder.build();

            HttpExecuteRequest executeRequest = HttpExecuteRequest.builder()
                    .request(request)
                    .contentStreamProvider(new FileContentStreamProvider(fileToPut.toPath()))
                    .build();

            try (SdkHttpClient sdkHttpClient = ApacheHttpClient.create()) {
                HttpExecuteResponse response = sdkHttpClient.prepareRequest(executeRequest).call();
                logger.info("Response code: {}", response.httpResponse().statusCode());
            }
        } catch (URISyntaxException | IOException e) {
            logger.error(e.getMessage(), e);
        }
    }
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/0a2b7b1db35fa7b8fd362222c449f43881d67895/javav2/example_code/s3/src/main/java/com/example/s3/GeneratePresignedUrlAndPutFileWithQueryParams.java) and [test](https://github.com/awsdocs/aws-doc-sdk-examples/blob/0a2b7b1db35fa7b8fd362222c449f43881d67895/javav2/example_code/s3/src/test/java/com/example/s3/presignurl/GeneratePresignedPutUrlTests.java) on GitHub.

### Check which headers a pre-signed request requires
<a name="presign-query-parameters-verify"></a>

To check which headers a specific pre-signed request requires the caller to send, call [signedHeaders()](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/awscore/presigner/PresignedRequest.html#signedHeaders()) on the returned [PresignedRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/awscore/presigner/PresignedRequest.html). Any `x-amz-*` name in the returned map is a header the caller must send. If you want to remove a header from the requirement, pass its value through `putRawQueryParameter` instead of setting the typed field.
