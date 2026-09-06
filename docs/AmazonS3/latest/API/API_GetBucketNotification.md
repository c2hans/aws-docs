---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketNotification.html
---

# GetBucketNotification
<a name="API_GetBucketNotification"></a>

**Note**
This operation is not supported for directory buckets.

 No longer used, see [GetBucketNotificationConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketNotificationConfiguration.html).

## Request Syntax
<a name="API_GetBucketNotification_RequestSyntax"></a>

```
GET /?notification HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}
```

## URI Request Parameters
<a name="API_GetBucketNotification_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Bucket](#API_GetBucketNotification_RequestSyntax) **   <a name="AmazonS3-GetBucketNotification-request-header-Bucket"></a>
The name of the bucket for which to get the notification configuration.
When you use this API operation with an access point, provide the alias of the access point in place of the bucket name.
When you use this API operation with an Object Lambda access point, provide the alias of the Object Lambda access point in place of the bucket name. If the Object Lambda access point alias in a request is not valid, the error code `InvalidAccessPointAliasError` is returned. For more information about `InvalidAccessPointAliasError`, see [List of Error Codes](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#ErrorCodeList).
Required: Yes

 ** [x-amz-expected-bucket-owner](#API_GetBucketNotification_RequestSyntax) **   <a name="AmazonS3-GetBucketNotification-request-header-ExpectedBucketOwner"></a>
The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Request Body
<a name="API_GetBucketNotification_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetBucketNotification_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<NotificationConfiguration>
   <TopicConfiguration>
      <Event>string</Event>
      <Event>string</Event>
      ...
      <Id>string</Id>
      <Topic>string</Topic>
   </TopicConfiguration>
   <QueueConfiguration>
      <Event>string</Event>
      <Event>string</Event>
      ...
      <Id>string</Id>
      <Queue>string</Queue>
   </QueueConfiguration>
   <CloudFunctionConfiguration>
      <CloudFunction>string</CloudFunction>
      <Event>string</Event>
      <Event>string</Event>
      ...
      <Id>string</Id>
      <InvocationRole>string</InvocationRole>
   </CloudFunctionConfiguration>
</NotificationConfiguration>
```

## Response Elements
<a name="API_GetBucketNotification_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [NotificationConfiguration](#API_GetBucketNotification_ResponseSyntax) **   <a name="AmazonS3-GetBucketNotification-response-NotificationConfigurationDeprecated"></a>
Root level tag for the NotificationConfiguration parameters.
Required: Yes

 ** [CloudFunctionConfiguration](#API_GetBucketNotification_ResponseSyntax) **   <a name="AmazonS3-GetBucketNotification-response-CloudFunctionConfiguration"></a>
Container for specifying the AWS Lambda notification configuration.
Type: [CloudFunctionConfiguration](API_CloudFunctionConfiguration.md) data type

 ** [QueueConfiguration](#API_GetBucketNotification_ResponseSyntax) **   <a name="AmazonS3-GetBucketNotification-response-QueueConfiguration"></a>
This data type is deprecated. This data type specifies the configuration for publishing messages to an Amazon Simple Queue Service (Amazon SQS) queue when Amazon S3 detects specified events.
Type: [QueueConfigurationDeprecated](API_QueueConfigurationDeprecated.md) data type

 ** [TopicConfiguration](#API_GetBucketNotification_ResponseSyntax) **   <a name="AmazonS3-GetBucketNotification-response-TopicConfiguration"></a>
This data type is deprecated. A container for specifying the configuration for publication of messages to an Amazon Simple Notification Service (Amazon SNS) topic when Amazon S3 detects specified events.
Type: [TopicConfigurationDeprecated](API_TopicConfigurationDeprecated.md) data type

## See Also
<a name="API_GetBucketNotification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketNotification)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/GetBucketNotification)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketNotification)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketNotification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketNotification)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketNotification)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketNotification)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketNotification)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketNotification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketNotification)
