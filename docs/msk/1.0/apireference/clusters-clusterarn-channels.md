---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-channels.html
---

# Clusters clusterArn Channels
<a name="clusters-clusterarn-channels"></a>

## URI
<a name="clusters-clusterarn-channels-url"></a>

`/v1/clusters/{{clusterArn}}/channels`

## HTTP methods
<a name="clusters-clusterarn-channels-http-methods"></a>

### GET
<a name="clusters-clusterarn-channelsget"></a>

**Operation ID:** `ListChannels`

Returns all channels in a cluster.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| topicNameFilter | String | False | Filters results to channels whose topic name matches the specified value. |
| nextToken | String | False | The paginated results marker. When the result of the operation is truncated, the call returns `NextToken` in the response. To get the next batch, provide this token in your next request. |
| maxResults | String | False | The maximum number of results to return in the response (default maximum 100 results per API call). If there are more results, the response includes a `NextToken` parameter. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  ListChannelsResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### POST
<a name="clusters-clusterarn-channelspost"></a>

**Operation ID:** `CreateChannel`

Creates a channel using the specified properties in the request on the cluster specified by the Amazon Resource Name (ARN) in the request.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  CreateChannelResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 409 | Error | This cluster name already exists. Retry your request using another name. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="clusters-clusterarn-channelsoptions"></a>

Enable CORS by returning correct headers

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="clusters-clusterarn-channels-schemas"></a>

### Request bodies
<a name="clusters-clusterarn-channels-request-examples"></a>

