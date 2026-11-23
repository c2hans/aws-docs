---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-topic-reassignments.html
---

# Topic Reassignments

A topic reassignment moves topic partitions between the two broker types of a mixed-mode cluster, which is a cluster that runs both Standard brokers and Express brokers during an in-place upgrade. Use these operations when you upgrade with `topicReassignment` set to `MANUAL`, the default.

## URI
<a name="clusters-clusterarn-topic-reassignments-url"></a>

`/v1/clusters/{{clusterArn}}/topic-reassignments`

## HTTP methods
<a name="clusters-clusterarn-topic-reassignments-http-methods"></a>

### GET
<a name="clusters-clusterarn-topic-reassignmentsget"></a>

**Operation ID:** `ListTopicReassignments`

Returns the topic reassignments for a cluster. Filter by `statusFilter` to return only reassignments in the statuses you name; omit it to return all of them.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| statusFilter | String | False | Optional filter. Only return reassignments matching these statuses. |
| maxResults | String | False | The maximum number of reassignment operations to return in the response. The default is 50 and the maximum is 100. If there are more results, the response includes a `NextToken` parameter. |
| nextToken | String | False | The paginated results marker. When the result of the operation is truncated, the call returns `NextToken` in the response. To get the next batch, provide this token in your next request. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListTopicReassignmentsResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### POST
<a name="clusters-clusterarn-topic-reassignmentspost"></a>

**Operation ID:** `StartTopicReassignment`

Starts a topic reassignment on a cluster that is in mixed mode, moving the partitions of the selected topics onto the brokers named by `targetInstanceType`. The operation returns as soon as the reassignment is recorded; poll `DescribeTopicReassignment` for progress.

The topic selection is resolved once, when you make the call. Topics created afterwards are not included, and topics already on the target brokers are skipped.

A cluster can have only one active reassignment at a time, and none can start while a cluster-level operation is in progress. To resume after `StopTopicReassignment`, call this operation again with the same selection: the partitions that already moved are skipped.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | StartTopicReassignmentResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 409 | Error | A reassignment is already active for this cluster, or a cluster-level operation is in progress. Wait for it to finish, then retry your request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="clusters-clusterarn-topic-reassignmentsoptions"></a>

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
<a name="clusters-clusterarn-topic-reassignments-schemas"></a>

### Request bodies
<a name="clusters-clusterarn-topic-reassignments-request-examples"></a>

#### POST schema
<a name="clusters-clusterarn-topic-reassignments-request-body-post-example"></a>

```json
{
  "clientToken": "string",
  "topicsToInclude": [
    "string"
  ],
  "topicsToExclude": [
    "string"
  ],
  "targetInstanceType": "string"
}
```

### Response bodies
<a name="clusters-clusterarn-topic-reassignments-response-examples"></a>

#### ListTopicReassignmentsResponse schema
<a name="clusters-clusterarn-topic-reassignments-response-body-listtopicreassignmentsresponse-example"></a>

```json
{
  "reassignments": [
    {
      "topicReassignmentOperationArn": "string",
      "targetInstanceType": "string",
      "status": enum,
      "totalTopics": integer,
      "completedTopics": integer,
      "creationTime": "string"
    }
  ],
  "nextToken": "string"
}
```

#### StartTopicReassignmentResponse schema
<a name="clusters-clusterarn-topic-reassignments-response-body-starttopicreassignmentresponse-example"></a>

```json
{
  "clusterArn": "string",
  "topicReassignmentOperationArn": "string",
  "status": enum
}
```

#### Error schema
<a name="clusters-clusterarn-topic-reassignments-response-body-error-example"></a>

