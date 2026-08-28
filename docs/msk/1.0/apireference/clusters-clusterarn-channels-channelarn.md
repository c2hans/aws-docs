---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-channels-channelarn.html
---

# Clusters clusterArn Channels channelArn
<a name="clusters-clusterarn-channels-channelarn"></a>

## URI
<a name="clusters-clusterarn-channels-channelarn-url"></a>

`/v1/clusters/{{clusterArn}}/channels/{{channelArn}}`

## HTTP methods
<a name="clusters-clusterarn-channels-channelarn-http-methods"></a>

### GET
<a name="clusters-clusterarn-channels-channelarnget"></a>

**Operation ID:** `DescribeChannel`

Returns details for a channel resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |
| {{channelArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the channel. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  DescribeChannelResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### PUT
<a name="clusters-clusterarn-channels-channelarnput"></a>

**Operation ID:** `UpdateChannel`

Updates the channel specified by the channelArn in the request from the cluster specified by the Amazon Resource Name (ARN) in the request.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |
| {{channelArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the channel. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  UpdateChannelResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### DELETE
<a name="clusters-clusterarn-channels-channelarndelete"></a>

**Operation ID:** `DeleteChannel`

Deletes the channel specified by the channelArn in the request from the cluster specified by the Amazon Resource Name (ARN) in the request.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |
| {{channelArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the channel. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  DeleteChannelResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="clusters-clusterarn-channels-channelarnoptions"></a>

Enable CORS by returning correct headers

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |
| {{channelArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the channel. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="clusters-clusterarn-channels-channelarn-schemas"></a>

### Request bodies
<a name="clusters-clusterarn-channels-channelarn-request-examples"></a>

#### PUT schema
<a name="clusters-clusterarn-channels-channelarn-request-body-put-example"></a>

```
{
  "icebergDestinationUpdate": {
    "dataFreshnessInSeconds": integer
  },
  "s3DestinationUpdate": {
    "dataFreshnessInSeconds": integer
  }
}
```

### Response bodies
<a name="clusters-clusterarn-channels-channelarn-response-examples"></a>

#### DescribeChannelResponse schema
<a name="clusters-clusterarn-channels-channelarn-response-body-describechannelresponse-example"></a>

```
{
  "s3DestinationConfiguration": {
    "dataFreshnessInSeconds": integer,
    "serviceExecutionRoleArn": "string",
    "deadLetterQueueS3": {
      "bucketArn": "string",
      "expectedBucketOwner": "string",
      "errorOutputPrefix": "string"
    },
    "storage": {
      "storageClass": enum,
      "bucketArn": "string",
      "outputKeyTemplate": "string",
      "outputPrefix": "string",
      "expectedBucketOwner": "string",
      "compressionType": enum
    }
  },
  "clusterOperationArn": "string",
  "creationTime": "string",
  "loggingInfo": {
    "s3": {
      "bucket": "string",
      "prefix": "string",
      "enabled": boolean
    },
    "firehose": {
      "deliveryStream": "string",
      "enabled": boolean
    },
    "cloudWatchLogs": {
      "logGroup": "string",
      "enabled": boolean
    }
  },
  "icebergDestinationConfiguration": {
    "dataFreshnessInSeconds": integer,
    "serviceExecutionRoleArn": "string",
    "catalog": {
      "catalogArn": "string",
      "warehouseLocation": "string"
    },
    "schemaEvolution": {
      "enableSchemaEvolution": boolean
    },
    "deadLetterQueueS3": {
      "bucketArn": "string",
      "expectedBucketOwner": "string",
      "errorOutputPrefix": "string"
    },
    "compressionType": enum,
    "destinationTableList": [
      {
        "destinationTableName": "string",
        "destinationDatabaseName": "string",
        "partitionSpec": {
          "partitionStrategy": enum,
          "sourceList": [
            {
              "sourceName": "string"
            }
          ]
        }
      }
    ],
    "tableCreation": {
      "enableTableCreation": boolean
    },
    "appendOnly": boolean
  },
  "tags": {
  },
  "channelArn": "string",
  "topicConfigurationList": [
    {
      "recordConverter": {
        "valueConverter": enum
      },
      "recordSchema": {
        "gsrArn": "string"
      },
      "topicArn": "string"
    }
  ],
  "stateInfo": {
    "code": "string",
    "message": "string"
  },
  "encryptionConfiguration": {
    "kmsKeyArn": "string"
  },
  "destinationType": enum,
  "channelName": "string",
  "status": enum
}
```

#### UpdateChannelResponse schema
<a name="clusters-clusterarn-channels-channelarn-response-body-updatechannelresponse-example"></a>

```
{
  "clusterOperationArn": "string",
  "channelArn": "string"
}
```

#### DeleteChannelResponse schema
<a name="clusters-clusterarn-channels-channelarn-response-body-deletechannelresponse-example"></a>

```
{
  "clusterOperationArn": "string",
  "channelArn": "string"
}
```

#### Error schema
<a name="clusters-clusterarn-channels-channelarn-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="clusters-clusterarn-channels-channelarn-properties"></a>

### Catalog
<a name="clusters-clusterarn-channels-channelarn-model-catalog"></a>

Configuration of the AWS Glue Data Catalog and S3 Tables warehouse used by the Apache Iceberg destination.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| catalogArn | string | False | The Amazon Resource Name (ARN) of the federated AWS Glue Data Catalog that projects the S3 Tables bucket. If omitted, MSK derives the catalog ARN from warehouseLocation. |
| warehouseLocation | string | False | The Amazon Resource Name (ARN) of the S3 Tables bucket that backs the Apache Iceberg warehouse. |

### ChannelDestinationType
<a name="clusters-clusterarn-channels-channelarn-model-channeldestinationtype"></a>

The type of destination configured for the channel.
+ `ICEBERG`
+ `S3`

### ChannelLoggingInfo
<a name="clusters-clusterarn-channels-channelarn-model-channellogginginfo"></a>

Configuration for the destinations to which the channel publishes operational logs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cloudWatchLogs | [CloudWatchLogs](#clusters-clusterarn-channels-channelarn-model-cloudwatchlogs) | False | Configuration for delivering logs to Amazon CloudWatch Logs. |
| firehose | [Firehose](#clusters-clusterarn-channels-channelarn-model-firehose) | False | Configuration for delivering logs to an Amazon Data Firehose delivery stream. |
| s3 | [S3](#clusters-clusterarn-channels-channelarn-model-s3) | False | Configuration for delivering logs to an Amazon S3 bucket. |

### ChannelStateInfo
<a name="clusters-clusterarn-channels-channelarn-model-channelstateinfo"></a>

Additional context for the current channel state, populated when the channel is in FAILED.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| code | string | False | A short, machine-readable code identifying the failure cause. |
| message | string | False | A human-readable message describing the failure. |

### ChannelStatus
<a name="clusters-clusterarn-channels-channelarn-model-channelstatus"></a>

The lifecycle state of a channel.
+ `CREATING`
+ `ACTIVE`
+ `UPDATING`
+ `DELETING`
+ `FAILED`
+ `SUSPENDING`
+ `SUSPENDED`

### CloudWatchLogs
<a name="clusters-clusterarn-channels-channelarn-model-cloudwatchlogs"></a>

Details of the CloudWatch Logs destination for broker logs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | True | Specifies whether broker logs get sent to the specified CloudWatch Logs destination. |
| logGroup | string | False | The CloudWatch log group that is the destination for broker logs. |

### DeadLetterQueueS3
<a name="clusters-clusterarn-channels-channelarn-model-deadletterqueues3"></a>

Configuration of the Amazon S3 bucket where records that fail to deliver are stored.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bucketArn | string | True | The Amazon Resource Name (ARN) of the dead-letter Amazon S3 bucket. |
| errorOutputPrefix | string | False | An optional prefix prepended to every dead-letter Amazon S3 object key. |
| expectedBucketOwner | string | False | Optional 12-digit AWS account ID expected to own the dead-letter Amazon S3 bucket. |

### DeleteChannelResponse
<a name="clusters-clusterarn-channels-channelarn-model-deletechannelresponse"></a>

Returns the channel ARN and the cluster-operation ARN that tracks the asynchronous delete.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| channelArn | string | True | The Amazon Resource Name (ARN) that uniquely identifies the channel. |
| clusterOperationArn | string | False | The Amazon Resource Name (ARN) of the cluster operation. |

### DescribeChannelResponse
<a name="clusters-clusterarn-channels-channelarn-model-describechannelresponse"></a>

Contains the current configuration and state of a channel.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| channelArn | string | True | The Amazon Resource Name (ARN) that uniquely identifies the channel. |
| channelName | string | True | The name of the channel. |
| clusterOperationArn | string | False | The Amazon Resource Name (ARN) of the in-flight cluster operation. Returned only while the channel is in CREATING, UPDATING, or DELETING. |
| creationTime | string | True | The time when the channel was created. |
| destinationType | [ChannelDestinationType](#clusters-clusterarn-channels-channelarn-model-channeldestinationtype) | True | The type of destination configured for the channel. |
| encryptionConfiguration | [EncryptionConfiguration](#clusters-clusterarn-channels-channelarn-model-encryptionconfiguration) | False | The encryption configuration applied to the channel. |
| icebergDestinationConfiguration | [IcebergDestinationConfiguration](#clusters-clusterarn-channels-channelarn-model-icebergdestinationconfiguration) | False | The Apache Iceberg destination for the channel, if configured. |
| loggingInfo | [ChannelLoggingInfo](#clusters-clusterarn-channels-channelarn-model-channellogginginfo) | False | The destinations to which the channel publishes operational logs. |
| s3DestinationConfiguration | [S3DestinationConfiguration](#clusters-clusterarn-channels-channelarn-model-s3destinationconfiguration) | False | The Amazon S3 destination for the channel, if configured. |
| stateInfo | [ChannelStateInfo](#clusters-clusterarn-channels-channelarn-model-channelstateinfo) | False | Additional context for the current channel state, populated when the channel is in FAILED. |
| status | [ChannelStatus](#clusters-clusterarn-channels-channelarn-model-channelstatus) | True | The current lifecycle state of the channel. |
| tags | object | False | The tags attached to the channel. |
| topicConfigurationList | Array of type [TopicConfiguration](#clusters-clusterarn-channels-channelarn-model-topicconfiguration) | True | The list of topic configurations for the channel. |

### DestinationTable
<a name="clusters-clusterarn-channels-channelarn-model-destinationtable"></a>

Configuration of an Apache Iceberg destination table.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| destinationDatabaseName | string | False | The name of the destination namespace (database) in the AWS Glue Data Catalog. |
| destinationTableName | string | False | The name of the destination Apache Iceberg table. |
| partitionSpec | [PartitionSpec](#clusters-clusterarn-channels-channelarn-model-partitionspec) | False | The partition specification for the destination table. |

### EncryptionConfiguration
<a name="clusters-clusterarn-channels-channelarn-model-encryptionconfiguration"></a>

The AWS KMS encryption configuration applied to data at rest.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| kmsKeyArn | string | True | The Amazon Resource Name (ARN) of the AWS KMS key used to encrypt the data. |

### Error
<a name="clusters-clusterarn-channels-channelarn-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### Firehose
<a name="clusters-clusterarn-channels-channelarn-model-firehose"></a>

Firehose details for BrokerLogs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| deliveryStream | string | False | The Kinesis Data Firehose delivery stream that is the destination for broker logs. |
| enabled | boolean | True | Specifies whether broker logs get sent to the specified Kinesis Data Firehose delivery stream. |

### IcebergCompressionType
<a name="clusters-clusterarn-channels-channelarn-model-icebergcompressiontype"></a>

Compression codec for Iceberg table data files. Defaults to ZSTD.
+ `ZSTD`
+ `SNAPPY`

### IcebergDestinationConfiguration
<a name="clusters-clusterarn-channels-channelarn-model-icebergdestinationconfiguration"></a>

Configuration of an Apache Iceberg destination for a channel.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| appendOnly | boolean | True | Whether the destination is append-only. Must be true; updates and deletes are not supported. |
| catalog | [Catalog](#clusters-clusterarn-channels-channelarn-model-catalog) | False | The AWS Glue Data Catalog and S3 Tables warehouse used by the destination. |
| compressionType | [IcebergCompressionType](#clusters-clusterarn-channels-channelarn-model-icebergcompressiontype) | False | The compression codec for Iceberg table data files. Defaults to ZSTD. |
| dataFreshnessInSeconds | integer | False | The maximum time, in seconds, that records buffer in MSK before being flushed to the destination. Allowed range: 300 to 900. Default: 600. |
| deadLetterQueueS3 | [DeadLetterQueueS3](#clusters-clusterarn-channels-channelarn-model-deadletterqueues3) | True | The Amazon S3 bucket and prefix where MSK writes records that fail to deliver. |
| destinationTableList | Array of type [DestinationTable](#clusters-clusterarn-channels-channelarn-model-destinationtable) | True | The destination Iceberg tables. Currently exactly one table must be specified. |
| schemaEvolution | [SchemaEvolution](#clusters-clusterarn-channels-channelarn-model-schemaevolution) | True | Configuration controlling whether the destination table's schema is evolved to match incoming records. |
| serviceExecutionRoleArn | string | True | The Amazon Resource Name (ARN) of the IAM role that MSK assumes to access the destination table, the AWS Glue Data Catalog, and the dead-letter Amazon S3 bucket. |
| tableCreation | [TableCreation](#clusters-clusterarn-channels-channelarn-model-tablecreation) | True | Configuration controlling whether MSK creates the destination table if it does not already exist. |

### IcebergDestinationUpdate
<a name="clusters-clusterarn-channels-channelarn-model-icebergdestinationupdate"></a>

Update payload for an Apache Iceberg destination.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| dataFreshnessInSeconds | integer | True | The maximum time, in seconds, that records buffer in MSK before being flushed to the destination. Allowed range: 300 to 900. |

### PartitionSource
<a name="clusters-clusterarn-channels-channelarn-model-partitionsource"></a>

A source column used by an Apache Iceberg destination table's partition specification.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| sourceName | string | False | The name of the source column. |

### PartitionSpec
<a name="clusters-clusterarn-channels-channelarn-model-partitionspec"></a>

Partition specification for an Apache Iceberg destination table.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| partitionStrategy | [PartitionStrategy](#clusters-clusterarn-channels-channelarn-model-partitionstrategy) | True | The partitioning strategy applied to records written to the table. |
| sourceList | Array of type [PartitionSource](#clusters-clusterarn-channels-channelarn-model-partitionsource) | False | The source columns used by the partitioning strategy. For TIME\_HOUR, must contain exactly one source column whose value is a timestamp. |

### PartitionStrategy
<a name="clusters-clusterarn-channels-channelarn-model-partitionstrategy"></a>

The partitioning strategy used to partition records in the destination Apache Iceberg table.
+ `TIME_HOUR`

### RecordConverter
<a name="clusters-clusterarn-channels-channelarn-model-recordconverter"></a>

Configuration that controls how Apache Kafka record values are deserialized for the destination.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| valueConverter | [ValueConverter](#clusters-clusterarn-channels-channelarn-model-valueconverter) | True | The deserialization format applied to Apache Kafka record values. |

### RecordSchema
<a name="clusters-clusterarn-channels-channelarn-model-recordschema"></a>

Schema configuration that controls how Apache Kafka record values are validated.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| gsrArn | string | True | The Amazon Resource Name (ARN) of the AWS Glue Schema Registry schema (not registry) used to validate records for the destination Apache Iceberg table. |

### S3
<a name="clusters-clusterarn-channels-channelarn-model-s3"></a>

The details of the Amazon S3 destination for broker logs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bucket | string | False | The name of the S3 bucket that is the destination for broker logs. |
| enabled | boolean | True | Specifies whether broker logs get sent to the specified Amazon S3 destination. |
| prefix | string | False | The S3 prefix that is the destination for broker logs. |

### S3CompressionType
<a name="clusters-clusterarn-channels-channelarn-model-s3compressiontype"></a>

The compression codec applied to delivered Amazon S3 objects.
+ `NONE`
+ `GZIP`
+ `ZSTD`

### S3DestinationConfiguration
<a name="clusters-clusterarn-channels-channelarn-model-s3destinationconfiguration"></a>

Configuration of an Amazon S3 destination for a channel.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| dataFreshnessInSeconds | integer | False | The maximum time, in seconds, that records buffer in MSK before being flushed to the destination. Allowed range: 300 to 900. Default: 600. |
| deadLetterQueueS3 | [DeadLetterQueueS3](#clusters-clusterarn-channels-channelarn-model-deadletterqueues3) | True | The Amazon S3 bucket and prefix where MSK writes records that fail to deliver. |
| serviceExecutionRoleArn | string | True | The Amazon Resource Name (ARN) of the IAM role that MSK assumes to write to the destination Amazon S3 bucket and the dead-letter bucket. |
| storage | [S3Storage](#clusters-clusterarn-channels-channelarn-model-s3storage) | True | The Amazon S3 bucket, prefix, and storage class for delivered records. |

### S3DestinationUpdate
<a name="clusters-clusterarn-channels-channelarn-model-s3destinationupdate"></a>

Update payload for an Amazon S3 destination.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| dataFreshnessInSeconds | integer | True | The maximum time, in seconds, that records buffer in MSK before being flushed to the destination. Allowed range: 300 to 900. |

### S3Storage
<a name="clusters-clusterarn-channels-channelarn-model-s3storage"></a>

Storage configuration for an Amazon S3 destination bucket.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bucketArn | string | True | The Amazon Resource Name (ARN) of the destination Amazon S3 bucket. |
| compressionType | [S3CompressionType](#clusters-clusterarn-channels-channelarn-model-s3compressiontype) | True | The compression codec applied to delivered Amazon S3 objects. |
| expectedBucketOwner | string | False | Optional 12-digit AWS account ID expected to own the Amazon S3 bucket. |
| outputKeyTemplate | string | False | An optional template that controls the Amazon S3 object key for each delivered record. Supports the placeholders \!{partition-id}, \!{sequence-number}, and \!{kafka-offset}. |
| outputPrefix | string | False | An optional prefix prepended to every Amazon S3 object key written by the channel. |
| storageClass | [S3StorageClass](#clusters-clusterarn-channels-channelarn-model-s3storageclass) | True | The Amazon S3 storage class for delivered objects. |

### S3StorageClass
<a name="clusters-clusterarn-channels-channelarn-model-s3storageclass"></a>

The Amazon S3 storage class applied to delivered objects.
+ `STANDARD`
+ `INTELLIGENT_TIERING`
+ `GLACIER_IR`

### SchemaEvolution
<a name="clusters-clusterarn-channels-channelarn-model-schemaevolution"></a>

Configuration controlling whether the Apache Iceberg destination table's schema is evolved as incoming records change.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enableSchemaEvolution | boolean | False | Whether to allow MSK to evolve the destination table's schema. Must be false for the current release. |

### TableCreation
<a name="clusters-clusterarn-channels-channelarn-model-tablecreation"></a>

Configuration controlling whether MSK creates the destination Apache Iceberg table if it does not already exist.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enableTableCreation | boolean | False | Whether MSK creates the destination table on the customer's behalf. Must be true for the current release. |

### TopicConfiguration
<a name="clusters-clusterarn-channels-channelarn-model-topicconfiguration"></a>

Configuration of an Apache Kafka topic that feeds a channel.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| recordConverter | [RecordConverter](#clusters-clusterarn-channels-channelarn-model-recordconverter) | True | Configuration that controls how Apache Kafka record values are deserialized for the destination. |
| recordSchema | [RecordSchema](#clusters-clusterarn-channels-channelarn-model-recordschema) | False | The schema used to validate records when the value converter requires one (for example, JSON\_SCHEMA\_GSR). |
| topicArn | string | True | The Amazon Resource Name (ARN) that uniquely identifies the topic. |

### UpdateChannelRequest
<a name="clusters-clusterarn-channels-channelarn-model-updatechannelrequest"></a>

Updates an existing channel's destination configuration. You must update the same destination type the channel was created with; the destination type cannot be changed.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| icebergDestinationUpdate | [IcebergDestinationUpdate](#clusters-clusterarn-channels-channelarn-model-icebergdestinationupdate) | False | Updates fields on an Apache Iceberg destination. Use only when the channel was created with an Iceberg destination. |
| s3DestinationUpdate | [S3DestinationUpdate](#clusters-clusterarn-channels-channelarn-model-s3destinationupdate) | False | Updates fields on an Amazon S3 destination. Use only when the channel was created with an Amazon S3 destination. |

### UpdateChannelResponse
<a name="clusters-clusterarn-channels-channelarn-model-updatechannelresponse"></a>

Returns the channel ARN and the cluster-operation ARN that tracks the asynchronous update.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| channelArn | string | True | The Amazon Resource Name (ARN) that uniquely identifies the channel. |
| clusterOperationArn | string | False | The Amazon Resource Name (ARN) of the cluster operation. |

### ValueConverter
<a name="clusters-clusterarn-channels-channelarn-model-valueconverter"></a>

The deserialization format applied to Apache Kafka record values.
+ `BYTE_ARRAY`
+ `JSON`
+ `JSON_SCHEMA_GSR`
+ `STRING`

## See also
<a name="clusters-clusterarn-channels-channelarn-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DescribeChannel
<a name="DescribeChannel-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/DescribeChannel)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/DescribeChannel)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/DescribeChannel)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/DescribeChannel)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/DescribeChannel)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/DescribeChannel)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/DescribeChannel)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/DescribeChannel)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/DescribeChannel)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/DescribeChannel)

### UpdateChannel
<a name="UpdateChannel-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/UpdateChannel)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/UpdateChannel)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/UpdateChannel)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/UpdateChannel)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/UpdateChannel)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/UpdateChannel)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/UpdateChannel)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/UpdateChannel)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/UpdateChannel)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/UpdateChannel)

### DeleteChannel
<a name="DeleteChannel-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/DeleteChannel)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/DeleteChannel)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/DeleteChannel)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/DeleteChannel)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/DeleteChannel)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/DeleteChannel)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/DeleteChannel)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/DeleteChannel)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/DeleteChannel)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/DeleteChannel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
