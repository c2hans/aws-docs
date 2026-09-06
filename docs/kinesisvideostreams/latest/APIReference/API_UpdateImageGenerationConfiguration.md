---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_UpdateImageGenerationConfiguration.html
---

# UpdateImageGenerationConfiguration
<a name="API_UpdateImageGenerationConfiguration"></a>

Updates the `StreamInfo` and `ImageProcessingConfiguration` fields.

## Request Syntax
<a name="API_UpdateImageGenerationConfiguration_RequestSyntax"></a>

```
POST /updateImageGenerationConfiguration HTTP/1.1
Content-type: application/json

{
   "ImageGenerationConfiguration": {
      "DestinationConfig": {
         "DestinationRegion": "{{string}}",
         "Uri": "{{string}}"
      },
      "Format": "{{string}}",
      "FormatConfig": {
         "{{string}}" : "{{string}}"
      },
      "HeightPixels": {{number}},
      "ImageSelectorType": "{{string}}",
      "SamplingInterval": {{number}},
      "Status": "{{string}}",
      "WidthPixels": {{number}}
   },
   "StreamARN": "{{string}}",
   "StreamName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateImageGenerationConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateImageGenerationConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ImageGenerationConfiguration](#API_UpdateImageGenerationConfiguration_RequestSyntax) **   <a name="KinesisVideo-UpdateImageGenerationConfiguration-request-ImageGenerationConfiguration"></a>
The structure that contains the information required for the KVS images delivery. If the structure is null, the configuration will be deleted from the stream.
Type: [ImageGenerationConfiguration](API_ImageGenerationConfiguration.md) object
Required: No

 ** [StreamARN](#API_UpdateImageGenerationConfiguration_RequestSyntax) **   <a name="KinesisVideo-UpdateImageGenerationConfiguration-request-StreamARN"></a>
The Amazon Resource Name (ARN) of the Kinesis video stream from where you want to update the image generation configuration. You must specify either the `StreamName` or the `StreamARN`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`
Required: No

 ** [StreamName](#API_UpdateImageGenerationConfiguration_RequestSyntax) **   <a name="KinesisVideo-UpdateImageGenerationConfiguration-request-StreamName"></a>
The name of the stream from which to update the image generation configuration. You must specify either the `StreamName` or the `StreamARN`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## Response Syntax
<a name="API_UpdateImageGenerationConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateImageGenerationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateImageGenerationConfiguration_Errors"></a>

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

 ** NoDataRetentionException **
The Stream data retention in hours is equal to zero.
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

## See Also
<a name="API_UpdateImageGenerationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisvideo-2017-09-30/UpdateImageGenerationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisvideo-2017-09-30/UpdateImageGenerationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisvideo-2017-09-30/UpdateImageGenerationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisvideo-2017-09-30/UpdateImageGenerationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisvideo-2017-09-30/UpdateImageGenerationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/UpdateImageGenerationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisvideo-2017-09-30/UpdateImageGenerationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisvideo-2017-09-30/UpdateImageGenerationConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesisvideo-2017-09-30/UpdateImageGenerationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisvideo-2017-09-30/UpdateImageGenerationConfiguration)
