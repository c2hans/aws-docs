---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-nodes-type.html
---

# Broker Type
<a name="clusters-clusterarn-nodes-type"></a>

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

```
{
  "targetInstanceType": "string",
  "currentVersion": "string"
}
```

### Response bodies
<a name="clusters-clusterarn-nodes-type-response-examples"></a>

#### UpdateBrokerTypeResponse schema
<a name="clusters-clusterarn-nodes-type-response-body-updatebrokertyperesponse-example"></a>

```
{
  "clusterArn": "string",
  "clusterOperationArn": "string"
}
```

#### Error schema
<a name="clusters-clusterarn-nodes-type-response-body-error-example"></a>

```
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
| targetInstanceType | string | True | The type of Amazon EC2 instances to use for Kafka brokers. |

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
