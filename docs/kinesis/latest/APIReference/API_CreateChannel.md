---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_CreateChannel.html
---

# CreateChannel
<a name="API_CreateChannel"></a>

Creates a channel that delivers records from a Kinesis data stream to a destination. A channel reads records from the specified stream and writes them to streaming tables on Apache Iceberg (Amazon S3 Tables) or to a general purpose Amazon S3 bucket.

You must specify either `S3DestinationConfiguration` or `S3TablesDestinationConfiguration`, but not both.

To use this operation, you must have permission to pass the specified service execution IAM role to Amazon Kinesis Data Streams (the `iam:PassRole` permission on that role).

Creating a channel is an asynchronous operation. Upon receiving the request, Amazon Kinesis Data Streams returns immediately with the channel in the `CREATING` state. After provisioning is complete, Amazon Kinesis Data Streams sets the state to `ACTIVE`. You can use [DescribeChannel](API_DescribeChannel.md) to check the current state.

This operation is only supported for data streams with the on-demand capacity mode.

This operation has a call limit of 5 transactions per second (TPS) for each AWS account. Exceeding 5 TPS results in a `LimitExceededException`.

## Request Syntax
<a name="API_CreateChannel_RequestSyntax"></a>

```
{
   "ChannelName": "{{string}}",
   "EncryptionConfiguration": {
      "EncryptionType": "{{string}}",
      "KeyId": "{{string}}"
   },
   "LoggingConfiguration": {
      "CloudWatchLogs": {
         "Enabled": {{boolean}},
         "LogGroupName": "{{string}}",
         "LogStreamName": "{{string}}"
      }
   },
   "S3DestinationConfiguration": {
      "DataFreshnessInSeconds": {{number}},
      "DeadLetterQueueS3Configuration": {
         "BucketARN": "{{string}}",
         "ErrorOutputPrefix": "{{string}}",
         "ExpectedBucketOwner": "{{string}}"
      },
      "StorageConfiguration": {
         "BucketARN": "{{string}}",
         "CompressionType": "{{string}}",
         "ExpectedBucketOwner": "{{string}}",
         "OutputKeyTemplate": "{{string}}",
         "StorageClass": "{{string}}"
      }
   },
   "S3TablesDestinationConfiguration": {
      "DataFreshnessInSeconds": {{number}},
      "DeadLetterQueueS3Configuration": {
         "BucketARN": "{{string}}",
         "ErrorOutputPrefix": "{{string}}",
         "ExpectedBucketOwner": "{{string}}"
      },
      "S3TablesConfigurationList": [
         {
            "CompressionType": "{{string}}",
            "Namespace": "{{string}}",
            "PartitionSpec": {
               "PartitionFields": [
                  {
                     "SourceName": "{{string}}",
                     "Transform": "{{string}}"
                  }
               ]
            },
            "TableBucketARN": "{{string}}",
            "TableName": "{{string}}"
         }
      ]
   },
   "ServiceExecutionRoleARN": "{{string}}",
   "StreamConfigurationList": [
      {
         "RecordConfiguration": {
            "GSRSchemaARN": "{{string}}",
            "RecordFormatType": "{{string}}"
         },
         "StreamARN": "{{string}}"
      }
   ],
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateChannel_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ChannelName](#API_CreateChannel_RequestSyntax) **   <a name="Streams-CreateChannel-request-ChannelName"></a>
The name of the channel. The name is unique within your AWS account and AWS Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [EncryptionConfiguration](#API_CreateChannel_RequestSyntax) **   <a name="Streams-CreateChannel-request-EncryptionConfiguration"></a>
The server-side encryption configuration that uses an AWS KMS key to encrypt data delivered to the destination.
Type: [ChannelEncryptionConfiguration](API_ChannelEncryptionConfiguration.md) object
Required: No

 ** [LoggingConfiguration](#API_CreateChannel_RequestSyntax) **   <a name="Streams-CreateChannel-request-LoggingConfiguration"></a>
The Amazon CloudWatch Logs configuration for the channel.
Type: [ChannelLoggingConfiguration](API_ChannelLoggingConfiguration.md) object
Required: No

 ** [S3DestinationConfiguration](#API_CreateChannel_RequestSyntax) **   <a name="Streams-CreateChannel-request-S3DestinationConfiguration"></a>
The configuration for delivery to a general purpose Amazon S3 bucket. Specify this parameter when `S3TablesDestinationConfiguration` is not specified.
Type: [S3DestinationConfiguration](API_S3DestinationConfiguration.md) object
Required: No

 ** [S3TablesDestinationConfiguration](#API_CreateChannel_RequestSyntax) **   <a name="Streams-CreateChannel-request-S3TablesDestinationConfiguration"></a>
The configuration for delivery to streaming tables on Apache Iceberg in Amazon S3 Tables. Specify this parameter when `S3DestinationConfiguration` is not specified.
Type: [S3TablesDestinationConfiguration](API_S3TablesDestinationConfiguration.md) object
Required: No

 ** [ServiceExecutionRoleARN](#API_CreateChannel_RequestSyntax) **   <a name="Streams-CreateChannel-request-ServiceExecutionRoleARN"></a>
The Amazon Resource Name (ARN) of the IAM role that Amazon Kinesis Data Streams assumes to write records to the destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:aws[-a-z0-9]*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [StreamConfigurationList](#API_CreateChannel_RequestSyntax) **   <a name="Streams-CreateChannel-request-StreamConfigurationList"></a>
The source stream configuration for the channel. Currently, one stream is supported per channel.
Type: Array of [ChannelStreamConfiguration](API_ChannelStreamConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10000 items.
Required: Yes

 ** [Tags](#API_CreateChannel_RequestSyntax) **   <a name="Streams-CreateChannel-request-Tags"></a>
A set of key-value pairs to assign to the channel. A tag consists of a required key and an optional value.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateChannel_ResponseSyntax"></a>

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
<a name="API_CreateChannel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChannelDescription](#API_CreateChannel_ResponseSyntax) **   <a name="Streams-CreateChannel-response-ChannelDescription"></a>
The configuration and current status of the channel, including its ARN, destination configuration, and lifecycle state. Immediately after creation, the state is `CREATING`.
Type: [ChannelDescription](API_ChannelDescription.md) object

## Errors
<a name="API_CreateChannel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Specifies that you do not have the permissions required to perform this operation.
HTTP Status Code: 400

 ** InvalidArgumentException **
A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** KMSAccessDeniedException **
The ciphertext references a key that doesn't exist or that you don't have access to.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** KMSDisabledException **
The request was rejected because the specified customer master key (CMK) isn't enabled.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** KMSInvalidStateException **
The request was rejected because the state of the specified resource isn't valid for this request. For more information, see [How Key State Affects Use of a Customer Master Key](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * AWS Key Management Service Developer Guide*.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** KMSNotFoundException **
The request was rejected because the specified entity or resource can't be found.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** KMSOptInRequired **
The AWS access key ID needs a subscription for the service.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** KMSThrottlingException **
The request was denied due to request throttling. For more information about throttling, see [Limits](https://docs.aws.amazon.com/kms/latest/developerguide/limits.html#requests-per-second) in the * AWS Key Management Service Developer Guide*.
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

## Examples
<a name="API_CreateChannel_Examples"></a>

### To create a channel that delivers to streaming tables on Apache Iceberg
<a name="API_CreateChannel_Example_1"></a>

The following JSON example creates a channel that writes records from a Kinesis data stream to a streaming table on Apache Iceberg backed by Amazon S3 Tables.

#### Sample Request
<a name="API_CreateChannel_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: kinesis.<region>.<domain>
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Authorization: <AuthParams>
Connection: Keep-Alive
X-Amz-Date: <Date>
X-Amz-Target: Kinesis_20131202.CreateChannel
{
  "ChannelName": "orders-iceberg-channel",
  "ServiceExecutionRoleARN": "arn:aws:iam::123456789012:role/KinesisDeliveryRole",
  "StreamConfigurationList": [
    {
      "StreamARN": "arn:aws:kinesis:us-east-1:123456789012:stream/orders-stream",
      "RecordConfiguration": {
        "RecordFormatType": "JSON",
        "GSRSchemaARN": "arn:aws:glue:us-east-1:123456789012:schema/my-registry/orders-schema"
      }
    }
  ],
  "S3TablesDestinationConfiguration": {
    "DataFreshnessInSeconds": 300,
    "DeadLetterQueueS3Configuration": {
      "BucketARN": "arn:aws:s3:::my-dlq-bucket",
      "ExpectedBucketOwner": "123456789012",
      "ErrorOutputPrefix": "errors/"
    },
    "S3TablesConfigurationList": [
      {
        "TableBucketARN": "arn:aws:s3tables:us-east-1:123456789012:bucket/analytics-table-bucket",
        "Namespace": "analytics_db",
        "TableName": "orders_iceberg",
        "CompressionType": "ZSTD",
        "PartitionSpec": {
          "PartitionFields": [
            { "Transform": "TIME_HOUR", "SourceName": "event_timestamp" }
          ]
        }
      }
    ]
  }
}
```

