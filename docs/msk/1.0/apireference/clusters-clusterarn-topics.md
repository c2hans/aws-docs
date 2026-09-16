---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-topics.html
---

# Topics
<a name="clusters-clusterarn-topics"></a>

## URI
<a name="clusters-clusterarn-topics-url"></a>

`/v1/clusters/{{clusterArn}}/topics`

## HTTP methods
<a name="clusters-clusterarn-topics-http-methods"></a>

### GET
<a name="clusters-clusterarn-topicsget"></a>

**Operation ID:** `ListTopics`

Returns all topics in a cluster.

This API response reflects data that updates approximately every minute. For the most current topic state after making changes, allow approximately one minute before querying.

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
| 200 |  ListTopicsResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### POST
<a name="clusters-clusterarn-topicspost"></a>

**Operation ID:** `CreateTopic`

Creates a topic using the specified properties in the request on the cluster specified by the Amazon Resource Name (ARN) in the request.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  CreateTopicResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 409 | Error | This cluster name already exists. Retry your request using another name. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="clusters-clusterarn-topicsoptions"></a>

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
<a name="clusters-clusterarn-topics-schemas"></a>

### Request bodies
<a name="clusters-clusterarn-topics-request-examples"></a>

#### POST schema
<a name="clusters-clusterarn-topics-request-body-post-example"></a>

```
{
  "partitionCount": integer,
  "configs": "string",
  "replicationFactor": integer,
  "topicName": "string",
  "tags": {
  }
}
```

### Response bodies
<a name="clusters-clusterarn-topics-response-examples"></a>

#### ListTopicsResponse schema
<a name="clusters-clusterarn-topics-response-body-listtopicsresponse-example"></a>

```
{
  "topics": [
    {
      "partitionCount": number,
      "replicationFactor": number,
      "topicName": "string",
      "topicArn": "string",
      "outOfSyncReplicaCount": number
    }
  ],
  "nextToken": "string"
}
```

#### CreateTopicResponse schema
<a name="clusters-clusterarn-topics-response-body-createtopicresponse-example"></a>

```
{
  "topicName": "string",
  "topicArn": "string",
  "status": enum
}
```

#### Error schema
<a name="clusters-clusterarn-topics-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="clusters-clusterarn-topics-properties"></a>

### CreateTopicRequest
<a name="clusters-clusterarn-topics-model-createtopicrequest"></a>

Request body for CreateTopic.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| configs | string | False | Base64 encoded Kafka configs. |
| partitionCount | integer | True | How many partitions in the topic to be created. |
| replicationFactor | integer | True | The replication factor of the topic. |
| tags | object | False | Tags attached to the topic. |
| topicName | string | True | Name of the topic. |

### CreateTopicResponse
<a name="clusters-clusterarn-topics-model-createtopicresponse"></a>

Returns information about the created topic.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| status | [TopicStatus](#clusters-clusterarn-topics-model-topicstatus) | False | Status of the topic. |
| topicArn | string | False | ARN of the topic. |
| topicName | string | False | Name of the topic. |

### Error
<a name="clusters-clusterarn-topics-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### ListTopicsResponse
<a name="clusters-clusterarn-topics-model-listtopicsresponse"></a>

The response contains an array of topics in a cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | string | False | If the response of ListTopics is truncated, it returns a NextToken in the response. This NextToken should be sent in the subsequent request to ListTopics. |
| topics | Array of type [TopicInfo](#clusters-clusterarn-topics-model-topicinfo) | False | List containing topics info. |

### TopicInfo
<a name="clusters-clusterarn-topics-model-topicinfo"></a>

Includes identification info about the topic.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| outOfSyncReplicaCount | number | False | Number of out of sync replica for topic |
| partitionCount | number | False | Partition count for a topic |
| replicationFactor | number | False | Replication factor for a topic |
| topicArn | string | False | ARN of the topic. |
| topicName | string | False | Name for a topic. |

### TopicStatus
<a name="clusters-clusterarn-topics-model-topicstatus"></a>

Status of a kafka topic
+ `CREATING`
+ `UPDATING`
+ `DELETING`
+ `ACTIVE`

## See also
<a name="clusters-clusterarn-topics-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListTopics
<a name="ListTopics-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/ListTopics)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/ListTopics)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/ListTopics)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/ListTopics)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/ListTopics)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/ListTopics)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/ListTopics)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/ListTopics)
+ [AWS SDK for Python (Boto3)](/goto/boto3/kafka-2018-11-14/ListTopics)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/ListTopics)

### CreateTopic
<a name="CreateTopic-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/CreateTopic)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/CreateTopic)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/CreateTopic)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/CreateTopic)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/CreateTopic)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/CreateTopic)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/CreateTopic)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/CreateTopic)
+ [AWS SDK for Python (Boto3)](/goto/boto3/kafka-2018-11-14/CreateTopic)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/CreateTopic)
