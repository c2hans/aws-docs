---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketNotificationConfiguration.html
---

# GetBucketNotificationConfiguration
<a name="API_GetBucketNotificationConfiguration"></a>

**Note**
This operation is not supported for directory buckets.

Returns the notification configuration of a bucket.

If notifications are not enabled on the bucket, the action returns an empty `NotificationConfiguration` element.

By default, you must be the bucket owner to read the notification configuration of a bucket. However, the bucket owner can use a bucket policy to grant permission to other users to read this configuration with the `s3:GetBucketNotification` permission.

When you use this API operation with an access point, provide the alias of the access point in place of the bucket name.

When you use this API operation with an Object Lambda access point, provide the alias of the Object Lambda access point in place of the bucket name. If the Object Lambda access point alias in a request is not valid, the error code `InvalidAccessPointAliasError` is returned. For more information about `InvalidAccessPointAliasError`, see [List of Error Codes](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#ErrorCodeList).

For more information about setting and reading the notification configuration on a bucket, see [Setting Up Notification of Bucket Events](https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html). For more information about bucket policies, see [Using Bucket Policies](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html).

The following action is related to `GetBucketNotification`:
+  [PutBucketNotification](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketNotification.html)

**Important**
You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax
<a name="API_GetBucketNotificationConfiguration_RequestSyntax"></a>

```
GET /?notification HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}
```

## URI Request Parameters
<a name="API_GetBucketNotificationConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Bucket](#API_GetBucketNotificationConfiguration_RequestSyntax) **   <a name="AmazonS3-GetBucketNotificationConfiguration-request-header-Bucket"></a>
The name of the bucket for which to get the notification configuration.
When you use this API operation with an access point, provide the alias of the access point in place of the bucket name.
When you use this API operation with an Object Lambda access point, provide the alias of the Object Lambda access point in place of the bucket name. If the Object Lambda access point alias in a request is not valid, the error code `InvalidAccessPointAliasError` is returned. For more information about `InvalidAccessPointAliasError`, see [List of Error Codes](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#ErrorCodeList).
Required: Yes

 ** [x-amz-expected-bucket-owner](#API_GetBucketNotificationConfiguration_RequestSyntax) **   <a name="AmazonS3-GetBucketNotificationConfiguration-request-header-ExpectedBucketOwner"></a>
The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Request Body
<a name="API_GetBucketNotificationConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetBucketNotificationConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<NotificationConfiguration>
   <TopicConfiguration>
      <Event>string</Event>
      ...
      <Filter>
         <S3Key>
            <FilterRule>
               <Name>string</Name>
               <Value>string</Value>
            </FilterRule>
            ...
         </S3Key>
      </Filter>
      <Id>string</Id>
      <Topic>string</Topic>
   </TopicConfiguration>
   ...
   <QueueConfiguration>
      <Event>string</Event>
      ...
      <Filter>
         <S3Key>
            <FilterRule>
               <Name>string</Name>
               <Value>string</Value>
            </FilterRule>
            ...
         </S3Key>
      </Filter>
      <Id>string</Id>
      <Queue>string</Queue>
   </QueueConfiguration>
   ...
   <CloudFunctionConfiguration>
      <Event>string</Event>
      ...
      <Filter>
         <S3Key>
            <FilterRule>
               <Name>string</Name>
               <Value>string</Value>
            </FilterRule>
            ...
         </S3Key>
      </Filter>
      <Id>string</Id>
      <CloudFunction>string</CloudFunction>
   </CloudFunctionConfiguration>
   ...
   <EventBridgeConfiguration>
   </EventBridgeConfiguration>
</NotificationConfiguration>
```

## Response Elements
<a name="API_GetBucketNotificationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [NotificationConfiguration](#API_GetBucketNotificationConfiguration_ResponseSyntax) **   <a name="AmazonS3-GetBucketNotificationConfiguration-response-NotificationConfiguration"></a>
Root level tag for the NotificationConfiguration parameters.
Required: Yes

 ** [CloudFunctionConfiguration](#API_GetBucketNotificationConfiguration_ResponseSyntax) **   <a name="AmazonS3-GetBucketNotificationConfiguration-response-LambdaFunctionConfigurations"></a>
Describes the AWS Lambda functions to invoke and the events for which to invoke them.
Type: Array of [LambdaFunctionConfiguration](API_LambdaFunctionConfiguration.md) data types

 ** [EventBridgeConfiguration](#API_GetBucketNotificationConfiguration_ResponseSyntax) **   <a name="AmazonS3-GetBucketNotificationConfiguration-response-EventBridgeConfiguration"></a>
Enables delivery of events to Amazon EventBridge.
Type: [EventBridgeConfiguration](API_EventBridgeConfiguration.md) data type

 ** [QueueConfiguration](#API_GetBucketNotificationConfiguration_ResponseSyntax) **   <a name="AmazonS3-GetBucketNotificationConfiguration-response-QueueConfigurations"></a>
The Amazon Simple Queue Service queues to publish messages to and the events for which to publish messages.
Type: Array of [QueueConfiguration](API_QueueConfiguration.md) data types

 ** [TopicConfiguration](#API_GetBucketNotificationConfiguration_ResponseSyntax) **   <a name="AmazonS3-GetBucketNotificationConfiguration-response-TopicConfigurations"></a>
The topic to which notifications are sent and the events for which notifications are generated.
Type: Array of [TopicConfiguration](API_TopicConfiguration.md) data types

## Examples
<a name="API_GetBucketNotificationConfiguration_Examples"></a>

### Sample Request
<a name="API_GetBucketNotificationConfiguration_Example_1"></a>

This request returns the notification configuration on the bucket `amzn-s3-demo-bucket.s3.<Region>.amazonaws.com`.

```
            GET ?notification HTTP/1.1
            Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
            Date: Wed, 15 Oct 2014 16:59:03 GMT
            Authorization: authorization string
```

### Sample Response
<a name="API_GetBucketNotificationConfiguration_Example_2"></a>

This response returns that the notification configuration for the specified bucket.

```
            HTTP/1.1 200 OK
            x-amz-id-2: YgIPIfBiKa2bj0KMgUAdQkf3ShJTOOpXUueF6QKo
            x-amz-request-id: 236A8905248E5A02
            Date: Wed, 15 Oct 2014 16:59:04 GMT
            Server: AmazonS3
            <?xml version="1.0" encoding="UTF-8"?>

            <NotificationConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
             <TopicConfiguration>
               <Id>YjVkM2Y0YmUtNGI3NC00ZjQyLWEwNGItNDIyYWUxY2I0N2M4</Id>
              <Topic>arn:aws:sns:us-east-1:account-id:s3notificationtopic2</Topic>
              <Event>s3:ReducedRedundancyLostObject</Event>
              <Event>s3:ObjectCreated:*</Event>
             </TopicConfiguration>
            </NotificationConfiguration>
```

## See Also
<a name="API_GetBucketNotificationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketNotificationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/GetBucketNotificationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketNotificationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketNotificationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketNotificationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketNotificationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketNotificationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketNotificationConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketNotificationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketNotificationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