```json
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="clusters-clusterarn-topic-reassignments-properties"></a>

### Error
<a name="clusters-clusterarn-topic-reassignments-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### ListTopicReassignmentsResponse
<a name="clusters-clusterarn-topic-reassignments-model-listtopicreassignmentsresponse"></a>

Returns a list of topic reassignment operations for a cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | string | False | If the response is truncated, it returns a nextToken. Send this in the subsequent request to get the remaining results. |
| reassignments | Array of type [TopicReassignmentInfo](#clusters-clusterarn-topic-reassignments-model-topicreassignmentinfo) | False | A list of topic reassignment operation summaries. |

### StartTopicReassignmentRequest
<a name="clusters-clusterarn-topic-reassignments-model-starttopicreassignmentrequest"></a>

Initiates topic partition reassignment between broker types in a mixed-mode cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clientToken | string<br />MinLength: 1<br />MaxLength: 64 | False | A unique, case-sensitive identifier that makes the request idempotent. |
| targetInstanceType | string<br />MinLength: 1<br />MaxLength: 256 | True | The instance type of the brokers to move the selected topics onto. It must name brokers the cluster actually runs: the Express instance type (for example, `express.m7g.large`) to move topics onto the Express brokers, or the Standard instance type (for example, `kafka.m7g.large`) to move them back onto the Standard brokers.<br />The prefix determines the direction of the move, so a value that is well formed but names brokers the cluster does not run is rejected. |
| topicsToExclude | Array of type string | False | Regular expressions that remove topics from the selection. They are applied after `topicsToInclude`, so a topic matched by both is excluded. You can supply up to 10 patterns of up to 256 characters each. |
| topicsToInclude | Array of type string | True | Regular expressions that select the topics to reassign. Specify `[".*"]` to select every topic. You can supply up to 10 patterns of up to 256 characters each.<br />Patterns are resolved against the cluster's topics at the moment of the call. Topics created afterwards are not reassigned. |

### StartTopicReassignmentResponse
<a name="clusters-clusterarn-topic-reassignments-model-starttopicreassignmentresponse"></a>

Returns information about the initiated topic reassignment operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clusterArn | string<br />MaxLength: 2048 | False | The Amazon Resource Name (ARN) of the cluster. |
| status | [TopicReassignmentStatus](#clusters-clusterarn-topic-reassignments-model-topicreassignmentstatus) | False | The current status of the reassignment operation. |
| topicReassignmentOperationArn | string<br />MaxLength: 2048 | False | The Amazon Resource Name (ARN) of the topic reassignment operation. |

### TopicReassignmentInfo
<a name="clusters-clusterarn-topic-reassignments-model-topicreassignmentinfo"></a>

Summary information about a topic reassignment operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| completedTopics | integer | False | Number of topics fully migrated. |
| creationTime | string | False | When the operation was created. |
| status | [TopicReassignmentStatus](#clusters-clusterarn-topic-reassignments-model-topicreassignmentstatus) | False | The current status of the reassignment operation. |
| targetInstanceType | string | False | The target broker instance type for this reassignment. |
| topicReassignmentOperationArn | string<br />MaxLength: 2048 | False | The Amazon Resource Name (ARN) of the topic reassignment operation. |
| totalTopics | integer | False | Total number of topics matching the selector. |

### TopicReassignmentStatus
<a name="clusters-clusterarn-topic-reassignments-model-topicreassignmentstatus"></a>

The lifecycle status of a topic reassignment. A reassignment that is `PENDING` has been recorded but has not started moving partitions yet, and one that is `IN_PROGRESS` is moving them. `STOPPING` means that `StopTopicReassignment` was called and the in-flight partitions are reverting. A reassignment is `COMPLETE` when every selected topic is on the target broker type, `STOPPED` when it stopped at your request, in which case the partitions that had already moved remain on the target broker type, and `FAILED` when it stopped on an error that `errorInfo` explains.
+ `PENDING`
+ `IN_PROGRESS`
+ `STOPPING`
+ `COMPLETE`
+ `FAILED`
+ `STOPPED`

## See also
<a name="clusters-clusterarn-topic-reassignments-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListTopicReassignments
<a name="ListTopicReassignments-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/ListTopicReassignments)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/ListTopicReassignments)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/ListTopicReassignments)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/ListTopicReassignments)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/ListTopicReassignments)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/ListTopicReassignments)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/ListTopicReassignments)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/ListTopicReassignments)
+ [AWS SDK for Python (Boto3)](/goto/boto3/kafka-2018-11-14/ListTopicReassignments)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/ListTopicReassignments)

### StartTopicReassignment
<a name="StartTopicReassignment-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/StartTopicReassignment)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/StartTopicReassignment)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/StartTopicReassignment)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/StartTopicReassignment)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/StartTopicReassignment)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/StartTopicReassignment)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/StartTopicReassignment)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/StartTopicReassignment)
+ [AWS SDK for Python (Boto3)](/goto/boto3/kafka-2018-11-14/StartTopicReassignment)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/StartTopicReassignment)
