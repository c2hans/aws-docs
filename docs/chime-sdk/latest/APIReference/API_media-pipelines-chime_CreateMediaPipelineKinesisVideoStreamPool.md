---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaPipelineKinesisVideoStreamPool.html
---

# CreateMediaPipelineKinesisVideoStreamPool
<a name="API_media-pipelines-chime_CreateMediaPipelineKinesisVideoStreamPool"></a>

Creates an Amazon Kinesis Video Stream pool for use with media stream pipelines.

**Note**
If a meeting uses an opt-in Region as its [MediaRegion](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeeting.html#chimesdk-meeting-chime_CreateMeeting-request-MediaRegion), the KVS stream must be in that same Region. For example, if a meeting uses the `af-south-1` Region, the KVS stream must also be in `af-south-1`. However, if the meeting uses a Region that AWS turns on by default, the KVS stream can be in any available Region, including an opt-in Region. For example, if the meeting uses `ca-central-1`, the KVS stream can be in `eu-west-2`, `us-east-1`, `af-south-1`, or any other Region that the Amazon Chime SDK supports.
To learn which AWS Region a meeting uses, call the [GetMeeting](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_GetMeeting.html) API and use the [MediaRegion](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeeting.html#chimesdk-meeting-chime_CreateMeeting-request-MediaRegion) parameter from the response.
For more information about opt-in Regions, refer to [Available Regions](https://docs.aws.amazon.com/chime-sdk/latest/dg/sdk-available-regions.html) in the *Amazon Chime SDK Developer Guide*, and [Specify which AWS Regions your account can use](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html#rande-manage-enable.html), in the *AWS Account Management Reference Guide*.

## Request Syntax
<a name="API_media-pipelines-chime_CreateMediaPipelineKinesisVideoStreamPool_RequestSyntax"></a>

```
POST /media-pipeline-kinesis-video-stream-pools HTTP/1.1
Content-type: application/json

{
   "ClientRequestToken": "{{string}}",
   "PoolName": "{{string}}",
   "StreamConfiguration": {
      "DataRetentionInHours": {{number}},
      "Region": "{{string}}"
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_media-pipelines-chime_CreateMediaPipelineKinesisVideoStreamPool_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_media-pipelines-chime_CreateMediaPipelineKinesisVideoStreamPool_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_media-pipelines-chime_CreateMediaPipelineKinesisVideoStreamPool_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaPipelineKinesisVideoStreamPool-request-ClientRequestToken"></a>
The token assigned to the client making the request.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Pattern: `[-_a-zA-Z0-9]*`
Required: No

 ** [PoolName](#API_media-pipelines-chime_CreateMediaPipelineKinesisVideoStreamPool_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaPipelineKinesisVideoStreamPool-request-PoolName"></a>
The name of the pool.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[0-9a-zA-Z._-]+`
Required: Yes

 ** [StreamConfiguration](#API_media-pipelines-chime_CreateMediaPipelineKinesisVideoStreamPool_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaPipelineKinesisVideoStreamPool-request-StreamConfiguration"></a>
The configuration settings for the stream.
Type: [KinesisVideoStreamConfiguration](API_media-pipelines-chime_KinesisVideoStreamConfiguration.md) object
Required: Yes

 ** [Tags](#API_media-pipelines-chime_CreateMediaPipelineKinesisVideoStreamPool_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaPipelineKinesisVideoStreamPool-request-Tags"></a>
The tags assigned to the stream pool.
Type: Array of [Tag](API_media-pipelines-chime_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_media-pipelines-chime_CreateMediaPipelineKinesisVideoStreamPool_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_media-pipelines-chime_CreateMediaPipelineKinesisVideoStreamPool_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [KinesisVideoStreamPoolConfiguration](#API_media-pipelines-chime_CreateMediaPipelineKinesisVideoStreamPool_ResponseSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaPipelineKinesisVideoStreamPool-response-KinesisVideoStreamPoolConfiguration"></a>
The configuration for applying the streams to the pool.

Type: [KinesisVideoStreamPoolConfiguration](API_media-pipelines-chime_KinesisVideoStreamPoolConfiguration.md) object

## Errors
<a name="API_media-pipelines-chime_CreateMediaPipelineKinesisVideoStreamPool_Errors"></a>

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

 ** ResourceLimitExceededException **
The request exceeds the resource limit.
 ** RequestId **
The request ID associated with the call responsible for the exception.
HTTP Status Code: 400

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
<a name="API_media-pipelines-chime_CreateMediaPipelineKinesisVideoStreamPool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-media-pipelines-2021-07-15/CreateMediaPipelineKinesisVideoStreamPool)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-media-pipelines-2021-07-15/CreateMediaPipelineKinesisVideoStreamPool)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/CreateMediaPipelineKinesisVideoStreamPool)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-media-pipelines-2021-07-15/CreateMediaPipelineKinesisVideoStreamPool)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/CreateMediaPipelineKinesisVideoStreamPool)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-media-pipelines-2021-07-15/CreateMediaPipelineKinesisVideoStreamPool)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-media-pipelines-2021-07-15/CreateMediaPipelineKinesisVideoStreamPool)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-media-pipelines-2021-07-15/CreateMediaPipelineKinesisVideoStreamPool)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-media-pipelines-2021-07-15/CreateMediaPipelineKinesisVideoStreamPool)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/CreateMediaPipelineKinesisVideoStreamPool)
