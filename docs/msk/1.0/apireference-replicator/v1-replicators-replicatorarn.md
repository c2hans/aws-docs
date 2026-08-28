---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference-replicator/v1-replicators-replicatorarn.html
---

# V1 Replicators replicatorArn
<a name="v1-replicators-replicatorarn"></a>

## URI
<a name="v1-replicators-replicatorarn-url"></a>

`/replication/v1/replicators/{{replicatorArn}}`

## HTTP methods
<a name="v1-replicators-replicatorarn-http-methods"></a>

### GET
<a name="v1-replicators-replicatorarnget"></a>

**Operation ID:** `DescribeReplicator`

Describes a replicator.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{replicatorArn}} | String | True | The Amazon Resource Name (ARN) of the replicator to be described. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  DescribeReplicatorResponse | HTTP Status Code 200: OK. |
| 400 | None | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 401 | None | HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated. |
| 403 | None | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 404 | None | HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it. |
| 429 | None | HTTP Status Code 429: Limit exceeded. Resource limit reached. |
| 500 | None | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | None | HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue. |

### DELETE
<a name="v1-replicators-replicatorarndelete"></a>

**Operation ID:** `DeleteReplicator`

Deletes a replicator.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{replicatorArn}} | String | True | The Amazon Resource Name (ARN) of the replicator to be described. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| currentVersion | String | False | The current version of the replicator. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  DeleteReplicatorResponse | HTTP Status Code 200: OK. |
| 400 | None | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 401 | None | HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated. |
| 403 | None | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 404 | None | HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it. |
| 429 | None | HTTP Status Code 429: Limit exceeded. Resource limit reached. |
| 500 | None | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | None | HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue. |

### OPTIONS
<a name="v1-replicators-replicatorarnoptions"></a>

Enable CORS by returning correct headers

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{replicatorArn}} | String | True | The Amazon Resource Name (ARN) of the replicator to be described. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="v1-replicators-replicatorarn-schemas"></a>

### Response bodies
<a name="v1-replicators-replicatorarn-response-examples"></a>

#### DescribeReplicatorResponse schema
<a name="v1-replicators-replicatorarn-response-body-describereplicatorresponse-example"></a>

```
{
  "replicatorArn": "string",
  "creationTime": "string",
  "kafkaClusters": [
    {
      "kafkaClusterAlias": "string",
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
  "currentVersion": "string",
  "tags": {
  },
  "replicatorDescription": "string",
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
      "sourceKafkaClusterAlias": "string",
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
      "targetKafkaClusterAlias": "string"
    }
  ],
  "stateInfo": {
    "code": "string",
    "message": "string"
  },
  "replicatorState": enum,
  "isReplicatorReference": boolean,
  "replicatorResourceArn": "string"
}
```

#### DeleteReplicatorResponse schema
<a name="v1-replicators-replicatorarn-response-body-deletereplicatorresponse-example"></a>

```
{
  "replicatorArn": "string",
  "replicatorState": enum
}
```

## Properties
<a name="v1-replicators-replicatorarn-properties"></a>

### AmazonMskCluster
<a name="v1-replicators-replicatorarn-model-amazonmskcluster"></a>

Details of an Amazon MSK Cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| mskClusterArn | string | True | The Amazon Resource Name (ARN) of an Amazon MSK cluster. |

### ApacheKafkaCluster
<a name="v1-replicators-replicatorarn-model-apachekafkacluster"></a>

Details of an Apache Kafka cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| apacheKafkaClusterId | string | True | The globally unique cluster ID of the Apache Kafka cluster. For information on how to retrieve the cluster ID, see https://github.com/apache/kafka/blob/trunk/bin/kafka-cluster.sh |
| bootstrapBrokerString | string | True | The bootstrap broker string of the Apache Kafka cluster. |

### CloudWatchLogs
<a name="v1-replicators-replicatorarn-model-cloudwatchlogs"></a>

CloudWatch Logs details for ReplicatorLogDelivery.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | True | Whether log delivery to CloudWatch Logs is enabled. |
| logGroup | string | False | The CloudWatch log group that is the destination for log delivery. |

### ConsumerGroupOffsetSyncMode
<a name="v1-replicators-replicatorarn-model-consumergroupoffsetsyncmode"></a>

The consumer group offset synchronization mode. With LEGACY, offsets are synchronized when producers write to the source cluster. With ENHANCED, consumer offsets are synchronized regardless of producer location. ENHANCED requires a corresponding replicator that replicates data from the target cluster to the source cluster.
+ `LEGACY`
+ `ENHANCED`

