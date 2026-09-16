---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-rebalancing.html
---

# Clusters clusterArn Rebalancing
<a name="clusters-clusterarn-rebalancing"></a>

## URI
<a name="clusters-clusterarn-rebalancing-url"></a>

`/v1/clusters/{{clusterArn}}/rebalancing`

## HTTP methods
<a name="clusters-clusterarn-rebalancing-http-methods"></a>

### PUT
<a name="clusters-clusterarn-rebalancingput"></a>

**Operation ID:** `UpdateRebalancing`

Use this resource to update the intelligent rebalancing status of an Amazon MSK Provisioned cluster with Express brokers.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  UpdateRebalancingResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="clusters-clusterarn-rebalancingoptions"></a>

Use this resource to update the intelligent rebalancing status of an Amazon MSK Provisioned cluster with Express brokers.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="clusters-clusterarn-rebalancing-schemas"></a>

### Request bodies
<a name="clusters-clusterarn-rebalancing-request-examples"></a>

#### PUT schema
<a name="clusters-clusterarn-rebalancing-request-body-put-example"></a>

```
{
  "currentVersion": "string",
  "rebalancing": {
    "status": enum
  }
}
```

### Response bodies
<a name="clusters-clusterarn-rebalancing-response-examples"></a>

#### UpdateRebalancingResponse schema
<a name="clusters-clusterarn-rebalancing-response-body-updaterebalancingresponse-example"></a>

```
{
  "clusterArn": "string",
  "clusterOperationArn": "string"
}
```

#### Error schema
<a name="clusters-clusterarn-rebalancing-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="clusters-clusterarn-rebalancing-properties"></a>

### Error
<a name="clusters-clusterarn-rebalancing-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### Rebalancing
<a name="clusters-clusterarn-rebalancing-model-rebalancing"></a>

Specifies whether or not intelligent rebalancing is turned on for a newly created MSK Provisioned cluster with Express brokers. Intelligent rebalancing performs automatic partition balancing operations when you scale your clusters up or down.

By default, intelligent rebalancing is `ACTIVE` for all new Express-based clusters.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| status | [RebalancingStatus](#clusters-clusterarn-rebalancing-model-rebalancingstatus) | True | Intelligent rebalancing status. The default intelligent rebalancing status is `ACTIVE` for all new Express-based clusters. |

### RebalancingStatus
<a name="clusters-clusterarn-rebalancing-model-rebalancingstatus"></a>

Intelligent rebalancing status. The default intelligent rebalancing status is `ACTIVE` for all new Express-based clusters.
+ `PAUSED`
+ `ACTIVE`

### UpdateRebalancingRequest
<a name="clusters-clusterarn-rebalancing-model-updaterebalancingrequest"></a>

Updates the intelligent rebalancing status for a new MSK Provisioned cluster with Express brokers.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| currentVersion | string | True | The current version of the cluster. |
| rebalancing | [Rebalancing](#clusters-clusterarn-rebalancing-model-rebalancing) | True | Specifies if intelligent rebalancing should be turned on for your cluster. The default intelligent rebalancing status is `ACTIVE` for all new MSK Provisioned clusters that you create with Express brokers. |

### UpdateRebalancingResponse
<a name="clusters-clusterarn-rebalancing-model-updaterebalancingresponse"></a>

Provides information about the intelligent rebalancing update for a cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clusterArn | string | False | The Amazon Resource Name (ARN) of the cluster whose intelligent rebalancing status you've updated. |
| clusterOperationArn | string | False | The Amazon Resource Name (ARN) of the cluster operation. |

## See also
<a name="clusters-clusterarn-rebalancing-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### UpdateRebalancing
<a name="UpdateRebalancing-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/UpdateRebalancing)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/UpdateRebalancing)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/UpdateRebalancing)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/UpdateRebalancing)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/UpdateRebalancing)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/UpdateRebalancing)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/UpdateRebalancing)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/UpdateRebalancing)
+ [AWS SDK for Python (Boto3)](/goto/boto3/kafka-2018-11-14/UpdateRebalancing)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/UpdateRebalancing)
