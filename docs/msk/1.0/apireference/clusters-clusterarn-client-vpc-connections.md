---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-client-vpc-connections.html
---

# Clusters clusterArn Client-vpc-connections
<a name="clusters-clusterarn-client-vpc-connections"></a>

## URI
<a name="clusters-clusterarn-client-vpc-connections-url"></a>

`/v1/clusters/{{clusterArn}}/client-vpc-connections`

## HTTP methods
<a name="clusters-clusterarn-client-vpc-connections-http-methods"></a>

### GET
<a name="clusters-clusterarn-client-vpc-connectionsget"></a>

**Operation ID:** `ListClientVpcConnections`

List client VPC connections.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The paginated results marker. When the result of the operation is truncated, the call returns `NextToken` in the response. To get the next batch, provide this token in your next request. |
| maxResults | String | False | The maximum number of results to return in the response (default maximum 100 results per API call). If there are more results, the response includes a `NextToken` parameter. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  ListClientVpcConnectionsResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="clusters-clusterarn-client-vpc-connectionsoptions"></a>

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
<a name="clusters-clusterarn-client-vpc-connections-schemas"></a>

### Response bodies
<a name="clusters-clusterarn-client-vpc-connections-response-examples"></a>

#### ListClientVpcConnectionsResponse schema
<a name="clusters-clusterarn-client-vpc-connections-response-body-listclientvpcconnectionsresponse-example"></a>

```
{
  "clientVpcConnections": [
    {
      "owner": "string",
      "vpcConnectionArn": "string",
      "creationTime": "string",
      "state": enum,
      "authentication": "string"
    }
  ],
  "nextToken": "string"
}
```

#### Error schema
<a name="clusters-clusterarn-client-vpc-connections-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="clusters-clusterarn-client-vpc-connections-properties"></a>

### ClientVpcConnection
<a name="clusters-clusterarn-client-vpc-connections-model-clientvpcconnection"></a>

VPC Connection description

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| authentication | string | False | The type of private link authentication. |
| creationTime | string | False | The time which the VPC Connnection is created. |
| owner | string | False | The Owner of the VPC Connection. |
| state | [VpcConnectionState](#clusters-clusterarn-client-vpc-connections-model-vpcconnectionstate) | False | State of the Remote VPC Connection. |
| vpcConnectionArn | string | True | The Amazon Resource Name (ARN) of the Remote VPC. |

### Error
<a name="clusters-clusterarn-client-vpc-connections-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### ListClientVpcConnectionsResponse
<a name="clusters-clusterarn-client-vpc-connections-model-listclientvpcconnectionsresponse"></a>

The response contains an array vpc connections.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clientVpcConnections | Array of type [ClientVpcConnection](#clusters-clusterarn-client-vpc-connections-model-clientvpcconnection) | False | An array of client vpc connections information objects. |
| nextToken | string | False | If the response of ListClientVpcConnections is truncated, it returns a NextToken in the response. This Nexttoken should be sent in the subsequent request to ListClientVpcConnections. |

### VpcConnectionState
<a name="clusters-clusterarn-client-vpc-connections-model-vpcconnectionstate"></a>

State of the vpc connection
+ `CREATING`
+ `AVAILABLE`
+ `INACTIVE`
+ `UPDATING`
+ `DEACTIVATING`
+ `DELETING`
+ `FAILED`
+ `REJECTED`
+ `REJECTING`

## See also
<a name="clusters-clusterarn-client-vpc-connections-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListClientVpcConnections
<a name="ListClientVpcConnections-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/ListClientVpcConnections)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/ListClientVpcConnections)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/ListClientVpcConnections)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/ListClientVpcConnections)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/ListClientVpcConnections)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/ListClientVpcConnections)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/ListClientVpcConnections)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/ListClientVpcConnections)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/ListClientVpcConnections)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/ListClientVpcConnections)
