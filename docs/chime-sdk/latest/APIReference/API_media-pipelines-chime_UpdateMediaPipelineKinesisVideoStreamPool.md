---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_UpdateMediaPipelineKinesisVideoStreamPool.html
---

# UpdateMediaPipelineKinesisVideoStreamPool
<a name="API_media-pipelines-chime_UpdateMediaPipelineKinesisVideoStreamPool"></a>

Updates an Amazon Kinesis Video Stream pool in a media pipeline.

## Request Syntax
<a name="API_media-pipelines-chime_UpdateMediaPipelineKinesisVideoStreamPool_RequestSyntax"></a>

```
PUT /media-pipeline-kinesis-video-stream-pools/{{identifier}} HTTP/1.1
Content-type: application/json

{
   "StreamConfiguration": {
      "DataRetentionInHours": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_media-pipelines-chime_UpdateMediaPipelineKinesisVideoStreamPool_RequestParameters"></a>

The request uses the following URI parameters.

 ** [identifier](#API_media-pipelines-chime_UpdateMediaPipelineKinesisVideoStreamPool_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_UpdateMediaPipelineKinesisVideoStreamPool-request-uri-Identifier"></a>
The unique identifier of the requested resource. Valid values include the name and ARN of the media pipeline Kinesis Video Stream pool.
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_media-pipelines-chime_UpdateMediaPipelineKinesisVideoStreamPool_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [StreamConfiguration](#API_media-pipelines-chime_UpdateMediaPipelineKinesisVideoStreamPool_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_UpdateMediaPipelineKinesisVideoStreamPool-request-StreamConfiguration"></a>
The configuration settings for the video stream.
Type: [KinesisVideoStreamConfigurationUpdate](API_media-pipelines-chime_KinesisVideoStreamConfigurationUpdate.md) object
Required: No

## Response Syntax
<a name="API_media-pipelines-chime_UpdateMediaPipelineKinesisVideoStreamPool_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "KinesisVideoStreamPoolConfiguration": {
      "CreatedTimestamp": "string",
      "PoolArn": "string",
      "PoolId": "string",
      "PoolName": "string",
      "PoolSize": number,
      "PoolStatus": "string",
      "StreamConfiguration": {
         "DataRetentionInHours": number,
         "Region": "string"
      },
      "UpdatedTimestamp": "string"
   }
}
```

## Response Elements
<a name="API_media-pipelines-chime_UpdateMediaPipelineKinesisVideoStreamPool_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [KinesisVideoStreamPoolConfiguration](#API_media-pipelines-chime_UpdateMediaPipelineKinesisVideoStreamPool_ResponseSyntax) **   <a name="chimesdk-media-pipelines-chime_UpdateMediaPipelineKinesisVideoStreamPool-response-KinesisVideoStreamPoolConfiguration"></a>
The video stream pool configuration object.
Type: [KinesisVideoStreamPoolConfiguration](API_media-pipelines-chime_KinesisVideoStreamPoolConfiguration.md) object

## Errors
<a name="API_media-pipelines-chime_UpdateMediaPipelineKinesisVideoStreamPool_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
 ** RequestId **
The request ID associated with the call responsible for the exception.
HTTP Status Code: 400

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource.
 ** RequestId **
The request ID associated with the call responsible for the exception.
HTTP Status Code: 409

 ** ForbiddenException **
The client is permanently forbidden from making the request.
 ** RequestId **
The request id associated with the call responsible for the exception.
HTTP Status Code: 403

 ** NotFoundException **
One or more of the resources in the request does not exist in the system.
 ** RequestId **
The request ID associated with the call responsible for the exception.
HTTP Status Code: 404

 ** ServiceFailureException **
The service encountered an unexpected error.
 ** RequestId **
The request ID associated with the call responsible for the exception.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
 ** RequestId **
The request ID associated with the call responsible for the exception.
HTTP Status Code: 503

 ** ThrottledClientException **
The client exceeded its request rate limit.
 ** RequestId **
The request ID associated with the call responsible for the exception.
HTTP Status Code: 429

 ** UnauthorizedClientException **
The client is not currently authorized to make the request.
 ** RequestId **
The request ID associated with the call responsible for the exception.
HTTP Status Code: 401

## See Also
<a name="API_media-pipelines-chime_UpdateMediaPipelineKinesisVideoStreamPool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-media-pipelines-2021-07-15/UpdateMediaPipelineKinesisVideoStreamPool)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-media-pipelines-2021-07-15/UpdateMediaPipelineKinesisVideoStreamPool)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/UpdateMediaPipelineKinesisVideoStreamPool)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-media-pipelines-2021-07-15/UpdateMediaPipelineKinesisVideoStreamPool)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/UpdateMediaPipelineKinesisVideoStreamPool)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-media-pipelines-2021-07-15/UpdateMediaPipelineKinesisVideoStreamPool)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-media-pipelines-2021-07-15/UpdateMediaPipelineKinesisVideoStreamPool)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-media-pipelines-2021-07-15/UpdateMediaPipelineKinesisVideoStreamPool)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-media-pipelines-2021-07-15/UpdateMediaPipelineKinesisVideoStreamPool)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/UpdateMediaPipelineKinesisVideoStreamPool)
