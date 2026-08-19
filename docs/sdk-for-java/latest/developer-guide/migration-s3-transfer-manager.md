---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-s3-transfer-manager.html
---

# Migrate the Transfer Manager from version 1 to version 2 of the AWS SDK for Java
<a name="migration-s3-transfer-manager"></a>

This migration guide covers the key differences between Transfer Manager v1 and S3 Transfer Manager v2, including constructor changes, method mappings, and code examples for common operations. After reviewing these differences, you can successfully migrate your existing Transfer Manager code to take advantage of improved performance and asynchronous operations in v2.

**About the AWS SDK migration tool**
The AWS SDK for Java provides an automated [migration tool](migration-tool.md) that can migrate much of the v1 Transfer Manager API to v2. However, the migration tool doesn't support several v1 Transfer Manager features. For these cases, you need to manually migrate Transfer Manager code using the guidance in this topic.
Throughout this guide, the **Migration Status** shows whether the migration tool can automatically migrate a constructor, method, or feature:
**Supported**: The migration tool can automatically transform this code
**Not Supported**: You need to manually migrate code
Even for items marked as "Supported," review the migration results and test thoroughly. Transfer Manager migration involves significant architectural changes from synchronous to asynchronous operations.

## Overview
<a name="s3-tm-migration-overview"></a>

S3 Transfer Manager v2 introduces significant changes to the Transfer Manager API. S3 Transfer Manager v2 is built on asynchronous operations and provides better performance, especially when you use the AWS CRT-based Amazon S3 client.

### Key differences
<a name="s3-tm-migration-key-differences"></a>
+ **Package**: `com.amazonaws.services.s3.transfer` → `software.amazon.awssdk.transfer.s3`
+ **Class name**: `TransferManager` → `S3TransferManager`
+ **Client dependency**: Synchronous Amazon S3 client → Asynchronous Amazon S3 client (`S3AsyncClient`)
+ **Architecture**: Synchronous operations → Asynchronous operations with `CompletableFuture`
+ **Performance**: Enhanced with AWS CRT-based client support

## High-level changes
<a name="s3-tm-migration-high-level-changes"></a>

| Aspect | V1 | V2 |
| --- | --- | --- |
| Maven dependency | aws-java-sdk-s3 | s3-transfer-manager |
| Package | com.amazonaws.services.s3.transfer | software.amazon.awssdk.transfer.s3 |
| Main class | TransferManager | S3TransferManager |
| Amazon S3 client | AmazonS3 (sync) | S3AsyncClient (async) |
| Return types | Blocking operations | CompletableFuture<T> |

## Maven dependencies
<a name="s3-tm-migration-dependencies"></a>

| V1 | V2 |
| --- | --- |
|  <pre><dependencyManagement><br />    <dependencies><br />        <dependency><br />            <groupId>com.amazonaws</groupId><br />            <artifactId>aws-java-sdk-bom</artifactId><br />            <version>>{{1.12.7871}}</version><br />            <type>pom</type><br />            <scope>import</scope><br />        </dependency><br />    </dependencies><br /></dependencyManagement><br /><dependencies><br />    <dependency><br />        <groupId>com.amazonaws</groupId><br />        <artifactId>aws-java-sdk-s3</artifactId><br />    </dependency><br /></dependencies></pre>  |  <pre><dependencyManagement><br />    <dependencies><br />        <dependency><br />            <groupId>software.amazon.awssdk</groupId><br />            <artifactId>bom</artifactId><br />            <version>{{2.31.682}}</version><br />            <type>pom</type><br />            <scope>import</scope><br />        </dependency><br />    </dependencies><br /></dependencyManagement><br /><dependencies><br />    <dependency><br />        <groupId>software.amazon.awssdk</groupId><br />        <artifactId>s3-transfer-manager</artifactId><br />    </dependency><br />    <!-- Optional: For enhanced performance with AWS CRT --><br />    <dependency><br />        <groupId>software.amazon.awssdk.crt</groupId><br />        <artifactId>aws-crt</artifactId><br />        <version>{{0.38.53}}</version><br />    </dependency><br /></dependencies></pre>  |

