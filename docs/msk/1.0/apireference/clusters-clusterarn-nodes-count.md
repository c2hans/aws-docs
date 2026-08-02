---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-nodes-count.html
---

# Broker Count
<a name="clusters-clusterarn-nodes-count"></a>

The number of broker nodes in a cluster.

## URI
<a name="clusters-clusterarn-nodes-count-url"></a>

`/v1/clusters/{{clusterArn}}/nodes/count`

## HTTP methods
<a name="clusters-clusterarn-nodes-count-http-methods"></a>

### PUT
<a name="clusters-clusterarn-nodes-countput"></a>

**Operation ID:** `UpdateBrokerCount`

Updates the number of broker nodes in the cluster. You can use this operation to increase or decrease the number of brokers in an existing cluster.

The following Python 3.6 example shows how you can increase the number of brokers in a cluster to 6 brokers. The update operation returns immediately, with a response that includes the Amazon Resource Name (ARN) that Amazon MSK assigns to this cluster operation. You can use that ARN to check the state of the operation. When the state changes from `PENDING` to `UPDATE_COMPLETE`, the operation is complete.

```
import boto3
import time

client = boto3.client('kafka')

update_broker_count_response = client.update_broker_count(
    ClusterArn='arn:aws:kafka:us-east-1:0123456789019:cluster/SalesCluster/abcd1234-abcd-cafe-abab-9876543210ab-4',
    CurrentVersion='K12V3IB1VIZHHY',
    TargetNumberOfBrokerNodes=6
)

operation_arn = update_broker_count_response['ClusterOperationArn']

print(operation_arn)

describe_cluster_operation_response = client.describe_cluster_operation(ClusterOperationArn=operation_arn)
operation_state = describe_cluster_operation_response['ClusterOperationInfo']['OperationState']
print(operation_state)

expanded = False

while not expanded:
    print('Sleeping for 15 seconds before checking to see if the cluster update is done...')
    time.sleep(15)
    describe_cluster_operation_response = client.describe_cluster_operation(ClusterOperationArn=operation_arn)
    operation_state = describe_cluster_operation_response['ClusterOperationInfo']['OperationState']
    if 'UPDATE_COMPLETE' == operation_state:
        expanded = True
        print('The cluster has 6 brokers now.')
```

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  UpdateBrokerCountResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="clusters-clusterarn-nodes-countoptions"></a>

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
<a name="clusters-clusterarn-nodes-count-schemas"></a>

### Request bodies
<a name="clusters-clusterarn-nodes-count-request-examples"></a>

#### PUT schema
<a name="clusters-clusterarn-nodes-count-request-body-put-example"></a>

```
{
  "targetNumberOfBrokerNodes": integer,
  "currentVersion": "string"
}
```

### Response bodies
<a name="clusters-clusterarn-nodes-count-response-examples"></a>

#### UpdateBrokerCountResponse schema
<a name="clusters-clusterarn-nodes-count-response-body-updatebrokercountresponse-example"></a>

```
{
  "clusterArn": "string",
  "clusterOperationArn": "string"
}
```

#### Error schema
<a name="clusters-clusterarn-nodes-count-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="clusters-clusterarn-nodes-count-properties"></a>

### Error
<a name="clusters-clusterarn-nodes-count-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### UpdateBrokerCountRequest
<a name="clusters-clusterarn-nodes-count-model-updatebrokercountrequest"></a>

Request body for UpdateBrokerCount. Accepts a targetNumberOfBrokerNodes value that is 2 or 3 less than the current broker node count for the cluster (for 2 and 3 AZ clusters respectively).

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| currentVersion | string | True | The current version of the cluster. |
| targetNumberOfBrokerNodes | integer | True | The number of broker nodes that you want the cluster to have after this operation completes successfully. |

### UpdateBrokerCountResponse
<a name="clusters-clusterarn-nodes-count-model-updatebrokercountresponse"></a>

Response body for UpdateBrokerCount.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clusterArn | string | False | The Amazon Resource Name (ARN) of the cluster. |
| clusterOperationArn | string | False | The Amazon Resource Name (ARN) of the cluster operation. |

## See also
<a name="clusters-clusterarn-nodes-count-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### UpdateBrokerCount
<a name="UpdateBrokerCount-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/UpdateBrokerCount)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/UpdateBrokerCount)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/UpdateBrokerCount)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/UpdateBrokerCount)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/UpdateBrokerCount)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/UpdateBrokerCount)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/UpdateBrokerCount)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/UpdateBrokerCount)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/UpdateBrokerCount)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/UpdateBrokerCount)
