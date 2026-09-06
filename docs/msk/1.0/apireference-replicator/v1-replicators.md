---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference-replicator/v1-replicators.html
---

# V1 Replicators
<a name="v1-replicators"></a>

## URI
<a name="v1-replicators-url"></a>

`/replication/v1/replicators`

## HTTP methods
<a name="v1-replicators-http-methods"></a>

### GET
<a name="v1-replicatorsget"></a>

**Operation ID:** `ListReplicators`

Lists the replicators.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| replicatorNameFilter | String | False | Returns replicators starting with given name. |
| nextToken | String | False | If the response of ListReplicators is truncated, it returns a NextToken in the response. This NextToken should be sent in the subsequent request to ListReplicators. |
| maxResults | String | False | The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  ListReplicatorsResponse | HTTP Status Code 200: OK. |
| 400 | None | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 401 | None | HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated. |
| 403 | None | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 404 | None | HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it. |
| 429 | None | HTTP Status Code 429: Limit exceeded. Resource limit reached. |
| 500 | None | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | None | HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue. |

### POST
<a name="v1-replicatorspost"></a>

**Operation ID:** `CreateReplicator`

Creates the replicator.

Note: Enhanced consumer offset syncing is only supported when the `topicNameConfiguration` type is `IDENTICAL`.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  CreateReplicatorResponse | HTTP Status Code 200: OK. |
| 400 | None | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 401 | None | HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated. |
| 403 | None | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 404 | None | HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it. |
| 409 | None | HTTP Status Code 409: Conflict. This replicator name already exists. Retry your request with another name. |
| 429 | None | HTTP Status Code 429: Limit exceeded. Resource limit reached. |
| 500 | None | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | None | HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue. |

### OPTIONS
<a name="v1-replicatorsoptions"></a>

Enable CORS by returning correct headers

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="v1-replicators-schemas"></a>

### Request bodies
<a name="v1-replicators-request-examples"></a>

#### POST schema
<a name="v1-replicators-request-body-post-example"></a>

```
{
  "replicatorName": "string",
  "logDelivery": {
    "replicatorLogDelivery": {
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
    }
  },
  "serviceExecutionRoleArn": "string",
  "replicationInfoList": [
    {
      "consumerGroupReplication": {
        "consumerGroupsToExclude": [
          "string"
        ],
        "consumerGroupOffsetSyncMode": enum,
        "detectAndCopyNewConsumerGroups": boolean,
        "consumerGroupsToReplicate": [
          "string"
        ],
        "synchroniseConsumerGroupOffsets": boolean
      },
      "targetCompressionType": enum,
      "topicReplication": {
        "copyAccessControlListsForTopics": boolean,
        "detectAndCopyNewTopics": boolean,
        "topicNameConfiguration": {
          "type": enum
        },
        "copyTopicConfigurations": boolean,
        "startingPosition": {
          "type": enum
        },
        "topicsToReplicate": [
          "string"
        ],
        "topicsToExclude": [
          "string"
        ]
      },
      "sourceKafkaClusterArn": "string",
      "targetKafkaClusterArn": "string",
      "sourceKafkaClusterId": "string",
      "targetKafkaClusterId": "string"
    }
  ],
  "description": "string",
  "kafkaClusters": [
    {
      "amazonMskCluster": {
        "mskClusterArn": "string"
      },
      "vpcConfig": {
        "securityGroupIds": [
          "string"
        ],
        "subnetIds": [
          "string"
        ]
      },
      "encryptionInTransit": {
        "encryptionType": enum,
        "rootCaCertificate": "string"
      },
      "apacheKafkaCluster": {
        "bootstrapBrokerString": "string",
        "apacheKafkaClusterId": "string"
      },
      "clientAuthentication": {
        "saslScram": {
          "secretArn": "string",
          "mechanism": enum
        }
      }
    }
  ],
  "tags": {
  }
}
```

### Response bodies
<a name="v1-replicators-response-examples"></a>

#### ListReplicatorsResponse schema
<a name="v1-replicators-response-body-listreplicatorsresponse-example"></a>

