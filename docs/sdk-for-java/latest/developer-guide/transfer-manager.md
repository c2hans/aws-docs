---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/transfer-manager.html
---

# Transfer files and directories with the Amazon S3 Transfer Manager
<a name="transfer-manager"></a>

The Amazon S3 Transfer Manager is an open source, high level file transfer utility for the AWS SDK for Java 2.x. Use it to transfer files and directories to and from Amazon Simple Storage Service (Amazon S3).

When built on top of the [AWS CRT-based S3 client](crt-based-s3-client.md) or the [standard Java-based S3 async client with multipart enabled](s3-async-client-multipart.md), the S3 Transfer Manager can take advantage of performance improvements such as the [multipart upload API](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html) and [byte-range fetches](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance-guidelines.html#optimizing-performance-guidelines-get-range).

With the S3 Transfer Manager, you can also monitor a transfer's progress in real time and pause the transfer for later execution.

## Get started
<a name="transfer-manager-prerequisites"></a>

### Add dependencies to your build file
<a name="transfer-manager-add-dependency"></a>

To use the S3 Transfer Manager with enhanced multipart performance, configure your build file with necessary dependencies.

------
#### [ Use the AWS CRT-based S3 client ]

```
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>software.amazon.awssdk</groupId>
            <artifactId>bom</artifactId>
            <version>{{2.27.211}}</version>
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
    <dependency>
        <groupId>software.amazon.awssdk.crt</groupId>
        <artifactId>aws-crt</artifactId>
        <version>{{0.29.1432}}</version>
    </dependency>
</dependencies>
```

1 [Find the latest BOM version on the Maven Central Repository](https://central.sonatype.com/artifact/software.amazon.awssdk/bom). 2[Find the latest CRT version on the Maven Central Repository](https://central.sonatype.com/artifact/software.amazon.awssdk.crt/aws-crt).

------
#### [ Use the Java-based S3 async client ]

```
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>software.amazon.awssdk</groupId>
            <artifactId>bom</artifactId>
            <version>{{2.27.211}}</version>
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

------

### Create an instance of the S3 Transfer Manager
<a name="transfer-manager-create"></a>

To enable parallel transfer, you must pass in a AWS CRT-based S3 client OR a Java-based S3 async client with multipart enabled. The following examples shows how to configure a S3 Transfer Manager with custom settings.

------
#### [ Use the AWS CRT-based S3 client ]

```
        S3AsyncClient s3AsyncClient = S3AsyncClient.builder()
                .credentialsProvider(DefaultCredentialsProvider.create())
                .region(Region.US_EAST_1)
                .multipartEnabled(true)
                .multipartConfiguration(c -> c.minimumPartSizeInBytes(8 * MB))
                .build();

        S3TransferManager transferManager = S3TransferManager.builder()
                .s3Client(s3AsyncClient)
                .build();
```

------
#### [ Use the Java-based S3 async client ]

If the `aws-crt` dependency is not included in the build file, the S3 Transfer Manager is built on top of the standard Java-based S3 async client used in the SDK for Java 2.x.

**Custom configuration of S3 client - requires multipart enabled**

```
        S3AsyncClient s3AsyncClient = S3AsyncClient.builder()
                .multipartEnabled(true)
                .credentialsProvider(DefaultCredentialsProvider.create())
                .region(Region.US_EAST_1)
                .build();

        S3TransferManager transferManager = S3TransferManager.builder()
                .s3Client(s3AsyncClient)
                .build();
```

**No configuration of S3 client - multipart support automatically enabled**

```
S3TransferManager transferManager = S3TransferManager.create();
```

------

## Upload a file to an S3 bucket
<a name="transfer-manager-upload"></a>

The following example shows a file upload example along with the optional use of a [LoggingTransferListener](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/transfer/s3/progress/LoggingTransferListener.html), which logs the progress of the upload.

To upload a file to Amazon S3 using the S3 Transfer Manager, pass an [`UploadFileRequest`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/transfer/s3/model/UploadFileRequest.html) object to the `S3TransferManager`'s [uploadFile](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/transfer/s3/S3TransferManager.html#uploadFile(software.amazon.awssdk.transfer.s3.model.UploadFileRequest)) method.

The [FileUpload](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/transfer/s3/model/FileUpload.html) object returned from the `uploadFile` method represents the upload process. After the request finishes, the [CompletedFileUpload](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/transfer/s3/model/CompletedFileUpload.html) object contains information about the upload.

```
    public void trackUploadFile(S3TransferManager transferManager, String bucketName,
                             String key, URI filePathURI) {
        UploadFileRequest uploadFileRequest = UploadFileRequest.builder()
                .putObjectRequest(b -> b.bucket(bucketName).key(key))
                .addTransferListener(LoggingTransferListener.create())  // Add listener.
                .source(Paths.get(filePathURI))
                .build();

        FileUpload fileUpload = transferManager.uploadFile(uploadFileRequest);

        fileUpload.completionFuture().join();
        /*
            The SDK provides a LoggingTransferListener implementation of the TransferListener interface.
            You can also implement the interface to provide your own logic.

            Configure log4J2 with settings such as the following.
                <Configuration status="WARN">
                    <Appenders>
                        <Console name="AlignedConsoleAppender" target="SYSTEM_OUT">
                            <PatternLayout pattern="%m%n"/>
                        </Console>
                    </Appenders>

                    <Loggers>
                        <logger name="software.amazon.awssdk.transfer.s3.progress.LoggingTransferListener" level="INFO" additivity="false">
                            <AppenderRef ref="AlignedConsoleAppender"/>
                        </logger>
                    </Loggers>
                </Configuration>

            Log4J2 logs the progress. The following is example output for a 21.3 MB file upload.
                Transfer initiated...
                |                    | 0.0%
                |====                | 21.1%
                |============        | 60.5%
                |====================| 100.0%
                Transfer complete!
        */
    }
```

### Imports
<a name="transfer-manager-upload-imports"></a>

```
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import software.amazon.awssdk.transfer.s3.S3TransferManager;
import software.amazon.awssdk.transfer.s3.model.CompletedFileUpload;
import software.amazon.awssdk.transfer.s3.model.FileUpload;
import software.amazon.awssdk.transfer.s3.model.UploadFileRequest;
import software.amazon.awssdk.transfer.s3.progress.LoggingTransferListener;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.URL;
import java.nio.file.Paths;
import java.util.UUID;
```

## Download a file from an S3 bucket
<a name="transfer-manager-download"></a>

The following example shows a download example along with the optional use of a [LoggingTransferListener](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/transfer/s3/progress/LoggingTransferListener.html), which logs the progress of the download.

To download an object from an S3 bucket using the S3 Transfer Manager, build a [DownloadFileRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/transfer/s3/model/DownloadFileRequest.html) object and pass it to the [downloadFile](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/transfer/s3/S3TransferManager.html#downloadFile(software.amazon.awssdk.transfer.s3.model.DownloadFileRequest)) method.

The [FileDownload](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/transfer/s3/model/FileDownload.html) object returned by the `S3TransferManager`'s `downloadFile` method represents the file transfer. After the download completes, the [CompletedFileDownload](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/transfer/s3/model/CompletedFileDownload.html) contains access to information about the download.

```
    public void trackDownloadFile(S3TransferManager transferManager, String bucketName,
                             String key, String downloadedFileWithPath) {
        DownloadFileRequest downloadFileRequest = DownloadFileRequest.builder()
                .getObjectRequest(b -> b.bucket(bucketName).key(key))
                .addTransferListener(LoggingTransferListener.create())  // Add listener.
                .destination(Paths.get(downloadedFileWithPath))
                .build();

        FileDownload downloadFile = transferManager.downloadFile(downloadFileRequest);

        CompletedFileDownload downloadResult = downloadFile.completionFuture().join();
        /*
            The SDK provides a LoggingTransferListener implementation of the TransferListener interface.
            You can also implement the interface to provide your own logic.

            Configure log4J2 with settings such as the following.
                <Configuration status="WARN">
                    <Appenders>
                        <Console name="AlignedConsoleAppender" target="SYSTEM_OUT">
                            <PatternLayout pattern="%m%n"/>
                        </Console>
                    </Appenders>

                    <Loggers>
                        <logger name="software.amazon.awssdk.transfer.s3.progress.LoggingTransferListener" level="INFO" additivity="false">
                            <AppenderRef ref="AlignedConsoleAppender"/>
                        </logger>
                    </Loggers>
                </Configuration>

            Log4J2 logs the progress. The following is example output for a 21.3 MB file download.
                Transfer initiated...
                |=======             | 39.4%
                |===============     | 78.8%
                |====================| 100.0%
                Transfer complete!
        */
    }
```

### Imports
<a name="transfer-manager-download-import"></a>

```
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import software.amazon.awssdk.core.exception.SdkException;
import software.amazon.awssdk.core.sync.RequestBody;
import software.amazon.awssdk.transfer.s3.S3TransferManager;
import software.amazon.awssdk.transfer.s3.model.CompletedFileDownload;
import software.amazon.awssdk.transfer.s3.model.DownloadFileRequest;
import software.amazon.awssdk.transfer.s3.model.FileDownload;
import software.amazon.awssdk.transfer.s3.progress.LoggingTransferListener;

import java.io.IOException;
import java.net.URISyntaxException;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.NoSuchFileException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.UUID;
```

## Copy an Amazon S3 object to another bucket
<a name="transfer-manager-copy"></a>

The following example shows how to copy an object with the S3 Transfer Manager.

To begin the copy of an object from an S3 bucket to another bucket, create a basic [CopyObjectRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/model/CopyObjectRequest.html) instance.

Next, wrap the basic `CopyObjectRequest` in a [CopyRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/transfer/s3/model/CopyRequest.html) that can be used by the S3 Transfer Manager.

The `Copy` object returned by the `S3TransferManager`'s `copy` method represents the copy process. After the copy process completes, the [CompletedCopy](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/transfer/s3/model/CompletedCopy.html) object contains details about the response.

```
    public String copyObject(S3TransferManager transferManager, String bucketName,
            String key, String destinationBucket, String destinationKey) {
        CopyObjectRequest copyObjectRequest = CopyObjectRequest.builder()
                .sourceBucket(bucketName)
                .sourceKey(key)
                .destinationBucket(destinationBucket)
                .destinationKey(destinationKey)
                .build();

        CopyRequest copyRequest = CopyRequest.builder()
                .copyObjectRequest(copyObjectRequest)
                .build();

        Copy copy = transferManager.copy(copyRequest);

        CompletedCopy completedCopy = copy.completionFuture().join();
        return completedCopy.response().copyObjectResult().eTag();
    }
```

**Note**
To perform a cross-Region copy with the S3 Transfer Manager, enable `crossRegionAccessEnabled` on the AWS CRT-based S3 client builder as shown in the following snippet.

```
S3AsyncClient s3AsyncClient = S3AsyncClient.crtBuilder()
                .crossRegionAccessEnabled(true)
                .build();

S3TransferManager transferManager = S3TransferManager.builder()
                .s3Client(s3AsyncClient)
                .build();
```

### Imports
<a name="transfer-manager-copy-import"></a>

```
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import software.amazon.awssdk.core.sync.RequestBody;
import software.amazon.awssdk.services.s3.model.CopyObjectRequest;
import software.amazon.awssdk.transfer.s3.S3TransferManager;
import software.amazon.awssdk.transfer.s3.model.CompletedCopy;
import software.amazon.awssdk.transfer.s3.model.Copy;
import software.amazon.awssdk.transfer.s3.model.CopyRequest;

import java.util.UUID;
```

## Upload a local directory to an S3 bucket
<a name="transfer-manager-upload_directory"></a>

The following example demonstrates how you can upload a local directory to S3.

Start by calling the [uploadDirectory](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/transfer/s3/S3TransferManager.html#uploadDirectory(software.amazon.awssdk.transfer.s3.model.UploadDirectoryRequest)) method of the `S3TransferManager` instance, passing in an [UploadDirectoryRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/transfer/s3/model/UploadDirectoryRequest.html).

The [DirectoryUpload](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/transfer/s3/model/DirectoryUpload.html) object represents the upload process, which generates a [CompletedDirectoryUpload](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/transfer/s3/model/CompletedDirectoryUpload.html) when the request completes. The `CompleteDirectoryUpload` object contains information about the results of the transfer, including which files failed to transfer.

```
    public Integer uploadDirectory(S3TransferManager transferManager,
            URI sourceDirectory, String bucketName) {
        DirectoryUpload directoryUpload = transferManager.uploadDirectory(UploadDirectoryRequest.builder()
                .source(Paths.get(sourceDirectory))
                .bucket(bucketName)
                .build());

        CompletedDirectoryUpload completedDirectoryUpload = directoryUpload.completionFuture().join();
        completedDirectoryUpload.failedTransfers()
                .forEach(fail -> logger.warn("Object [{}] failed to transfer", fail.toString()));
        return completedDirectoryUpload.failedTransfers().size();
    }
```

### Imports
<a name="transfer-manager-upload_directory-import"></a>

```
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import software.amazon.awssdk.services.s3.model.ObjectIdentifier;
import software.amazon.awssdk.transfer.s3.S3TransferManager;
import software.amazon.awssdk.transfer.s3.model.CompletedDirectoryUpload;
import software.amazon.awssdk.transfer.s3.model.DirectoryUpload;
import software.amazon.awssdk.transfer.s3.model.UploadDirectoryRequest;

import java.net.URI;
import java.net.URISyntaxException;
import java.net.URL;
import java.nio.file.Paths;
```

## Download S3 bucket objects to a local directory
<a name="transfer-manager-download_directory"></a>

You can download the objects in an S3 bucket to a local directory as shown in the following example.

To download the objects in an S3 bucket to a local directory, begin by calling the [downloadDirectory](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/transfer/s3/S3TransferManager.html#downloadDirectory(software.amazon.awssdk.transfer.s3.model.DownloadDirectoryRequest)) method of the Transfer Manager, passing in a [DownloadDirectoryRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/transfer/s3/model/DownloadDirectoryRequest.html).

The [DirectoryDownload](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/transfer/s3/model/DirectoryDownload.html) object represents the download process, which generates a [CompletedDirectoryDownload](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/transfer/s3/model/CompletedDirectoryDownload.html) when the request completes. The `CompleteDirectoryDownload` object contains information about the results of the transfer, including which files failed to transfer.

```
    public Integer downloadObjectsToDirectory(S3TransferManager transferManager,
            URI destinationPathURI, String bucketName) {
        DirectoryDownload directoryDownload = transferManager.downloadDirectory(DownloadDirectoryRequest.builder()
                .destination(Paths.get(destinationPathURI))
                .bucket(bucketName)
                .build());
        CompletedDirectoryDownload completedDirectoryDownload = directoryDownload.completionFuture().join();

        completedDirectoryDownload.failedTransfers()
                .forEach(fail -> logger.warn("Object [{}] failed to transfer", fail.toString()));
        return completedDirectoryDownload.failedTransfers().size();
    }
```

### Imports
<a name="transfer-manager-download_directory-import"></a>

```
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import software.amazon.awssdk.core.sync.RequestBody;
import software.amazon.awssdk.services.s3.model.ObjectIdentifier;
import software.amazon.awssdk.transfer.s3.S3TransferManager;
import software.amazon.awssdk.transfer.s3.model.CompletedDirectoryDownload;
import software.amazon.awssdk.transfer.s3.model.DirectoryDownload;
import software.amazon.awssdk.transfer.s3.model.DownloadDirectoryRequest;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.HashSet;
import java.util.Set;
import java.util.UUID;
import java.util.stream.Collectors;
```

## Download using a pre-signed URL
<a name="transfer-manager-presigned-url-download"></a>

Use the S3 Transfer Manager to download objects with a pre-signed URL. Track download progress with `TransferListener`. This feature is available in SDK version {{2.48.0}} and later.

**CRT client limitation**
Pre-signed URL downloads require the standard Java-based `S3AsyncClient`. The AWS CRT-based S3 client (`S3AsyncClient.crtBuilder()`) does not currently support this feature.

### Add the dependency
<a name="transfer-manager-presigned-dependency"></a>

Add the `s3-transfer-manager` artifact to your project if you haven't already:

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

#### Imports
<a name="transfer-manager-presigned-imports"></a>

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

### Download with progress tracking
<a name="transfer-manager-presigned-download-examples"></a>

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

## See complete examples
<a name="transfer-manager-example-location"></a>

[GitHub contains the complete](https://github.com/awsdocs/aws-doc-sdk-examples/tree/d73001daea05266eaa9e074ccb71b9383832369a/javav2/example_code/s3/src/main/java/com/example/s3/transfermanager) code for all examples on this page.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
