---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/vpc-connections.html
---

# Vpc-connections
<a name="vpc-connections"></a>

## URI
<a name="vpc-connections-url"></a>

`/v1/vpc-connections`

## HTTP methods
<a name="vpc-connections-http-methods"></a>

### GET
<a name="vpc-connectionsget"></a>

**Operation ID:** `ListVpcConnections`

Lists all VPC connections.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The paginated results marker. When the result of the operation is truncated, the call returns `NextToken` in the response. To get the next batch, provide this token in your next request. |
| maxResults | String | False | The maximum number of results to return in the response (default maximum 100 results per API call). If there are more results, the response includes a `NextToken` parameter. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  ListVpcConnectionsResponse | HTTP Status Code 200: OK. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="vpc-connectionsoptions"></a>

Enable CORS by returning correct headers.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method. |

## Schemas
<a name="vpc-connections-schemas"></a>

### Response bodies
<a name="vpc-connections-response-examples"></a>

#### ListVpcConnectionsResponse schema
<a name="vpc-connections-response-body-listvpcconnectionsresponse-example"></a>

```
{
  "nextToken": "string",
  "vpcConnections": [
    {
      "vpcConnectionArn": "string",
      "creationTime": "string",
      "targetClusterArn": "string",
      "vpcId": "string",
      "state": enum,
      "authentication": "string"
    }
  ]
}
```

#### Error schema
<a name="vpc-connections-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="vpc-connections-properties"></a>

### Error
<a name="vpc-connections-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### ListVpcConnectionsResponse
<a name="vpc-connections-model-listvpcconnectionsresponse"></a>

The response contains an array of vpcConnections and a next token if the response is truncated.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | string | False | If the response of ListVpcConnections is truncated, it returns a NextToken in the response. This NextToken should be sent in the subsequent request to ListVpcConnections. |
| vpcConnections | Array of type [VpcConnection](#vpc-connections-model-vpcconnection) | False | An array of VPC Connection. |

### VpcConnection
<a name="vpc-connections-model-vpcconnection"></a>

Vpc Connection description

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| authentication | string | False | The type of private link authentication. |
| creationTime | string | False | The time which the VPC Connnection is created. |
| state | [VpcConnectionState](#vpc-connections-model-vpcconnectionstate) | False | State of the Remote VPC Connection. |
| targetClusterArn | string | True | The Amazon Resource Name (ARN) of the target cluster. |
| vpcConnectionArn | string | True | The Amazon Resource Name (ARN) of the Remote Vpc. |
| vpcId | string | False | The description of the vpcId. |

### VpcConnectionState
<a name="vpc-connections-model-vpcconnectionstate"></a>

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
<a name="vpc-connections-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListVpcConnections
<a name="ListVpcConnections-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/ListVpcConnections)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/ListVpcConnections)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/ListVpcConnections)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/ListVpcConnections)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/ListVpcConnections)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/ListVpcConnections)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/ListVpcConnections)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/ListVpcConnections)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/ListVpcConnections)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/ListVpcConnections)
