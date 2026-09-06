---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_DescribeEdgeConfiguration.html
---

# DescribeEdgeConfiguration
<a name="API_DescribeEdgeConfiguration"></a>

Describes a stream’s edge configuration that was set using the `StartEdgeConfigurationUpdate` API and the latest status of the edge agent's recorder and uploader jobs. Use this API to get the status of the configuration to determine if the configuration is in sync with the Edge Agent. Use this API to evaluate the health of the Edge Agent.

**Note**
This API isn't available in the AWS Africa (Cape Town) region, af-south-1.

## Request Syntax
<a name="API_DescribeEdgeConfiguration_RequestSyntax"></a>

```
POST /describeEdgeConfiguration HTTP/1.1
Content-type: application/json

{
   "StreamARN": "{{string}}",
   "StreamName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeEdgeConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeEdgeConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [StreamARN](#API_DescribeEdgeConfiguration_RequestSyntax) **   <a name="KinesisVideo-DescribeEdgeConfiguration-request-StreamARN"></a>
The Amazon Resource Name (ARN) of the stream. Specify either the `StreamName`or the `StreamARN`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`
Required: No

 ** [StreamName](#API_DescribeEdgeConfiguration_RequestSyntax) **   <a name="KinesisVideo-DescribeEdgeConfiguration-request-StreamName"></a>
The name of the stream whose edge configuration you want to update. Specify either the `StreamName` or the `StreamARN`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## Response Syntax
<a name="API_DescribeEdgeConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreationTime": number,
   "EdgeAgentStatus": {
      "LastRecorderStatus": {
         "JobStatusDetails": "string",
         "LastCollectedTime": number,
         "LastUpdatedTime": number,
         "RecorderStatus": "string"
      },
      "LastUploaderStatus": {
         "JobStatusDetails": "string",
         "LastCollectedTime": number,
         "LastUpdatedTime": number,
         "UploaderStatus": "string"
      }
   },
   "EdgeConfig": {
      "DeletionConfig": {
         "DeleteAfterUpload": boolean,
         "EdgeRetentionInHours": number,
         "LocalSizeConfig": {
            "MaxLocalMediaSizeInMB": number,
            "StrategyOnFullSize": "string"
         }
      },
      "HubDeviceArn": "string",
      "RecorderConfig": {
         "MediaSourceConfig": {
            "MediaUriSecretArn": "string",
            "MediaUriType": "string"
         },
         "ScheduleConfig": {
            "DurationInSeconds": number,
            "ScheduleExpression": "string"
         }
      },
      "UploaderConfig": {
         "ScheduleConfig": {
            "DurationInSeconds": number,
            "ScheduleExpression": "string"
         }
      }
   },
   "FailedStatusDetails": "string",
   "LastUpdatedTime": number,
   "StreamARN": "string",
   "StreamName": "string",
   "SyncStatus": "string"
}
```

## Response Elements
<a name="API_DescribeEdgeConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_DescribeEdgeConfiguration_ResponseSyntax) **   <a name="KinesisVideo-DescribeEdgeConfiguration-response-CreationTime"></a>
The timestamp at which a stream’s edge configuration was first created.
Type: Timestamp

 ** [EdgeAgentStatus](#API_DescribeEdgeConfiguration_ResponseSyntax) **   <a name="KinesisVideo-DescribeEdgeConfiguration-response-EdgeAgentStatus"></a>
An object that contains the latest status details for an edge agent's recorder and uploader jobs. Use this information to determine the current health of an edge agent.
Type: [EdgeAgentStatus](API_EdgeAgentStatus.md) object

 ** [EdgeConfig](#API_DescribeEdgeConfiguration_ResponseSyntax) **   <a name="KinesisVideo-DescribeEdgeConfiguration-response-EdgeConfig"></a>
A description of the stream's edge configuration that will be used to sync with the Edge Agent IoT Greengrass component. The Edge Agent component will run on an IoT Hub Device setup at your premise.
Type: [EdgeConfig](API_EdgeConfig.md) object

 ** [FailedStatusDetails](#API_DescribeEdgeConfiguration_ResponseSyntax) **   <a name="KinesisVideo-DescribeEdgeConfiguration-response-FailedStatusDetails"></a>
A description of the generated failure status.
Type: String

 ** [LastUpdatedTime](#API_DescribeEdgeConfiguration_ResponseSyntax) **   <a name="KinesisVideo-DescribeEdgeConfiguration-response-LastUpdatedTime"></a>
The timestamp at which a stream’s edge configuration was last updated.
Type: Timestamp

 ** [StreamARN](#API_DescribeEdgeConfiguration_ResponseSyntax) **   <a name="KinesisVideo-DescribeEdgeConfiguration-response-StreamARN"></a>
The Amazon Resource Name (ARN) of the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

 ** [StreamName](#API_DescribeEdgeConfiguration_ResponseSyntax) **   <a name="KinesisVideo-DescribeEdgeConfiguration-response-StreamName"></a>
The name of the stream from which the edge configuration was updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [SyncStatus](#API_DescribeEdgeConfiguration_ResponseSyntax) **   <a name="KinesisVideo-DescribeEdgeConfiguration-response-SyncStatus"></a>
The latest status of the edge configuration update.
Type: String
Valid Values: `SYNCING | ACKNOWLEDGED | IN_SYNC | SYNC_FAILED | DELETING | DELETE_FAILED | DELETING_ACKNOWLEDGED`

## Errors
<a name="API_DescribeEdgeConfiguration_Errors"></a>

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

 ** StreamEdgeConfigurationNotFoundException **
The Exception rendered when the Amazon Kinesis Video Stream can't find a stream's edge configuration that you specified.
HTTP Status Code: 404

## See Also
<a name="API_DescribeEdgeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisvideo-2017-09-30/DescribeEdgeConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisvideo-2017-09-30/DescribeEdgeConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisvideo-2017-09-30/DescribeEdgeConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisvideo-2017-09-30/DescribeEdgeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisvideo-2017-09-30/DescribeEdgeConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/DescribeEdgeConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisvideo-2017-09-30/DescribeEdgeConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisvideo-2017-09-30/DescribeEdgeConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesisvideo-2017-09-30/DescribeEdgeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisvideo-2017-09-30/DescribeEdgeConfiguration)
