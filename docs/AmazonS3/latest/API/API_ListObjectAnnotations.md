---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectAnnotations.html
---

# ListObjectAnnotations
<a name="API_ListObjectAnnotations"></a>

Lists the annotations attached to an Amazon S3 object. Results are paginated, with a maximum of 1,000 annotations per object. Use the `AnnotationPrefix` parameter to filter the results by name prefix.

To use this operation, you must have the `s3:ListObjectAnnotations` permission.

**Note**
Annotations are not supported by the following features: S3 Inventory Reports, API Gateway, S3 Storage Lens, Amazon S3 File Gateway, Amazon FSx, S3 on Outposts, and S3 Express One Zone (directory buckets).

The following operations are related to `ListObjectAnnotations`:
+  [PutObjectAnnotation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAnnotation.html)
+  [GetObjectAnnotation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAnnotation.html)
+  [DeleteObjectAnnotation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectAnnotation.html)

## Request Syntax
<a name="API_ListObjectAnnotations_RequestSyntax"></a>

```
GET /{Key+}?annotation&annotation-prefix={{AnnotationPrefix}}&continuation-token={{ContinuationToken}}&max-annotation-results={{MaxAnnotationResults}}&versionId={{VersionId}} HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
x-amz-request-payer: {{RequestPayer}}
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}
```