```
{
  "nextToken": "string",
  "replicators": [
    {
      "replicatorArn": "string",
      "replicatorName": "string",
      "creationTime": "string",
      "kafkaClustersSummary": [
        {
          "kafkaClusterAlias": "string",
          "amazonMskCluster": {
            "mskClusterArn": "string"
          },
          "apacheKafkaCluster": {
            "bootstrapBrokerString": "string",
            "apacheKafkaClusterId": "string"
          }
        }
      ],
      "replicatorState": enum,
      "isReplicatorReference": boolean,
      "replicationInfoSummaryList": [
        {
          "sourceKafkaClusterAlias": "string",
          "targetKafkaClusterAlias": "string"
        }
      ],
      "replicatorResourceArn": "string",
      "currentVersion": "string"
    }
  ]
}
```

#### CreateReplicatorResponse schema
<a name="v1-replicators-response-body-createreplicatorresponse-example"></a>

```
{
  "replicatorArn": "string",
  "replicatorName": "string",
  "replicatorState": enum
}
```

## Properties
<a name="v1-replicators-properties"></a>

### AmazonMskCluster
<a name="v1-replicators-model-amazonmskcluster"></a>

Details of an Amazon MSK Cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| mskClusterArn | string | True | The Amazon Resource Name (ARN) of an Amazon MSK cluster. |

### ApacheKafkaCluster
<a name="v1-replicators-model-apachekafkacluster"></a>

Details of an Apache Kafka cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| apacheKafkaClusterId | string | True | The globally unique cluster ID of the Apache Kafka cluster. For information on how to retrieve the cluster ID, see https://github.com/apache/kafka/blob/trunk/bin/kafka-cluster.sh |
| bootstrapBrokerString | string | True | The bootstrap broker string of the Apache Kafka cluster. |

### CloudWatchLogs
<a name="v1-replicators-model-cloudwatchlogs"></a>

CloudWatch Logs details for ReplicatorLogDelivery.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | True | Whether log delivery to CloudWatch Logs is enabled. |
| logGroup | string | False | The CloudWatch log group that is the destination for log delivery. |

### ConsumerGroupOffsetSyncMode
<a name="v1-replicators-model-consumergroupoffsetsyncmode"></a>

The consumer group offset synchronization mode. With LEGACY, offsets are synchronized when producers write to the source cluster. With ENHANCED, consumer offsets are synchronized regardless of producer location. ENHANCED requires a corresponding replicator that replicates data from the target cluster to the source cluster.
+ `LEGACY`
+ `ENHANCED`

### ConsumerGroupReplication
<a name="v1-replicators-model-consumergroupreplication"></a>

