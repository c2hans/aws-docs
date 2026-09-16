---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-client-vpc-connection.html
---

# Clusters clusterArn Client-vpc-connection
<a name="clusters-clusterarn-client-vpc-connection"></a>

## URI
<a name="clusters-clusterarn-client-vpc-connection-url"></a>

`/v1/clusters/{{clusterArn}}/client-vpc-connection`

## HTTP methods
<a name="clusters-clusterarn-client-vpc-connection-http-methods"></a>

### PUT
<a name="clusters-clusterarn-client-vpc-connectionput"></a>

**Operation ID:** `RejectClientVpcConnection`

Reject client VPC connection.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  RejectClientVpcConnectionResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="clusters-clusterarn-client-vpc-connectionoptions"></a>

Enable CORS by returning correct headers.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="clusters-clusterarn-client-vpc-connection-schemas"></a>

### Request bodies
<a name="clusters-clusterarn-client-vpc-connection-request-examples"></a>

#### PUT schema
<a name="clusters-clusterarn-client-vpc-connection-request-body-put-example"></a>

```
{
  "vpcConnectionArn": "string"
}
```

### Response bodies
<a name="clusters-clusterarn-client-vpc-connection-response-examples"></a>

#### RejectClientVpcConnectionResponse schema
<a name="clusters-clusterarn-client-vpc-connection-response-body-rejectclientvpcconnectionresponse-example"></a>

```
{
}
```

#### Error schema
<a name="clusters-clusterarn-client-vpc-connection-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="clusters-clusterarn-client-vpc-connection-properties"></a>

### Error
<a name="clusters-clusterarn-client-vpc-connection-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### RejectClientVpcConnectionRequest
<a name="clusters-clusterarn-client-vpc-connection-model-rejectclientvpcconnectionrequest"></a>

Reject VPC Connection

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| vpcConnectionArn | string<br />MinLength: 1 | True | VPC Connection Amazon Resource Name (ARN). |

### RejectClientVpcConnectionResponse
<a name="clusters-clusterarn-client-vpc-connection-model-rejectclientvpcconnectionresponse"></a>

Blocks client connections connecting to the cluster

## See also
<a name="clusters-clusterarn-client-vpc-connection-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### RejectClientVpcConnection
<a name="RejectClientVpcConnection-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/RejectClientVpcConnection)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/RejectClientVpcConnection)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/RejectClientVpcConnection)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/RejectClientVpcConnection)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/RejectClientVpcConnection)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/RejectClientVpcConnection)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/RejectClientVpcConnection)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/RejectClientVpcConnection)
+ [AWS SDK for Python (Boto3)](/goto/boto3/kafka-2018-11-14/RejectClientVpcConnection)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/RejectClientVpcConnection)
