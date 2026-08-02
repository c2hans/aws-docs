---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/vpc-connection-arn.html
---

# Vpc-connection arn
<a name="vpc-connection-arn"></a>

## URI
<a name="vpc-connection-arn-url"></a>

`/v1/vpc-connection/{{arn}}`

## HTTP methods
<a name="vpc-connection-arn-http-methods"></a>

### GET
<a name="vpc-connection-arnget"></a>

**Operation ID:** `DescribeVpcConnection`

Describes Remote VPC Connection.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{arn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its revisions. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  DescribeVpcConnectionResponse | HTTP Status Code 200: OK. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### DELETE
<a name="vpc-connection-arndelete"></a>

**Operation ID:** `DeleteVpcConnection`

Delete remote VPC connection.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{arn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its revisions. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  DeleteVpcConnectionResponse | HTTP Status Code 200: OK. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="vpc-connection-arnoptions"></a>

Enable CORS by returning correct headers.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{arn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its revisions. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method. |

## Schemas
<a name="vpc-connection-arn-schemas"></a>

### Response bodies
<a name="vpc-connection-arn-response-examples"></a>

#### DescribeVpcConnectionResponse schema
<a name="vpc-connection-arn-response-body-describevpcconnectionresponse-example"></a>

```
{
  "vpcConnectionArn": "string",
  "creationTime": "string",
  "targetClusterArn": "string",
  "vpcId": "string",
  "subnets": [
    "string"
  ],
  "securityGroups": [
    "string"
  ],
  "state": enum,
  "tags": {
  },
  "authentication": "string"
}
```

#### DeleteVpcConnectionResponse schema
<a name="vpc-connection-arn-response-body-deletevpcconnectionresponse-example"></a>

```
{
  "vpcConnectionArn": "string",
  "state": enum
}
```

#### Error schema
<a name="vpc-connection-arn-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="vpc-connection-arn-properties"></a>

### DeleteVpcConnectionResponse
<a name="vpc-connection-arn-model-deletevpcconnectionresponse"></a>

Returns information about the deleted VPC connection.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| state | [VpcConnectionState](#vpc-connection-arn-model-vpcconnectionstate) | False | State of the Remote VPC Connection. |
| vpcConnectionArn | string | False | The Amazon Resource Name (ARN) of the Remote VPC. |

### DescribeVpcConnectionResponse
<a name="vpc-connection-arn-model-describevpcconnectionresponse"></a>

Response body for DescribeVpcConnection.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| authentication | string | False | The type of private link authentication. |
| creationTime | string | True | The time when the configuration was created. |
| securityGroups | Array of type string | False | The list of security groups in Remote VPC Connection. |
| state | [VpcConnectionState](#vpc-connection-arn-model-vpcconnectionstate) | False | State of the Remote VPC Connection. |
| subnets | Array of type string | False | The list of subnets in Remote VPC Connection. |
| tags | object | False | Tags attached to the vpc connection. |
| targetClusterArn | string | True | The Amazon Resource Name (ARN) of the target cluster. |
| vpcConnectionArn | string | True | The Amazon Resource Name (ARN) of the Remote VPC. |
| vpcId | string | False | The description of the vpcId. |

### Error
<a name="vpc-connection-arn-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### VpcConnectionState
<a name="vpc-connection-arn-model-vpcconnectionstate"></a>

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
<a name="vpc-connection-arn-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DescribeVpcConnection
<a name="DescribeVpcConnection-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/DescribeVpcConnection)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/DescribeVpcConnection)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/DescribeVpcConnection)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/DescribeVpcConnection)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/DescribeVpcConnection)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/DescribeVpcConnection)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/DescribeVpcConnection)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/DescribeVpcConnection)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/DescribeVpcConnection)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/DescribeVpcConnection)

### DeleteVpcConnection
<a name="DeleteVpcConnection-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/DeleteVpcConnection)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/DeleteVpcConnection)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/DeleteVpcConnection)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/DeleteVpcConnection)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/DeleteVpcConnection)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/DeleteVpcConnection)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/DeleteVpcConnection)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/DeleteVpcConnection)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/DeleteVpcConnection)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/DeleteVpcConnection)
