---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/s3-checksums.html
---

# Data integrity protection with checksums
<a name="s3-checksums"></a>

Amazon Simple Storage Service (Amazon S3) provides the ability to specify a checksum when you upload an object. When you specify a checksum, it is stored with the object and can be validated when the object is downloaded.

Checksums provide an additional layer of data integrity when you transfer files. With checksums, you can verify data consistency by confirming that the received file matches the original file. For more information about checksums with Amazon S3, see the [Amazon Simple Storage Service User Guide](/AmazonS3/latest/userguide/checking-object-integrity.html) including the [supported algorithms](/AmazonS3/latest/userguide/checking-object-integrity.html#using-additional-checksums).

You have the flexibility to choose the algorithm that best fits your needs and let the SDK calculate the checksum. Alternatively, you can provide a pre-computed checksum value by using one of the supported algorithms.

**Note**
Beginning with version 1.4.0 of the AWS SDK for Kotlin, the SDK provides default integrity protections by automatically calculating a `CRC32` checksum for uploads. The SDK calculates this checksum if you don’t provide a precalculated checksum value or if you don’t specify an algorithm that the SDK should use to calculate a checksum.
The SDK also provides global settings for data integrity protections that you can set externally, which you can read about in the [AWS SDKs and Tools Reference Guide](/sdkref/latest/guide/feature-dataintegrity.html).

We discuss checksums in two request phases: uploading an object and downloading an object.

## Upload an object
<a name="use-service-S3-checksum-upload"></a>

You upload objects to Amazon S3 with the SDK for Kotlin by using the [putObject](/sdk-for-kotlin/api/latest/s3/aws.sdk.kotlin.services.s3/put-object.html) function with a request parameter. The request data type provides the `checksumAlgorithm` property to enable checksum computation.

The following code snippet shows a request to upload an object with a `CRC32` checksum. When the SDK sends the request, it calculates the `CRC32` checksum and uploads the object. Amazon S3 stores the checksum with the object.

```
val request = PutObjectRequest {
    bucket = "amzn-s3-demo-bucket"
    key = "key"
    checksumAlgorithm = ChecksumAlgorithm.CRC32
}
```

If you don’t provide a checksum algorithm with the request, the checksum behavior varies depending on the version of the SDK that you use as shown in the following table.

 **Checksum behavior when no checksum algorithm is provided**

| Kotlin SDK version | Checksum behavior |
| --- | --- |
| earlier than 1.4.0 | The SDK doesn’t automatically calculate a CRC-based checksum and provide it in the request. |
| 1.4.0 or later | The SDK uses the `CRC32` algorithm to calculate the checksum and provides it in the request. Amazon S3 validates the integrity of the transfer by computing its own `CRC32` checksum and compares it to the checksum provided by the SDK. If the checksums match, the checksum is saved with the object. |

### Use a pre-calculated checksum value
<a name="use-service-S3-checksum-upload-pre"></a>

A pre-calculated checksum value provided with the request disables automatic computation by the SDK and uses the provided value instead.

The following example shows a request with a pre-calculated SHA256 checksum.

```
val request = PutObjectRequest {
    bucket = "amzn-s3-demo-bucket"
    key = "key"
    body = ByteStream.fromFile(File("file_to_upload.txt"))
    checksumAlgorithm = ChecksumAlgorithm.SHA256
    checksumSha256 = "cfb6d06da6e6f51c22ae3e549e33959dbb754db75a93665b8b579605464ce299"
}
```

If Amazon S3 determines the checksum value is incorrect for the specified algorithm, the service returns an error response.

### Multipart uploads
<a name="use-service-S3-checksum-upload-multi"></a>

You can also use checksums with multipart uploads.

You must specify the checksum algorithm in the [`CreateMultipartUpload`](/sdk-for-kotlin/api/latest/s3/aws.sdk.kotlin.services.s3/-s3-client/create-multipart-upload.html) request and in each [`UploadPart`](/sdk-for-kotlin/api/latest/s3/aws.sdk.kotlin.services.s3/-s3-client/upload-part.html) request. As a final step, you must specify the checksum of each part in the [`CompleteMultipartUpload`](/sdk-for-kotlin/api/latest/s3/aws.sdk.kotlin.services.s3/-s3-client/complete-multipart-upload.html). The following example shows how to create a multipart upload with the checksum algorithm specified.

```
val multipartUpload = s3.createMultipartUpload {
    bucket = "amzn-s3-demo-bucket"
    key = "key"
    checksumAlgorithm = ChecksumAlgorithm.Sha1
}

val partFilesToUpload = listOf("data-part1.csv", "data-part2.csv", "data-part3.csv")

val completedParts = partFilesToUpload
    .mapIndexed { i, fileName ->
        val uploadPartResponse = s3.uploadPart {
            bucket = "amzn-s3-demo-bucket"
            key = "key"
            body = ByteStream.fromFile(File(fileName))
            uploadId = multipartUpload.uploadId
            partNumber = i + 1 // Part numbers begin at 1.
            checksumAlgorithm = ChecksumAlgorithm.Sha1
        }

        CompletedPart {
            eTag = uploadPartResponse.eTag
            partNumber = i + 1
            checksumSha1 = uploadPartResponse.checksumSha1
        }
    }

s3.completeMultipartUpload {
    uploadId = multipartUpload.uploadId
    bucket = "amzn-s3-demo-bucket"
    key = "key"
    multipartUpload {
        parts = completedParts
    }
}
```

## Download an object
<a name="use-service-S3-checksum-download"></a>

When you use the [getObject](/sdk-for-kotlin/api/latest/s3/aws.sdk.kotlin.services.s3/-s3-client/get-object.html) method to download an object, the SDK automatically validates the checksum when the `checksumMode` property of the builder for the [`GetObjectRequest`](/sdk-for-kotlin/api/latest/s3/aws.sdk.kotlin.services.s3.model/-get-object-request/index.html) is set to `ChecksumMode.Enabled`.

The request in the following snippet directs the SDK to validate the checksum in the response by calculating the checksum and comparing the values.

```
val request = GetObjectRequest {
    bucket = "amzn-s3-demo-bucket"
    key = "key"
    checksumMode = ChecksumMode.Enabled
}
```

**Note**
If the object wasn’t uploaded with a checksum, no validation takes place.

If you use an SDK version of 1.4.0 or later, the SDK automatically checks the integrity of [`getObject`](/sdk-for-kotlin/api/latest/s3/aws.sdk.kotlin.services.s3/-s3-client/get-object.html) requests without adding `checksumMode = ChecksumMode.Enabled` to the request.

### Asynchronous validation
<a name="service-s3-checksum-getObject-kotlin-asyncValidation"></a>

Because the SDK for Kotlin uses streaming responses when it downloads an object from Amazon S3, the checksum will be calculated as you consume the object. Therefore, you *must* consume the object so that the checksum is validated.

The following example shows how to validate a checksum by fully consuming the response.

```
val request = GetObjectRequest {
    bucket = "amzn-s3-demo-bucket"
    key = "key"
    checksumMode = checksumMode.Enabled
}

val response = s3Client.getObject(request) {
    println(response.body?.decodeToString()) // Fully consume the object.
    // The checksum is valid.
}
```

By contrast, the code in the following example doesn’t use the object in any way, so the checksum is not validated.

```
s3Client.getObject(request) {
    println("Got the object.")
}
```

If the checksum calculated by the SDK does not match the expected checksum sent with the response, the SDK throws a [`ChecksumMismatchException`](/smithy-kotlin/api/latest/http-client/aws.smithy.kotlin.runtime.http.interceptors/-checksum-mismatch-exception/index.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Kotlin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-kotlin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
