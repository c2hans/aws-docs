---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectRetention.html
---

# PutObjectRetention
<a name="API_PutObjectRetention"></a>

**Note**
This operation is not supported for directory buckets.

Places an Object Retention configuration on an object. For more information, see [Locking Objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html). Users or accounts require the `s3:PutObjectRetention` permission in order to place an Object Retention configuration on objects. Bypassing a Governance Retention configuration requires the `s3:BypassGovernanceRetention` permission.

This functionality is not supported for Amazon S3 on Outposts.

**Important**
You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax
<a name="API_PutObjectRetention_RequestSyntax"></a>

```
PUT /{Key+}?retention&versionId={{VersionId}} HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
x-amz-request-payer: {{RequestPayer}}
x-amz-bypass-governance-retention: {{BypassGovernanceRetention}}
Content-MD5: {{ContentMD5}}
x-amz-sdk-checksum-algorithm: {{ChecksumAlgorithm}}
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}
<?xml version="1.0" encoding="UTF-8"?>
<Retention xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <Mode>{{string}}</Mode>
   <RetainUntilDate>{{timestamp}}</RetainUntilDate>
   <EventHold>{{string}}</EventHold>
   <EventHoldDuration>
      <Days>{{integer}}</Days>
      <Years>{{integer}}</Years>
   </EventHoldDuration>
</Retention>
```

## URI Request Parameters
<a name="API_PutObjectRetention_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Bucket](#API_PutObjectRetention_RequestSyntax) **   <a name="AmazonS3-PutObjectRetention-request-header-Bucket"></a>
The bucket name that contains the object you want to apply this Object Retention configuration to.
 **Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html) in the *Amazon S3 User Guide*.
Required: Yes

 ** [Content-MD5](#API_PutObjectRetention_RequestSyntax) **   <a name="AmazonS3-PutObjectRetention-request-header-ContentMD5"></a>
The MD5 hash for the request body.
For requests made using the AWS Command Line Interface (CLI) or AWS SDKs, this field is calculated automatically.

 ** [Key](#API_PutObjectRetention_RequestSyntax) **   <a name="AmazonS3-PutObjectRetention-request-uri-uri-Key"></a>
The key name for the object that you want to apply this Object Retention configuration to.
Length Constraints: Minimum length of 1.
Required: Yes

 ** [versionId](#API_PutObjectRetention_RequestSyntax) **   <a name="AmazonS3-PutObjectRetention-request-uri-querystring-VersionId"></a>
The version ID for the object that you want to apply this Object Retention configuration to.

 ** [x-amz-bypass-governance-retention](#API_PutObjectRetention_RequestSyntax) **   <a name="AmazonS3-PutObjectRetention-request-header-BypassGovernanceRetention"></a>
Indicates whether this action should bypass Governance-mode restrictions.

 ** [x-amz-expected-bucket-owner](#API_PutObjectRetention_RequestSyntax) **   <a name="AmazonS3-PutObjectRetention-request-header-ExpectedBucketOwner"></a>
The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

 ** [x-amz-request-payer](#API_PutObjectRetention_RequestSyntax) **   <a name="AmazonS3-PutObjectRetention-request-header-RequestPayer"></a>
Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. If either the source or destination S3 bucket has Requester Pays enabled, the requester will pay for the corresponding charges. For information about downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the *Amazon S3 User Guide*.
This functionality is not supported for directory buckets.
Valid Values: `requester`

 ** [x-amz-sdk-checksum-algorithm](#API_PutObjectRetention_RequestSyntax) **   <a name="AmazonS3-PutObjectRetention-request-header-ChecksumAlgorithm"></a>
Indicates the algorithm used to create the checksum for the object when you use the SDK. This header will not provide any additional functionality if you don't use the SDK. When you send this header, there must be a corresponding `x-amz-checksum` or `x-amz-trailer` header sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request`. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.
If you provide an individual checksum, Amazon S3 ignores any provided `ChecksumAlgorithm` parameter.
Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME | SHA512 | MD5 | XXHASH64 | XXHASH3 | XXHASH128`

## Request Body
<a name="API_PutObjectRetention_RequestBody"></a>

The request accepts the following data in XML format.

 ** [Retention](#API_PutObjectRetention_RequestSyntax) **   <a name="AmazonS3-PutObjectRetention-request-Retention"></a>
Root level tag for the Retention parameters.
Required: Yes

 ** [EventHold](#API_PutObjectRetention_RequestSyntax) **   <a name="AmazonS3-PutObjectRetention-request-EventHold"></a>
The event hold status for the object. Set to `ON` to enable an event hold or `OFF` to disable it.
Type: String
Valid Values: `ON | OFF`
Required: No

 ** [EventHoldDuration](#API_PutObjectRetention_RequestSyntax) **   <a name="AmazonS3-PutObjectRetention-request-EventHoldDuration"></a>
The event hold duration for the object. Specifies how long the object remains protected after the event hold is released.
Type: [EventHoldDuration](API_EventHoldDuration.md) data type
Required: No

 ** [Mode](#API_PutObjectRetention_RequestSyntax) **   <a name="AmazonS3-PutObjectRetention-request-Mode"></a>
Indicates the Retention mode for the specified object.
Type: String
Valid Values: `GOVERNANCE | COMPLIANCE`
Required: No

 ** [RetainUntilDate](#API_PutObjectRetention_RequestSyntax) **   <a name="AmazonS3-PutObjectRetention-request-RetainUntilDate"></a>
The date on which this Object Lock Retention will expire.
Type: Timestamp
Required: No

## Response Syntax
<a name="API_PutObjectRetention_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amz-request-charged: {{RequestCharged}}
```

## Response Elements
<a name="API_PutObjectRetention_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [x-amz-request-charged](#API_PutObjectRetention_ResponseSyntax) **   <a name="AmazonS3-PutObjectRetention-response-header-RequestCharged"></a>
If present, indicates that the requester was successfully charged for the request. For more information, see [Using Requester Pays buckets for storage transfers and usage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) in the *Amazon Simple Storage Service user guide*.
This functionality is not supported for directory buckets.
Valid Values: `requester`

## See Also
<a name="API_PutObjectRetention_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutObjectRetention)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/PutObjectRetention)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutObjectRetention)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutObjectRetention)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutObjectRetention)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutObjectRetention)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutObjectRetention)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutObjectRetention)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutObjectRetention)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutObjectRetention)
