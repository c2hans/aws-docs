---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketNotification.html
---

# PutBucketNotification
<a name="API_PutBucketNotification"></a>

**Note**
This operation is not supported for directory buckets.

 No longer used, see the [PutBucketNotificationConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketNotificationConfiguration.html) operation.

## Request Syntax
<a name="API_PutBucketNotification_RequestSyntax"></a>

```
PUT /?notification HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
Content-MD5: {{ContentMD5}}
x-amz-sdk-checksum-algorithm: {{ChecksumAlgorithm}}
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}
<?xml version="1.0" encoding="UTF-8"?>
<NotificationConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <TopicConfiguration>
      <Event>{{string}}</Event>
      <Event>{{string}}</Event>
      ...
      <Id>{{string}}</Id>
      <Topic>{{string}}</Topic>
   </TopicConfiguration>
   <QueueConfiguration>
      <Event>{{string}}</Event>
      <Event>{{string}}</Event>
      ...
      <Id>{{string}}</Id>
      <Queue>{{string}}</Queue>
   </QueueConfiguration>
   <CloudFunctionConfiguration>
      <CloudFunction>{{string}}</CloudFunction>
      <Event>{{string}}</Event>
      <Event>{{string}}</Event>
      ...
      <Id>{{string}}</Id>
      <InvocationRole>{{string}}</InvocationRole>
   </CloudFunctionConfiguration>
</NotificationConfiguration>
```

## URI Request Parameters
<a name="API_PutBucketNotification_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Bucket](#API_PutBucketNotification_RequestSyntax) **   <a name="AmazonS3-PutBucketNotification-request-header-Bucket"></a>
The name of the bucket.
Required: Yes

 ** [Content-MD5](#API_PutBucketNotification_RequestSyntax) **   <a name="AmazonS3-PutBucketNotification-request-header-ContentMD5"></a>
The MD5 hash of the `PutPublicAccessBlock` request body.
For requests made using the AWS Command Line Interface (CLI) or AWS SDKs, this field is calculated automatically.

 ** [x-amz-expected-bucket-owner](#API_PutBucketNotification_RequestSyntax) **   <a name="AmazonS3-PutBucketNotification-request-header-ExpectedBucketOwner"></a>
The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

 ** [x-amz-sdk-checksum-algorithm](#API_PutBucketNotification_RequestSyntax) **   <a name="AmazonS3-PutBucketNotification-request-header-ChecksumAlgorithm"></a>
Indicates the algorithm used to create the checksum for the request when you use the SDK. This header will not provide any additional functionality if you don't use the SDK. When you send this header, there must be a corresponding `x-amz-checksum` or `x-amz-trailer` header sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request`. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.
If you provide an individual checksum, Amazon S3 ignores any provided `ChecksumAlgorithm` parameter.
Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME | SHA512 | MD5 | XXHASH64 | XXHASH3 | XXHASH128`

## Request Body
<a name="API_PutBucketNotification_RequestBody"></a>

The request accepts the following data in XML format.

 ** [NotificationConfiguration](#API_PutBucketNotification_RequestSyntax) **   <a name="AmazonS3-PutBucketNotification-request-NotificationConfiguration"></a>
Root level tag for the NotificationConfiguration parameters.
Required: Yes

 ** [CloudFunctionConfiguration](#API_PutBucketNotification_RequestSyntax) **   <a name="AmazonS3-PutBucketNotification-request-CloudFunctionConfiguration"></a>
Container for specifying the AWS Lambda notification configuration.
Type: [CloudFunctionConfiguration](API_CloudFunctionConfiguration.md) data type
Required: No

 ** [QueueConfiguration](#API_PutBucketNotification_RequestSyntax) **   <a name="AmazonS3-PutBucketNotification-request-QueueConfiguration"></a>
This data type is deprecated. This data type specifies the configuration for publishing messages to an Amazon Simple Queue Service (Amazon SQS) queue when Amazon S3 detects specified events.
Type: [QueueConfigurationDeprecated](API_QueueConfigurationDeprecated.md) data type
Required: No

 ** [TopicConfiguration](#API_PutBucketNotification_RequestSyntax) **   <a name="AmazonS3-PutBucketNotification-request-TopicConfiguration"></a>
This data type is deprecated. A container for specifying the configuration for publication of messages to an Amazon Simple Notification Service (Amazon SNS) topic when Amazon S3 detects specified events.
Type: [TopicConfigurationDeprecated](API_TopicConfigurationDeprecated.md) data type
Required: No

## Response Syntax
<a name="API_PutBucketNotification_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutBucketNotification_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## See Also
<a name="API_PutBucketNotification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketNotification)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/PutBucketNotification)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketNotification)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketNotification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketNotification)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketNotification)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketNotification)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketNotification)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketNotification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketNotification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
