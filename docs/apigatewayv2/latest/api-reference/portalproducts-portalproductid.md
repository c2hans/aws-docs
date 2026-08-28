---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portalproducts-portalproductid.html
---

# Portal product
<a name="portalproducts-portalproductid"></a>

Represents a portal product.

## URI
<a name="portalproducts-portalproductid-url"></a>

`/v2/portalproducts/{{portalProductId}}`

## HTTP methods
<a name="portalproducts-portalproductid-http-methods"></a>

### GET
<a name="portalproducts-portalproductidget"></a>

**Operation ID:** `GetPortalProduct`

Gets a portal product.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{portalProductId}} | String | True | The portal product identifier. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| resourceOwnerAccountId | String | False | The account ID of the resource owner of the portal product. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetPortalProductResponseContent | Success |
| 400 | BadRequestExceptionResponseContent | One of the parameters in the request is invalid. |
| 403 | AccessDeniedExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | The resource specified in the request was not found. |
| 429 | LimitExceededExceptionResponseContent | The client is sending more than the allowed number of requests per unit of time. |

### DELETE
<a name="portalproducts-portalproductiddelete"></a>

**Operation ID:** `DeletePortalProduct`

Deletes a portal product.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{portalProductId}} | String | True | The portal product identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | The request has succeeded, and there is no additional content to send in the response payload body. |
| 400 | BadRequestExceptionResponseContent | One of the parameters in the request is invalid. |
| 403 | AccessDeniedExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | The resource specified in the request was not found. |
| 429 | LimitExceededExceptionResponseContent | The client is sending more than the allowed number of requests per unit of time. |

### PATCH
<a name="portalproducts-portalproductidpatch"></a>

**Operation ID:** `UpdatePortalProduct`

Updates the portal product.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{portalProductId}} | String | True | The portal product identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | UpdatePortalProductResponseContent | 200 response |
| 400 | BadRequestExceptionResponseContent | One of the parameters in the request is invalid. |
| 403 | AccessDeniedExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | The resource specified in the request was not found. |
| 429 | LimitExceededExceptionResponseContent | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="portalproducts-portalproductid-schemas"></a>

### Request bodies
<a name="portalproducts-portalproductid-request-examples"></a>

#### PATCH schema
<a name="portalproducts-portalproductid-request-body-patch-example"></a>

```
{
  "displayName": "string",
  "displayOrder": {
    "productPageArns": [
      "string"
    ],
    "contents": [
      {
        "sectionName": "string",
        "productRestEndpointPageArns": [
          "string"
        ]
      }
    ],
    "overviewPageArn": "string"
  },
  "description": "string"
}
```

### Response bodies
<a name="portalproducts-portalproductid-response-examples"></a>

#### GetPortalProductResponseContent schema
<a name="portalproducts-portalproductid-response-body-getportalproductresponsecontent-example"></a>

```
{
  "displayName": "string",
  "displayOrder": {
    "productPageArns": [
      "string"
    ],
    "contents": [
      {
        "sectionName": "string",
        "productRestEndpointPageArns": [
          "string"
        ]
      }
    ],
    "overviewPageArn": "string"
  },
  "description": "string",
  "portalProductId": "string",
  "portalProductArn": "string",
  "lastModified": "string",
  "tags": {
  }
}
```

#### UpdatePortalProductResponseContent schema
<a name="portalproducts-portalproductid-response-body-updateportalproductresponsecontent-example"></a>

```
{
  "displayName": "string",
  "displayOrder": {
    "productPageArns": [
      "string"
    ],
    "contents": [
      {
        "sectionName": "string",
        "productRestEndpointPageArns": [
          "string"
        ]
      }
    ],
    "overviewPageArn": "string"
  },
  "description": "string",
  "portalProductId": "string",
  "portalProductArn": "string",
  "lastModified": "string",
  "tags": {
  }
}
```

#### BadRequestExceptionResponseContent schema
<a name="portalproducts-portalproductid-response-body-badrequestexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedExceptionResponseContent schema
<a name="portalproducts-portalproductid-response-body-accessdeniedexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundExceptionResponseContent schema
<a name="portalproducts-portalproductid-response-body-notfoundexceptionresponsecontent-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededExceptionResponseContent schema
<a name="portalproducts-portalproductid-response-body-limitexceededexceptionresponsecontent-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="portalproducts-portalproductid-properties"></a>

### AccessDeniedExceptionResponseContent
<a name="portalproducts-portalproductid-model-accessdeniedexceptionresponsecontent"></a>

The error message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The message. |

### BadRequestExceptionResponseContent
<a name="portalproducts-portalproductid-model-badrequestexceptionresponsecontent"></a>

The response content for bad request exception.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The message of the bad request exception response content. |

### DisplayOrder
<a name="portalproducts-portalproductid-model-displayorder"></a>

