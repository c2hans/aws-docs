---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_DescribeStreamStorageConfiguration.html
---

# DescribeStreamStorageConfiguration
<a name="API_DescribeStreamStorageConfiguration"></a>

Retrieves the current storage configuration for the specified Kinesis video stream.

In the request, you must specify either the `StreamName` or the `StreamARN`.

You must have permissions for the `KinesisVideo:DescribeStreamStorageConfiguration` action.

## Request Syntax
<a name="API_DescribeStreamStorageConfiguration_RequestSyntax"></a>

```
POST /describeStreamStorageConfiguration HTTP/1.1
Content-type: application/json

{
   "StreamARN": "{{string}}",
   "StreamName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeStreamStorageConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeStreamStorageConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [StreamARN](#API_DescribeStreamStorageConfiguration_RequestSyntax) **   <a name="KinesisVideo-DescribeStreamStorageConfiguration-request-StreamARN"></a>
The Amazon Resource Name (ARN) of the stream for which you want to retrieve the storage configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`
Required: No

 ** [StreamName](#API_DescribeStreamStorageConfiguration_RequestSyntax) **   <a name="KinesisVideo-DescribeStreamStorageConfiguration-request-StreamName"></a>
The name of the stream for which you want to retrieve the storage configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## Response Syntax
<a name="API_DescribeStreamStorageConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "StreamARN": "string",
   "StreamName": "string",
   "StreamStorageConfiguration": {
      "DefaultStorageTier": "string"
   }
}
```

## Response Elements
<a name="API_DescribeStreamStorageConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [StreamARN](#API_DescribeStreamStorageConfiguration_ResponseSyntax) **   <a name="KinesisVideo-DescribeStreamStorageConfiguration-response-StreamARN"></a>
The Amazon Resource Name (ARN) of the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

 ** [StreamName](#API_DescribeStreamStorageConfiguration_ResponseSyntax) **   <a name="KinesisVideo-DescribeStreamStorageConfiguration-response-StreamName"></a>
The name of the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [StreamStorageConfiguration](#API_DescribeStreamStorageConfiguration_ResponseSyntax) **   <a name="KinesisVideo-DescribeStreamStorageConfiguration-response-StreamStorageConfiguration"></a>
The current storage configuration for the stream, including the default storage tier and other storage-related settings.
Type: [StreamStorageConfiguration](API_StreamStorageConfiguration.md) object

## Errors
<a name="API_DescribeStreamStorageConfiguration_Errors"></a>

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
<a name="API_DescribeStreamStorageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisvideo-2017-09-30/DescribeStreamStorageConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisvideo-2017-09-30/DescribeStreamStorageConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisvideo-2017-09-30/DescribeStreamStorageConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisvideo-2017-09-30/DescribeStreamStorageConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisvideo-2017-09-30/DescribeStreamStorageConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/DescribeStreamStorageConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisvideo-2017-09-30/DescribeStreamStorageConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisvideo-2017-09-30/DescribeStreamStorageConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesisvideo-2017-09-30/DescribeStreamStorageConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisvideo-2017-09-30/DescribeStreamStorageConfiguration)