1 [Latest version](https://central.sonatype.com/artifact/com.amazonaws/aws-java-sdk-bom). 2 [Latest version](https://central.sonatype.com/artifact/software.amazon.awssdk/bom). 3[Latest version](https://central.sonatype.com/artifact/software.amazon.awssdk.crt/aws-crt).

## Client constructor migration
<a name="s3-tm-migration-client-constructor"></a>

### Supported constructors (automatic migration)
<a name="s3-tm-migration-supported-constructors"></a>

| V1 constructor | V2 equivalent | Migration status |
| --- | --- | --- |
| new TransferManager() | S3TransferManager.create() | Supported |
| TransferManagerBuilder. defaultTransferManager() | S3TransferManager.create() | Supported |
| TransferManagerBuilder. standard().build() | S3TransferManager.builder().build() | Supported |
| new TransferManager(AWSCredentials) | S3TransferManager.builder() .s3Client(S3AsyncClient.builder() .credentialsProvider(...).build()) .build() | Supported |
| new TransferManager( AWSCredentialsProvider) | S3TransferManager.builder() .s3Client(S3AsyncClient.builder() .credentialsProvider(...).build()) .build() | Supported |

### Unsupported constructors (manual migration required)
<a name="s3-tm-migration-unsupported-constructors"></a>

| V1 constructor | V2 equivalent | Migration notes |
| --- | --- | --- |
| new TransferManager(AmazonS3) | Manual migration required | Create an S3AsyncClient separately |
| new TransferManager(AmazonS3, ExecutorService) | Manual migration required | Create an S3AsyncClient and configure executor |
| new TransferManager(AmazonS3, ExecutorService, boolean) | Manual migration required | shutDownThreadPools parameter not supported |

### Manual migration examples
<a name="s3-tm-migration-manual-examples"></a>

**V1 code:**

```
AmazonS3 s3Client = AmazonS3ClientBuilder.defaultClient();
TransferManager transferManager = new TransferManager(s3Client);
```

**V2 code:**

```
// Create an `S3AsyncClient` with similar configuration
S3AsyncClient s3AsyncClient = S3AsyncClient.builder()
    .credentialsProvider(DefaultCredentialsProvider.create())
    .build();

// Provide the configured `S3AsyncClient` to the S3 transfer manager builder.
S3TransferManager transferManager = S3TransferManager.builder()
    .s3Client(s3AsyncClient)
    .build();
```

## Client method migration
<a name="s3-tm-migration-client-methods"></a>

Currently, the migration tool supports basic `copy`, `download`, `upload`, `uploadDirectory`, `downloadDirectory`, `resumeDownload`, and `resumeUpload` methods.

### Core transfer methods
<a name="s3-tm-migration-core-transfer-methods"></a>

| V1 method | V2 method | Return type change | Migration status |
| --- | --- | --- | --- |
| upload(String, String, File) | uploadFile(UploadFileRequest) | Upload → FileUpload | Supported |
| upload(PutObjectRequest) | upload(UploadRequest) | Upload → Upload | Supported |
| download(String, String, File) | downloadFile(DownloadFileRequest) | Download → FileDownload | Supported |
| download(GetObjectRequest, File) | downloadFile(DownloadFileRequest) | Download → FileDownload | Supported |
| copy(String, String, String, String) | copy(CopyRequest) | Copy → Copy | Supported |
| copy(CopyObjectRequest) | copy(CopyRequest) | Copy → Copy | Supported |
| uploadDirectory(String, String, File, boolean) | uploadDirectory( UploadDirectoryRequest) | MultipleFileUpload → DirectoryUpload | Supported |
| downloadDirectory(String, String, File) | downloadDirectory( DownloadDirectoryRequest) | MultipleFileDownload → DirectoryDownload | Supported |
| download(PresignedUrlDownloadRequest, File) | downloadFileWithPresignedUrl( PresignedDownloadFileRequest) | PresignedUrlDownload → PresignedFileDownload | Supported |
| No equivalent | downloadWithPresignedUrl( PresignedDownloadRequest<T>) | Not applicable | New in v2 |

### Resumable transfer methods
<a name="s3-tm-migration-resumable-methods"></a>

| V1 method | V2 method | Migration status |
| --- | --- | --- |
| resumeUpload(PersistableUpload) | resumeUploadFile(ResumableFileUpload) | Supported |
| resumeDownload(PersistableDownload) | resumeDownloadFile(ResumableFileDownload) | Supported |

### Lifecycle methods
<a name="s3-tm-migration-lifecycle-methods"></a>

| V1 method | V2 method | Migration status |
| --- | --- | --- |
| shutdownNow() | close() | Supported |
| shutdownNow(boolean) | Manually adjust code using the close() method | Not Supported |

### Unsupported V1 client methods
<a name="s3-tm-migration-unsupported-methods"></a>

| V1 method | V2 alternative | Notes |
| --- | --- | --- |
| abortMultipartUploads(String, Date) | Use the low-level Amazon S3 client | Not Supported |
| getAmazonS3Client() | Save a reference separately | Not Supported; no getter in v2 |
| getConfiguration() | Save a reference separately | Not Supported; no getter in v2 |
| uploadFileList(...) | Make multiple uploadFile() calls | Not Supported |
| copy methods with a TransferStateChangeListener parameter | Use TransferListener | [See manual migration example](#tm-unsupported-client-methods-copy) |
| download methods with an S3ProgressListener parameter | Use [`TransferListener`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/transfer/s3/progress/TransferListener.html) | [See manual migration example](#tm-unsupported-client-methods-download) |
| `downloadDirectory` methods with 4 or more parameters |  | [See manual migration example](#tm-unsupported-client-methods-download-dir) |
| upload method with an ObjectMetadataProvider parameter | Set metadata in request | [See manual migration example](#tm-unsupported-client-methods-upload) |
| uploadDirectory methods with \*Provider parameter | Set tags in request | [See manual migration example](#tm-unsupported-client-methods-uploadDirectory) |

#### `copy` methods with a `TransferStateChangeListener` parameter
<a name="tm-unsupported-client-methods-copy"></a>
+ `copy(CopyObjectRequest copyObjectRequest, AmazonS3 srcS3, TransferStateChangeListener stateChangeListener)`
+ `copy(CopyObjectRequest copyObjectRequest, TransferStateChangeListener stateChangeListener)`

```
// V1 ----------------------------------------------------------------------------------------------
// Initialize source S3 client
AmazonS3 s3client = AmazonS3ClientBuilder.standard()
                .withRegion("us-west-2")
                .build();

// Initialize Transfer Manager
TransferManager tm = TransferManagerBuilder.standard()
                .withS3Client(srcS3)
                .build();

CopyObjectRequest copyObjectRequest = new CopyObjectRequest(
                "amzn-s3-demo-source-bucket",
                "source-key",
                "amzn-s3-demo-destination-bucket",
                "destination-key"
        );

TransferStateChangeListener stateChangeListener = new TransferStateChangeListener() {
            @Override
            public void transferStateChanged(Transfer transfer, TransferState state) {
              //Implementation of the TransferStateChangeListener
            }
        };

Copy copy = tm.copy(copyObjectRequest, srcS3, stateChangeListener);

// V2 ----------------------------------------------------------------------------------------------
S3AsyncClient s3AsyncClient = S3AsyncClient.builder()
                .region(Region.US_WEST_2)
                .build();

S3TransferManager transferManager = S3TransferManager.builder()
                .s3Client(s3AsyncClient)
                .build();

// Create transfer listener (equivalent to TransferStateChangeListener in v1)
TransferListener transferListener = new TransferListener() {
            @Override
            public void transferInitiated(Context.TransferInitiated context) {
               //Implementation
               System.out.println("Transfer initiated");
            }

            @Override
            public void bytesTransferred(Context.BytesTransferred context) {
                //Implementation
                System.out.println("Bytes transferred");
            }

            @Override
            public void transferComplete(Context.TransferComplete context) {
                //Implementation
                System.out.println("Transfer completed!");
            }

            @Override
            public void transferFailed(Context.TransferFailed context) {
                //Implementation
                System.out.println("Transfer failed");
            }
        };

CopyRequest copyRequest = CopyRequest.builder()
                              .copyObjectRequest(req -> req
                                  .sourceBucket("amzn-s3-demo-source-bucket")
                                  .sourceKey("source-key")
                                  .destinationBucket("amzn-s3-demo-destination-bucket")
                                  .destinationKey("destination-key")
                               )
                                .addTransferListener(transferListener) // Configure the transferListener into the request
                                .build();

Copy copy = transferManager.copy(copyRequest);
```

#### `download` methods with an `S3ProgressListener` parameter
<a name="tm-unsupported-client-methods-download"></a>
+ `download(GetObjectRequest getObjectRequest, File file, S3ProgressListener progressListener)`
+ `download(GetObjectRequest getObjectRequest, File file, S3ProgressListener progressListener, long timeoutMillis)`
+ `download(GetObjectRequest getObjectRequest, File file, S3ProgressListener progressListener, long timeoutMillis, boolean resumeOnRetry)`

```
// V1 ----------------------------------------------------------------------------------------------
S3ProgressListener progressListener = new S3ProgressListener() {
        @Override
        public void progressChanged(com.amazonaws.event.ProgressEvent progressEvent) {
            long bytes = progressEvent.getBytesTransferred();
            ProgressEventType eventType = progressEvent.getEventType();
            // Use bytes and eventType as needed
        }

        @Override
        public void onPersistableTransfer(PersistableTransfer persistableTransfer) {

        }
    };

Download download1 = tm.download(getObjectRequest, file, progressListener);
Download download2 = tm.download(getObjectRequest, file, progressListener, timeoutMillis)
Download download3 = tm.download(getObjectRequest, file, progressListener, timeoutMillis, true)

// V2 ----------------------------------------------------------------------------------------------
TransferListener transferListener = new TransferListener() {
    @Override
    public void transferInitiated(Context.InitializedContext context) {
        // Equivalent to ProgressEventType.TRANSFER_STARTED_EVENT
        System.out.println("Transfer initiated");
    }

    @Override
    public void bytesTransferred(Context.BytesTransferred context) {
        // Equivalent to ProgressEventType.REQUEST_BYTE_TRANSFER_EVENT
        long bytes = context.bytesTransferred();
        System.out.println("Bytes transferred: " + bytes);
    }

    @Override
    public void transferComplete(Context.TransferComplete context) {
        // Equivalent to ProgressEventType.TRANSFER_COMPLETED_EVENT
        System.out.println("Transfer completed");
    }

    @Override
    public void transferFailed(Context.TransferFailed context) {
        // Equivalent to ProgressEventType.TRANSFER_FAILED_EVENT
        System.out.println("Transfer failed: " + context.exception().getMessage());
    }
};
DownloadFileRequest downloadFileRequest =
                         DownloadFileRequest.builder()
                             .getObjectRequest(getObjectRequest)
                             .destination(file.toPath())
                             .addTransferListener(transferListener)
                             .build();

// For download1
FileDownload download = transferManager.downloadFile(downloadFileRequest);

// For download2
CompletedFileDownload completedFileDownload = download.completionFuture()
                                                  .get(timeoutMillis, TimeUnit.MILLISECONDS);

// For download3, the v2 SDK does not have a direct equiavalent to the `resumeOnRetry` method of v1.
// If a download is interrupted, you need to start a new download request.
```

#### `downloadDirectory` methods with 4 or more parameters
<a name="tm-unsupported-client-methods-download-dir"></a>
+ `downloadDirectory(String bucketName, String keyPrefix, File destinationDirectory, boolean resumeOnRetry)`
+ `downloadDirectory(String bucketName, String keyPrefix, File destinationDirectory, boolean resumeOnRetry, KeyFilter filter)`
+ `downloadDirectory(String bucketName, String keyPrefix, File destinationDirectory, KeyFilter filter)`

```
// V1 ----------------------------------------------------------------------------------------------
KeyFilter filter = new KeyFilter() {
            @Override
            public boolean shouldInclude(S3ObjectSummary objectSummary) {
                //Filter implementation
            }
        };
MultipleFileDownload multipleFileDownload = tm.downloadDirectory(bucketName, keyPrefix, destinationDirectory, filter);

// V2 ----------------------------------------------------------------------------------------------
// The v2 SDK does not have a direct equiavalent to the `resumeOnRetry` method of v1.
// If a download is interrupted, you need to start a new download request.
DownloadFilter filter = new DownloadFilter() {
            @Override
            public boolean test(S3Object s3Object) {
                // Filter implementation.
            }
        };

DownloadDirectoryRequest downloadDirectoryRequest =
                              DownloadDirectoryRequest.builder()
                                  .bucket(bucketName)
                                  .filter(filter)
                                  .listObjectsV2RequestTransformer(builder -> builder.prefix(keyPrefix))
                                  .destination(destinationDirectory.toPath())
                                  .build();

DirectoryDownload directoryDownload = transferManager.downloadDirectory(downloadDirectoryRequest);
```

#### `upload` method with `ObjectMetadata` parameter
<a name="tm-unsupported-client-methods-upload"></a>
+ `upload(String bucketName, String key, InputStream input, ObjectMetadata objectMetadata)`

```
// V1 ----------------------------------------------------------------------------------------------ObjectMetadata metadata = new ObjectMetadata();
ObjectMetadata metadata = new ObjectMetadata();

metadata.setContentType("text/plain");        // System-defined metadata
metadata.setContentLength(22L);               // System-defined metadata
metadata.addUserMetadata("myKey", "myValue"); // User-defined metadata

PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, key, inputStream, metadata);

Upload upload = transferManager.upload("amzn-s3-demo-bucket", "my-key", inputStream, metadata);

// V2 ----------------------------------------------------------------------------------------------
/* When you use an InputStream to upload in V2, you should specify the content length
   and use `RequestBody.fromInputStream()`.
   If you don't provide the content length, the entire stream will be buffered in memory.
   If you can't determine the content length, we recommend using the CRT-based S3 client.
*/
Map<String, String> userMetadata = new HashMap<>();
userMetadata.put("x-amz-meta-myKey", "myValue");

PutObjectRequest putObjectRequest =
                        PutObjectRequest.builder()
                            .bucket("amzn-s3-demo-bucket1")
                            .key("k")
                            .contentType("text/plain") //System-defined metadata usually has separate methods in the builder.
                            .contentLength(22L)
                            .metadata(userMetadata) //metadata() is only for user-defined metadata.
                            .build();

UploadRequest uploadRequest =
                        UploadRequest.builder()
                            .putObjectRequest(putObjectRequest)
                            .requestBody(AsyncRequestBody.fromInputStream(stream, 22L, executor))
                            .build();

transferManager.upload(uploadRequest).completionFuture().join();
```

#### `uploadDirectory` with `ObjectMetadataProvider` parameter
<a name="tm-unsupported-client-methods-uploadDirectory"></a>
+ `uploadDirectory(String bucketName, String virtualDirectoryKeyPrefix, File directory, boolean includeSubdirectories, ObjectMetadataProvider metadataProvider)`
+ `uploadDirectory(String bucketName, String virtualDirectoryKeyPrefix, File directory, boolean includeSubdirectories, ObjectMetadataProvider metadataProvider, ObjectTaggingProvider taggingProvider)`
+ `uploadDirectory(String bucketName, String virtualDirectoryKeyPrefix, File directory, boolean includeSubdirectories, ObjectMetadataProvider metadataProvider, ObjectTaggingProvider taggingProvider, ObjectCannedAclProvider cannedAclProvider)`

```
// V1 ----------------------------------------------------------------------------------------------
tm.uploadDirectory(bucketName, virtualDirectoryKeyPrefix, directory, includeSubdirectories, metadataProvider)
tm.uploadDirectory(bucketName, virtualDirectoryKeyPrefix, directory, includeSubdirectories, metadataProvider, taggingProvider)
tm.uploadDirectory(bucketName, virtualDirectoryKeyPrefix, directory, includeSubdirectories, metadataProvider, taggingProvider, cannedAclProvider)

// V2 ----------------------------------------------------------------------------------------------
UploadDirectoryRequest request = UploadDirectoryRequest.builder()
                                  .bucket(bucketName)
                                  .s3Prefix(virtualDirectoryKeyPrefix)
                                  .source(directory.toPath())
                                  .maxDepth(includeSubdirectories ? Integer.MAX_VALUE : 1)
                                  .uploadFileRequestTransformer(builder -> {
                                      // 1.Replace `ObjectMetadataProvider`, `ObjectTaggingProvider`, and `ObjectCannedAclProvider` with an
                                        // `UploadFileRequestTransformer` that can combine the functionality of all three *Provider implementations.
                                        // 2. Convert your v1 `ObjectMetadata` to v2 `PutObjectRequest` parameters.
                                        // 3. Convert your v1 `ObjectTagging` to v2 `Tagging`.
                                        // 4. Convert your v1 `CannedAccessControlList` to v2 `ObjectCannedACL`.
                                  })
                                  .build();

DirectoryUpload directoryUpload = transferManager.uploadDirectory(request);
```

## Model object migration
<a name="s3-tm-migration-model-objects"></a>

In AWS SDK for Java 2.x, many of the `TransferManager` model objects have been redesigned, and several getter and setter methods available in v1's model objects are no longer supported.

In v2, you can use the `CompletableFuture<T>` class to perform actions when the transfer completes—either successfully or with an exception. You can use the `join()` method to wait for completion if needed.

### Core transfer objects
<a name="s3-tm-migration-core-transfer-objects"></a>

| V1 class | V2 class | Migration status |
| --- | --- | --- |
| TransferManager | S3TransferManager | Supported |
| TransferManagerBuilder | S3TransferManager.Builder | Supported |
| Transfer | Transfer | Supported |
| AbortableTransfer | Transfer | Supported (no separate class) |
| Copy | Copy | Supported |
| Download | FileDownload | Supported |
| Upload | Upload / FileUpload | Supported |
| MultipleFileDownload | DirectoryDownload | Supported |
| MultipleFileUpload | DirectoryUpload | Supported |

### Persistence objects
<a name="s3-tm-migration-persistence-objects"></a>

| V1 class | V2 class | Migration status |
| --- | --- | --- |
| PersistableDownload | ResumableFileDownload | Supported |
| PersistableUpload | ResumableFileUpload | Supported |
| PersistableTransfer | ResumableTransfer | Supported |
| PauseResult<T> | Direct resumable object | Not Supported |

### Result objects
<a name="s3-tm-migration-result-objects"></a>

| V1 class | V2 class | Migration status |
| --- | --- | --- |
| CopyResult | CompletedCopy | Supported |
| UploadResult | CompletedUpload | Supported |

### Configuration objects
<a name="s3-tm-migration-configuration-objects"></a>

| V1 class | V2 class | Migration status |
| --- | --- | --- |
| TransferManagerConfiguration | MultipartConfiguration (on Amazon S3 client) | Supported |
| TransferProgress | TransferProgress \+ TransferProgressSnapshot | Supported |
| KeyFilter | DownloadFilter | Supported |

### Unsupported objects
<a name="s3-tm-migration-unsupported-objects"></a>

| V1 class | V2 alternative | Migration status |
| --- | --- | --- |
| PauseStatus | Not supported | Not Supported |
| UploadContext | Not supported | Not Supported |
| ObjectCannedAclProvider | PutObjectRequest.builder().acl() | Not Supported |
| ObjectMetadataProvider | PutObjectRequest.builder().metadata() | Not Supported |
| ObjectTaggingProvider | PutObjectRequest.builder().tagging() | Not Supported |
| PresignedUrlDownload | PresignedGetObjectRequest | Supported. See [Migrate pre-signed URL downloads from AWS SDK for Java v1 to v2](migration-s3-presign-download.md). |

## TransferManagerBuilder configuration migration
<a name="s3-tm-migration-builder-configuration"></a>

### Configuration changes
<a name="migration-transfer-manager-config-changes"></a>

The configuration changes that you need to set for the v2 transfer manager depend on which S3 client that you use. You have the choice of the AWS CRT-based S3 client or the standard Java-based S3 async client. For information about the differences, see the [S3 clients in the AWS SDK for Java 2.x](examples-s3.md#s3-clients) topic.

------
#### [ Use the AWS CRT-based S3 client ]

| Setting | v1 | v2 - Transfer Manager using AWS CRT-based S3 client |
| --- | --- | --- |
|  <br />(get a builder) |  <pre>TransferManagerBuilder tmBuilder = <br />   TransferManagerBuilder.standard();</pre>  |  <pre>S3TransferManager.Builder tmBuilder  = <br />  S3TransferManager.builder();</pre>  |
|  <br />S3 client |  <pre>tmBuilder.withS3Client(...);<br />tmBuilder.setS3Client(...);</pre>  |  <pre>tmBuilder.s3Client(...);</pre>  |
|  <br />Executor |  <pre>tmBuilder.withExecutorFactory(...);<br />tmBuilder.setExecutorFactory(...);</pre>  |  <pre>tmBuilder.executor(...);</pre>  |
|  <br />Shutdown thread pools |  <pre>tmBuilder.withShutDownThreadPools(...);<br />tmBuilder.setShutdownThreadPools(...);</pre>  | Not supported. The provided executor will not be shut down when the S3TransferManager is closed |
|  <br />Minimum upload part size |  <pre>tmBuilder.withMinimumUploadPartSize(...);<br />tmBuilder.setMinimumUploadPartSize(...);</pre>  |  <pre>S3AsyncClient s3 = S3AsyncClient.crtBuilder().<br />      minimumPartSizeInBytes(...).build();<br /><br />tmBuilder.s3Client(s3);</pre>  |
|  <br />Multipart upload threshold |  <pre>tmBuilder.withMultipartUploadThreshold(...);<br />tmBuilder.setMultipartUploadThreshold(...);</pre>  |  <pre>S3AsyncClient s3 = S3AsyncClient.crtBuilder().<br />      thresholdInBytes(...).build();<br /><br />tmBuilder.s3Client(s3);</pre>  |
|  <br />Minimum copy part size |  <pre>tmBuilder.withMultipartCopyPartSize(...);<br />tmBuilder.setMultipartCopyPartSize(...);</pre>  |  <pre>S3AsyncClient s3 = S3AsyncClient.crtBuilder().<br />      minimumPartSizeInBytes(...).build();<br /><br />tmBuilder.s3Client(s3);</pre>  |
|  <br />Multipart copy threshold |  <pre>tmBuilder.withMultipartCopyThreshold(...);<br />tmBuilder.setMultipartCopyThreshold(...);</pre>  |  <pre>S3AsyncClient s3 = S3AsyncClient.crtBuilder().<br />      thresholdInBytes(...).build();<br /><br />tmBuilder.s3Client(s3);</pre>  |
|  <br />Disable parallel downloads |  <pre>tmBuilder.withDisableParallelDownloads(...);<br />tmBuilder.setDisableParallelDownloads(...);</pre>  | Disable parallel downloads by passing a standard Java-based S3 client with multipart disabled (default) to the transfer manager.<pre>S3AsyncClient s3 =<br />   S3AsyncClient.builder().build();<br /><br />tmBuilder.s3Client(s3);</pre> |
|  <br />Always calculate multipart md5 |  <pre>tmBuilder.withAlwaysCalculateMultipartMd5(...);<br />tmBuilder.setAlwaysCalculateMultipartMd5(...);</pre>  | Not supported. |

------
#### [ Use Java-based S3 async client ]

| Setting | v1 | v2 - Transfer Manager using Java-based S3 async client |
| --- | --- | --- |
|  <br />(get a builder) |  <pre>TransferManagerBuilder tmBuilder = <br />   TransferManagerBuilder.standard();</pre>  |  <pre>S3TransferManager.Builder tmBuilder  = <br />  S3TransferManager.builder();</pre>  |
|  <br />S3 client |  <pre>tmBuilder.withS3Client(...);<br />tmBuilder.setS3Client(...);</pre>  |  <pre>tmBuilder.s3Client(...);</pre>  |
|  <br />Executor |  <pre>tmBuilder.withExecutorFactory(...);<br />tmBuilder.setExecutorFactory(...);</pre>  |  <pre>tmBuilder.executor(...);</pre>  |
|  <br />Shutdown thread pools |  <pre>tmBuilder.withShutDownThreadPools(...);<br />tmBuilder.setShutdownThreadPools(...);</pre>  | Not supported. The provided executor will not be shut down when the S3TransferManager is closed |
|  <br />Minimum upload part size |  <pre>tmBuilder.withMinimumUploadPartSize(...);<br />tmBuilder.setMinimumUploadPartSize(...);</pre>  |  <pre>S3AsyncClient s3 = S3AsyncClient.builder()<br />    .multipartConfiguration(cfg -><br />        cfg.minimumPartSizeInBytes(...)).build();<br /><br />tmBuilder.s3Client(s3);</pre>  |
|  <br />Multipart upload threshold |  <pre>tmBuilder.withMultipartUploadThreshold(...);<br />tmBuilder.setMultipartUploadThreshold(...);</pre>  |  <pre>S3AsyncClient s3 = S3AsyncClient.builder()<br />    .multipartConfiguration(cfg -><br />        cfg.thresholdInBytes(...)).build();<br /><br />tmBuilder.s3Client(s3);</pre>  |
|  <br />Minimum copy part size |  <pre>tmBuilder.withMultipartCopyPartSize(...);<br />tmBuilder.setMultipartCopyPartSize(...);</pre>  |  <pre>S3AsyncClient s3 = S3AsyncClient.builder()<br />    .multipartConfiguration(cfg -><br />        cfg.minimumPartSizeInBytes(...)).build();<br /><br />tmBuilder.s3Client(s3);</pre>  |
|  <br />Multipart copy threshold |  <pre>tmBuilder.withMultipartCopyThreshold(...);<br />tmBuilder.setMultipartCopyThreshold(...);</pre>  |  <pre>S3AsyncClient s3 = S3AsyncClient.builder()<br />    .multipartConfiguration(cfg -><br />        cfg.thresholdInBytes(...)).build();<br /><br />tmBuilder.s3Client(s3);</pre>  |
|  <br />Disable parallel downloads |  <pre>tmBuilder.withDisableParallelDownloads(...);<br />tmBuilder.setDisableParallelDownloads(...);</pre>  | Disable parallel downloads by passing a standard Java-based S3 client with multipart disabled (default) to the transfer manager.<pre>S3AsyncClient s3 =<br />   S3AsyncClient.builder().build();<br /><br />tmBuilder.s3Client(s3);</pre> |
|  <br />Always calculate multipart md5 |  <pre>tmBuilder.withAlwaysCalculateMultipartMd5(...);<br />tmBuilder.setAlwaysCalculateMultipartMd5(...);</pre>  | Not supported. |

------

## Behavior changes
<a name="s3-tm-migration-behavior-changes"></a>

### Asynchronous operations
<a name="s3-tm-migration-async-operations"></a>

**V1 (blocking):**

```
Upload upload = transferManager.upload("amzn-s3-demo-bucket", "key", file);
upload.waitForCompletion(); // Blocks until complete
```

**V2 (asynchronous):**

```
FileUpload upload = transferManager.uploadFile(UploadFileRequest.builder()
    .putObjectRequest(PutObjectRequest.builder()
        .bucket("amzn-s3-demo-bucket")
        .key("key")
        .build())
    .source(file)
    .build());

CompletedFileUpload result = upload.completionFuture().join(); // Blocks until complete
// Or handle asynchronously:
upload.completionFuture().thenAccept(result -> {
    System.out.println("Upload completed: " + result.response().eTag());
});
```

### Error handling
<a name="s3-tm-migration-error-handling"></a>

**V1:** Directory transfers fail completely if any sub-request fails.

**V2:** Directory transfers complete successfully even if some sub-requests fail. Check for errors explicitly:

```
DirectoryUpload directoryUpload = transferManager.uploadDirectory(request);
CompletedDirectoryUpload result = directoryUpload.completionFuture().join();

// Check for failed transfers
if (!result.failedTransfers().isEmpty()) {
    System.out.println("Some uploads failed:");
    result.failedTransfers().forEach(failed ->
        System.out.println("Failed: " + failed.exception().getMessage()));
}
```

### Parallel download via byte-range fetches
<a name="migration-transfer-manager-behavior-fetches"></a>

When the automatic parallel transfer feature is enabled in the v2 SDK, the S3 Transfer Manager uses [byte-range fetches](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance-guidelines.html#optimizing-performance-guidelines-get-range) to retrieve specific portions of the object in parallel (multipart download). The way an object is downloaded with v2 does not depend on how the object was originally uploaded. All downloads can benefit from high throughput and concurrency.

In contrast, with v1's Transfer Manager, it does matter how the object was originally uploaded. The v1 Transfer Manager retrieves the parts of the object the same way that the parts were uploaded. If an object was originally uploaded as a single object, the v1 Transfer Manager is not able to accelerate the downloading process by using sub-requests.
