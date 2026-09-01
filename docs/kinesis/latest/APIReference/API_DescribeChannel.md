---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeChannel.html
---

# DescribeChannel
<a name="API_DescribeChannel"></a>

Describes the specified channel, including its configuration and current status.

Use this operation to verify that a channel reached the `ACTIVE` state after creation, or to diagnose a channel in the `FAILED` state by reading the `ChannelStatusReason`.

This operation has a call limit of 5 transactions per second (TPS) for each AWS account. Exceeding 5 TPS results in a `LimitExceededException`.

## Request Syntax
<a name="API_DescribeChannel_RequestSyntax"></a>

```
{
   "ChannelARN": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeChannel_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ChannelARN](#API_DescribeChannel_RequestSyntax) **   <a name="Streams-DescribeChannel-request-ChannelARN"></a>
The Amazon Resource Name (ARN) of the channel to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:channel/\S+`
Required: Yes

## Response Syntax
<a name="API_DescribeChannel_ResponseSyntax"></a>

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
<a name="API_DescribeChannel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChannelDescription](#API_DescribeChannel_ResponseSyntax) **   <a name="Streams-DescribeChannel-response-ChannelDescription"></a>
The configuration and current status of the channel, including its ARN, source stream, destination configuration, and lifecycle state.
Type: [ChannelDescription](API_ChannelDescription.md) object

## Errors
<a name="API_DescribeChannel_Errors"></a>

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

 ** ResourceNotFoundException **
The requested resource could not be found. The stream might not be specified correctly.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ValidationException **
Specifies that you tried to invoke this API for a data stream with the on-demand capacity mode. This API is only supported for data streams with the provisioned capacity mode.
HTTP Status Code: 400

## See Also
<a name="API_DescribeChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/DescribeChannel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/DescribeChannel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/DescribeChannel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/DescribeChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/DescribeChannel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/DescribeChannel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/DescribeChannel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/DescribeChannel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/DescribeChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/DescribeChannel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
