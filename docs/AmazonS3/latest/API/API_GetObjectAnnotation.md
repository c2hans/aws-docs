---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAnnotation.html
---

# GetObjectAnnotation
<a name="API_GetObjectAnnotation"></a>

Retrieves an annotation from an Amazon S3 object. To use this operation, you must have the `s3:GetObjectAnnotation` permission.

If checksum mode is enabled via the `x-amz-checksum-mode` header, Amazon S3 returns the stored checksum in the response headers for client-side validation.

**Note**
Annotations are not supported by the following features: S3 Inventory Reports, API Gateway, S3 Storage Lens, Amazon S3 File Gateway, Amazon FSx, S3 on Outposts, and S3 Express One Zone (directory buckets).

The following operations are related to `GetObjectAnnotation`:
+  [PutObjectAnnotation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAnnotation.html)
+  [ListObjectAnnotations](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectAnnotations.html)
+  [DeleteObjectAnnotation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectAnnotation.html)

## Request Syntax
<a name="API_GetObjectAnnotation_RequestSyntax"></a>

```
GET /{Key+}?annotation&annotationName={{AnnotationName}}&versionId={{VersionId}} HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
x-amz-request-payer: {{RequestPayer}}
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}
x-amz-checksum-mode: {{ChecksumMode}}
```

