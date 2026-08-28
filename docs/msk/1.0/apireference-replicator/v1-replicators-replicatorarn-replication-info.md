---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference-replicator/v1-replicators-replicatorarn-replication-info.html
---

# V1 Replicators replicatorArn Replication-info
<a name="v1-replicators-replicatorarn-replication-info"></a>

## URI
<a name="v1-replicators-replicatorarn-replication-info-url"></a>

`/replication/v1/replicators/{{replicatorArn}}/replication-info`

## HTTP methods
<a name="v1-replicators-replicatorarn-replication-info-http-methods"></a>

### PUT
<a name="v1-replicators-replicatorarn-replication-infoput"></a>

**Operation ID:** `UpdateReplicationInfo`

Updates replication info of a replicator.

Note: `logDelivery` cannot be updated in the same request as `topicReplication` or `consumerGroupReplication`. Update either `logDelivery` or `topicReplication` and `consumerGroupReplication` in separate requests.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{replicatorArn}} | String | True | The Amazon Resource Name (ARN) of the replicator to be described. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  UpdateReplicationInfoResponse | HTTP Status Code 200: OK. |
| 400 | None | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 401 | None | HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated. |
| 403 | None | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 404 | None | HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it. |
| 429 | None | HTTP Status Code 429: Limit exceeded. Resource limit reached. |
| 500 | None | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | None | HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue. |

### OPTIONS
<a name="v1-replicators-replicatorarn-replication-infooptions"></a>

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
<a name="v1-replicators-replicatorarn-replication-info-schemas"></a>

### Request bodies
<a name="v1-replicators-replicatorarn-replication-info-request-examples"></a>

#### PUT schema
<a name="v1-replicators-replicatorarn-replication-info-request-body-put-example"></a>

```
{
  "consumerGroupReplication": {
    "consumerGroupsToExclude": [
      "string"
    ],
    "detectAndCopyNewConsumerGroups": boolean,
    "consumerGroupsToReplicate": [
      "string"
    ],
    "synchroniseConsumerGroupOffsets": boolean
  },
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
  "topicReplication": {
    "copyAccessControlListsForTopics": boolean,
    "detectAndCopyNewTopics": boolean,
    "copyTopicConfigurations": boolean,
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
  "targetKafkaClusterId": "string",
  "currentVersion": "string"
}
```

### Response bodies
<a name="v1-replicators-replicatorarn-replication-info-response-examples"></a>

#### UpdateReplicationInfoResponse schema
<a name="v1-replicators-replicatorarn-replication-info-response-body-updatereplicationinforesponse-example"></a>

```
{
  "replicatorArn": "string",
  "replicatorState": enum
}
```

## Properties
<a name="v1-replicators-replicatorarn-replication-info-properties"></a>

### CloudWatchLogs
<a name="v1-replicators-replicatorarn-replication-info-model-cloudwatchlogs"></a>

CloudWatch Logs details for ReplicatorLogDelivery.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | True | Whether log delivery to CloudWatch Logs is enabled. |
| logGroup | string | False | The CloudWatch log group that is the destination for log delivery. |

### ConsumerGroupReplicationUpdate
<a name="v1-replicators-replicatorarn-replication-info-model-consumergroupreplicationupdate"></a>

Details about consumer group replication.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| consumerGroupsToExclude | Array of type string<br />MaxLength: 256 | True | List of regular expression patterns indicating the consumer groups that should not be replicated. |
| consumerGroupsToReplicate | Array of type string<br />MaxLength: 256 | True | List of regular expression patterns indicating the consumer groups to copy. |
| detectAndCopyNewConsumerGroups | boolean | True | Enables synchronization of consumer groups to target cluster. |
| synchroniseConsumerGroupOffsets | boolean | True | Enables synchronization of consumer group offsets to target cluster. The translated offsets will be written to topic \_\_consumer\_offsets. |

### Firehose
<a name="v1-replicators-replicatorarn-replication-info-model-firehose"></a>

Firehose details for ReplicatorLogDelivery.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| deliveryStream | string | False | The Firehose delivery stream that is the destination for log delivery. |
| enabled | boolean | True | Whether log delivery to Firehose is enabled. |

### LogDelivery
<a name="v1-replicators-replicatorarn-replication-info-model-logdelivery"></a>

