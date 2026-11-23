---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-nodes-type.html
---

# Broker Type

The type of brokers in the cluster. All of the brokers in a cluster are the same type.

## URI
<a name="clusters-clusterarn-nodes-type-url"></a>

`/v1/clusters/{{clusterArn}}/nodes/type`

## HTTP methods
<a name="clusters-clusterarn-nodes-type-http-methods"></a>

### PUT
<a name="clusters-clusterarn-nodes-typeput"></a>

**Operation ID:** `UpdateBrokerType`

For information about this operation, see [Updating the broker type](https://docs.aws.amazon.com/msk/latest/developerguide/msk-update-broker-type.html) in the developer guide.

This operation also drives each step of an in-place upgrade from Standard brokers to Express brokers. The step you take is determined by the value of `targetInstanceType`:
+ **Initiate the upgrade.** Send the composite instance type (for example, `kafka.m7g.large-express.m7g.large`) to add Express brokers alongside the cluster's existing Standard brokers. The cluster enters mixed mode, where it runs brokers of both types. Set `topicReassignment` to `AUTO` on this request to have Amazon MSK migrate every topic to the Express brokers, or leave it at `MANUAL` to migrate topics yourself with `StartTopicReassignment`.
+ **Complete the upgrade.** Send the Express instance type (for example, `express.m7g.large`) to decommission the Standard brokers. Every topic must already be on the Express brokers, and `topicReassignment` must be `MANUAL` or omitted.
+ **Roll back.** Send the Standard instance type (for example, `kafka.m7g.large`) to decommission the Express brokers and return the cluster to Standard. Every topic must already be back on the Standard brokers, and `topicReassignment` must be `MANUAL` or omitted.

Rolling back is available only while the cluster is in mixed mode. After you complete the upgrade, the Standard brokers are permanently removed.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  UpdateBrokerTypeResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="clusters-clusterarn-nodes-typeoptions"></a>

Enable CORS by returning the correct headers.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="clusters-clusterarn-nodes-type-schemas"></a>

### Request bodies
<a name="clusters-clusterarn-nodes-type-request-examples"></a>

#### PUT schema
<a name="clusters-clusterarn-nodes-type-request-body-put-example"></a>

```json
{
  "targetInstanceType": "string",
  "currentVersion": "string",
  "topicReassignment": "string"
}
```

### Response bodies
<a name="clusters-clusterarn-nodes-type-response-examples"></a>

#### UpdateBrokerTypeResponse schema
<a name="clusters-clusterarn-nodes-type-response-body-updatebrokertyperesponse-example"></a>

```json
{
  "clusterArn": "string",
  "clusterOperationArn": "string"
}
```

#### Error schema
<a name="clusters-clusterarn-nodes-type-response-body-error-example"></a>

```json
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="clusters-clusterarn-nodes-type-properties"></a>

### Error
<a name="clusters-clusterarn-nodes-type-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### UpdateBrokerTypeRequest
<a name="clusters-clusterarn-nodes-type-model-updatebrokertyperequest"></a>

Request body for UpdateBrokerType.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| currentVersion | string | True | Current cluster version. |
| targetInstanceType | string | True | The type of Amazon EC2 instances to use for Kafka brokers.<br />For an in-place upgrade from Standard brokers to Express brokers, this value selects the step:+  A composite value of the cluster's current Standard instance type and the target Express instance type, joined by a hyphen (for example, `kafka.m7g.large-express.m7g.large`), initiates the upgrade and puts the cluster into mixed mode. Write the Express half as `express.`*family*.*size*. Only the instance family may change across the upgrade (for example, `m5` to `m7g`); the instance size must match the cluster's current size. <br />+  The Express instance type alone (for example, `express.m7g.large`) completes the upgrade and decommissions the Standard brokers. <br />+  The Standard instance type alone (for example, `kafka.m7g.large`) rolls the upgrade back and decommissions the Express brokers.  |
| topicReassignment | string | False | Controls whether Amazon MSK reassigns topics for you when the cluster enters mixed mode.+  `AUTO` - Amazon MSK starts a reassignment of every topic onto the target broker type as soon as the new brokers join. Track it through the `topicReassignmentOperationArn` that `DescribeClusterOperation` reports in `brokerTypeUpgradeInfo`, and stop it at any time with `StopTopicReassignment`. <br />+  `MANUAL` - you reassign topics yourself with `StartTopicReassignment`, which returns a `topicReassignmentOperationArn` you can track with `DescribeTopicReassignment` and stop with `StopTopicReassignment`. This is the default. <br />This parameter is valid only on the request that initiates the upgrade, where `targetInstanceType` is a composite value. Set it to `MANUAL` or omit it when you complete the upgrade or roll it back. |

### UpdateBrokerTypeResponse
<a name="clusters-clusterarn-nodes-type-model-updatebrokertyperesponse"></a>

Response body for UpdateBrokerType.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clusterArn | string | False | The Amazon Resource Name (ARN) of the cluster. |
| clusterOperationArn | string | False | The Amazon Resource Name (ARN) of the cluster operation. |

## See also
<a name="clusters-clusterarn-nodes-type-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### UpdateBrokerType
<a name="UpdateBrokerType-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/UpdateBrokerType)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/UpdateBrokerType)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/UpdateBrokerType)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/UpdateBrokerType)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/UpdateBrokerType)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/UpdateBrokerType)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/UpdateBrokerType)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/UpdateBrokerType)
+ [AWS SDK for Python (Boto3)](/goto/boto3/kafka-2018-11-14/UpdateBrokerType)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/UpdateBrokerType)
