---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectAnnotation.html
---

# DeleteObjectAnnotation
<a name="API_DeleteObjectAnnotation"></a>

Deletes a specific annotation from an Amazon S3 object. Use the `x-amz-object-if-match` header to perform a conditional delete that only succeeds if the object's ETag matches the provided value, preventing race conditions during concurrent updates.

Deleting an annotation is permanent. Annotations are not independently versioned, so there is no delete marker or way to recover a deleted annotation.

To use this operation, you must have the `s3:DeleteObjectAnnotation` permission. If the object is protected by Object Lock in governance mode, you must also include the `x-amz-bypass-governance-retention` header.

**Note**
Annotations are not supported by the following features: S3 Inventory Reports, API Gateway, S3 Storage Lens, Amazon S3 File Gateway, Amazon FSx, S3 on Outposts, and S3 Express One Zone (directory buckets).

The following operations are related to `DeleteObjectAnnotation`:
+  [PutObjectAnnotation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAnnotation.html)
+  [GetObjectAnnotation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAnnotation.html)
+  [ListObjectAnnotations](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectAnnotations.html)

## Request Syntax
<a name="API_DeleteObjectAnnotation_RequestSyntax"></a>

```
DELETE /{Key+}?annotation&annotationName={{AnnotationName}}&versionId={{VersionId}} HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
x-amz-request-payer: {{RequestPayer}}
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}
x-amz-object-if-match: {{ObjectIfMatch}}
```

## URI Request Parameters
<a name="API_DeleteObjectAnnotation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [annotationName](#API_DeleteObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-DeleteObjectAnnotation-request-uri-querystring-AnnotationName"></a>
The name of the annotation to delete. Annotation names are UTF-8 encoded and cannot start with `aws` or `s3` (case-insensitive).
Length Constraints: Minimum length of 1. Maximum length of 512 bytes.
Required: Yes

 ** [Bucket](#API_DeleteObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-DeleteObjectAnnotation-request-header-Bucket"></a>
The name of the bucket that contains the object.
Required: Yes

 ** [Key](#API_DeleteObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-DeleteObjectAnnotation-request-uri-uri-Key"></a>
The object key.
Length Constraints: Minimum length of 1.
Required: Yes

 ** [versionId](#API_DeleteObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-DeleteObjectAnnotation-request-uri-querystring-VersionId"></a>
The version ID of the object.

 ** [x-amz-expected-bucket-owner](#API_DeleteObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-DeleteObjectAnnotation-request-header-ExpectedBucketOwner"></a>
The account ID of the expected bucket owner.

 ** [x-amz-object-if-match](#API_DeleteObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-DeleteObjectAnnotation-request-header-ObjectIfMatch"></a>
If specified, the operation only succeeds if the object's ETag matches the provided value.

 ** [x-amz-request-payer](#API_DeleteObjectAnnotation_RequestSyntax) **   <a name="AmazonS3-DeleteObjectAnnotation-request-header-RequestPayer"></a>
Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. If either the source or destination S3 bucket has Requester Pays enabled, the requester will pay for the corresponding charges. For information about downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the *Amazon S3 User Guide*.
This functionality is not supported for directory buckets.
Valid Values: `requester`

## Request Body
<a name="API_DeleteObjectAnnotation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteObjectAnnotation_ResponseSyntax"></a>

```
HTTP/1.1 204
x-amz-object-version-id: {{ObjectVersionId}}
x-amz-request-charged: {{RequestCharged}}
```

## Response Elements
<a name="API_DeleteObjectAnnotation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response.

The response returns the following HTTP headers.

 ** [x-amz-object-version-id](#API_DeleteObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-DeleteObjectAnnotation-response-header-ObjectVersionId"></a>
The version ID of the object that the annotation was deleted from.

 ** [x-amz-request-charged](#API_DeleteObjectAnnotation_ResponseSyntax) **   <a name="AmazonS3-DeleteObjectAnnotation-response-header-RequestCharged"></a>
If present, indicates that the requester was successfully charged for the request. For more information, see [Using Requester Pays buckets for storage transfers and usage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) in the *Amazon Simple Storage Service user guide*.
This functionality is not supported for directory buckets.
Valid Values: `requester`

## Errors
<a name="API_DeleteObjectAnnotation_Errors"></a>

 ** NoSuchBucket **
The specified bucket does not exist.
HTTP Status Code: 404

 ** NoSuchKey **
The specified key does not exist.
HTTP Status Code: 404

## See Also
<a name="API_DeleteObjectAnnotation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/DeleteObjectAnnotation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/DeleteObjectAnnotation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/DeleteObjectAnnotation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/DeleteObjectAnnotation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/DeleteObjectAnnotation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/DeleteObjectAnnotation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/DeleteObjectAnnotation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/DeleteObjectAnnotation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/DeleteObjectAnnotation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/DeleteObjectAnnotation)
