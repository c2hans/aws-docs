---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-s3-presign-download.html
---

# Migrate pre-signed URL downloads from AWS SDK for Java v1 to v2
<a name="migration-s3-presign-download"></a>

Migrate your pre-signed URL download code to use asynchronous processing and access expanded download options in version 2. This topic shows how to migrate from version 1.x (v1) to version 2.x (v2) of the AWS SDK for Java. For information about v2 pre-signed URL download capabilities, see [Work with Amazon S3 pre-signed URLs](examples-s3-presign.md).

## High-level changes
<a name="migration-s3-presign-high-level"></a>

The following list summarizes the key differences between v1 and v2 for pre-signed URL downloads:
+ **Package**: `com.amazonaws.services.s3` → `software.amazon.awssdk.services.s3`.
+ **Client class**: `AmazonS3` (synchronous) → `S3AsyncClient` (asynchronous).
+ **Architecture**: Synchronous blocking calls → Asynchronous calls with `CompletableFuture`.
+ **Multipart**: Available only through Transfer Manager → Available directly on client with `multipartEnabled(true)`.
+ **Transfer Manager**: File destination only → File, bytes, or custom transformer.

## Changes in dependencies, packages, and class names
<a name="migration-s3-presign-deps"></a>

The following table shows the dependency and class name changes from v1 to v2.

| Change | v1 | v2 |
| --- | --- | --- |
| Maven dependencies |  <pre><dependencyManagement><br />    <dependencies><br />        <dependency><br />            <groupId>com.amazonaws</groupId><br />            <artifactId>aws-java-sdk-bom</artifactId><br />            <version>{{1.12.7971}}</version><br />            <type>pom</type><br />            <scope>import</scope><br />        </dependency><br />    </dependencies><br /></dependencyManagement><br /><dependencies><br />    <dependency><br />        <groupId>com.amazonaws</groupId><br />        <artifactId>aws-java-sdk-s3</artifactId><br />    </dependency><br /></dependencies></pre>  |  <pre><dependencyManagement><br />    <dependencies><br />        <dependency><br />            <groupId>software.amazon.awssdk</groupId><br />            <artifactId>bom</artifactId><br />            <version>{{2.48.02}}</version><br />            <type>pom</type><br />            <scope>import</scope><br />        </dependency><br />    </dependencies><br /></dependencyManagement><br /><dependencies><br />    <dependency><br />        <groupId>software.amazon.awssdk</groupId><br />        <artifactId>s3</artifactId><br />    </dependency><br />    <!-- Optional: for Transfer Manager --><br />    <dependency><br />        <groupId>software.amazon.awssdk</groupId><br />        <artifactId>s3-transfer-manager</artifactId><br />    </dependency><br /></dependencies></pre>  |
| Package name | com.amazonaws.services.s3 | software.amazon.awssdk.services.s3 |
| Class names | AmazonS3, TransferManager | S3AsyncClient, S3TransferManager |