Configuration for log delivery to customer destinations.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| replicatorLogDelivery | [ReplicatorLogDelivery](#v1-replicators-replicatorarn-replication-info-model-replicatorlogdelivery) | False | Configuration for replicator log delivery. |

### ReplicatorLogDelivery
<a name="v1-replicators-replicatorarn-replication-info-model-replicatorlogdelivery"></a>

Configuration for replicator log delivery.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cloudWatchLogs | [CloudWatchLogs](#v1-replicators-replicatorarn-replication-info-model-cloudwatchlogs) | False | Configuration for CloudWatch Logs delivery. |
| firehose | [Firehose](#v1-replicators-replicatorarn-replication-info-model-firehose) | False | Configuration for Firehose delivery. |
| s3 | [S3](#v1-replicators-replicatorarn-replication-info-model-s3) | False | Configuration for S3 delivery. |

### ReplicatorState
<a name="v1-replicators-replicatorarn-replication-info-model-replicatorstate"></a>

State of a replicator.
+ `RUNNING`
+ `CREATING`
+ `UPDATING`
+ `DELETING`
+ `FAILED`

### S3
<a name="v1-replicators-replicatorarn-replication-info-model-s3"></a>

S3 details for ReplicatorLogDelivery.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bucket | string | False | The S3 bucket that is the destination for log delivery. |
| enabled | boolean | True | Whether log delivery to S3 is enabled. |
| prefix | string | False | The S3 prefix that is the destination for log delivery. |

### TopicReplicationUpdate
<a name="v1-replicators-replicatorarn-replication-info-model-topicreplicationupdate"></a>

Details for updating the topic replication of a replicator.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| copyAccessControlListsForTopics | boolean | True | Whether to periodically configure remote topic ACLs to match their corresponding upstream topics. |
| copyTopicConfigurations | boolean | True | Whether to periodically configure remote topics to match their corresponding upstream topics. |
| detectAndCopyNewTopics | boolean | True | Whether to periodically check for new topics and partitions. |
| topicsToExclude | Array of type string<br />MaxLength: 249 | True | List of regular expression patterns indicating the topics that should not be replicated. |
| topicsToReplicate | Array of type string<br />MaxLength: 249 | True | List of regular expression patterns indicating the topics to copy. |

### UpdateReplicationInfoRequest
<a name="v1-replicators-replicatorarn-replication-info-model-updatereplicationinforequest"></a>

Parameters for updating replication information between source and target Kafka clusters of a replicator.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| consumerGroupReplication | [ConsumerGroupReplicationUpdate](#v1-replicators-replicatorarn-replication-info-model-consumergroupreplicationupdate) | False | Updated consumer group replication information. |
| currentVersion | string | True | Current replicator version. |
| logDelivery | [LogDelivery](#v1-replicators-replicatorarn-replication-info-model-logdelivery) | False | Configuration for delivering replicator logs to customer destinations. |
| sourceKafkaClusterArn | string | False | The ARN of the source Kafka cluster. |
| sourceKafkaClusterId | string | False | The cluster ID of the source Apache Kafka cluster. |
| targetKafkaClusterArn | string | False | The ARN of the target Kafka cluster. |
| targetKafkaClusterId | string | False | The cluster ID of the target Apache Kafka cluster. |
| topicReplication | [TopicReplicationUpdate](#v1-replicators-replicatorarn-replication-info-model-topicreplicationupdate) | False | Updated topic replication information. |

### UpdateReplicationInfoResponse
<a name="v1-replicators-replicatorarn-replication-info-model-updatereplicationinforesponse"></a>

Updated Replication information of a replicator.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| replicatorArn | string | False | The Amazon Resource Name (ARN) of the replicator. |
| replicatorState | [ReplicatorState](#v1-replicators-replicatorarn-replication-info-model-replicatorstate) | False | State of the replicator. |

## See also
<a name="v1-replicators-replicatorarn-replication-info-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### UpdateReplicationInfo
<a name="UpdateReplicationInfo-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/UpdateReplicationInfo)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/UpdateReplicationInfo)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/UpdateReplicationInfo)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/UpdateReplicationInfo)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/UpdateReplicationInfo)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/UpdateReplicationInfo)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/UpdateReplicationInfo)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/UpdateReplicationInfo)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/UpdateReplicationInfo)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/UpdateReplicationInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