Details about consumer group replication.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| consumerGroupOffsetSyncMode | [ConsumerGroupOffsetSyncMode](#v1-replicators-model-consumergroupoffsetsyncmode) | False | The consumer group offset synchronization mode. With LEGACY, offsets are synchronized when producers write to the source cluster. With ENHANCED, consumer offsets are synchronized regardless of producer location. ENHANCED requires a corresponding replicator that replicates data from the target cluster to the source cluster. |
| consumerGroupsToExclude | Array of type string<br />MaxLength: 256 | False | List of regular expression patterns indicating the consumer groups that should not be replicated. |
| consumerGroupsToReplicate | Array of type string<br />MaxLength: 256 | True | List of regular expression patterns indicating the consumer groups to copy. |
| detectAndCopyNewConsumerGroups | boolean | False | Enables synchronization of consumer groups to target cluster. |
| synchroniseConsumerGroupOffsets | boolean | False | Enables synchronization of consumer group offsets to target cluster. The translated offsets will be written to topic \_\_consumer\_offsets. |

### CreateReplicatorRequest
<a name="v1-replicators-model-createreplicatorrequest"></a>

Request body for replicator.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| description | string<br />MaxLength: 1024 | False | A summary description of the replicator. |
| kafkaClusters | Array of type [KafkaCluster](#v1-replicators-model-kafkacluster) | True | Kafka Clusters to use in setting up sources / targets for replication. |
| logDelivery | [LogDelivery](#v1-replicators-model-logdelivery) | False | Configuration for delivering replicator logs to customer destinations. |
| replicationInfoList | Array of type [ReplicationInfo](#v1-replicators-model-replicationinfo) | True | A list of replication configurations, where each configuration targets a given source cluster to target cluster replication flow. |
| replicatorName | string<br />Pattern: `^[0-9A-Za-z][0-9A-Za-z-]{0,}$`<br />MinLength: 1<br />MaxLength: 128 | True | The name of the replicator. Alpha-numeric characters with '-' are allowed. |
| serviceExecutionRoleArn | string | True | The ARN of the IAM role used by the replicator to access resources in the customer's account (e.g source and target clusters) |
| tags | object | False | List of tags to attach to created Replicator. |

### CreateReplicatorResponse
<a name="v1-replicators-model-createreplicatorresponse"></a>

Returns information about the created replicator.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| replicatorArn | string | False | The Amazon Resource Name (ARN) of the replicator. |
| replicatorName | string | False | Name of the replicator provided by the customer. |
| replicatorState | [ReplicatorState](#v1-replicators-model-replicatorstate) | False | State of the replicator. |

### Firehose
<a name="v1-replicators-model-firehose"></a>

Firehose details for ReplicatorLogDelivery.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| deliveryStream | string | False | The Firehose delivery stream that is the destination for log delivery. |
| enabled | boolean | True | Whether log delivery to Firehose is enabled. |

### KafkaCluster
<a name="v1-replicators-model-kafkacluster"></a>

Information about Kafka Cluster to be used as source / target for replication.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| amazonMskCluster | [AmazonMskCluster](#v1-replicators-model-amazonmskcluster) | False | Details of an Amazon MSK Cluster. |
| apacheKafkaCluster | [ApacheKafkaCluster](#v1-replicators-model-apachekafkacluster) | False | Details of an Apache Kafka cluster. Exactly one of amazonMskCluster and apacheKafkaCluster is required. |
| clientAuthentication | [KafkaClusterClientAuthentication](#v1-replicators-model-kafkaclusterclientauthentication) | False | Details of the client authentication used by the Apache Kafka cluster. |
| encryptionInTransit | [KafkaClusterEncryptionInTransit](#v1-replicators-model-kafkaclusterencryptionintransit) | False | Details of encryption in transit to the Apache Kafka cluster. |
| vpcConfig | [KafkaClusterClientVpcConfig](#v1-replicators-model-kafkaclusterclientvpcconfig) | False | Details of an Amazon VPC which has network connectivity to the Apache Kafka cluster. |

### KafkaClusterClientAuthentication
<a name="v1-replicators-model-kafkaclusterclientauthentication"></a>

Details of the client authentication used by the Apache Kafka cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| saslScram | [KafkaClusterSaslScramAuthentication](#v1-replicators-model-kafkaclustersaslscramauthentication) | True | Details for SASL/SCRAM client authentication. |

### KafkaClusterClientVpcConfig
<a name="v1-replicators-model-kafkaclusterclientvpcconfig"></a>

Details of an Amazon VPC which has network connectivity to the Apache Kafka cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| securityGroupIds | Array of type string | False | The security groups to attach to the ENIs for the broker nodes. |
| subnetIds | Array of type string | True | The list of subnets in the client VPC to connect to. |

### KafkaClusterEncryptionInTransit
<a name="v1-replicators-model-kafkaclusterencryptionintransit"></a>

Details of encryption in transit to the Apache Kafka cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| encryptionType | [KafkaClusterEncryptionInTransitType](#v1-replicators-model-kafkaclusterencryptionintransittype) | True | The type of encryption in transit to the Apache Kafka cluster. |
| rootCaCertificate | string | False | Amazon Resource Name (ARN) of the Secrets Manager secret containing the root CA certificate for TLS encryption. |

### KafkaClusterEncryptionInTransitType
<a name="v1-replicators-model-kafkaclusterencryptionintransittype"></a>

The type of encryption in transit to the Apache Kafka cluster.
+ `TLS`

### KafkaClusterSaslScramAuthentication
<a name="v1-replicators-model-kafkaclustersaslscramauthentication"></a>

Details for SASL/SCRAM client authentication.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| mechanism | [KafkaClusterSaslScramMechanism](#v1-replicators-model-kafkaclustersaslscrammechanism) | True | The SCRAM mechanism to use for authentication. |
| secretArn | string | True | Amazon Resource Name (ARN) of the Secrets Manager secret containing the username and password. |

### KafkaClusterSaslScramMechanism
<a name="v1-replicators-model-kafkaclustersaslscrammechanism"></a>

The SCRAM mechanism to use for authentication.
+ `SHA256`
+ `SHA512`

### KafkaClusterSummary
<a name="v1-replicators-model-kafkaclustersummary"></a>

Summarized information about Kafka Cluster used as source / target for replication.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| amazonMskCluster | [AmazonMskCluster](#v1-replicators-model-amazonmskcluster) | False | Details of an Amazon MSK Cluster. |
| apacheKafkaCluster | [ApacheKafkaCluster](#v1-replicators-model-apachekafkacluster) | False | Details of an Apache Kafka Cluster. |
| kafkaClusterAlias | string | False | The alias of the Kafka cluster. Used to prefix names of replicated topics.  |

### ListReplicatorsResponse
<a name="v1-replicators-model-listreplicatorsresponse"></a>

The response contains an array containing replicator information and a NextToken if the response is truncated.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | string | False | If the response of ListReplicators is truncated, it returns a NextToken in the response. This NextToken should be sent in the subsequent request to ListReplicators. |
| replicators | Array of type [ReplicatorSummary](#v1-replicators-model-replicatorsummary) | False | List containing information of each of the replicators in the account. |

### LogDelivery
<a name="v1-replicators-model-logdelivery"></a>

Configuration for log delivery to customer destinations.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| replicatorLogDelivery | [ReplicatorLogDelivery](#v1-replicators-model-replicatorlogdelivery) | False | Configuration for replicator log delivery. |

### ReplicationInfo
<a name="v1-replicators-model-replicationinfo"></a>

Specifies configuration for replication between a source and target Kafka cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| consumerGroupReplication | [ConsumerGroupReplication](#v1-replicators-model-consumergroupreplication) | True | Configuration relating to consumer group replication. |
| sourceKafkaClusterArn | string | False | The ARN of the source Kafka cluster. |
| sourceKafkaClusterId | string | False | The cluster ID of the source Apache Kafka cluster. Specify either sourceKafkaClusterArn or sourceKafkaClusterId, but not both. |
| targetCompressionType | [TargetCompressionType](#v1-replicators-model-targetcompressiontype) | True | The compression type to use when producing records to target cluster. |
| targetKafkaClusterArn | string | False | The ARN of the target Kafka cluster. |
| targetKafkaClusterId | string | False | The cluster ID of the target Apache Kafka cluster. Specify either targetKafkaClusterArn or targetKafkaClusterId, but not both. |
| topicReplication | [TopicReplication](#v1-replicators-model-topicreplication) | True | Configuration relating to topic replication. |

### ReplicationInfoSummary
<a name="v1-replicators-model-replicationinfosummary"></a>

Summarized information of replication between clusters.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| sourceKafkaClusterAlias | string | False | The alias of the source Kafka cluster. |
| targetKafkaClusterAlias | string | False | The alias of the target Kafka cluster. |

### ReplicationStartingPosition
<a name="v1-replicators-model-replicationstartingposition"></a>

Specifies the position in the topics to start replicating from.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| type | [ReplicationStartingPositionType](#v1-replicators-model-replicationstartingpositiontype) | False | The type of replication starting position. |

### ReplicationStartingPositionType
<a name="v1-replicators-model-replicationstartingpositiontype"></a>

The type of replication starting position.
+ `LATEST`
+ `EARLIEST`

### ReplicationTopicNameConfiguration
<a name="v1-replicators-model-replicationtopicnameconfiguration"></a>

Configuration for specifying replicated topic names will be the same as their corresponding upstream topics or prefixed with source cluster alias.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| type | [ReplicationTopicNameConfigurationType](#v1-replicators-model-replicationtopicnameconfigurationtype) | False | The type of replication topic name configuration, identical to upstream topic name or prefixed with source cluster alias. |

### ReplicationTopicNameConfigurationType
<a name="v1-replicators-model-replicationtopicnameconfigurationtype"></a>

The type of replication topic name configuration, identical to upstream topic name or prefixed with source cluster alias.
+ `IDENTICAL`
+ `PREFIXED_WITH_SOURCE_CLUSTER_ALIAS`

### ReplicatorLogDelivery
<a name="v1-replicators-model-replicatorlogdelivery"></a>

Configuration for replicator log delivery.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cloudWatchLogs | [CloudWatchLogs](#v1-replicators-model-cloudwatchlogs) | False | Configuration for CloudWatch Logs delivery. |
| firehose | [Firehose](#v1-replicators-model-firehose) | False | Configuration for Firehose delivery. |
| s3 | [S3](#v1-replicators-model-s3) | False | Configuration for S3 delivery. |

### ReplicatorState
<a name="v1-replicators-model-replicatorstate"></a>

State of a replicator.
+ `RUNNING`
+ `CREATING`
+ `UPDATING`
+ `DELETING`
+ `FAILED`

### ReplicatorSummary
<a name="v1-replicators-model-replicatorsummary"></a>

Information about a replicator.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| creationTime | string | False | The time the replicator was created. |
| currentVersion | string | False | The current version of the replicator. |
| isReplicatorReference | boolean | False | Whether this resource is a replicator reference. |
| kafkaClustersSummary | Array of type [KafkaClusterSummary](#v1-replicators-model-kafkaclustersummary) | False | Kafka Clusters used in setting up sources / targets for replication. |
| replicationInfoSummaryList | Array of type [ReplicationInfoSummary](#v1-replicators-model-replicationinfosummary) | False | A list of summarized information of replications between clusters. |
| replicatorArn | string | False | The Amazon Resource Name (ARN) of the replicator. |
| replicatorName | string | False | The name of the replicator. |
| replicatorResourceArn | string | False | The Amazon Resource Name (ARN) of the replicator resource in the region where the replicator was created. |
| replicatorState | [ReplicatorState](#v1-replicators-model-replicatorstate) | False | State of the replicator. |

### S3
<a name="v1-replicators-model-s3"></a>

S3 details for ReplicatorLogDelivery.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bucket | string | False | The S3 bucket that is the destination for log delivery. |
| enabled | boolean | True | Whether log delivery to S3 is enabled. |
| prefix | string | False | The S3 prefix that is the destination for log delivery. |

### TargetCompressionType
<a name="v1-replicators-model-targetcompressiontype"></a>

The type of compression to use producing records to the target cluster.
+ `NONE`
+ `GZIP`
+ `SNAPPY`
+ `LZ4`
+ `ZSTD`

### TopicReplication
<a name="v1-replicators-model-topicreplication"></a>

Details about topic replication.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| copyAccessControlListsForTopics | boolean | False | Whether to periodically configure remote topic ACLs to match their corresponding upstream topics. |
| copyTopicConfigurations | boolean | False | Whether to periodically configure remote topics to match their corresponding upstream topics. |
| detectAndCopyNewTopics | boolean | False | Whether to periodically check for new topics and partitions. |
| startingPosition | [ReplicationStartingPosition](#v1-replicators-model-replicationstartingposition) | False | Specifies the position in the topics to start replicating from. |
| topicNameConfiguration | [ReplicationTopicNameConfiguration](#v1-replicators-model-replicationtopicnameconfiguration) | False | Configuration for specifying replicated topic names will be the same as their corresponding upstream topics or prefixed with source cluster alias. |
| topicsToExclude | Array of type string<br />MaxLength: 249 | False | List of regular expression patterns indicating the topics that should not be replicated. |
| topicsToReplicate | Array of type string<br />MaxLength: 249 | True | List of regular expression patterns indicating the topics to copy. |

## See also
<a name="v1-replicators-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListReplicators
<a name="ListReplicators-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/ListReplicators)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/ListReplicators)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/ListReplicators)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/ListReplicators)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/ListReplicators)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/ListReplicators)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/ListReplicators)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/ListReplicators)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/ListReplicators)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/ListReplicators)

### CreateReplicator
<a name="CreateReplicator-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/CreateReplicator)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/CreateReplicator)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/CreateReplicator)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/CreateReplicator)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/CreateReplicator)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/CreateReplicator)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/CreateReplicator)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/CreateReplicator)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/CreateReplicator)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/CreateReplicator)
