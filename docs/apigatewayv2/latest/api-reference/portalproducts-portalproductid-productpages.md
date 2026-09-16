---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portalproducts-portalproductid-productpages.html
---

# Product pages
<a name="portalproducts-portalproductid-productpages"></a>

Represents the collection of product pages for a portal product.

## URI
<a name="portalproducts-portalproductid-productpages-url"></a>

`/v2/portalproducts/{{portalProductId}}/productpages`

## HTTP methods
<a name="portalproducts-portalproductid-productpages-http-methods"></a>

### GET
<a name="portalproducts-portalproductid-productpagesget"></a>

**Operation ID:** `ListProductPages`

Lists the product pages for a portal product.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{portalProductId}} | String | True | The portal product identifier. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The next page of elements from this collection. Not valid for the last element of the collection. |
| maxResults | String | False | The maximum number of elements to be returned for this resource. |
| resourceOwnerAccountId | String | False | The account ID of the resource owner of the portal product. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListProductPagesResponseContent | Success |
| 400 | BadRequestExceptionResponseContent | One of the parameters in the request is invalid. |
| 403 | AccessDeniedExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | The resource specified in the request was not found. |
| 429 | LimitExceededExceptionResponseContent | The client is sending more than the allowed number of requests per unit of time. |

### POST
<a name="portalproducts-portalproductid-productpagespost"></a>

**Operation ID:** `CreateProductPage`

Creates a new product page for a portal product.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{portalProductId}} | String | True | The portal product identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | CreateProductPageResponseContent | The request has succeeded and has resulted in the creation of a resource. |
| 400 | BadRequestExceptionResponseContent | One of the parameters in the request is invalid. |
| 403 | AccessDeniedExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | The resource specified in the request was not found. |
| 429 | LimitExceededExceptionResponseContent | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="portalproducts-portalproductid-productpages-schemas"></a>

### Request bodies
<a name="portalproducts-portalproductid-productpages-request-examples"></a>

#### POST schema
<a name="portalproducts-portalproductid-productpages-request-body-post-example"></a>

```
{
  "displayContent": {
    "title": "string",
    "body": "string"
  }
}
```

### Response bodies
<a name="portalproducts-portalproductid-productpages-response-examples"></a>

#### ListProductPagesResponseContent schema
<a name="portalproducts-portalproductid-productpages-response-body-listproductpagesresponsecontent-example"></a>

```
{
  "nextToken": "string",
  "items": [
    {
      "pageTitle": "string",
      "productPageId": "string",
      "lastModified": "string",
      "productPageArn": "string"
    }
  ]
}
```

#### CreateProductPageResponseContent schema
<a name="portalproducts-portalproductid-productpages-response-body-createproductpageresponsecontent-example"></a>

```
{
  "displayContent": {
    "title": "string",
    "body": "string"
  },
  "productPageId": "string",
  "lastModified": "string",
  "productPageArn": "string"
}
```

#### BadRequestExceptionResponseContent schema
<a name="portalproducts-portalproductid-productpages-response-body-badrequestexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedExceptionResponseContent schema
<a name="portalproducts-portalproductid-productpages-response-body-accessdeniedexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundExceptionResponseContent schema
<a name="portalproducts-portalproductid-productpages-response-body-notfoundexceptionresponsecontent-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededExceptionResponseContent schema
<a name="portalproducts-portalproductid-productpages-response-body-limitexceededexceptionresponsecontent-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="portalproducts-portalproductid-productpages-properties"></a>

### AccessDeniedExceptionResponseContent
<a name="portalproducts-portalproductid-productpages-model-accessdeniedexceptionresponsecontent"></a>

The error message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The message. |

### BadRequestExceptionResponseContent
<a name="portalproducts-portalproductid-productpages-model-badrequestexceptionresponsecontent"></a>

The response content for bad request exception.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The message of the bad request exception response content. |

### CreateProductPageRequestContent
<a name="portalproducts-portalproductid-productpages-model-createproductpagerequestcontent"></a>

Creates a product page.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| displayContent | [DisplayContent](#portalproducts-portalproductid-productpages-model-displaycontent) | True | The content of the product page. |

### CreateProductPageResponseContent
<a name="portalproducts-portalproductid-productpages-model-createproductpageresponsecontent"></a>

Creates a product page.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| displayContent | [DisplayContent](#portalproducts-portalproductid-productpages-model-displaycontent) | False | The content of the product page. |
| lastModified | string<br />Format: date-time | True | The timestamp when the product page was last modified. |
| productPageArn | string<br />MinLength: 20<br />MaxLength: 2048 | True | The ARN of the product page. |
| productPageId | string<br />Pattern: `^[a-z0-9]+$`<br />MinLength: 10<br />MaxLength: 30 | True | The product page identifier. |

### DisplayContent
<a name="portalproducts-portalproductid-productpages-model-displaycontent"></a>

The content of the product page.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| body | string<br />MinLength: 1<br />MaxLength: 32768 | True | The body. |
| title | string<br />MinLength: 1<br />MaxLength: 255 | True | The title. |

### LimitExceededExceptionResponseContent
<a name="portalproducts-portalproductid-productpages-model-limitexceededexceptionresponsecontent"></a>

The response content for limit exceeded exception.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type of the limit exceeded exception response content. |
| message | string | False | The message of the limit exceeded exception response content. |

### ListProductPagesResponseContent
<a name="portalproducts-portalproductid-productpages-model-listproductpagesresponsecontent"></a>

Lists product pages.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| items | Array of type [ProductPageSummaryNoBody](#portalproducts-portalproductid-productpages-model-productpagesummarynobody) | True | The elements from this collection. |
| nextToken | string<br />MinLength: 1<br />MaxLength: 2048 | False | The next page of elements from this collection. Not valid for the last element of the collection. |

### NotFoundExceptionResponseContent
<a name="portalproducts-portalproductid-productpages-model-notfoundexceptionresponsecontent"></a>

The response content for not found exception.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The message of the not found exception response content. |
| resourceType | string | False | The resource type of the not found exception response content. |

### ProductPageSummaryNoBody
<a name="portalproducts-portalproductid-productpages-model-productpagesummarynobody"></a>

Represents a product page summary without listing any page content.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| lastModified | string<br />Format: date-time | True | The timestamp when the product page was last modified. |
| pageTitle | string<br />MinLength: 1<br />MaxLength: 255 | True | The page title. |
| productPageArn | string<br />MinLength: 20<br />MaxLength: 2048 | True | The ARN of the product page. |
| productPageId | string<br />Pattern: `^[a-z0-9]+$`<br />MinLength: 10<br />MaxLength: 30 | True | The product page identifier. |

## See also
<a name="portalproducts-portalproductid-productpages-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListProductPages
<a name="ListProductPages-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/ListProductPages)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/ListProductPages)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/ListProductPages)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/ListProductPages)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/ListProductPages)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/ListProductPages)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/ListProductPages)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/ListProductPages)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/ListProductPages)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/ListProductPages)

### CreateProductPage
<a name="CreateProductPage-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/CreateProductPage)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/CreateProductPage)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/CreateProductPage)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/CreateProductPage)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/CreateProductPage)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/CreateProductPage)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/CreateProductPage)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/CreateProductPage)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/CreateProductPage)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/CreateProductPage)
