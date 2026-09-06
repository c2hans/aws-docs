---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/vpclinks.html
---

# VPCLinks
<a name="vpclinks"></a>

Represents your VPC links as a collection. A collection offers a paginated view of your VPC links.

## URI
<a name="vpclinks-url"></a>

`/v2/vpclinks`

## HTTP methods
<a name="vpclinks-http-methods"></a>

### GET
<a name="vpclinksget"></a>

**Operation ID:** `GetVpcLinks`

Gets a collection of VPC links.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The next page of elements from this collection. Not valid for the last element of the collection. |
| maxResults | String | False | The maximum number of elements to be returned for this resource. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | VpcLinks | Success |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### POST
<a name="vpclinkspost"></a>

**Operation ID:** `CreateVpcLink`

Creates a VPC link.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | VpcLink | The request has succeeded and has resulted in the creation of a resource. |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="vpclinks-schemas"></a>

### Request bodies
<a name="vpclinks-request-examples"></a>

#### POST schema
<a name="vpclinks-request-body-post-example"></a>

```
{
  "name": "string",
  "subnetIds": [
    "string"
  ],
  "securityGroupIds": [
    "string"
  ],
  "tags": {
  }
}
```

### Response bodies
<a name="vpclinks-response-examples"></a>

#### VpcLinks schema
<a name="vpclinks-response-body-vpclinks-example"></a>

```
{
  "items": [
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
  ],
  "nextToken": "string"
}
```

#### VpcLink schema
<a name="vpclinks-response-body-vpclink-example"></a>

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
<a name="vpclinks-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceededException schema
<a name="vpclinks-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="vpclinks-properties"></a>

### BadRequestException
<a name="vpclinks-model-badrequestexception"></a>

The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### CreateVpcLinkInput
<a name="vpclinks-model-createvpclinkinput"></a>

Represents the input parameters for a `CreateVpcLink` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| name | string | True | The name of the VPC link. |
| securityGroupIds | Array of type string | False | A list of security group IDs for the VPC link. |
| subnetIds | Array of type string | True | A list of subnet IDs to include in the VPC link. |
| tags | [Tags](#vpclinks-model-tags) | False | A list of tags. |

### LimitExceededException
<a name="vpclinks-model-limitexceededexception"></a>

A limit has been exceeded. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type. |
| message | string | False | Describes the error encountered. |

### Tags
<a name="vpclinks-model-tags"></a>

Represents a collection of tags associated with the resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### VpcLink
<a name="vpclinks-model-vpclink"></a>

Represents a VPC link.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| createdDate | string<br />Format: date-time | False | The timestamp when the VPC link was created. |
| name | string | True | The name of the VPC link. |
| securityGroupIds | Array of type string | True | A list of security group IDs for the VPC link. |
| subnetIds | Array of type string | True | A list of subnet IDs to include in the VPC link. |
| tags | [Tags](#vpclinks-model-tags) | False | Tags for the VPC link. |
| vpcLinkId | string | True | The ID of the VPC link. |
| vpcLinkStatus | [VpcLinkStatus](#vpclinks-model-vpclinkstatus) | False | The status of the VPC link. |
| vpcLinkStatusMessage | string | False | A message summarizing the cause of the status of the VPC link. |
| vpcLinkVersion | [VpcLinkVersion](#vpclinks-model-vpclinkversion) | False | The version of the VPC link. |

### VpcLinkStatus
<a name="vpclinks-model-vpclinkstatus"></a>

The status of the VPC link.
+ `PENDING`
+ `AVAILABLE`
+ `DELETING`
+ `FAILED`
+ `INACTIVE`

### VpcLinkVersion
<a name="vpclinks-model-vpclinkversion"></a>

The version of the VPC link.
+ `V2`

### VpcLinks
<a name="vpclinks-model-vpclinks"></a>

Represents a collection of VPCLinks.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| items | Array of type [VpcLink](#vpclinks-model-vpclink) | False | A collection of VPC links. |
| nextToken | string | False | The next page of elements from this collection. Not valid for the last element of the collection. |

## See also
<a name="vpclinks-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetVpcLinks
<a name="GetVpcLinks-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/GetVpcLinks)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/GetVpcLinks)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/GetVpcLinks)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/GetVpcLinks)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/GetVpcLinks)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/GetVpcLinks)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/GetVpcLinks)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/GetVpcLinks)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/GetVpcLinks)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/GetVpcLinks)

### CreateVpcLink
<a name="CreateVpcLink-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/CreateVpcLink)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/CreateVpcLink)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/CreateVpcLink)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/CreateVpcLink)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/CreateVpcLink)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/CreateVpcLink)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/CreateVpcLink)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/CreateVpcLink)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/CreateVpcLink)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/CreateVpcLink)
