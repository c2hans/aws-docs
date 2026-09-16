---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-topics-topicname-partitions.html
---

# Topic Partitions
<a name="clusters-clusterarn-topics-topicname-partitions"></a>

## URI
<a name="clusters-clusterarn-topics-topicname-partitions-url"></a>

`/v1/clusters/{{clusterArn}}/topics/{{topicName}}/partitions`

## HTTP methods
<a name="clusters-clusterarn-topics-topicname-partitions-http-methods"></a>

### GET
<a name="clusters-clusterarn-topics-topicname-partitionsget"></a>

**Operation ID:** `DescribeTopicPartitions`

Returns all partition information for a topic on a cluster.

This API response reflects data that updates approximately every minute. For the most current topic state after making changes, allow approximately one minute before querying.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |
| {{topicName}} | String | True | The name of the topic. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The paginated results marker. When the result of the operation is truncated, the call returns `NextToken` in the response. To get the next batch, provide this token in your next request. |
| maxResults | String | False | The maximum number of results to return in the response (default maximum 100 results per API call). If there are more results, the response includes a `NextToken` parameter. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  DescribeTopicPartitionsResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="clusters-clusterarn-topics-topicname-partitionsoptions"></a>

Enable CORS by returning correct headers

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |
| {{topicName}} | String | True | The name of the topic. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="clusters-clusterarn-topics-topicname-partitions-schemas"></a>

### Response bodies
<a name="clusters-clusterarn-topics-topicname-partitions-response-examples"></a>

#### DescribeTopicPartitionsResponse schema
<a name="clusters-clusterarn-topics-topicname-partitions-response-body-describetopicpartitionsresponse-example"></a>

```
{
  "partitions": [
    {
      "leader": number,
      "partition": number,
      "replicas": [
        number
      ],
      "isr": [
        number
      ]
    }
  ],
  "nextToken": "string"
}
```

#### Error schema
<a name="clusters-clusterarn-topics-topicname-partitions-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="clusters-clusterarn-topics-topicname-partitions-properties"></a>

### DescribeTopicPartitionsResponse
<a name="clusters-clusterarn-topics-topicname-partitions-model-describetopicpartitionsresponse"></a>

The response contains information about partitions for a topic on a cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | string | False | If the response of DescribeTopicPartitions is truncated, it returns a NextToken in the response. This NextToken should be sent in the subsequent request to DescribeTopicPartitions. |
| partitions | Array of type [TopicPartitionInfo](#clusters-clusterarn-topics-topicname-partitions-model-topicpartitioninfo) | False | List containing partition info. |

### Error
<a name="clusters-clusterarn-topics-topicname-partitions-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### TopicPartitionInfo
<a name="clusters-clusterarn-topics-topicname-partitions-model-topicpartitioninfo"></a>

Includes information about a partition.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| isr | Array of type number | False | The list of in-sync replica broker IDs for this partition. |
| leader | number | False | The broker ID of the leader for this partition. |
| partition | number | False | The partition number. |
| replicas | Array of type number | False | The list of broker IDs that are replicas for this partition. |

## See also
<a name="clusters-clusterarn-topics-topicname-partitions-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DescribeTopicPartitions
<a name="DescribeTopicPartitions-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/DescribeTopicPartitions)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/DescribeTopicPartitions)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/DescribeTopicPartitions)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/DescribeTopicPartitions)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/DescribeTopicPartitions)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/DescribeTopicPartitions)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/DescribeTopicPartitions)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/DescribeTopicPartitions)
+ [AWS SDK for Python (Boto3)](/goto/boto3/kafka-2018-11-14/DescribeTopicPartitions)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/DescribeTopicPartitions)