### ConsumerGroupReplication
<a name="v1-replicators-replicatorarn-model-consumergroupreplication"></a>

Details about consumer group replication.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| consumerGroupOffsetSyncMode | [ConsumerGroupOffsetSyncMode](#v1-replicators-replicatorarn-model-consumergroupoffsetsyncmode) | False | The consumer group offset synchronization mode. With LEGACY, offsets are synchronized when producers write to the source cluster. With ENHANCED, consumer offsets are synchronized regardless of producer location. ENHANCED requires a corresponding replicator that replicates data from the target cluster to the source cluster. |
| consumerGroupsToExclude | Array of type string<br />MaxLength: 256 | False | List of regular expression patterns indicating the consumer groups that should not be replicated. |
| consumerGroupsToReplicate | Array of type string<br />MaxLength: 256 | True | List of regular expression patterns indicating the consumer groups to copy. |
| detectAndCopyNewConsumerGroups | boolean | False | Enables synchronization of consumer groups to target cluster. |
| synchroniseConsumerGroupOffsets | boolean | False | Enables synchronization of consumer group offsets to target cluster. The translated offsets will be written to topic \_\_consumer\_offsets. |

### DeleteReplicatorResponse
<a name="v1-replicators-replicatorarn-model-deletereplicatorresponse"></a>

Returns information about the deleted replicator.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| replicatorArn | string | False | The Amazon Resource Name (ARN) of the replicator. |
| replicatorState | [ReplicatorState](#v1-replicators-replicatorarn-model-replicatorstate) | False | State of the replicator. |

### DescribeReplicatorResponse
<a name="v1-replicators-replicatorarn-model-describereplicatorresponse"></a>

Response body for DescribeReplicator.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| creationTime | string | False | The time when the replicator was created. |
| currentVersion | string | False | The current version number of the replicator. |
| isReplicatorReference | boolean | False | Whether this resource is a replicator reference. |
| kafkaClusters | Array of type [KafkaClusterDescription](#v1-replicators-replicatorarn-model-kafkaclusterdescription) | False | Kafka Clusters used in setting up sources / targets for replication. |
| logDelivery | [LogDelivery](#v1-replicators-replicatorarn-model-logdelivery) | False | Configuration for log delivery. |
| replicationInfoList | Array of type [ReplicationInfoDescription](#v1-replicators-replicatorarn-model-replicationinfodescription) | False | A list of replication configurations, where each configuration targets a given source cluster to target cluster replication flow. |
| replicatorArn | string | False | The Amazon Resource Name (ARN) of the replicator. |
| replicatorDescription | string | False | The description of the replicator. |
| replicatorName | string | False | The name of the replicator. |
| replicatorResourceArn | string | False | The Amazon Resource Name (ARN) of the replicator resource in the region where the replicator was created. |
| replicatorState | [ReplicatorState](#v1-replicators-replicatorarn-model-replicatorstate) | False | State of the replicator. |
| serviceExecutionRoleArn | string | False | The Amazon Resource Name (ARN) of the IAM role used by the replicator to access resources in the customer's account (e.g source and target clusters) |
| stateInfo | [ReplicationStateInfo](#v1-replicators-replicatorarn-model-replicationstateinfo) | False | Details about the state of the replicator. |
| tags | object | False | List of tags attached to the Replicator. |

### Firehose
<a name="v1-replicators-replicatorarn-model-firehose"></a>

Firehose details for ReplicatorLogDelivery.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| deliveryStream | string | False | The Firehose delivery stream that is the destination for log delivery. |
| enabled | boolean | True | Whether log delivery to Firehose is enabled. |

### KafkaClusterClientAuthentication
<a name="v1-replicators-replicatorarn-model-kafkaclusterclientauthentication"></a>

Details of the client authentication used by the Apache Kafka cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| saslScram | [KafkaClusterSaslScramAuthentication](#v1-replicators-replicatorarn-model-kafkaclustersaslscramauthentication) | True | Details for SASL/SCRAM client authentication. |

### KafkaClusterClientVpcConfig
<a name="v1-replicators-replicatorarn-model-kafkaclusterclientvpcconfig"></a>

Details of an Amazon VPC which has network connectivity to the Apache Kafka cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| securityGroupIds | Array of type string | False | The security groups to attach to the ENIs for the broker nodes. |
| subnetIds | Array of type string | True | The list of subnets in the client VPC to connect to. |

### KafkaClusterDescription
<a name="v1-replicators-replicatorarn-model-kafkaclusterdescription"></a>

Information about Kafka Cluster used as source / target for replication.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| amazonMskCluster | [AmazonMskCluster](#v1-replicators-replicatorarn-model-amazonmskcluster) | False | Details of an Amazon MSK Cluster. |
| apacheKafkaCluster | [ApacheKafkaCluster](#v1-replicators-replicatorarn-model-apachekafkacluster) | False | Details of an Apache Kafka Cluster. |
| clientAuthentication | [KafkaClusterClientAuthentication](#v1-replicators-replicatorarn-model-kafkaclusterclientauthentication) | False | Details of the client authentication used by the Apache Kafka cluster. |
| encryptionInTransit | [KafkaClusterEncryptionInTransit](#v1-replicators-replicatorarn-model-kafkaclusterencryptionintransit) | False | Details of encryption in transit to the Apache Kafka cluster. |
| kafkaClusterAlias | string | False | The alias of the Kafka cluster. Used to prefix names of replicated topics.  |
| vpcConfig | [KafkaClusterClientVpcConfig](#v1-replicators-replicatorarn-model-kafkaclusterclientvpcconfig) | False | Details of an Amazon VPC which has network connectivity to the Apache Kafka cluster. |

### KafkaClusterEncryptionInTransit
<a name="v1-replicators-replicatorarn-model-kafkaclusterencryptionintransit"></a>

Details of encryption in transit to the Apache Kafka cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| encryptionType | [KafkaClusterEncryptionInTransitType](#v1-replicators-replicatorarn-model-kafkaclusterencryptionintransittype) | True | The type of encryption in transit to the Apache Kafka cluster. |
| rootCaCertificate | string | False | Amazon Resource Name (ARN) of the Secrets Manager secret containing the root CA certificate for TLS encryption. |

### KafkaClusterEncryptionInTransitType
<a name="v1-replicators-replicatorarn-model-kafkaclusterencryptionintransittype"></a>

The type of encryption in transit to the Apache Kafka cluster.
+ `TLS`

### KafkaClusterSaslScramAuthentication
<a name="v1-replicators-replicatorarn-model-kafkaclustersaslscramauthentication"></a>

Details for SASL/SCRAM client authentication.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| mechanism | [KafkaClusterSaslScramMechanism](#v1-replicators-replicatorarn-model-kafkaclustersaslscrammechanism) | True | The SCRAM mechanism to use for authentication. |
| secretArn | string | True | Amazon Resource Name (ARN) of the Secrets Manager secret containing the username and password. |

### KafkaClusterSaslScramMechanism
<a name="v1-replicators-replicatorarn-model-kafkaclustersaslscrammechanism"></a>

The SCRAM mechanism to use for authentication.
+ `SHA256`
+ `SHA512`

### LogDelivery
<a name="v1-replicators-replicatorarn-model-logdelivery"></a>

Configuration for log delivery to customer destinations.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| replicatorLogDelivery | [ReplicatorLogDelivery](#v1-replicators-replicatorarn-model-replicatorlogdelivery) | False | Configuration for replicator log delivery. |

### ReplicationInfoDescription
<a name="v1-replicators-replicatorarn-model-replicationinfodescription"></a>

Specifies configuration for replication between a source and target Kafka cluster (sourceKafkaClusterAlias -> targetKafkaClusterAlias)

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| consumerGroupReplication | [ConsumerGroupReplication](#v1-replicators-replicatorarn-model-consumergroupreplication) | False | Configuration relating to consumer group replication. |
| sourceKafkaClusterAlias | string | False | The alias of the source Kafka cluster. |
| targetCompressionType | [TargetCompressionType](#v1-replicators-replicatorarn-model-targetcompressiontype) | False | The compression type to use when producing records to target cluster. |
| targetKafkaClusterAlias | string | False | The alias of the target Kafka cluster. |
| topicReplication | [TopicReplication](#v1-replicators-replicatorarn-model-topicreplication) | False | Configuration relating to topic replication. |

### ReplicationStartingPosition
<a name="v1-replicators-replicatorarn-model-replicationstartingposition"></a>

Specifies the position in the topics to start replicating from.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| type | [ReplicationStartingPositionType](#v1-replicators-replicatorarn-model-replicationstartingpositiontype) | False | The type of replication starting position. |

### ReplicationStartingPositionType
<a name="v1-replicators-replicatorarn-model-replicationstartingpositiontype"></a>

The type of replication starting position.
+ `LATEST`
+ `EARLIEST`

### ReplicationStateInfo
<a name="v1-replicators-replicatorarn-model-replicationstateinfo"></a>

Details about the state of a replicator.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| code | string | False | Code that describes the state of the replicator. |
| message | string | False | Message that describes the state of the replicator. |

### ReplicationTopicNameConfiguration
<a name="v1-replicators-replicatorarn-model-replicationtopicnameconfiguration"></a>

Configuration for specifying replicated topic names will be the same as their corresponding upstream topics or prefixed with source cluster alias.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| type | [ReplicationTopicNameConfigurationType](#v1-replicators-replicatorarn-model-replicationtopicnameconfigurationtype) | False | The type of replication topic name configuration, identical to upstream topic name or prefixed with source cluster alias. |

### ReplicationTopicNameConfigurationType
<a name="v1-replicators-replicatorarn-model-replicationtopicnameconfigurationtype"></a>

The type of replication topic name configuration, identical to upstream topic name or prefixed with source cluster alias.
+ `IDENTICAL`
+ `PREFIXED_WITH_SOURCE_CLUSTER_ALIAS`

### ReplicatorLogDelivery
<a name="v1-replicators-replicatorarn-model-replicatorlogdelivery"></a>

Configuration for replicator log delivery.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cloudWatchLogs | [CloudWatchLogs](#v1-replicators-replicatorarn-model-cloudwatchlogs) | False | Configuration for CloudWatch Logs delivery. |
| firehose | [Firehose](#v1-replicators-replicatorarn-model-firehose) | False | Configuration for Firehose delivery. |
| s3 | [S3](#v1-replicators-replicatorarn-model-s3) | False | Configuration for S3 delivery. |

### ReplicatorState
<a name="v1-replicators-replicatorarn-model-replicatorstate"></a>

State of a replicator.
+ `RUNNING`
+ `CREATING`
+ `UPDATING`
+ `DELETING`
+ `FAILED`

### S3
<a name="v1-replicators-replicatorarn-model-s3"></a>

S3 details for ReplicatorLogDelivery.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bucket | string | False | The S3 bucket that is the destination for log delivery. |
| enabled | boolean | True | Whether log delivery to S3 is enabled. |
| prefix | string | False | The S3 prefix that is the destination for log delivery. |

### TargetCompressionType
<a name="v1-replicators-replicatorarn-model-targetcompressiontype"></a>

The type of compression to use producing records to the target cluster.
+ `NONE`
+ `GZIP`
+ `SNAPPY`
+ `LZ4`
+ `ZSTD`

### TopicReplication
<a name="v1-replicators-replicatorarn-model-topicreplication"></a>

Details about topic replication.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| copyAccessControlListsForTopics | boolean | False | Whether to periodically configure remote topic ACLs to match their corresponding upstream topics. |
| copyTopicConfigurations | boolean | False | Whether to periodically configure remote topics to match their corresponding upstream topics. |
| detectAndCopyNewTopics | boolean | False | Whether to periodically check for new topics and partitions. |
| startingPosition | [ReplicationStartingPosition](#v1-replicators-replicatorarn-model-replicationstartingposition) | False | Specifies the position in the topics to start replicating from. |
| topicNameConfiguration | [ReplicationTopicNameConfiguration](#v1-replicators-replicatorarn-model-replicationtopicnameconfiguration) | False | Configuration for specifying replicated topic names will be the same as their corresponding upstream topics or prefixed with source cluster alias. |
| topicsToExclude | Array of type string<br />MaxLength: 249 | False | List of regular expression patterns indicating the topics that should not be replicated. |
| topicsToReplicate | Array of type string<br />MaxLength: 249 | True | List of regular expression patterns indicating the topics to copy. |

## See also
<a name="v1-replicators-replicatorarn-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DescribeReplicator
<a name="DescribeReplicator-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/DescribeReplicator)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/DescribeReplicator)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/DescribeReplicator)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/DescribeReplicator)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/DescribeReplicator)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/DescribeReplicator)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/DescribeReplicator)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/DescribeReplicator)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/DescribeReplicator)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/DescribeReplicator)

### DeleteReplicator
<a name="DeleteReplicator-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/DeleteReplicator)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/DeleteReplicator)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/DeleteReplicator)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/DeleteReplicator)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/DeleteReplicator)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/DeleteReplicator)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/DeleteReplicator)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/DeleteReplicator)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/DeleteReplicator)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/DeleteReplicator)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
