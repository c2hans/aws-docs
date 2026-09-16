---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/vpc-connection.html
---

# Vpc-connection
<a name="vpc-connection"></a>

## URI
<a name="vpc-connection-url"></a>

`/v1/vpc-connection`

## HTTP methods
<a name="vpc-connection-http-methods"></a>

### POST
<a name="vpc-connectionpost"></a>

**Operation ID:** `CreateVpcConnection`

Create remote VPC connection.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  CreateVpcConnectionResponse | HTTP Status Code 200: OK. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="vpc-connectionoptions"></a>

Enable CORS by returning correct headers.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method. |

## Schemas
<a name="vpc-connection-schemas"></a>

### Request bodies
<a name="vpc-connection-request-examples"></a>

#### POST schema
<a name="vpc-connection-request-body-post-example"></a>

```
{
  "clientSubnets": [
    "string"
  ],
  "targetClusterArn": "string",
  "vpcId": "string",
  "securityGroups": [
    "string"
  ],
  "tags": {
  },
  "authentication": "string"
}
```

### Response bodies
<a name="vpc-connection-response-examples"></a>

#### CreateVpcConnectionResponse schema
<a name="vpc-connection-response-body-createvpcconnectionresponse-example"></a>

```
{
  "vpcConnectionArn": "string",
  "clientSubnets": [
    "string"
  ],
  "creationTime": "string",
  "vpcId": "string",
  "securityGroups": [
    "string"
  ],
  "state": enum,
  "tags": {
  },
  "authentication": "string"
}
```

#### Error schema
<a name="vpc-connection-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="vpc-connection-properties"></a>

### CreateVpcConnectionRequest
<a name="vpc-connection-model-createvpcconnectionrequest"></a>

Creates a remote VPC connection for account client.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| authentication | string<br />MinLength: 3<br />MaxLength: 10 | True | The authentication type for the client VPC connection. Specify one of these auth type strings: `SASL_IAM`, `SASL_SCRAM`, or `TLS`. |
| clientSubnets | Array of type string | True | The list of subnets in the client VPC to connect to. |
| securityGroups | Array of type string | False | The security groups to attach to the ENIs for the broker nodes. |
| tags | object | False | Create tags when creating the VPC connection. |
| targetClusterArn | string | True | The Amazon Resource Name (ARN) of the cluster. |
| vpcId | string | True | The VPC id of the remote client. |

### CreateVpcConnectionResponse
<a name="vpc-connection-model-createvpcconnectionresponse"></a>

Returns information about the created VPC connection.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| authentication | string<br />MinLength: 3<br />MaxLength: 10 | False | The type of authentication to be uses by remote clients. |
| clientSubnets | Array of type string | False | The list of subnets in the client VPC to connect to. |
| creationTime | string | False | The time when the VPC connection was created. |
| securityGroups | Array of type string | False | The security groups to attach to the ENIs for the broker nodes. |
| state | [VpcConnectionState](#vpc-connection-model-vpcconnectionstate) | False | State of the VPC connection. |
| tags | object | False | Tags attached to the VPC connection. |
| vpcConnectionArn | string | False | The Amazon Resource Name (ARN) of the remote VPC connection. |
| vpcId | string | False | The VPC id of the remote client. |

### Error
<a name="vpc-connection-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### VpcConnectionState
<a name="vpc-connection-model-vpcconnectionstate"></a>

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
<a name="vpc-connection-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### CreateVpcConnection
<a name="CreateVpcConnection-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/CreateVpcConnection)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/CreateVpcConnection)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/CreateVpcConnection)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/CreateVpcConnection)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/CreateVpcConnection)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/CreateVpcConnection)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/CreateVpcConnection)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/CreateVpcConnection)
+ [AWS SDK for Python (Boto3)](/goto/boto3/kafka-2018-11-14/CreateVpcConnection)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/CreateVpcConnection)