#### Sample Response
<a name="API_CreateChannel_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "ChannelDescription": {
    "ChannelName": "orders-iceberg-channel",
    "ChannelARN": "arn:aws:kinesis:us-east-1:123456789012:channel/orders-iceberg-channel",
    "ChannelId": "abcd1234efgh5678",
    "ChannelStatus": "CREATING",
    "ChannelCreationTimestamp": 1755500000,
    "ServiceExecutionRoleARN": "arn:aws:iam::123456789012:role/KinesisDeliveryRole",
    "StreamConfigurationList": [
      {
        "StreamARN": "arn:aws:kinesis:us-east-1:123456789012:stream/orders-stream",
        "StreamCreationTimestamp": 1755400000,
        "RecordConfiguration": {
          "RecordFormatType": "JSON",
          "GSRSchemaARN": "arn:aws:glue:us-east-1:123456789012:schema/my-registry/orders-schema"
        }
      }
    ],
    "S3TablesDestinationConfiguration": {
      "DataFreshnessInSeconds": 300,
      "DeadLetterQueueS3Configuration": {
        "BucketARN": "arn:aws:s3:::my-dlq-bucket",
        "ExpectedBucketOwner": "123456789012",
        "ErrorOutputPrefix": "errors/"
      },
      "S3TablesConfigurationList": [
        {
          "TableBucketARN": "arn:aws:s3tables:us-east-1:123456789012:bucket/analytics-table-bucket",
          "Namespace": "analytics_db",
          "TableName": "orders_iceberg",
          "CompressionType": "ZSTD",
          "PartitionSpec": {
            "PartitionFields": [
              { "Transform": "TIME_HOUR", "SourceName": "event_timestamp" }
            ]
          }
        }
      ]
    }
  }
}
```

## See Also
<a name="API_CreateChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/CreateChannel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/CreateChannel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/CreateChannel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/CreateChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/CreateChannel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/CreateChannel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/CreateChannel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/CreateChannel)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/CreateChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/CreateChannel)
