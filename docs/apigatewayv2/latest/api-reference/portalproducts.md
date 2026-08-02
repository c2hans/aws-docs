---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portalproducts.html
---

# Portal products
<a name="portalproducts"></a>

Represents the collection of portal products.

## URI
<a name="portalproducts-url"></a>

`/v2/portalproducts`

## HTTP methods
<a name="portalproducts-http-methods"></a>

### GET
<a name="portalproductsget"></a>

**Operation ID:** `ListPortalProducts`

Lists portal products.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| resourceOwner | String | False | The resource owner of the portal product. |
| nextToken | String | False | The next page of elements from this collection. Not valid for the last element of the collection. |
| maxResults | String | False | The maximum number of elements to be returned for this resource. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListPortalProductsResponseContent | Success |
| 400 | BadRequestExceptionResponseContent | One of the parameters in the request is invalid. |
| 403 | AccessDeniedExceptionResponseContent | 403 response |
| 429 | LimitExceededExceptionResponseContent | The client is sending more than the allowed number of requests per unit of time. |

### POST
<a name="portalproductspost"></a>

**Operation ID:** `CreatePortalProduct`

Creates a new portal product.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | CreatePortalProductResponseContent | The request has succeeded and has resulted in the creation of a resource. |
| 400 | BadRequestExceptionResponseContent | One of the parameters in the request is invalid. |
| 403 | AccessDeniedExceptionResponseContent | 403 response |
| 429 | LimitExceededExceptionResponseContent | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="portalproducts-schemas"></a>

### Request bodies
<a name="portalproducts-request-examples"></a>

#### POST schema
<a name="portalproducts-request-body-post-example"></a>

```
{
  "displayName": "string",
  "description": "string",
  "tags": {
  }
}
```

### Response bodies
<a name="portalproducts-response-examples"></a>

#### ListPortalProductsResponseContent schema
<a name="portalproducts-response-body-listportalproductsresponsecontent-example"></a>

```
{
  "nextToken": "string",
  "items": [
    {
      "displayName": "string",
      "description": "string",
      "portalProductId": "string",
      "portalProductArn": "string",
      "lastModified": "string",
      "tags": {
      }
    }
  ]
}
```

#### CreatePortalProductResponseContent schema
<a name="portalproducts-response-body-createportalproductresponsecontent-example"></a>

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
<a name="portalproducts-response-body-badrequestexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedExceptionResponseContent schema
<a name="portalproducts-response-body-accessdeniedexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceededExceptionResponseContent schema
<a name="portalproducts-response-body-limitexceededexceptionresponsecontent-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="portalproducts-properties"></a>

### AccessDeniedExceptionResponseContent
<a name="portalproducts-model-accessdeniedexceptionresponsecontent"></a>

The error message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The message. |

### BadRequestExceptionResponseContent
<a name="portalproducts-model-badrequestexceptionresponsecontent"></a>

The response content for bad request exception.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The message of the bad request exception response content. |

### CreatePortalProductRequestContent
<a name="portalproducts-model-createportalproductrequestcontent"></a>

Creates a portal product.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| description | string<br />MinLength: 0<br />MaxLength: 1024 | False | A description of the portal product. |
| displayName | string<br />MinLength: 1<br />MaxLength: 255 | True | The name of the portal product as it appears in a published portal. |
| tags | [Tags](#portalproducts-model-tags) | False | The collection of tags. Each tag element is associated with a given resource. |

### CreatePortalProductResponseContent
<a name="portalproducts-model-createportalproductresponsecontent"></a>

Creates a portal product.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| description | string<br />MinLength: 0<br />MaxLength: 1024 | False | A description of the portal product. |
| displayName | string<br />MinLength: 1<br />MaxLength: 255 | True | The display name for the portal product. |
| displayOrder | [DisplayOrder](#portalproducts-model-displayorder) | False | The visual ordering of the product pages and product REST endpoint pages in a published portal. |
| lastModified | string<br />Format: date-time | True | The timestamp when the portal product was last modified. |
| portalProductArn | string<br />MinLength: 20<br />MaxLength: 2048 | True | The ARN of the portal product. |
| portalProductId | string<br />Pattern: `^[a-z0-9]+$`<br />MinLength: 10<br />MaxLength: 30 | True | The portal product identifier. |
| tags | [Tags](#portalproducts-model-tags) | False | The collection of tags. Each tag element is associated with a given resource. |

### DisplayOrder
<a name="portalproducts-model-displayorder"></a>

The display order.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| contents | Array of type [Section](#portalproducts-model-section) | False | Represents a list of sections which include section name and list of product REST endpoints for a product. |
| overviewPageArn | string<br />MinLength: 20<br />MaxLength: 2048 | False | The ARN of the overview page. |
| productPageArns | Array of type string<br />MinLength: 20<br />MaxLength: 2048 | False | The product page ARNs. |

### LimitExceededExceptionResponseContent
<a name="portalproducts-model-limitexceededexceptionresponsecontent"></a>

The response content for limit exceeded exception.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type of the limit exceeded exception response content. |
| message | string | False | The message of the limit exceeded exception response content. |

### ListPortalProductsResponseContent
<a name="portalproducts-model-listportalproductsresponsecontent"></a>

Lists portal products.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| items | Array of type [PortalProductSummary](#portalproducts-model-portalproductsummary) | False | The elements from this collection. |
| nextToken | string<br />MinLength: 1<br />MaxLength: 2048 | False | The next page of elements from this collection. Not valid for the last element of the collection. |

### PortalProductSummary
<a name="portalproducts-model-portalproductsummary"></a>

Represents a portal product.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| description | string<br />MinLength: 0<br />MaxLength: 1024 | True | The description. |
| displayName | string<br />MinLength: 1<br />MaxLength: 255 | True | The display name of a portal product. |
| lastModified | string<br />Format: date-time | True | The timestamp when the portal product was last modified. |
| portalProductArn | string<br />MinLength: 20<br />MaxLength: 2048 | True | The ARN of a portal product. |
| portalProductId | string<br />Pattern: `^[a-z0-9]+$`<br />MinLength: 10<br />MaxLength: 30 | True | The portal product identifier. |
| tags | [Tags](#portalproducts-model-tags) | False | The collection of tags. Each tag element is associated with a given resource. |

### Section
<a name="portalproducts-model-section"></a>

Contains the section name and list of product REST endpoints for a product.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| productRestEndpointPageArns | Array of type string<br />MinLength: 20<br />MaxLength: 2048 | True | The ARNs of the product REST endpoint pages in a portal product. |
| sectionName | string | True | The section name. |

### Tags
<a name="portalproducts-model-tags"></a>

Represents a collection of tags associated with the resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

## See also
<a name="portalproducts-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListPortalProducts
<a name="ListPortalProducts-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/ListPortalProducts)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/ListPortalProducts)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/ListPortalProducts)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/ListPortalProducts)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/ListPortalProducts)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/ListPortalProducts)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/ListPortalProducts)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/ListPortalProducts)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/ListPortalProducts)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/ListPortalProducts)

### CreatePortalProduct
<a name="CreatePortalProduct-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/CreatePortalProduct)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/CreatePortalProduct)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/CreatePortalProduct)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/CreatePortalProduct)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/CreatePortalProduct)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/CreatePortalProduct)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/CreatePortalProduct)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/CreatePortalProduct)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/CreatePortalProduct)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/CreatePortalProduct)
