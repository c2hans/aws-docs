---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/vpclinks-vpclinkid.html
---

# VPCLink
<a name="vpclinks-vpclinkid"></a>

Represents a VPC link. A VPC link enables you to create integrations with private resources in a VPC.

## URI
<a name="vpclinks-vpclinkid-url"></a>

`/v2/vpclinks/{{vpcLinkId}}`

## HTTP methods
<a name="vpclinks-vpclinkid-http-methods"></a>

### GET
<a name="vpclinks-vpclinkidget"></a>

**Operation ID:** `GetVpcLink`

Gets a VPC link.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{vpcLinkId}} | String | True | The ID of the VPC link. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | VpcLink | Success |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### DELETE
<a name="vpclinks-vpclinkiddelete"></a>

**Operation ID:** `DeleteVpcLink`

Deletes a VPC link.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{vpcLinkId}} | String | True | The ID of the VPC link. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 202 | None | 202 response |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### PATCH
<a name="vpclinks-vpclinkidpatch"></a>

**Operation ID:** `UpdateVpcLink`

Updates a VPC link.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{vpcLinkId}} | String | True | The ID of the VPC link. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | VpcLink | 200 response |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="vpclinks-vpclinkid-schemas"></a>

### Request bodies
<a name="vpclinks-vpclinkid-request-examples"></a>

#### PATCH schema
<a name="vpclinks-vpclinkid-request-body-patch-example"></a>

```
{
  "name": "string"
}
```

### Response bodies
<a name="vpclinks-vpclinkid-response-examples"></a>

#### VpcLink schema
<a name="vpclinks-vpclinkid-response-body-vpclink-example"></a>

```
{
  "vpcLinkId": "string",
  "name": "string",
  "subnetIds": [
    "string"
  ],
  "securityGroupIds": [
    "string"
  ],
  "tags": {
  },
  "createdDate": "string",
  "vpcLinkStatus": enum,
  "vpcLinkStatusMessage": "string",
  "vpcLinkVersion": enum
}
```

#### BadRequestException schema
<a name="vpclinks-vpclinkid-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="vpclinks-vpclinkid-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededException schema
<a name="vpclinks-vpclinkid-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="vpclinks-vpclinkid-properties"></a>

### BadRequestException
<a name="vpclinks-vpclinkid-model-badrequestexception"></a>

The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### LimitExceededException
<a name="vpclinks-vpclinkid-model-limitexceededexception"></a>

A limit has been exceeded. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type. |
| message | string | False | Describes the error encountered. |

### NotFoundException
<a name="vpclinks-vpclinkid-model-notfoundexception"></a>

The resource specified in the request was not found. See the `message` field for more information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |
| resourceType | string | False | The resource type. |

### Tags
<a name="vpclinks-vpclinkid-model-tags"></a>

Represents a collection of tags associated with the resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### UpdateVpcLinkInput
<a name="vpclinks-vpclinkid-model-updatevpclinkinput"></a>

Represents the input parameters for an `UpdateVpcLink` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| name | string | False | The name of the VPC link. |

### VpcLink
<a name="vpclinks-vpclinkid-model-vpclink"></a>

Represents a VPC link.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| createdDate | string<br />Format: date-time | False | The timestamp when the VPC link was created. |
| name | string | True | The name of the VPC link. |
| securityGroupIds | Array of type string | True | A list of security group IDs for the VPC link. |
| subnetIds | Array of type string | True | A list of subnet IDs to include in the VPC link. |
| tags | [Tags](#vpclinks-vpclinkid-model-tags) | False | Tags for the VPC link. |
| vpcLinkId | string | True | The ID of the VPC link. |
| vpcLinkStatus | [VpcLinkStatus](#vpclinks-vpclinkid-model-vpclinkstatus) | False | The status of the VPC link. |
| vpcLinkStatusMessage | string | False | A message summarizing the cause of the status of the VPC link. |
| vpcLinkVersion | [VpcLinkVersion](#vpclinks-vpclinkid-model-vpclinkversion) | False | The version of the VPC link. |

### VpcLinkStatus
<a name="vpclinks-vpclinkid-model-vpclinkstatus"></a>

The status of the VPC link.
+ `PENDING`
+ `AVAILABLE`
+ `DELETING`
+ `FAILED`
+ `INACTIVE`

### VpcLinkVersion
<a name="vpclinks-vpclinkid-model-vpclinkversion"></a>

The version of the VPC link.
+ `V2`

## See also
<a name="vpclinks-vpclinkid-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetVpcLink
<a name="GetVpcLink-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/GetVpcLink)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/GetVpcLink)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/GetVpcLink)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/GetVpcLink)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/GetVpcLink)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/GetVpcLink)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/GetVpcLink)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/GetVpcLink)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/GetVpcLink)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/GetVpcLink)

### DeleteVpcLink
<a name="DeleteVpcLink-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/DeleteVpcLink)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/DeleteVpcLink)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/DeleteVpcLink)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/DeleteVpcLink)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/DeleteVpcLink)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/DeleteVpcLink)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/DeleteVpcLink)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/DeleteVpcLink)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/DeleteVpcLink)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/DeleteVpcLink)

### UpdateVpcLink
<a name="UpdateVpcLink-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/UpdateVpcLink)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/UpdateVpcLink)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/UpdateVpcLink)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/UpdateVpcLink)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/UpdateVpcLink)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/UpdateVpcLink)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/UpdateVpcLink)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/UpdateVpcLink)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/UpdateVpcLink)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/UpdateVpcLink)
