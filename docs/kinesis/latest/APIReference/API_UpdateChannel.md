---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_UpdateChannel.html
---

# UpdateChannel
<a name="API_UpdateChannel"></a>

Updates the data freshness interval or the Amazon CloudWatch Logs configuration of an existing channel. You cannot change the destination, source stream, record format, schema, encryption configuration, or service execution role of an existing channel. To change any other setting, delete the channel and create a new one.

Updating a channel is an asynchronous operation. Upon receiving the request, Amazon Kinesis Data Streams sets the channel to the `UPDATING` state and returns immediately. After the change is applied, Amazon Kinesis Data Streams sets the channel back to the `ACTIVE` state.

This operation has a call limit of 5 transactions per second (TPS) for each AWS account. Exceeding 5 TPS results in a `LimitExceededException`.

## Request Syntax
<a name="API_UpdateChannel_RequestSyntax"></a>

```
{
   "ChannelARN": "{{string}}",
   "LoggingConfiguration": {
      "CloudWatchLogs": {
         "Enabled": {{boolean}},
         "LogGroupName": "{{string}}",
         "LogStreamName": "{{string}}"
      }
   },
   "S3DestinationConfiguration": {
      "DataFreshnessInSeconds": {{number}}
   },
   "S3TablesDestinationConfiguration": {
      "DataFreshnessInSeconds": {{number}}
   }
}
```

## Request Parameters
<a name="API_UpdateChannel_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ChannelARN](#API_UpdateChannel_RequestSyntax) **   <a name="Streams-UpdateChannel-request-ChannelARN"></a>
The Amazon Resource Name (ARN) of the channel to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:channel/\S+`
Required: Yes

 ** [LoggingConfiguration](#API_UpdateChannel_RequestSyntax) **   <a name="Streams-UpdateChannel-request-LoggingConfiguration"></a>
The updated Amazon CloudWatch Logs configuration for the channel.
Type: [ChannelLoggingUpdateInput](API_ChannelLoggingUpdateInput.md) object
Required: No

 ** [S3DestinationConfiguration](#API_UpdateChannel_RequestSyntax) **   <a name="Streams-UpdateChannel-request-S3DestinationConfiguration"></a>
The updated configuration for a general purpose Amazon S3 destination. Specify this parameter when the channel delivers to a general purpose Amazon S3 bucket. Only `DataFreshnessInSeconds` can be updated.
Type: [S3DestinationUpdateInput](API_S3DestinationUpdateInput.md) object
Required: No

 ** [S3TablesDestinationConfiguration](#API_UpdateChannel_RequestSyntax) **   <a name="Streams-UpdateChannel-request-S3TablesDestinationConfiguration"></a>
The updated configuration for a streaming table destination. Specify this parameter when the channel delivers to streaming tables on Apache Iceberg in Amazon S3 Tables. Only `DataFreshnessInSeconds` can be updated.
Type: [S3TablesDestinationUpdateInput](API_S3TablesDestinationUpdateInput.md) object
Required: No

## Response Syntax
<a name="API_UpdateChannel_ResponseSyntax"></a>

```
{
   "ChannelDescription": {
      "ChannelARN": "string",
      "ChannelCreationTimestamp": number,
      "ChannelId": "string",
      "ChannelName": "string",
      "ChannelStatus": "string",
      "ChannelStatusReason": "string",
      "EncryptionConfiguration": {
         "EncryptionType": "string",
         "KeyId": "string"
      },
      "LoggingConfiguration": {
         "CloudWatchLogs": {
            "Enabled": boolean,
            "LogGroupName": "string",
            "LogStreamName": "string"
         }
      },
      "S3DestinationConfiguration": {
         "DataFreshnessInSeconds": number,
         "DeadLetterQueueS3Configuration": {
            "BucketARN": "string",
            "ErrorOutputPrefix": "string",
            "ExpectedBucketOwner": "string"
         },
         "StorageConfiguration": {
            "BucketARN": "string",
            "CompressionType": "string",
            "ExpectedBucketOwner": "string",
            "OutputKeyTemplate": "string",
            "StorageClass": "string"
         }
      },
      "S3TablesDestinationConfiguration": {
         "DataFreshnessInSeconds": number,
         "DeadLetterQueueS3Configuration": {
            "BucketARN": "string",
            "ErrorOutputPrefix": "string",
            "ExpectedBucketOwner": "string"
         },
         "S3TablesConfigurationList": [
            {
               "CompressionType": "string",
               "Namespace": "string",
               "PartitionSpec": {
                  "PartitionFields": [
                     {
                        "SourceName": "string",
                        "Transform": "string"
                     }
                  ]
               },
               "TableBucketARN": "string",
               "TableName": "string"
            }
         ]
      },
      "ServiceExecutionRoleARN": "string",
      "StreamConfigurationList": [
         {
            "RecordConfiguration": {
               "GSRSchemaARN": "string",
               "RecordFormatType": "string"
            },
            "StreamARN": "string",
            "StreamCreationTimestamp": number
         }
      ]
   }
}
```

## Response Elements
<a name="API_UpdateChannel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChannelDescription](#API_UpdateChannel_ResponseSyntax) **   <a name="Streams-UpdateChannel-response-ChannelDescription"></a>
The configuration and current status of the channel after the update, including its ARN, destination configuration, and lifecycle state. Immediately after the request, the state is `UPDATING`.
Type: [ChannelDescription](API_ChannelDescription.md) object

## Errors
<a name="API_UpdateChannel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Specifies that you do not have the permissions required to perform this operation.
HTTP Status Code: 400

 ** InvalidArgumentException **
A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** LimitExceededException **
The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ResourceInUseException **
The resource is not available for this operation. For successful operation, the resource must be in the `ACTIVE` state.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource could not be found. The stream might not be specified correctly.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ValidationException **
Specifies that you tried to invoke this API for a data stream with the on-demand capacity mode. This API is only supported for data streams with the provisioned capacity mode.
HTTP Status Code: 400

## See Also
<a name="API_UpdateChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/UpdateChannel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/UpdateChannel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/UpdateChannel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/UpdateChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/UpdateChannel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/UpdateChannel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/UpdateChannel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/UpdateChannel)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/UpdateChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/UpdateChannel)
