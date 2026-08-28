---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/s3-checksums.html
---

# Data integrity protection with checksums
<a name="s3-checksums"></a>

Amazon Simple Storage Service (Amazon S3) provides the ability to specify a checksum when you upload an object. When you specify a checksum, it is stored with the object and can be validated when the object is downloaded.

Checksums provide an additional layer of data integrity when you transfer files. With checksums, you can verify data consistency by confirming that the received file matches the original file. For more information about checksums with Amazon S3, see the [Amazon Simple Storage Service User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) including the [supported algorithms](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#using-additional-checksums).

You have the flexibility to choose the algorithm that best fits your needs and let the SDK calculate the checksum. Alternatively, you can provide a pre-computed checksum value by using one of the supported algorithms.

**Note**
Beginning with version 2.30.0 of the AWS SDK for Java 2.x, the SDK provides default integrity protections by automatically calculating a `CRC32` checksum for uploads. The SDK calculates this checksum if you don't provide a precalculated checksum value or if you don't specify an algorithm that the SDK should use to calculate a checksum.
The SDK also provides global settings for data integrity protections that you can set externally, which you can read about in the [AWS SDKs and Tools Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/feature-dataintegrity.html).

We discuss checksums in two request phases: uploading an object and downloading an object.

## Upload an object
<a name="use-service-S3-checksum-upload"></a>

When you upload an object with the `putObject` method and provide a checksum algorithm, the SDK computes the checksum for the specified algorithm.

The following code snippet shows a request to upload an object with a `SHA256` checksum. When the SDK sends the request, it calculates the `SHA256` checksum and uploads the object. Amazon S3 validates the integrity of the content by calculating the checksum and comparing it to the checksum provided by the SDK. Amazon S3 then stores the checksum with the object.

```
public void putObjectWithChecksum() {
        s3Client.putObject(b -> b
                .bucket(bucketName)
                .key(key)
                .checksumAlgorithm(ChecksumAlgorithm.SHA256),
            RequestBody.fromString("This is a test"));
}
```

If you don't provide a checksum algorithm with the request, the checksum behavior varies depending on the version of the SDK that you use as shown in the following table.

**Checksum behavior when no checksum algorithm is provided**

| Java SDK version | Checksum behavior |
| --- | --- |
| earlier than 2.30.0 | The SDK doesn't automatically calculate a CRC-based checksum and provide it in the request. |
| 2.30.0 or later | The SDK uses the `CRC32` algorithm to calculate the checksum and provides it in the request. Amazon S3 validates the integrity of the transfer by computing its own `CRC32` checksum and compares it to the checksum provided by the SDK. If the checksums match, the checksum is saved with the object. |

### Use a pre-calculated checksum value
<a name="use-service-S3-checksum-upload-pre"></a>

A pre-calculated checksum value provided with the request disables automatic computation by the SDK and uses the provided value instead.

The following example shows a request with a pre-calculated SHA256 checksum.

```
    public void putObjectWithPrecalculatedChecksum(String bucketName, String key, String filePath) {
        String checksum = calculateChecksum(filePath, "SHA-256");

        s3Client.putObject((b -> b
                .bucket(bucketName)
                .key(key)
                .checksumSHA256(checksum)),
            RequestBody.fromFile(Paths.get(filePath)));
    }
```

If Amazon S3 determines the checksum value is incorrect for the specified algorithm, the service returns an error response.

### Multipart uploads
<a name="use-service-S3-checksum-upload-multi"></a>

You can also use checksums with multipart uploads.

 The SDK for Java 2.x provides two options to use checksums with multipart uploads. The first option uses the `S3TransferManager`.

The following transfer manager example specifies the SHA1 algorithm for the upload.

```
    public void multipartUploadWithChecksumTm(String bucketName, String key, String filePath) {
        S3TransferManager transferManager = S3TransferManager.create();
        UploadFileRequest uploadFileRequest = UploadFileRequest.builder()
            .putObjectRequest(b -> b
                .bucket(bucketName)
                .key(key)
                .checksumAlgorithm(ChecksumAlgorithm.SHA1))
            .source(Paths.get(filePath))
            .build();
        FileUpload fileUpload = transferManager.uploadFile(uploadFileRequest);
        fileUpload.completionFuture().join();
        transferManager.close();
    }
```

If you don't provide a checksum algorithm when using the transfer manager for uploads, the SDK automatically calculates and checksum based on the `CRC32` algorithm. The SDK performs this calculation for all versions of the SDK.

The second option uses the [`S3Client` API](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3Client.html) (or the [`S3AsyncClient` API](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3AsyncClient.html)) to perform the multipart upload. If you specify a checksum with this approach, you must specify the algorithm to use on the initiation of the upload. You must also specify the algorithm for each part request and provide the checksum calculated for each part after it is uploaded.

```
    public void multipartUploadWithChecksumS3Client(String bucketName, String key, String filePath) {
        ChecksumAlgorithm algorithm = ChecksumAlgorithm.CRC32;

        // Initiate the multipart upload.
        CreateMultipartUploadResponse createMultipartUploadResponse = s3Client.createMultipartUpload(b -> b
            .bucket(bucketName)
            .key(key)
            .checksumAlgorithm(algorithm)); // Checksum specified on initiation.
        String uploadId = createMultipartUploadResponse.uploadId();

        // Upload the parts of the file.
        int partNumber = 1;
        List<CompletedPart> completedParts = new ArrayList<>();
        ByteBuffer bb = ByteBuffer.allocate(1024 * 1024 * 5); // 5 MB byte buffer

        try (RandomAccessFile file = new RandomAccessFile(filePath, "r")) {
            long fileSize = file.length();
            long position = 0;
            while (position < fileSize) {
                file.seek(position);
                long read = file.getChannel().read(bb);

                bb.flip(); // Swap position and limit before reading from the buffer.
                UploadPartRequest uploadPartRequest = UploadPartRequest.builder()
                    .bucket(bucketName)
                    .key(key)
                    .uploadId(uploadId)
                    .checksumAlgorithm(algorithm) // Checksum specified on each part.
                    .partNumber(partNumber)
                    .build();

                UploadPartResponse partResponse = s3Client.uploadPart(
                    uploadPartRequest,
                    RequestBody.fromByteBuffer(bb));

                CompletedPart part = CompletedPart.builder()
                    .partNumber(partNumber)
                    .checksumCRC32(partResponse.checksumCRC32()) // Provide the calculated checksum.
                    .eTag(partResponse.eTag())
                    .build();
                completedParts.add(part);

                bb.clear();
                position += read;
                partNumber++;
            }
        } catch (IOException e) {
            System.err.println(e.getMessage());
        }

        // Complete the multipart upload.
        s3Client.completeMultipartUpload(b -> b
            .bucket(bucketName)
            .key(key)
            .uploadId(uploadId)
            .multipartUpload(CompletedMultipartUpload.builder().parts(completedParts).build()));
    }
```

[Code for the complete examples](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javav2/example_code/s3/src/main/java/com/example/s3/PerformMultiPartUpload.java) and [tests](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javav2/example_code/s3/src/test/java/com/example/s3/PerformMultiPartUploadTests.java) are in the GitHub code examples repository.

## Download an object
<a name="use-service-S3-checksum-download"></a>

When you use the [getObject](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3Client.html#getObject(software.amazon.awssdk.services.s3.model.GetObjectRequest)) method to download an object, the SDK automatically validates the checksum  when the `checksumMode` method of the builder for the `GetObjectRequest` is set to `ChecksumMode.ENABLED`.

The request in the following snippet directs the SDK to validate the checksum in the response by calculating the checksum and comparing the values.

```
    public GetObjectResponse getObjectWithChecksum() {
        return s3Client.getObject(b -> b
                        .bucket(bucketName)
                        .key(key)
                        .checksumMode(ChecksumMode.ENABLED))
                .response();
    }
```

**Note**
If the object wasn't uploaded with a checksum, no validation takes place.

## Other checksum calculation options
<a name="S3-checsum-calculation-options"></a>

**Note**
To verify the data integrity of transmitted data and to identify any transmission errors, we encourage users to keep the SDK default settings for the checksum calculation options. By default, the SDK adds this important check for many S3 operations including `PutObject` and `GetObject`.

If your use of Amazon S3 requires minimal checksum validation, however, you can disable many checks by changing the default configuration settings.

### Disable automatic checksum calculation unless it's required
<a name="S3-minimize-checksum-calc-global"></a>

You can disable automatic checksum calculation by the SDK for operations that support it, for example `PutObject` and `GetObject`. Some S3 operations, however, require a checksum calculation; you cannot disable checksum calculation for these operations.

The SDK provides separate settings for the calculation of a checksum for the payload of a request and for the payload of a response.

The following list describes the settings you can use to minimize checksum calculations at the different scopes.
+ **All applications scope**—By changing the settings in environment variables or in a profile in the shared AWS `config` and `credentials` files, all applications can use these settings. These settings affect all service clients in all AWS SDK applications unless overridden at the application or service client scope.
  + Add the settings in a profile:

    ```
    [default]
    request_checksum_calculation = WHEN_REQUIRED
    response_checksum_validation = WHEN_REQUIRED
    ```
  + Add environment variables:

    ```
    AWS_REQUEST_CHECKSUM_CALCULATION=WHEN_REQUIRED
    AWS_RESPONSE_CHECKSUM_VALIDATION=WHEN_REQUIRED
    ```
+ **Current application scope**—You can set the Java system property `aws.requestChecksumCalculation` to `WHEN_REQUIRED` to limit checksum calculation. The corresponding system property for responses is `aws.responseChecksumValidation`.

  These settings affect all SDK service clients in the application unless overridden during service client creation.

  Set the system property at the start of your application:

  ```
  import software.amazon.awssdk.core.SdkSystemSetting;
  import software.amazon.awssdk.core.checksums.RequestChecksumCalculation;
  import software.amazon.awssdk.core.checksums.ResponseChecksumValidation;
  import software.amazon.awssdk.services.s3.S3Client;

  class DemoClass {
      public static void main(String[] args) {

          System.setProperty(SdkSystemSetting.AWS_REQUEST_CHECKSUM_CALCULATION.property(), // Resolves to "aws.requestChecksumCalculation".
                  "WHEN_REQUIRED");
          System.setProperty(SdkSystemSetting.AWS_RESPONSE_CHECKSUM_VALIDATION.property(), // Resolves to "aws.responseChecksumValidation".
                  "WHEN_REQUIRED");

          S3Client s3Client = S3Client.builder().build();

          // Use s3Client.
      }
  }
  ```
+ **Single S3 service client scope**—You can configure a single S3 service client to calculate the minimum amount of checksums using builder methods:

  ```
  import software.amazon.awssdk.core.checksums.RequestChecksumCalculation;
  import software.amazon.awssdk.services.s3.S3Client;

  public class RequiredChecksums {
      public static void main(String[] args) {
          S3Client s3 = S3Client.builder()
                  .requestChecksumCalculation(RequestChecksumCalculation.WHEN_REQUIRED)
                  .responseChecksumValidation(ResponseChecksumValidation.WHEN_REQUIRED)
                  .build();

          // Use s3Client.
      }
  // ...
  }
  ```

### Use the `LegacyMd5Plugin` for simplified MD5 compatibility
<a name="S3-checksum-legacy-md5"></a>

Along with the release of CRC32 checksum behavior with version 2.30.0, the SDK stopped calculating MD5 checksums on required operations.

If you need legacy MD5 checksum behavior for S3 operations, you can use the `LegacyMd5Plugin`, which was released with version 2.31.32 of the SDK.

The `LegacyMd5Plugin` is particularly useful when you need to maintain compatibility with applications that depend on the legacy MD5 checksum behavior, especially when working with third-party S3-compatible storage providers like those used with S3A filesystem connectors (Apache Spark, Iceberg).

To use the `LegacyMd5Plugin`, add it to your S3 client builder:

```
// For synchronous S3 client.
S3Client s3Client = S3Client.builder()
                           .addPlugin(LegacyMd5Plugin.create())
                           .build();

// For asynchronous S3 client.
S3AsyncClient asyncClient = S3AsyncClient.builder()
                                       .addPlugin(LegacyMd5Plugin.create())
                                       .build();
```

If you want to add MD5 checksums to the operations that require checksums and want to skip adding SDK default checksums for operations that support checksums but are not required, you can enable the `ClientBuilder` options `requestChecksumCalculation` and `responseChecksumValidation` as `WHEN_REQUIRED`. This will add SDK default checksums only to operations that require checksums:

```
// Use the `LegacyMd5Plugin` with `requestChecksumCalculation` and `responseChecksumValidation` set to WHEN_REQUIRED.
S3AsyncClient asyncClient = S3AsyncClient.builder()
                                       .addPlugin(LegacyMd5Plugin.create())
                                       .requestChecksumCalculation(RequestChecksumCalculation.WHEN_REQUIRED)
                                       .responseChecksumValidation(ResponseChecksumValidation.WHEN_REQUIRED)
                                       .build();
```

This configuration is particularly useful when working with third-party S3-compatible storage systems that may not fully support the newer checksum algorithms but still require MD5 checksums for certain operations.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
