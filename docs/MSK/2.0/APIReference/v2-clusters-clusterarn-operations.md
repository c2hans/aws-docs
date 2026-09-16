---
source_url: https://docs.aws.amazon.com/MSK/2.0/APIReference/v2-clusters-clusterarn-operations.html
---

# V2 Clusters clusterArn Operations
<a name="v2-clusters-clusterarn-operations"></a>

## URI
<a name="v2-clusters-clusterarn-operations-url"></a>

`/api/v2/clusters/{{clusterArn}}/operations`

## HTTP methods
<a name="v2-clusters-clusterarn-operations-http-methods"></a>

### GET
<a name="v2-clusters-clusterarn-operationsget"></a>

**Operation ID:** `ListClusterOperationsV2`

Returns a list of all the operations that have been performed on the specified MSK cluster.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | ARN of the cluster to be described. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | If the response of ListClusters is truncated, it returns a nextToken in the response. This nextToken should be sent in the subsequent request to ListClusters. |
| maxResults | String | False | Maximum number of clusters to fetch in one get request. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  ListClusterOperationsV2Response | HTTP Status Code 200: OK. |
| 400 | None | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 401 | None | HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated. |
| 403 | None | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 404 | None | HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it. |
| 429 | None | HTTP Status Code 429: Limit exceeded. Resource limit reached. |
| 500 | None | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | None | HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue. |

### OPTIONS
<a name="v2-clusters-clusterarn-operationsoptions"></a>

Enable CORS by returning correct headers

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | ARN of the cluster to be described. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response |

## Schemas
<a name="v2-clusters-clusterarn-operations-schemas"></a>

### Response bodies
<a name="v2-clusters-clusterarn-operations-response-examples"></a>

#### ListClusterOperationsV2Response schema
<a name="v2-clusters-clusterarn-operations-response-body-listclusteroperationsv2response-example"></a>

```
{
  "nextToken": "string",
  "clusterOperationInfoList": [
    {
      "clusterType": enum,
      "clusterArn": "string",
      "operationState": "string",
      "startTime": "string",
      "operationType": "string",
      "endTime": "string",
      "operationArn": "string"
    }
  ]
}
```

## Properties
<a name="v2-clusters-clusterarn-operations-properties"></a>

### ClusterOperationV2Summary
<a name="v2-clusters-clusterarn-operations-model-clusteroperationv2summary"></a>

Returns information about a cluster operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clusterArn | string | False | ARN of the cluster. |
| clusterType | [ClusterType](#v2-clusters-clusterarn-operations-model-clustertype) | False | Type of the backend cluster. |
| endTime | string | False | The time at which the operation finished. |
| operationArn | string | False | ARN of the cluster operation. |
| operationState | string | False | State of the cluster operation. |
| operationType | string | False | Type of the cluster operation. |
| startTime | string | False | The time at which operation was created. |

### ClusterType
<a name="v2-clusters-clusterarn-operations-model-clustertype"></a>

The type of backend cluster.
+ `PROVISIONED`
+ `SERVERLESS`

### ListClusterOperationsV2Response
<a name="v2-clusters-clusterarn-operations-model-listclusteroperationsv2response"></a>

The response contains an array containing cluster operation information and a nextToken if the response is truncated. Displays operations of the type DECREASE\_BROKER\_COUNT in results list after a successful broker removal operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clusterOperationInfoList | Array of type [ClusterOperationV2Summary](#v2-clusters-clusterarn-operations-model-clusteroperationv2summary) | False | An array of cluster operation information objects. |
| nextToken | string | False | If the response of ListClusterOperationsV2 is truncated, it returns a nextToken in the response. This nextToken should be sent in the subsequent request to ListClusterOperationsV2. |

## See also
<a name="v2-clusters-clusterarn-operations-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListClusterOperationsV2
<a name="ListClusterOperationsV2-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/ListClusterOperationsV2)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/ListClusterOperationsV2)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/ListClusterOperationsV2)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/ListClusterOperationsV2)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/ListClusterOperationsV2)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/ListClusterOperationsV2)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/ListClusterOperationsV2)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/ListClusterOperationsV2)
+ [AWS SDK for Python (Boto3)](/goto/boto3/kafka-2018-11-14/ListClusterOperationsV2)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/ListClusterOperationsV2)
