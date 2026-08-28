---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_UpdateStreamStorageConfiguration.html
---

# UpdateStreamStorageConfiguration
<a name="API_UpdateStreamStorageConfiguration"></a>

Updates the storage configuration for an existing Kinesis video stream.

This operation allows you to modify the storage tier settings for a stream, enabling you to optimize storage costs and performance based on your access patterns.

 `UpdateStreamStorageConfiguration` is an asynchronous operation.

You must have permissions for the `KinesisVideo:UpdateStreamStorageConfiguration` action.

## Request Syntax
<a name="API_UpdateStreamStorageConfiguration_RequestSyntax"></a>

```
POST /updateStreamStorageConfiguration HTTP/1.1
Content-type: application/json

{
   "CurrentVersion": "{{string}}",
   "StreamARN": "{{string}}",
   "StreamName": "{{string}}",
   "StreamStorageConfiguration": {
      "DefaultStorageTier": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateStreamStorageConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateStreamStorageConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CurrentVersion](#API_UpdateStreamStorageConfiguration_RequestSyntax) **   <a name="KinesisVideo-UpdateStreamStorageConfiguration-request-CurrentVersion"></a>
The version of the stream whose storage configuration you want to change. To get the version, call either the `DescribeStream` or the `ListStreams` API.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]+`
Required: Yes

 ** [StreamARN](#API_UpdateStreamStorageConfiguration_RequestSyntax) **   <a name="KinesisVideo-UpdateStreamStorageConfiguration-request-StreamARN"></a>
The Amazon Resource Name (ARN) of the stream for which you want to update the storage configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`
Required: No

 ** [StreamName](#API_UpdateStreamStorageConfiguration_RequestSyntax) **   <a name="KinesisVideo-UpdateStreamStorageConfiguration-request-StreamName"></a>
The name of the stream for which you want to update the storage configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** [StreamStorageConfiguration](#API_UpdateStreamStorageConfiguration_RequestSyntax) **   <a name="KinesisVideo-UpdateStreamStorageConfiguration-request-StreamStorageConfiguration"></a>
The new storage configuration for the stream. This includes the default storage tier that determines how stream data is stored and accessed.
Different storage tiers offer varying levels of performance and cost optimization to match your specific use case requirements.
Type: [StreamStorageConfiguration](API_StreamStorageConfiguration.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateStreamStorageConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateStreamStorageConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateStreamStorageConfiguration_Errors"></a>

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

 ** ResourceInUseException **
When the input `StreamARN` or `ChannelARN` in `CLOUD_STORAGE_MODE` is already mapped to a different Kinesis Video Stream resource, or if the provided input `StreamARN` or `ChannelARN` is not in Active status, try one of the following :

1. The `DescribeMediaStorageConfiguration` API to determine what the stream given channel is mapped to.

1. The `DescribeMappedResourceConfiguration` API to determine the channel that the given stream is mapped to.

1. The `DescribeStream` or `DescribeSignalingChannel` API to determine the status of the resource.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Amazon Kinesis Video Streams can't find the stream that you specified.
HTTP Status Code: 404

 ** VersionMismatchException **
The stream version that you specified is not the latest version. To get the latest version, use the [DescribeStream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeStream.html) API.
HTTP Status Code: 400

## See Also
<a name="API_UpdateStreamStorageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisvideo-2017-09-30/UpdateStreamStorageConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisvideo-2017-09-30/UpdateStreamStorageConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisvideo-2017-09-30/UpdateStreamStorageConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisvideo-2017-09-30/UpdateStreamStorageConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisvideo-2017-09-30/UpdateStreamStorageConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/UpdateStreamStorageConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisvideo-2017-09-30/UpdateStreamStorageConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisvideo-2017-09-30/UpdateStreamStorageConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesisvideo-2017-09-30/UpdateStreamStorageConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisvideo-2017-09-30/UpdateStreamStorageConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Video Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisvideostreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
