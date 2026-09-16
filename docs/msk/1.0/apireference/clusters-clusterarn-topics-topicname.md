---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-topics-topicname.html
---

# Topic
<a name="clusters-clusterarn-topics-topicname"></a>

## URI
<a name="clusters-clusterarn-topics-topicname-url"></a>

`/v1/clusters/{{clusterArn}}/topics/{{topicName}}`

## HTTP methods
<a name="clusters-clusterarn-topics-topicname-http-methods"></a>

### GET
<a name="clusters-clusterarn-topics-topicnameget"></a>

**Operation ID:** `DescribeTopic`

Returns details for a topic on a cluster.

This API response reflects data that updates approximately every minute. For the most current topic state after making changes, allow approximately one minute before querying.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |
| {{topicName}} | String | True | The name of the topic. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  DescribeTopicResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### PUT
<a name="clusters-clusterarn-topics-topicnameput"></a>

**Operation ID:** `UpdateTopic`

Updates topic partition or topic configs.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |
| {{topicName}} | String | True | The name of the topic. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  UpdateTopicResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### DELETE
<a name="clusters-clusterarn-topics-topicnamedelete"></a>

**Operation ID:** `DeleteTopic`

Deletes the topic specified by the topicName in the request from the cluster specified by the Amazon Resource Name (ARN) in the request.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |
| {{topicName}} | String | True | The name of the topic. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  DeleteTopicResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="clusters-clusterarn-topics-topicnameoptions"></a>

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
<a name="clusters-clusterarn-topics-topicname-schemas"></a>

### Request bodies
<a name="clusters-clusterarn-topics-topicname-request-examples"></a>

#### PUT schema
<a name="clusters-clusterarn-topics-topicname-request-body-put-example"></a>

```
{
  "partitionCount": integer,
  "configs": "string",
  "tags": {
  }
}
```

### Response bodies
<a name="clusters-clusterarn-topics-topicname-response-examples"></a>

#### DescribeTopicResponse schema
<a name="clusters-clusterarn-topics-topicname-response-body-describetopicresponse-example"></a>

```
{
  "replicationFactor": number,
  "partitionCount": number,
  "configs": "string",
  "topicName": "string",
  "topicArn": "string",
  "status": enum
}
```

#### UpdateTopicResponse schema
<a name="clusters-clusterarn-topics-topicname-response-body-updatetopicresponse-example"></a>

```
{
  "topicName": "string",
  "topicArn": "string",
  "status": enum
}
```

#### DeleteTopicResponse schema
<a name="clusters-clusterarn-topics-topicname-response-body-deletetopicresponse-example"></a>

```
{
  "topicName": "string",
  "topicArn": "string",
  "status": enum
}
```

#### Error schema
<a name="clusters-clusterarn-topics-topicname-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="clusters-clusterarn-topics-topicname-properties"></a>

### DeleteTopicResponse
<a name="clusters-clusterarn-topics-topicname-model-deletetopicresponse"></a>

Returns information about the deleted topic.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| status | [TopicStatus](#clusters-clusterarn-topics-topicname-model-topicstatus) | False | Status of the topic. |
| topicArn | string | False | ARN of the topic. |
| topicName | string | False | Name of the topic. |

### DescribeTopicResponse
<a name="clusters-clusterarn-topics-topicname-model-describetopicresponse"></a>

The response contains metadata for a topic on a cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| configs | string | False | Kafka configs for a topic. |
| partitionCount | number | False | Partition count for a topic |
| replicationFactor | number | False | Replication factor for a topic |
| status | [TopicStatus](#clusters-clusterarn-topics-topicname-model-topicstatus) | False | Status of the topic.  |
| topicArn | string | False | ARN of the topic. |
| topicName | string | False | Name for a topic. |

### Error
<a name="clusters-clusterarn-topics-topicname-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### TopicStatus
<a name="clusters-clusterarn-topics-topicname-model-topicstatus"></a>

Status of a kafka topic
+ `CREATING`
+ `UPDATING`
+ `DELETING`
+ `ACTIVE`

### UpdateTopicRequest
<a name="clusters-clusterarn-topics-topicname-model-updatetopicrequest"></a>

Request body for UpdateTopic.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| configs | string | False | Base64 encoded kafka configs. |
| partitionCount | integer | False | How many partitions in the topic to be created. |
| tags | object | False | Tags attached to the topic. |

### UpdateTopicResponse
<a name="clusters-clusterarn-topics-topicname-model-updatetopicresponse"></a>

Returns information about the updated topic.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| status | [TopicStatus](#clusters-clusterarn-topics-topicname-model-topicstatus) | False | Status of the topic. |
| topicArn | string | False | ARN of the topic. |
| topicName | string | False | Name of the topic. |

## See also
<a name="clusters-clusterarn-topics-topicname-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DescribeTopic
<a name="DescribeTopic-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/DescribeTopic)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/DescribeTopic)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/DescribeTopic)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/DescribeTopic)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/DescribeTopic)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/DescribeTopic)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/DescribeTopic)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/DescribeTopic)
+ [AWS SDK for Python (Boto3)](/goto/boto3/kafka-2018-11-14/DescribeTopic)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/DescribeTopic)

### UpdateTopic
<a name="UpdateTopic-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/UpdateTopic)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/UpdateTopic)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/UpdateTopic)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/UpdateTopic)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/UpdateTopic)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/UpdateTopic)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/UpdateTopic)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/UpdateTopic)
+ [AWS SDK for Python (Boto3)](/goto/boto3/kafka-2018-11-14/UpdateTopic)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/UpdateTopic)

### DeleteTopic
<a name="DeleteTopic-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/DeleteTopic)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/DeleteTopic)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/DeleteTopic)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/DeleteTopic)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/DeleteTopic)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/DeleteTopic)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/DeleteTopic)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/DeleteTopic)
+ [AWS SDK for Python (Boto3)](/goto/boto3/kafka-2018-11-14/DeleteTopic)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/DeleteTopic)