The display order.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| contents | Array of type [Section](#portalproducts-portalproductid-model-section) | False | Represents a list of sections which include section name and list of product REST endpoints for a product. |
| overviewPageArn | string<br />MinLength: 20<br />MaxLength: 2048 | False | The ARN of the overview page. |
| productPageArns | Array of type string<br />MinLength: 20<br />MaxLength: 2048 | False | The product page ARNs. |

### GetPortalProductResponseContent
<a name="portalproducts-portalproductid-model-getportalproductresponsecontent"></a>

Gets a portal product.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| description | string<br />MinLength: 0<br />MaxLength: 1024 | True | The description of a portal product. |
| displayName | string<br />MinLength: 1<br />MaxLength: 255 | True | The display name. |
| displayOrder | [DisplayOrder](#portalproducts-portalproductid-model-displayorder) | True | The display order. |
| lastModified | string<br />Format: date-time | True | The timestamp when the portal product was last modified. |
| portalProductArn | string<br />MinLength: 20<br />MaxLength: 2048 | True | The ARN of the portal product. |
| portalProductId | string<br />Pattern: `^[a-z0-9]+$`<br />MinLength: 10<br />MaxLength: 30 | True | The portal product identifier. |
| tags | [Tags](#portalproducts-portalproductid-model-tags) | False | The collection of tags. Each tag element is associated with a given resource. |

### LimitExceededExceptionResponseContent
<a name="portalproducts-portalproductid-model-limitexceededexceptionresponsecontent"></a>

The response content for limit exceeded exception.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type of the limit exceeded exception response content. |
| message | string | False | The message of the limit exceeded exception response content. |

### NotFoundExceptionResponseContent
<a name="portalproducts-portalproductid-model-notfoundexceptionresponsecontent"></a>

The response content for not found exception.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The message of the not found exception response content. |
| resourceType | string | False | The resource type of the not found exception response content. |

### Section
<a name="portalproducts-portalproductid-model-section"></a>

Contains the section name and list of product REST endpoints for a product.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| productRestEndpointPageArns | Array of type string<br />MinLength: 20<br />MaxLength: 2048 | True | The ARNs of the product REST endpoint pages in a portal product. |
| sectionName | string | True | The section name. |

### Tags
<a name="portalproducts-portalproductid-model-tags"></a>

Represents a collection of tags associated with the resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### UpdatePortalProductRequestContent
<a name="portalproducts-portalproductid-model-updateportalproductrequestcontent"></a>

Updates a portal product.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| description | string<br />MinLength: 0<br />MaxLength: 1024 | False | The description. |
| displayName | string<br />MinLength: 1<br />MaxLength: 255 | False | The displayName. |
| displayOrder | [DisplayOrder](#portalproducts-portalproductid-model-displayorder) | False | The display order. |

### UpdatePortalProductResponseContent
<a name="portalproducts-portalproductid-model-updateportalproductresponsecontent"></a>

Updates a portal product.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| description | string<br />MinLength: 0<br />MaxLength: 1024 | False | The description of the portal product. |
| displayName | string<br />MinLength: 1<br />MaxLength: 255 | True | The display name of a portal product. |
| displayOrder | [DisplayOrder](#portalproducts-portalproductid-model-displayorder) | False | The display order that the portal products will appear in a portal. |
| lastModified | string<br />Format: date-time | True | The timestamp when the portal product was last modified. |
| portalProductArn | string<br />MinLength: 20<br />MaxLength: 2048 | True | The ARN of the portal product. |
| portalProductId | string<br />Pattern: `^[a-z0-9]+$`<br />MinLength: 10<br />MaxLength: 30 | True | The portal product identifier. |
| tags | [Tags](#portalproducts-portalproductid-model-tags) | False | The collection of tags. Each tag element is associated with a given resource. |

## See also
<a name="portalproducts-portalproductid-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetPortalProduct
<a name="GetPortalProduct-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/GetPortalProduct)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/GetPortalProduct)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/GetPortalProduct)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/GetPortalProduct)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/GetPortalProduct)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/GetPortalProduct)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/GetPortalProduct)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/GetPortalProduct)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/GetPortalProduct)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/GetPortalProduct)

### DeletePortalProduct
<a name="DeletePortalProduct-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/DeletePortalProduct)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/DeletePortalProduct)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/DeletePortalProduct)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/DeletePortalProduct)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/DeletePortalProduct)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/DeletePortalProduct)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/DeletePortalProduct)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/DeletePortalProduct)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/DeletePortalProduct)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/DeletePortalProduct)

### UpdatePortalProduct
<a name="UpdatePortalProduct-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/UpdatePortalProduct)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/UpdatePortalProduct)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/UpdatePortalProduct)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/UpdatePortalProduct)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/UpdatePortalProduct)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/UpdatePortalProduct)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/UpdatePortalProduct)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/UpdatePortalProduct)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/UpdatePortalProduct)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/UpdatePortalProduct)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigatewayv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
