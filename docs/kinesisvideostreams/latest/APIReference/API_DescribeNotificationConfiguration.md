---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_DescribeNotificationConfiguration.html
---

# DescribeNotificationConfiguration
<a name="API_DescribeNotificationConfiguration"></a>

Gets the `NotificationConfiguration` for a given Kinesis video stream.

## Request Syntax
<a name="API_DescribeNotificationConfiguration_RequestSyntax"></a>

```
POST /describeNotificationConfiguration HTTP/1.1
Content-type: application/json

{
   "StreamARN": "{{string}}",
   "StreamName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeNotificationConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeNotificationConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [StreamARN](#API_DescribeNotificationConfiguration_RequestSyntax) **   <a name="KinesisVideo-DescribeNotificationConfiguration-request-StreamARN"></a>
The Amazon Resource Name (ARN) of the Kinesis video stream from where you want to retrieve the notification configuration. You must specify either the `StreamName` or the StreamARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`
Required: No

 ** [StreamName](#API_DescribeNotificationConfiguration_RequestSyntax) **   <a name="KinesisVideo-DescribeNotificationConfiguration-request-StreamName"></a>
The name of the stream from which to retrieve the notification configuration. You must specify either the `StreamName` or the `StreamARN`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## Response Syntax
<a name="API_DescribeNotificationConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NotificationConfiguration": {
      "DestinationConfig": {
         "Uri": "string"
      },
      "Status": "string"
   }
}
```

## Response Elements
<a name="API_DescribeNotificationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NotificationConfiguration](#API_DescribeNotificationConfiguration_ResponseSyntax) **   <a name="KinesisVideo-DescribeNotificationConfiguration-response-NotificationConfiguration"></a>
The structure that contains the information required for notifications. If the structure is null, the configuration will be deleted from the stream.
Type: [NotificationConfiguration](API_NotificationConfiguration.md) object

## Errors
<a name="API_DescribeNotificationConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have required permissions to perform this operation.
HTTP Status Code: 401

 ** ClientLimitExceededException **
Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.
HTTP Status Code: 400

 ** InvalidArgumentException **
The value for this input parameter is invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Amazon Kinesis Video Streams can't find the stream that you specified.
HTTP Status Code: 404

## See Also
<a name="API_DescribeNotificationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisvideo-2017-09-30/DescribeNotificationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisvideo-2017-09-30/DescribeNotificationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisvideo-2017-09-30/DescribeNotificationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisvideo-2017-09-30/DescribeNotificationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisvideo-2017-09-30/DescribeNotificationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/DescribeNotificationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisvideo-2017-09-30/DescribeNotificationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisvideo-2017-09-30/DescribeNotificationConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesisvideo-2017-09-30/DescribeNotificationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisvideo-2017-09-30/DescribeNotificationConfiguration)
