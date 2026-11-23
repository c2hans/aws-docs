---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-topic-reassignments-topicreassignmentoperationarn-stop.html
---

# Stop Topic Reassignment

## URI
<a name="clusters-clusterarn-topic-reassignments-topicreassignmentoperationarn-stop-url"></a>

`/v1/clusters/{{clusterArn}}/topic-reassignments/{{topicReassignmentOperationArn}}/stop`

## HTTP methods
<a name="clusters-clusterarn-topic-reassignments-topicreassignmentoperationarn-stop-http-methods"></a>

### POST
<a name="clusters-clusterarn-topic-reassignments-topicreassignmentoperationarn-stoppost"></a>

**Operation ID:** `StopTopicReassignment`

Stops an active topic reassignment. The operation returns `STOPPING` immediately and the reassignment reaches `STOPPED` once the partitions that were in flight have reverted.

Only the in-flight batch is reverted. Partitions that already finished moving stay on the target brokers. To move them back, start a new reassignment whose `targetInstanceType` names the brokers you want them on.

A reassignment that has already reached a terminal status cannot be stopped.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |
| {{topicReassignmentOperationArn}} | String | True | The Amazon Resource Name (ARN) of the topic reassignment operation to stop. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | StopTopicReassignmentResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="clusters-clusterarn-topic-reassignments-topicreassignmentoperationarn-stopoptions"></a>

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
<a name="clusters-clusterarn-topic-reassignments-topicreassignmentoperationarn-stop-schemas"></a>

### Response bodies
<a name="clusters-clusterarn-topic-reassignments-topicreassignmentoperationarn-stop-response-examples"></a>

#### StopTopicReassignmentResponse schema
<a name="clusters-clusterarn-topic-reassignments-topicreassignmentoperationarn-stop-response-body-stoptopicreassignmentresponse-example"></a>

```json
{
  "topicReassignmentOperationArn": "string",
  "status": enum
}
```

#### Error schema
<a name="clusters-clusterarn-topic-reassignments-topicreassignmentoperationarn-stop-response-body-error-example"></a>

```json
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="clusters-clusterarn-topic-reassignments-topicreassignmentoperationarn-stop-properties"></a>

### Error
<a name="clusters-clusterarn-topic-reassignments-topicreassignmentoperationarn-stop-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### StopTopicReassignmentResponse
<a name="clusters-clusterarn-topic-reassignments-topicreassignmentoperationarn-stop-model-stoptopicreassignmentresponse"></a>

Returns the result of stopping a topic reassignment operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| status | [TopicReassignmentStatus](#clusters-clusterarn-topic-reassignments-topicreassignmentoperationarn-stop-model-topicreassignmentstatus) | False | The current status of the operation. Will be STOPPING. |
| topicReassignmentOperationArn | string<br />MaxLength: 2048 | False | The Amazon Resource Name (ARN) of the topic reassignment operation. |

### TopicReassignmentStatus
<a name="clusters-clusterarn-topic-reassignments-topicreassignmentoperationarn-stop-model-topicreassignmentstatus"></a>

The lifecycle status of a topic reassignment. A reassignment that is `PENDING` has been recorded but has not started moving partitions yet, and one that is `IN_PROGRESS` is moving them. `STOPPING` means that `StopTopicReassignment` was called and the in-flight partitions are reverting. A reassignment is `COMPLETE` when every selected topic is on the target broker type, `STOPPED` when it stopped at your request, in which case the partitions that had already moved remain on the target broker type, and `FAILED` when it stopped on an error that `errorInfo` explains.
+ `PENDING`
+ `IN_PROGRESS`
+ `STOPPING`
+ `COMPLETE`
+ `FAILED`
+ `STOPPED`

## See also
<a name="clusters-clusterarn-topic-reassignments-topicreassignmentoperationarn-stop-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### StopTopicReassignment
<a name="StopTopicReassignment-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/StopTopicReassignment)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/StopTopicReassignment)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/StopTopicReassignment)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/StopTopicReassignment)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/StopTopicReassignment)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/StopTopicReassignment)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/StopTopicReassignment)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/StopTopicReassignment)
+ [AWS SDK for Python (Boto3)](/goto/boto3/kafka-2018-11-14/StopTopicReassignment)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/StopTopicReassignment)
