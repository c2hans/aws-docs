---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-topic-reassignments-topicreassignmentoperationarn.html
---

# Topic Reassignment

## URI
<a name="clusters-clusterarn-topic-reassignments-topicreassignmentoperationarn-url"></a>

`/v1/clusters/{{clusterArn}}/topic-reassignments/{{topicReassignmentOperationArn}}`

## HTTP methods
<a name="clusters-clusterarn-topic-reassignments-topicreassignmentoperationarn-http-methods"></a>

### GET
<a name="clusters-clusterarn-topic-reassignments-topicreassignmentoperationarnget"></a>

**Operation ID:** `DescribeTopicReassignment`

Returns the progress of a topic reassignment. The partition counters (`migratedPartitions` against `totalPartitions`) advance continuously and are the most responsive signal that a long-running reassignment is making progress; the topic counters (`completedTopics` against `totalTopics`) advance only as whole topics finish.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |
| {{topicReassignmentOperationArn}} | String | True | The Amazon Resource Name (ARN) of the topic reassignment operation. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | DescribeTopicReassignmentResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="clusters-clusterarn-topic-reassignments-topicreassignmentoperationarnoptions"></a>

Enable CORS by returning correct headers

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |
| {{topicReassignmentOperationArn}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="clusters-clusterarn-topic-reassignments-topicreassignmentoperationarn-schemas"></a>

### Response bodies
<a name="clusters-clusterarn-topic-reassignments-topicreassignmentoperationarn-response-examples"></a>

#### DescribeTopicReassignmentResponse schema
<a name="clusters-clusterarn-topic-reassignments-topicreassignmentoperationarn-response-body-describetopicreassignmentresponse-example"></a>

```json
{
  "topicReassignmentOperationArn": "string",
  "clusterArn": "string",
  "targetInstanceType": "string",
  "topicsToInclude": [
    "string"
  ],
  "topicsToExclude": [
    "string"
  ],
  "status": enum,
  "totalTopics": integer,
  "completedTopics": integer,
  "totalPartitions": integer,
  "migratedPartitions": integer,
  "errorInfo": {
    "errorString": "string",
    "errorCode": "string"
  },
  "creationTime": "string",
  "lastUpdateTime": "string"
}
```

#### Error schema
<a name="clusters-clusterarn-topic-reassignments-topicreassignmentoperationarn-response-body-error-example"></a>

```json
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="clusters-clusterarn-topic-reassignments-topicreassignmentoperationarn-properties"></a>

### DescribeTopicReassignmentResponse
<a name="clusters-clusterarn-topic-reassignments-topicreassignmentoperationarn-model-describetopicreassignmentresponse"></a>

Returns the status and progress of a topic reassignment operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clusterArn | string<br />MaxLength: 2048 | False | The Amazon Resource Name (ARN) of the cluster. |
| completedTopics | integer | False | Number of topics fully migrated to the target broker type. |
| creationTime | string | False | When the operation was created. |
| errorInfo | [ErrorInfo](#clusters-clusterarn-topic-reassignments-topicreassignmentoperationarn-model-errorinfo) | False | Error details. Present only when status is FAILED. |
| lastUpdateTime | string | False | Last time the status or progress counters were updated. |
| migratedPartitions | integer | False | Number of partitions confirmed on the target broker type. |
| status | [TopicReassignmentStatus](#clusters-clusterarn-topic-reassignments-topicreassignmentoperationarn-model-topicreassignmentstatus) | False | The current status of the reassignment operation. |
| targetInstanceType | string | False | The target broker instance type for this reassignment. |
| topicReassignmentOperationArn | string<br />MaxLength: 2048 | False | The Amazon Resource Name (ARN) of the topic reassignment operation. |
| topicsToExclude | Array of type string | False | The original exclude patterns provided in the request. |
| topicsToInclude | Array of type string | False | The original include patterns provided in the request. |
| totalPartitions | integer | False | Total number of partitions across all matched topics. |
| totalTopics | integer | False | Total number of topics matching the selector at resolution time. |

### Error
<a name="clusters-clusterarn-topic-reassignments-topicreassignmentoperationarn-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### ErrorInfo
<a name="clusters-clusterarn-topic-reassignments-topicreassignmentoperationarn-model-errorinfo"></a>

Returns information about an error state of the cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| errorCode | string | False | A number describing the error programmatically. |
| errorString | string | False | An optional field to provide more details about the error. |

### TopicReassignmentStatus
<a name="clusters-clusterarn-topic-reassignments-topicreassignmentoperationarn-model-topicreassignmentstatus"></a>

The lifecycle status of a topic reassignment. A reassignment that is `PENDING` has been recorded but has not started moving partitions yet, and one that is `IN_PROGRESS` is moving them. `STOPPING` means that `StopTopicReassignment` was called and the in-flight partitions are reverting. A reassignment is `COMPLETE` when every selected topic is on the target broker type, `STOPPED` when it stopped at your request, in which case the partitions that had already moved remain on the target broker type, and `FAILED` when it stopped on an error that `errorInfo` explains.
+ `PENDING`
+ `IN_PROGRESS`
+ `STOPPING`
+ `COMPLETE`
+ `FAILED`
+ `STOPPED`

## See also
<a name="clusters-clusterarn-topic-reassignments-topicreassignmentoperationarn-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DescribeTopicReassignment
<a name="DescribeTopicReassignment-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/DescribeTopicReassignment)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/DescribeTopicReassignment)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/DescribeTopicReassignment)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/DescribeTopicReassignment)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/DescribeTopicReassignment)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/DescribeTopicReassignment)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/DescribeTopicReassignment)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/DescribeTopicReassignment)
+ [AWS SDK for Python (Boto3)](/goto/boto3/kafka-2018-11-14/DescribeTopicReassignment)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/DescribeTopicReassignment)
