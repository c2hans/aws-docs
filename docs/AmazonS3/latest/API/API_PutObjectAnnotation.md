---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAnnotation.html
---

# PutObjectAnnotation
<a name="API_PutObjectAnnotation"></a>

Attaches an annotation to an Amazon S3 object. An annotation is a named payload of 1 byte to 1 MiB that you can associate with a specific object or object version. Each object can have up to 1,000 annotations.

For annotation naming rules and restrictions, see [Annotation naming guidelines](https://docs.aws.amazon.com/AmazonS3/latest/userguide/annotations-overview.html) in the *Amazon S3 User Guide*.

Annotations inherit the encryption of their parent object. For objects without server-side encryption, annotations are encrypted with SSE-S3 (the default for new objects). Objects encrypted with SSE-C cannot have annotations.

To use this operation, you must have the `s3:PutObjectAnnotation` permission. If the bucket has Requester Pays enabled, you must include the `x-amz-request-payer` header.

**Note**
Annotations are not supported by the following features: S3 Inventory Reports, API Gateway, S3 Storage Lens, Amazon S3 File Gateway, Amazon FSx, S3 on Outposts, and S3 Express One Zone (directory buckets).

The following operations are related to `PutObjectAnnotation`:
+  [GetObjectAnnotation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAnnotation.html)
+  [ListObjectAnnotations](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectAnnotations.html)
+  [DeleteObjectAnnotation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectAnnotation.html)

## Request Syntax
<a name="API_PutObjectAnnotation_RequestSyntax"></a>

```
PUT /{Key+}?annotation&annotationName={{AnnotationName}}&versionId={{VersionId}} HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
x-amz-object-if-match: {{ObjectIfMatch}}
x-amz-sdk-checksum-algorithm: {{ChecksumAlgorithm}}
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
Content-MD5: {{ContentMD5}}
x-amz-request-payer: {{RequestPayer}}
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}

{{AnnotationPayload}}
```

## URI Request Parameters
<a name="API_PutObjectAnnotation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [annotationName](#API_PutObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-PutObjectAnnotation-request-uri-querystring-AnnotationName"></a>
The name of the annotation.
Length Constraints: Minimum length of 1. Maximum length of 512 bytes.
Required: Yes

 ** [Bucket](#API_PutObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-PutObjectAnnotation-request-header-Bucket"></a>
The name of the bucket that contains the object.
Required: Yes

 ** [Content-MD5](#API_PutObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-PutObjectAnnotation-request-header-ContentMD5"></a>
Base64-encoded MD5 digest of the message.

 ** [Key](#API_PutObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-PutObjectAnnotation-request-uri-uri-Key"></a>
The object key.
Length Constraints: Minimum length of 1.
Required: Yes

 ** [versionId](#API_PutObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-PutObjectAnnotation-request-uri-querystring-VersionId"></a>
The version ID of the object to attach the annotation to.

 ** [x-amz-checksum-crc32](#API_PutObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-PutObjectAnnotation-request-header-ChecksumCRC32"></a>
Base64-encoded CRC32 checksum of the annotation payload.

 ** [x-amz-checksum-crc32c](#API_PutObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-PutObjectAnnotation-request-header-ChecksumCRC32C"></a>
Base64-encoded CRC32C checksum of the annotation payload.

 ** [x-amz-checksum-crc64nvme](#API_PutObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-PutObjectAnnotation-request-header-ChecksumCRC64NVME"></a>
Base64-encoded CRC64NVME checksum of the annotation payload.

 ** [x-amz-checksum-md5](#API_PutObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-PutObjectAnnotation-request-header-ChecksumMD5"></a>
Base64-encoded MD5 checksum of the annotation payload.

 ** [x-amz-checksum-sha1](#API_PutObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-PutObjectAnnotation-request-header-ChecksumSHA1"></a>
Base64-encoded SHA1 checksum of the annotation payload.

 ** [x-amz-checksum-sha256](#API_PutObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-PutObjectAnnotation-request-header-ChecksumSHA256"></a>
Base64-encoded SHA256 checksum of the annotation payload.

 ** [x-amz-checksum-sha512](#API_PutObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-PutObjectAnnotation-request-header-ChecksumSHA512"></a>
Base64-encoded SHA512 checksum of the annotation payload.

 ** [x-amz-checksum-xxhash128](#API_PutObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-PutObjectAnnotation-request-header-ChecksumXXHASH128"></a>
Base64-encoded XXHASH128 checksum of the annotation payload.

 ** [x-amz-checksum-xxhash3](#API_PutObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-PutObjectAnnotation-request-header-ChecksumXXHASH3"></a>
Base64-encoded XXHASH3 checksum of the annotation payload.

 ** [x-amz-checksum-xxhash64](#API_PutObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-PutObjectAnnotation-request-header-ChecksumXXHASH64"></a>
Base64-encoded XXHASH64 checksum of the annotation payload.

 ** [x-amz-expected-bucket-owner](#API_PutObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-PutObjectAnnotation-request-header-ExpectedBucketOwner"></a>
The account ID of the expected bucket owner. If the bucket is owned by a different account, the request fails with an HTTP 403 (Access Denied) error.

 ** [x-amz-object-if-match](#API_PutObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-PutObjectAnnotation-request-header-ObjectIfMatch"></a>
If specified, the operation only succeeds if the object's ETag matches the provided value.

 ** [x-amz-request-payer](#API_PutObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-PutObjectAnnotation-request-header-RequestPayer"></a>
Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. If either the source or destination S3 bucket has Requester Pays enabled, the requester will pay for the corresponding charges. For information about downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the *Amazon S3 User Guide*.
This functionality is not supported for directory buckets.
Valid Values: `requester`

 ** [x-amz-sdk-checksum-algorithm](#API_PutObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-PutObjectAnnotation-request-header-ChecksumAlgorithm"></a>
The checksum algorithm to use. Supported values: `CRC32`, `CRC32C`, `CRC64NVME`, `SHA1`, `SHA256`, `SHA512`, `MD5`, `XXHASH64`, `XXHASH3`, `XXHASH128`.
Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME | SHA512 | MD5 | XXHASH64 | XXHASH3 | XXHASH128`

## Request Body
<a name="API_PutObjectAnnotation_RequestBody"></a>

The request accepts the following binary data.

 ** [AnnotationPayload](#API_PutObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-PutObjectAnnotation-request-AnnotationPayload"></a>

## Response Syntax
<a name="API_PutObjectAnnotation_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amz-object-version-id: {{ObjectVersionId}}
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
<?xml version="1.0" encoding="UTF-8"?>
<PutObjectAnnotationOutput>
   <Key>string</Key>
   <AnnotationName>string</AnnotationName>
</PutObjectAnnotationOutput>
```

## Response Elements
<a name="API_PutObjectAnnotation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [ETag](#API_PutObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-PutObjectAnnotation-response-header-ETag"></a>
The entity tag of the annotation.

 ** [x-amz-checksum-crc32](#API_PutObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-PutObjectAnnotation-response-header-ChecksumCRC32"></a>
The CRC32 checksum of the stored annotation.

 ** [x-amz-checksum-crc32c](#API_PutObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-PutObjectAnnotation-response-header-ChecksumCRC32C"></a>
The CRC32C checksum of the stored annotation.

 ** [x-amz-checksum-crc64nvme](#API_PutObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-PutObjectAnnotation-response-header-ChecksumCRC64NVME"></a>
The CRC64NVME checksum of the stored annotation.

 ** [x-amz-checksum-md5](#API_PutObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-PutObjectAnnotation-response-header-ChecksumMD5"></a>
The MD5 checksum of the stored annotation.

 ** [x-amz-checksum-sha1](#API_PutObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-PutObjectAnnotation-response-header-ChecksumSHA1"></a>
The SHA1 checksum of the stored annotation.

 ** [x-amz-checksum-sha256](#API_PutObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-PutObjectAnnotation-response-header-ChecksumSHA256"></a>
The SHA256 checksum of the stored annotation.

 ** [x-amz-checksum-sha512](#API_PutObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-PutObjectAnnotation-response-header-ChecksumSHA512"></a>
The SHA512 checksum of the stored annotation.

 ** [x-amz-checksum-type](#API_PutObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-PutObjectAnnotation-response-header-ChecksumType"></a>
The type of checksum used.
Valid Values: `COMPOSITE | FULL_OBJECT`

 ** [x-amz-checksum-xxhash128](#API_PutObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-PutObjectAnnotation-response-header-ChecksumXXHASH128"></a>
The XXHASH128 checksum of the stored annotation.

 ** [x-amz-checksum-xxhash3](#API_PutObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-PutObjectAnnotation-response-header-ChecksumXXHASH3"></a>
The XXHASH3 checksum of the stored annotation.

 ** [x-amz-checksum-xxhash64](#API_PutObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-PutObjectAnnotation-response-header-ChecksumXXHASH64"></a>
The XXHASH64 checksum of the stored annotation.

 ** [x-amz-object-version-id](#API_PutObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-PutObjectAnnotation-response-header-ObjectVersionId"></a>
The version ID of the object that the annotation was attached to.

 ** [x-amz-request-charged](#API_PutObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-PutObjectAnnotation-response-header-RequestCharged"></a>
If present, indicates that the requester was successfully charged for the request. For more information, see [Using Requester Pays buckets for storage transfers and usage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) in the *Amazon Simple Storage Service user guide*.
This functionality is not supported for directory buckets.
Valid Values: `requester`

 ** [x-amz-server-side-encryption](#API_PutObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-PutObjectAnnotation-response-header-ServerSideEncryption"></a>
The server-side encryption algorithm used to encrypt the annotation.
Valid Values: `AES256 | aws:fsx | aws:kms | aws:kms:dsse`

The following data is returned in XML format by the service.

 ** [PutObjectAnnotationOutput](#API_PutObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-PutObjectAnnotation-response-PutObjectAnnotationOutput"></a>
Root level tag for the PutObjectAnnotationOutput parameters.
Required: Yes

 ** [AnnotationName](#API_PutObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-PutObjectAnnotation-response-AnnotationName"></a>
The name of the annotation.
Type: String

 ** [Key](#API_PutObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-PutObjectAnnotation-response-Key"></a>
The object key.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_PutObjectAnnotation_Errors"></a>

 ** AnnotationLimitExceeded **
The request would exceed the maximum number of annotations allowed per object.
HTTP Status Code: 400

 ** AnnotationNameTooLong **
The annotation name exceeds 512 bytes.
HTTP Status Code: 400

 ** InvalidAnnotationName **
The annotation name you provided is invalid.
HTTP Status Code: 400

 ** InvalidRequest **
A parameter or header in your request isn't valid. For details, see the description of this API operation.
HTTP Status Code: 400

 ** NoSuchBucket **
The specified bucket does not exist.
HTTP Status Code: 404

 ** NoSuchKey **
The specified key does not exist.
HTTP Status Code: 404

 ** UnsupportedMediaType **
The annotation payload is not valid UTF-8 encoded text.
HTTP Status Code: 415

## See Also
<a name="API_PutObjectAnnotation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutObjectAnnotation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/PutObjectAnnotation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutObjectAnnotation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutObjectAnnotation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutObjectAnnotation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutObjectAnnotation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutObjectAnnotation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutObjectAnnotation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutObjectAnnotation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutObjectAnnotation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