## URI Request Parameters
<a name="API_GetObjectAnnotation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [annotationName](#API_GetObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-GetObjectAnnotation-request-uri-querystring-AnnotationName"></a>
The name of the annotation to retrieve.
Length Constraints: Minimum length of 1. Maximum length of 512 bytes.
Required: Yes

 ** [Bucket](#API_GetObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-GetObjectAnnotation-request-header-Bucket"></a>
The name of the bucket that contains the object.
Required: Yes

 ** [Key](#API_GetObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-GetObjectAnnotation-request-uri-uri-Key"></a>
The object key.
Length Constraints: Minimum length of 1.
Required: Yes

 ** [versionId](#API_GetObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-GetObjectAnnotation-request-uri-querystring-VersionId"></a>
The version ID of the object.

 ** [x-amz-checksum-mode](#API_GetObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-GetObjectAnnotation-request-header-ChecksumMode"></a>
Set to `ENABLED` to validate the checksum of the annotation payload on retrieval.
Valid Values: `ENABLED`

 ** [x-amz-expected-bucket-owner](#API_GetObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-GetObjectAnnotation-request-header-ExpectedBucketOwner"></a>
The account ID of the expected bucket owner. If the bucket is owned by a different account, the request fails with an HTTP 403 (Access Denied) error.

 ** [x-amz-request-payer](#API_GetObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-GetObjectAnnotation-request-header-RequestPayer"></a>
Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. If either the source or destination S3 bucket has Requester Pays enabled, the requester will pay for the corresponding charges. For information about downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the *Amazon S3 User Guide*.
This functionality is not supported for directory buckets.
Valid Values: `requester`

## Request Body
<a name="API_GetObjectAnnotation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetObjectAnnotation_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amz-object-version-id: {{ObjectVersionId}}
Last-Modified: {{LastModified}}
Content-Length: {{ContentLength}}
ETag: {{ETag}}
x-amz-checksum-crc32: {{ChecksumCRC32}}
x-amz-checksum-crc32c: {{ChecksumCRC32C}}
x-amz-checksum-crc64nvme: {{ChecksumCRC64NVME}}
x-amz-checksum-sha1: {{ChecksumSHA1}}
x-amz-checksum-sha256: {{ChecksumSHA256}}
x-amz-checksum-sha512: {{ChecksumSHA512}}
x-amz-checksum-md5: {{ChecksumMD5}}
x-amz-checksum-xxhash64: {{ChecksumXXHASH64}}
x-amz-checksum-xxhash3: {{ChecksumXXHASH3}}
x-amz-checksum-xxhash128: {{ChecksumXXHASH128}}
x-amz-checksum-type: {{ChecksumType}}
x-amz-server-side-encryption: {{ServerSideEncryption}}
x-amz-request-charged: {{RequestCharged}}
x-amz-replication-status: {{ReplicationStatus}}

{{AnnotationPayload}}
```

## Response Elements
<a name="API_GetObjectAnnotation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [Content-Length](#API_GetObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-GetObjectAnnotation-response-header-ContentLength"></a>
The size of the annotation payload, in bytes.

 ** [ETag](#API_GetObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-GetObjectAnnotation-response-header-ETag"></a>
The entity tag of the annotation.

 ** [Last-Modified](#API_GetObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-GetObjectAnnotation-response-header-LastModified"></a>
The date and time the annotation was last modified.

 ** [x-amz-checksum-crc32](#API_GetObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-GetObjectAnnotation-response-header-ChecksumCRC32"></a>
The CRC32 checksum of the annotation payload.

 ** [x-amz-checksum-crc32c](#API_GetObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-GetObjectAnnotation-response-header-ChecksumCRC32C"></a>
The CRC32C checksum of the annotation payload.

 ** [x-amz-checksum-crc64nvme](#API_GetObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-GetObjectAnnotation-response-header-ChecksumCRC64NVME"></a>
The CRC64NVME checksum of the annotation payload.

 ** [x-amz-checksum-md5](#API_GetObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-GetObjectAnnotation-response-header-ChecksumMD5"></a>
The MD5 checksum of the annotation payload.

 ** [x-amz-checksum-sha1](#API_GetObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-GetObjectAnnotation-response-header-ChecksumSHA1"></a>
The SHA1 checksum of the annotation payload.

 ** [x-amz-checksum-sha256](#API_GetObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-GetObjectAnnotation-response-header-ChecksumSHA256"></a>
The SHA256 checksum of the annotation payload.

 ** [x-amz-checksum-sha512](#API_GetObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-GetObjectAnnotation-response-header-ChecksumSHA512"></a>
The SHA512 checksum of the annotation payload.

 ** [x-amz-checksum-type](#API_GetObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-GetObjectAnnotation-response-header-ChecksumType"></a>
The type of checksum used.
Valid Values: `COMPOSITE | FULL_OBJECT`

 ** [x-amz-checksum-xxhash128](#API_GetObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-GetObjectAnnotation-response-header-ChecksumXXHASH128"></a>
The XXHASH128 checksum of the annotation payload.

 ** [x-amz-checksum-xxhash3](#API_GetObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-GetObjectAnnotation-response-header-ChecksumXXHASH3"></a>
The XXHASH3 checksum of the annotation payload.

 ** [x-amz-checksum-xxhash64](#API_GetObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-GetObjectAnnotation-response-header-ChecksumXXHASH64"></a>
The XXHASH64 checksum of the annotation payload.

 ** [x-amz-object-version-id](#API_GetObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-GetObjectAnnotation-response-header-ObjectVersionId"></a>
The version ID of the object that the annotation is attached to.

 ** [x-amz-replication-status](#API_GetObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-GetObjectAnnotation-response-header-ReplicationStatus"></a>
The replication status of the annotation. Possible values include `PENDING`, `COMPLETED`, `FAILED`, and `REPLICA`.
Valid Values: `COMPLETE | PENDING | FAILED | REPLICA | COMPLETED`

 ** [x-amz-request-charged](#API_GetObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-GetObjectAnnotation-response-header-RequestCharged"></a>
If present, indicates that the requester was successfully charged for the request. For more information, see [Using Requester Pays buckets for storage transfers and usage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) in the *Amazon Simple Storage Service user guide*.
This functionality is not supported for directory buckets.
Valid Values: `requester`

 ** [x-amz-server-side-encryption](#API_GetObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-GetObjectAnnotation-response-header-ServerSideEncryption"></a>
The server-side encryption algorithm used.
Valid Values: `AES256 | aws:fsx | aws:kms | aws:kms:dsse`

The following data is returned in binary format by the service.

 ** [AnnotationPayload](#API_GetObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-GetObjectAnnotation-response-AnnotationPayload"></a>

## Errors
<a name="API_GetObjectAnnotation_Errors"></a>

 ** NoSuchAnnotation **
The specified annotation does not exist on this object.
HTTP Status Code: 404

 ** NoSuchBucket **
The specified bucket does not exist.
HTTP Status Code: 404

 ** NoSuchKey **
The specified key does not exist.
HTTP Status Code: 404

## See Also
<a name="API_GetObjectAnnotation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetObjectAnnotation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/GetObjectAnnotation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetObjectAnnotation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetObjectAnnotation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetObjectAnnotation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetObjectAnnotation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetObjectAnnotation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetObjectAnnotation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetObjectAnnotation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetObjectAnnotation)