1 [Latest version](https://central.sonatype.com/artifact/com.amazonaws/aws-java-sdk-bom) on the Maven Central website. 2 [Latest version](https://central.sonatype.com/artifact/software.amazon.awssdk/bom) on the Maven Central website.

## API changes
<a name="migration-s3-presign-api-changes"></a>

### S3 client downloads
<a name="migration-s3-presign-api-s3client"></a>

The following table compares v1 and v2 API calls for S3 client downloads.

| Use case | v1 | v2 |
| --- | --- | --- |
| Create the client |  <pre>AmazonS3 s3Client = <br />        AmazonS3ClientBuilder.defaultClient();</pre>  |  <pre>S3AsyncClient s3AsyncClient = <br />        S3AsyncClient.create();<br />AsyncPresignedUrlExtension extension = <br />        s3AsyncClient.presignedUrlExtension();</pre>  |
| Generate a pre-signed URL |  <pre>Date expiration = new Date(<br />        System.currentTimeMillis() + 600_000);<br />URL presignedUrl = s3Client.generatePresignedUrl(<br />        new GeneratePresignedUrlRequest(<br />            "my-bucket", "my-key")<br />            .withMethod(HttpMethod.GET)<br />            .withExpiration(expiration));</pre>  |  <pre>S3Presigner presigner = S3Presigner.create();<br />PresignedGetObjectRequest presigned = <br />        presigner.presignGetObject(r -> r<br />            .getObjectRequest(req -> req<br />                .bucket("my-bucket").key("my-key"))<br />            .signatureDuration(Duration.ofMinutes(10)));<br />URL presignedUrl = presigned.url();<br />presigner.close();</pre>  |
| Create the download request |  <pre>PresignedUrlDownloadRequest downloadRequest = <br />        new PresignedUrlDownloadRequest(presignedUrl);</pre>  |  <pre>PresignedUrlDownloadRequest downloadRequest = <br />        PresignedUrlDownloadRequest.builder()<br />            .presignedUrl(presignedUrl)<br />            .build();</pre>  |
| Download to stream |  <pre>PresignedUrlDownloadResult result = <br />        s3Client.download(downloadRequest);<br />InputStream content = result.getS3Object()<br />        .getObjectContent();</pre>  |  <pre>ResponseBytes<GetObjectResponse> bytes = <br />        extension.getObject(downloadRequest,<br />            AsyncResponseTransformer.toBytes())<br />        .join();</pre>  |
| Download to file |  <pre>s3Client.download(downloadRequest,<br />        new File("/tmp/file.bin"));</pre>  |  <pre>extension.getObject(downloadRequest,<br />            Paths.get("/tmp/file.bin"))<br />        .join();</pre>  |
| Download with range |  <pre>PresignedUrlDownloadRequest rangeRequest = <br />        new PresignedUrlDownloadRequest(presignedUrl);<br />rangeRequest.setRange(0, 1023);<br />s3Client.download(rangeRequest);</pre>  |  <pre>PresignedUrlDownloadRequest rangeRequest = <br />        PresignedUrlDownloadRequest.builder()<br />            .presignedUrl(presignedUrl)<br />            .range("bytes=0-1023")<br />            .build();<br />extension.getObject(rangeRequest,<br />            Paths.get("/tmp/partial.bin"))<br />        .join();</pre>  |

### Transfer Manager downloads
<a name="migration-s3-presign-api-tm"></a>

The following table compares v1 and v2 API calls for Transfer Manager downloads.

| Use case | v1 | v2 |
| --- | --- | --- |
| Create the Transfer Manager |  <pre>TransferManager tm = <br />        TransferManagerBuilder.standard().build();</pre>  |  <pre>S3TransferManager tm = <br />        S3TransferManager.create();</pre>  |
| Download |  <pre>PresignedUrlDownload download = tm.download(<br />        new PresignedUrlDownloadRequest(presignedUrl),<br />        new File("/tmp/file.bin"));<br />download.waitForCompletion();</pre>  |  <pre>PresignedFileDownload download = <br />        tm.downloadFileWithPresignedUrl(<br />            PresignedDownloadFileRequest.builder()<br />                .presignedUrlDownloadRequest(<br />                    downloadRequest)<br />                .destination(Paths.get("/tmp/file.bin"))<br />                .addTransferListener(<br />                    LoggingTransferListener.create())<br />                .build());<br />download.completionFuture().join();</pre>  |

For more information, see [Download using a pre-signed URL](transfer-manager.md#transfer-manager-presigned-url-download).

## Configuration changes
<a name="migration-s3-presign-config"></a>

### S3 client
<a name="migration-s3-presign-config-s3"></a>

The following table describes the S3 client configuration changes from v1 to v2.

| Setting | v1 | v2 |
| --- | --- | --- |
| Multipart configuration | PresignedUrlDownloadConfig.withDownloadSizePerRequest(long) | S3AsyncClient.builder().multipartConfiguration(c -> c.minimumPartSizeInBytes(...)) |
| Custom headers | PresignedUrlDownloadRequest.putCustomRequestHeader(String, String) | Not supported. Only Range and If-Match can be set at download time. |

### Transfer Manager
<a name="migration-s3-presign-config-tm"></a>

The following table describes the Transfer Manager configuration changes from v1 to v2.

| Setting | v1 | v2 |
| --- | --- | --- |
| Progress tracking | PresignedUrlDownloadConfig.withS3progressListener(...) | PresignedDownloadFileRequest.builder().addTransferListener(...) |
| Resume on retry | PresignedUrlDownloadConfig.withResumeOnRetry(true) | Not supported |
| Pause/Resume | Not supported | Not supported |

**Note**
The AWS CRT-based S3 client (`S3AsyncClient.crtBuilder()`) does not currently support the pre-signed URL extension. Use `S3AsyncClient.builder()`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