## URI Request Parameters
<a name="API_ListObjectAnnotations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [annotation-prefix](#API_ListObjectAnnotations_RequestSyntax) **   <a name="AmazonS3-ListObjectAnnotations-request-uri-querystring-AnnotationPrefix"></a>
Filter results to annotations whose name begins with the specified prefix.

 ** [Bucket](#API_ListObjectAnnotations_RequestSyntax) **   <a name="AmazonS3-ListObjectAnnotations-request-header-Bucket"></a>
The name of the bucket that contains the object.
Required: Yes

 ** [continuation-token](#API_ListObjectAnnotations_RequestSyntax) **   <a name="AmazonS3-ListObjectAnnotations-request-uri-querystring-ContinuationToken"></a>
Continuation token returned by a previous request to retrieve the next page.

 ** [Key](#API_ListObjectAnnotations_RequestSyntax) **   <a name="AmazonS3-ListObjectAnnotations-request-uri-uri-Key"></a>
The object key.
Length Constraints: Minimum length of 1.
Required: Yes

 ** [max-annotation-results](#API_ListObjectAnnotations_RequestSyntax) **   <a name="AmazonS3-ListObjectAnnotations-request-uri-querystring-MaxAnnotationResults"></a>
The maximum number of annotations to return in the response. Maximum is 1,000.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [versionId](#API_ListObjectAnnotations_RequestSyntax) **   <a name="AmazonS3-ListObjectAnnotations-request-uri-querystring-VersionId"></a>
The version ID of the object.

 ** [x-amz-expected-bucket-owner](#API_ListObjectAnnotations_RequestSyntax) **   <a name="AmazonS3-ListObjectAnnotations-request-header-ExpectedBucketOwner"></a>
The account ID of the expected bucket owner.

 ** [x-amz-request-payer](#API_ListObjectAnnotations_RequestSyntax) **   <a name="AmazonS3-ListObjectAnnotations-request-header-RequestPayer"></a>
Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. If either the source or destination S3 bucket has Requester Pays enabled, the requester will pay for the corresponding charges. For information about downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the *Amazon S3 User Guide*.
This functionality is not supported for directory buckets.
Valid Values: `requester`

## Request Body
<a name="API_ListObjectAnnotations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListObjectAnnotations_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amz-object-version-id: {{ObjectVersionId}}
x-amz-request-charged: {{RequestCharged}}
<?xml version="1.0" encoding="UTF-8"?>
<ListObjectAnnotationsOutput>
   <Annotations>
      <AnnotationEntry>
         <AnnotationName>string</AnnotationName>
         <ChecksumAlgorithm>string</ChecksumAlgorithm>
         ...
         <ETag>string</ETag>
         <LastModified>timestamp</LastModified>
         <ReplicationStatus>string</ReplicationStatus>
         <Size>long</Size>
      </AnnotationEntry>
   </Annotations>
   <Bucket>string</Bucket>
   <Key>string</Key>
   <AnnotationPrefix>string</AnnotationPrefix>
   <MaxAnnotationResults>integer</MaxAnnotationResults>
   <AnnotationCount>integer</AnnotationCount>
   <ContinuationToken>string</ContinuationToken>
   <NextContinuationToken>string</NextContinuationToken>
</ListObjectAnnotationsOutput>
```

## Response Elements
<a name="API_ListObjectAnnotations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [x-amz-object-version-id](#API_ListObjectAnnotations_ResponseSyntax) **   <a name="AmazonS3-ListObjectAnnotations-response-header-ObjectVersionId"></a>
The version ID of the object.

 ** [x-amz-request-charged](#API_ListObjectAnnotations_ResponseSyntax) **   <a name="AmazonS3-ListObjectAnnotations-response-header-RequestCharged"></a>
If present, indicates that the requester was successfully charged for the request. For more information, see [Using Requester Pays buckets for storage transfers and usage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) in the *Amazon Simple Storage Service user guide*.
This functionality is not supported for directory buckets.
Valid Values: `requester`

The following data is returned in XML format by the service.

 ** [ListObjectAnnotationsOutput](#API_ListObjectAnnotations_ResponseSyntax) **   <a name="AmazonS3-ListObjectAnnotations-response-ListObjectAnnotationsOutput"></a>
Root level tag for the ListObjectAnnotationsOutput parameters.
Required: Yes

 ** [AnnotationCount](#API_ListObjectAnnotations_ResponseSyntax) **   <a name="AmazonS3-ListObjectAnnotations-response-AnnotationCount"></a>
The number of annotations returned.
Type: Integer

 ** [AnnotationPrefix](#API_ListObjectAnnotations_ResponseSyntax) **   <a name="AmazonS3-ListObjectAnnotations-response-AnnotationPrefix"></a>
The prefix used to filter the response.
Type: String

 ** [Annotations](#API_ListObjectAnnotations_ResponseSyntax) **   <a name="AmazonS3-ListObjectAnnotations-response-Annotations"></a>
The list of annotations attached to the object.
Type: Array of [AnnotationEntry](API_AnnotationEntry.md) data types

 ** [Bucket](#API_ListObjectAnnotations_ResponseSyntax) **   <a name="AmazonS3-ListObjectAnnotations-response-Bucket"></a>
The bucket name.
Type: String

 ** [ContinuationToken](#API_ListObjectAnnotations_ResponseSyntax) **   <a name="AmazonS3-ListObjectAnnotations-response-ContinuationToken"></a>
The continuation token used in this request.
Type: String

 ** [Key](#API_ListObjectAnnotations_ResponseSyntax) **   <a name="AmazonS3-ListObjectAnnotations-response-Key"></a>
The object key.
Type: String
Length Constraints: Minimum length of 1.

 ** [MaxAnnotationResults](#API_ListObjectAnnotations_ResponseSyntax) **   <a name="AmazonS3-ListObjectAnnotations-response-MaxAnnotationResults"></a>
The maximum number of annotations returned in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextContinuationToken](#API_ListObjectAnnotations_ResponseSyntax) **   <a name="AmazonS3-ListObjectAnnotations-response-NextContinuationToken"></a>
The continuation token to use to retrieve the next page of results.
Type: String

## Errors
<a name="API_ListObjectAnnotations_Errors"></a>

 ** InvalidPrefix **
The annotation prefix you provided is invalid.
HTTP Status Code: 400

 ** NoSuchBucket **
The specified bucket does not exist.
HTTP Status Code: 404

 ** NoSuchKey **
The specified key does not exist.
HTTP Status Code: 404

## See Also
<a name="API_ListObjectAnnotations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/ListObjectAnnotations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/ListObjectAnnotations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ListObjectAnnotations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/ListObjectAnnotations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ListObjectAnnotations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/ListObjectAnnotations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/ListObjectAnnotations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/ListObjectAnnotations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/ListObjectAnnotations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ListObjectAnnotations)
