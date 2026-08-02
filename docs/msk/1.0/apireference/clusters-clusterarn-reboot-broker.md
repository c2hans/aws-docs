---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-reboot-broker.html
---

# Reboot Broker
<a name="clusters-clusterarn-reboot-broker"></a>

## URI
<a name="clusters-clusterarn-reboot-broker-url"></a>

`/v1/clusters/{{clusterArn}}/reboot-broker`

## HTTP methods
<a name="clusters-clusterarn-reboot-broker-http-methods"></a>

### PUT
<a name="clusters-clusterarn-reboot-brokerput"></a>

**Operation ID:** `RebootBroker`

Reboots a broker. In a given cluster, you can reboot one broker at a time.

 To reboot a broker, wait for the cluster status to be ACTIVE. This operation returns an error if you invoke it while the cluster status is HEALING. You must wait for the status to change from HEALING to ACTIVE before you reboot the broker.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  RebootBrokerResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="clusters-clusterarn-reboot-brokeroptions"></a>

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
<a name="clusters-clusterarn-reboot-broker-schemas"></a>

### Request bodies
<a name="clusters-clusterarn-reboot-broker-request-examples"></a>

#### PUT schema
<a name="clusters-clusterarn-reboot-broker-request-body-put-example"></a>

```
{
  "brokerIds": [
    "string"
  ]
}
```

### Response bodies
<a name="clusters-clusterarn-reboot-broker-response-examples"></a>

#### RebootBrokerResponse schema
<a name="clusters-clusterarn-reboot-broker-response-body-rebootbrokerresponse-example"></a>

```
{
  "clusterArn": "string",
  "clusterOperationArn": "string"
}
```

#### Error schema
<a name="clusters-clusterarn-reboot-broker-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="clusters-clusterarn-reboot-broker-properties"></a>

### Error
<a name="clusters-clusterarn-reboot-broker-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### RebootBrokerRequest
<a name="clusters-clusterarn-reboot-broker-model-rebootbrokerrequest"></a>

The request body for the RebootBroker action.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| brokerIds | Array of type string | True | The list of broker IDs to be rebooted. Specify only one broker ID. |

### RebootBrokerResponse
<a name="clusters-clusterarn-reboot-broker-model-rebootbrokerresponse"></a>

The response body for RebootBroker.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clusterArn | string | False | The Amazon Resource Name (ARN) of the cluster. |
| clusterOperationArn | string | False | The Amazon Resource Name (ARN) of the cluster operation. |

## See also
<a name="clusters-clusterarn-reboot-broker-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### RebootBroker
<a name="RebootBroker-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/RebootBroker)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/RebootBroker)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/RebootBroker)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/RebootBroker)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/RebootBroker)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/RebootBroker)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/RebootBroker)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/RebootBroker)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/RebootBroker)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/RebootBroker)