#### POST schema
<a name="clusters-clusterarn-channels-request-body-post-example"></a>

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
  "encryptionConfiguration": {
    "kmsKeyArn": "string"
  },
  "channelName": "string",
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
  }
}
```

### Response bodies
<a name="clusters-clusterarn-channels-response-examples"></a>

#### ListChannelsResponse schema
<a name="clusters-clusterarn-channels-response-body-listchannelsresponse-example"></a>

```
{
  "channels": [
    {
      "clusterOperationArn": "string",
      "channelArn": "string",
      "creationTime": "string",
      "destinationType": enum,
      "channelName": "string",
      "status": enum
    }
  ],
  "nextToken": "string"
}
```

#### CreateChannelResponse schema
<a name="clusters-clusterarn-channels-response-body-createchannelresponse-example"></a>

```
{
  "clusterOperationArn": "string",
  "channelArn": "string"
}
```

#### Error schema
<a name="clusters-clusterarn-channels-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="clusters-clusterarn-channels-properties"></a>

### Catalog
<a name="clusters-clusterarn-channels-model-catalog"></a>

Configuration of the AWS Glue Data Catalog and S3 Tables warehouse used by the Apache Iceberg destination.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| catalogArn | string | False | The Amazon Resource Name (ARN) of the federated AWS Glue Data Catalog that projects the S3 Tables bucket. If omitted, MSK derives the catalog ARN from warehouseLocation. |
| warehouseLocation | string | False | The Amazon Resource Name (ARN) of the S3 Tables bucket that backs the Apache Iceberg warehouse. |

### ChannelDestinationType
<a name="clusters-clusterarn-channels-model-channeldestinationtype"></a>

The type of destination configured for the channel.
+ `ICEBERG`
+ `S3`

### ChannelInfo
<a name="clusters-clusterarn-channels-model-channelinfo"></a>

Summary information about a channel returned by ListChannels.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| channelArn | string | True | The Amazon Resource Name (ARN) that uniquely identifies the channel. |
| channelName | string | True | The name of the channel. |
| clusterOperationArn | string | False | The Amazon Resource Name (ARN) of the in-flight cluster operation. Returned only while the channel is in CREATING, UPDATING, or DELETING. |
| creationTime | string | True | The time when the channel was created. |
| destinationType | [ChannelDestinationType](#clusters-clusterarn-channels-model-channeldestinationtype) | True | The type of destination configured for the channel. |
| status | [ChannelStatus](#clusters-clusterarn-channels-model-channelstatus) | True | The current lifecycle state of the channel. |

### ChannelLoggingInfo
<a name="clusters-clusterarn-channels-model-channellogginginfo"></a>

Configuration for the destinations to which the channel publishes operational logs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cloudWatchLogs | [CloudWatchLogs](#clusters-clusterarn-channels-model-cloudwatchlogs) | False | Configuration for delivering logs to Amazon CloudWatch Logs. |
| firehose | [Firehose](#clusters-clusterarn-channels-model-firehose) | False | Configuration for delivering logs to an Amazon Data Firehose delivery stream. |
| s3 | [S3](#clusters-clusterarn-channels-model-s3) | False | Configuration for delivering logs to an Amazon S3 bucket. |

### ChannelStatus
<a name="clusters-clusterarn-channels-model-channelstatus"></a>

The lifecycle state of a channel.
+ `CREATING`
+ `ACTIVE`
+ `UPDATING`
+ `DELETING`
+ `FAILED`
+ `SUSPENDING`
+ `SUSPENDED`

### CloudWatchLogs
<a name="clusters-clusterarn-channels-model-cloudwatchlogs"></a>

Details of the CloudWatch Logs destination for broker logs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | True | Specifies whether broker logs get sent to the specified CloudWatch Logs destination. |
| logGroup | string | False | The CloudWatch log group that is the destination for broker logs. |

### CreateChannelRequest
<a name="clusters-clusterarn-channels-model-createchannelrequest"></a>

Creates a Channel that streams records from an Amazon MSK Express cluster topic to Amazon S3 or Apache Iceberg.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| channelName | string | True | The name of the channel. Must be unique within the cluster. |
| encryptionConfiguration | [EncryptionConfiguration](#clusters-clusterarn-channels-model-encryptionconfiguration) | False | The encryption configuration applied to the channel. |
| icebergDestinationConfiguration | [IcebergDestinationConfiguration](#clusters-clusterarn-channels-model-icebergdestinationconfiguration) | False | The Apache Iceberg destination for the channel. Mutually exclusive with s3DestinationConfiguration. |
| loggingInfo | [ChannelLoggingInfo](#clusters-clusterarn-channels-model-channellogginginfo) | False | The destinations to which the channel publishes operational logs. |
| s3DestinationConfiguration | [S3DestinationConfiguration](#clusters-clusterarn-channels-model-s3destinationconfiguration) | False | The Amazon S3 destination for the channel. Mutually exclusive with icebergDestinationConfiguration. |
| tags | object | False | The tags attached to the channel. |
| topicConfigurationList | Array of type [TopicConfiguration](#clusters-clusterarn-channels-model-topicconfiguration) | True | The list of topic configurations for the channel. Currently exactly one topic must be specified. |

### CreateChannelResponse
<a name="clusters-clusterarn-channels-model-createchannelresponse"></a>

Returns the channel ARN and the cluster-operation ARN that tracks the asynchronous create.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| channelArn | string | True | The Amazon Resource Name (ARN) that uniquely identifies the channel. |
| clusterOperationArn | string | False | The Amazon Resource Name (ARN) of the cluster operation. |

### DeadLetterQueueS3
<a name="clusters-clusterarn-channels-model-deadletterqueues3"></a>

Configuration of the Amazon S3 bucket where records that fail to deliver are stored.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bucketArn | string | True | The Amazon Resource Name (ARN) of the dead-letter Amazon S3 bucket. |
| errorOutputPrefix | string | False | An optional prefix prepended to every dead-letter Amazon S3 object key. |
| expectedBucketOwner | string | False | Optional 12-digit AWS account ID expected to own the dead-letter Amazon S3 bucket. |

### DestinationTable
<a name="clusters-clusterarn-channels-model-destinationtable"></a>

Configuration of an Apache Iceberg destination table.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| destinationDatabaseName | string | False | The name of the destination namespace (database) in the AWS Glue Data Catalog. |
| destinationTableName | string | False | The name of the destination Apache Iceberg table. |
| partitionSpec | [PartitionSpec](#clusters-clusterarn-channels-model-partitionspec) | False | The partition specification for the destination table. |

### EncryptionConfiguration
<a name="clusters-clusterarn-channels-model-encryptionconfiguration"></a>

The AWS KMS encryption configuration applied to data at rest.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| kmsKeyArn | string | True | The Amazon Resource Name (ARN) of the AWS KMS key used to encrypt the data. |

### Error
<a name="clusters-clusterarn-channels-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### Firehose
<a name="clusters-clusterarn-channels-model-firehose"></a>

Firehose details for BrokerLogs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| deliveryStream | string | False | The Kinesis Data Firehose delivery stream that is the destination for broker logs. |
| enabled | boolean | True | Specifies whether broker logs get sent to the specified Kinesis Data Firehose delivery stream. |

### IcebergCompressionType
<a name="clusters-clusterarn-channels-model-icebergcompressiontype"></a>

Compression codec for Iceberg table data files. Defaults to ZSTD.
+ `ZSTD`
+ `SNAPPY`

### IcebergDestinationConfiguration
<a name="clusters-clusterarn-channels-model-icebergdestinationconfiguration"></a>

Configuration of an Apache Iceberg destination for a channel.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| appendOnly | boolean | True | Whether the destination is append-only. Must be true; updates and deletes are not supported. |
| catalog | [Catalog](#clusters-clusterarn-channels-model-catalog) | False | The AWS Glue Data Catalog and S3 Tables warehouse used by the destination. |
| compressionType | [IcebergCompressionType](#clusters-clusterarn-channels-model-icebergcompressiontype) | False | The compression codec for Iceberg table data files. Defaults to ZSTD. |
| dataFreshnessInSeconds | integer | False | The maximum time, in seconds, that records buffer in MSK before being flushed to the destination. Allowed range: 300 to 900. Default: 600. |
| deadLetterQueueS3 | [DeadLetterQueueS3](#clusters-clusterarn-channels-model-deadletterqueues3) | True | The Amazon S3 bucket and prefix where MSK writes records that fail to deliver. |
| destinationTableList | Array of type [DestinationTable](#clusters-clusterarn-channels-model-destinationtable) | True | The destination Iceberg tables. Currently exactly one table must be specified. |
| schemaEvolution | [SchemaEvolution](#clusters-clusterarn-channels-model-schemaevolution) | True | Configuration controlling whether the destination table's schema is evolved to match incoming records. |
| serviceExecutionRoleArn | string | True | The Amazon Resource Name (ARN) of the IAM role that MSK assumes to access the destination table, the AWS Glue Data Catalog, and the dead-letter Amazon S3 bucket. |
| tableCreation | [TableCreation](#clusters-clusterarn-channels-model-tablecreation) | True | Configuration controlling whether MSK creates the destination table if it does not already exist. |

### ListChannelsResponse
<a name="clusters-clusterarn-channels-model-listchannelsresponse"></a>

Returns the list of channels in the cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| channels | Array of type [ChannelInfo](#clusters-clusterarn-channels-model-channelinfo) | False | The list of channels in the cluster. |
| nextToken | string | False | If the response from ListChannels is truncated, this token is included. Send it as the nextToken parameter on a subsequent ListChannels call to retrieve the next page. |

### PartitionSource
<a name="clusters-clusterarn-channels-model-partitionsource"></a>

A source column used by an Apache Iceberg destination table's partition specification.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| sourceName | string | False | The name of the source column. |

### PartitionSpec
<a name="clusters-clusterarn-channels-model-partitionspec"></a>

Partition specification for an Apache Iceberg destination table.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| partitionStrategy | [PartitionStrategy](#clusters-clusterarn-channels-model-partitionstrategy) | True | The partitioning strategy applied to records written to the table. |
| sourceList | Array of type [PartitionSource](#clusters-clusterarn-channels-model-partitionsource) | False | The source columns used by the partitioning strategy. For TIME\_HOUR, must contain exactly one source column whose value is a timestamp. |

### PartitionStrategy
<a name="clusters-clusterarn-channels-model-partitionstrategy"></a>

The partitioning strategy used to partition records in the destination Apache Iceberg table.
+ `TIME_HOUR`

### RecordConverter
<a name="clusters-clusterarn-channels-model-recordconverter"></a>

Configuration that controls how Apache Kafka record values are deserialized for the destination.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| valueConverter | [ValueConverter](#clusters-clusterarn-channels-model-valueconverter) | True | The deserialization format applied to Apache Kafka record values. |

### RecordSchema
<a name="clusters-clusterarn-channels-model-recordschema"></a>

Schema configuration that controls how Apache Kafka record values are validated.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| gsrArn | string | True | The Amazon Resource Name (ARN) of the AWS Glue Schema Registry schema (not registry) used to validate records for the destination Apache Iceberg table. |

### S3
<a name="clusters-clusterarn-channels-model-s3"></a>

The details of the Amazon S3 destination for broker logs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bucket | string | False | The name of the S3 bucket that is the destination for broker logs. |
| enabled | boolean | True | Specifies whether broker logs get sent to the specified Amazon S3 destination. |
| prefix | string | False | The S3 prefix that is the destination for broker logs. |

### S3CompressionType
<a name="clusters-clusterarn-channels-model-s3compressiontype"></a>

The compression codec applied to delivered Amazon S3 objects.
+ `NONE`
+ `GZIP`
+ `ZSTD`

### S3DestinationConfiguration
<a name="clusters-clusterarn-channels-model-s3destinationconfiguration"></a>

Configuration of an Amazon S3 destination for a channel.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| dataFreshnessInSeconds | integer | False | The maximum time, in seconds, that records buffer in MSK before being flushed to the destination. Allowed range: 300 to 900. Default: 600. |
| deadLetterQueueS3 | [DeadLetterQueueS3](#clusters-clusterarn-channels-model-deadletterqueues3) | True | The Amazon S3 bucket and prefix where MSK writes records that fail to deliver. |
| serviceExecutionRoleArn | string | True | The Amazon Resource Name (ARN) of the IAM role that MSK assumes to write to the destination Amazon S3 bucket and the dead-letter bucket. |
| storage | [S3Storage](#clusters-clusterarn-channels-model-s3storage) | True | The Amazon S3 bucket, prefix, and storage class for delivered records. |

### S3Storage
<a name="clusters-clusterarn-channels-model-s3storage"></a>

Storage configuration for an Amazon S3 destination bucket.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bucketArn | string | True | The Amazon Resource Name (ARN) of the destination Amazon S3 bucket. |
| compressionType | [S3CompressionType](#clusters-clusterarn-channels-model-s3compressiontype) | True | The compression codec applied to delivered Amazon S3 objects. |
| expectedBucketOwner | string | False | Optional 12-digit AWS account ID expected to own the Amazon S3 bucket. |
| outputKeyTemplate | string | False | An optional template that controls the Amazon S3 object key for each delivered record. Supports the placeholders \!{partition-id}, \!{sequence-number}, and \!{kafka-offset}. |
| outputPrefix | string | False | An optional prefix prepended to every Amazon S3 object key written by the channel. |
| storageClass | [S3StorageClass](#clusters-clusterarn-channels-model-s3storageclass) | True | The Amazon S3 storage class for delivered objects. |

### S3StorageClass
<a name="clusters-clusterarn-channels-model-s3storageclass"></a>

The Amazon S3 storage class applied to delivered objects.
+ `STANDARD`
+ `INTELLIGENT_TIERING`
+ `GLACIER_IR`

### SchemaEvolution
<a name="clusters-clusterarn-channels-model-schemaevolution"></a>

Configuration controlling whether the Apache Iceberg destination table's schema is evolved as incoming records change.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enableSchemaEvolution | boolean | False | Whether to allow MSK to evolve the destination table's schema. Must be false for the current release. |

### TableCreation
<a name="clusters-clusterarn-channels-model-tablecreation"></a>

Configuration controlling whether MSK creates the destination Apache Iceberg table if it does not already exist.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enableTableCreation | boolean | False | Whether MSK creates the destination table on the customer's behalf. Must be true for the current release. |

### TopicConfiguration
<a name="clusters-clusterarn-channels-model-topicconfiguration"></a>

Configuration of an Apache Kafka topic that feeds a channel.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| recordConverter | [RecordConverter](#clusters-clusterarn-channels-model-recordconverter) | True | Configuration that controls how Apache Kafka record values are deserialized for the destination. |
| recordSchema | [RecordSchema](#clusters-clusterarn-channels-model-recordschema) | False | The schema used to validate records when the value converter requires one (for example, JSON\_SCHEMA\_GSR). |
| topicArn | string | True | The Amazon Resource Name (ARN) that uniquely identifies the topic. |

### ValueConverter
<a name="clusters-clusterarn-channels-model-valueconverter"></a>

The deserialization format applied to Apache Kafka record values.
+ `BYTE_ARRAY`
+ `JSON`
+ `JSON_SCHEMA_GSR`
+ `STRING`

## See also
<a name="clusters-clusterarn-channels-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListChannels
<a name="ListChannels-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/ListChannels)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/ListChannels)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/ListChannels)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/ListChannels)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/ListChannels)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/ListChannels)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/ListChannels)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/ListChannels)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/ListChannels)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/ListChannels)

### CreateChannel
<a name="CreateChannel-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/CreateChannel)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/CreateChannel)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/CreateChannel)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/CreateChannel)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/CreateChannel)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/CreateChannel)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/CreateChannel)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/CreateChannel)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/CreateChannel)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/CreateChannel)
