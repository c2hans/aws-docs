---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portalproducts-portalproductid-productpages-productpageid.html
---

# Product page
<a name="portalproducts-portalproductid-productpages-productpageid"></a>

Represents a product page.

## URI
<a name="portalproducts-portalproductid-productpages-productpageid-url"></a>

`/v2/portalproducts/{{portalProductId}}/productpages/{{productPageId}}`

## HTTP methods
<a name="portalproducts-portalproductid-productpages-productpageid-http-methods"></a>

### GET
<a name="portalproducts-portalproductid-productpages-productpageidget"></a>

**Operation ID:** `GetProductPage`

Gets a product page of a portal product.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{portalProductId}} | String | True | The portal product identifier. |
| {{productPageId}} | String | True | The portal product identifier. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| resourceOwnerAccountId | String | False | The account ID of the resource owner of the portal product. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetProductPageResponseContent | Success |
| 400 | BadRequestExceptionResponseContent | One of the parameters in the request is invalid. |
| 403 | AccessDeniedExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | The resource specified in the request was not found. |
| 429 | LimitExceededExceptionResponseContent | The client is sending more than the allowed number of requests per unit of time. |

### DELETE
<a name="portalproducts-portalproductid-productpages-productpageiddelete"></a>

**Operation ID:** `DeleteProductPage`

Deletes a product page of a portal product.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{portalProductId}} | String | True | The portal product identifier. |
| {{productPageId}} | String | True | The portal product identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | The request has succeeded, and there is no additional content to send in the response payload body. |
| 400 | BadRequestExceptionResponseContent | One of the parameters in the request is invalid. |
| 403 | AccessDeniedExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | The resource specified in the request was not found. |
| 429 | LimitExceededExceptionResponseContent | The client is sending more than the allowed number of requests per unit of time. |

### PATCH
<a name="portalproducts-portalproductid-productpages-productpageidpatch"></a>

**Operation ID:** `UpdateProductPage`

Updates a product page of a portal product.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{portalProductId}} | String | True | The portal product identifier. |
| {{productPageId}} | String | True | The portal product identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | UpdateProductPageResponseContent | 200 response |
| 400 | BadRequestExceptionResponseContent | One of the parameters in the request is invalid. |
| 403 | AccessDeniedExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | The resource specified in the request was not found. |
| 429 | LimitExceededExceptionResponseContent | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="portalproducts-portalproductid-productpages-productpageid-schemas"></a>

### Request bodies
<a name="portalproducts-portalproductid-productpages-productpageid-request-examples"></a>

#### PATCH schema
<a name="portalproducts-portalproductid-productpages-productpageid-request-body-patch-example"></a>

```
{
  "displayContent": {
    "title": "string",
    "body": "string"
  }
}
```

### Response bodies
<a name="portalproducts-portalproductid-productpages-productpageid-response-examples"></a>

#### GetProductPageResponseContent schema
<a name="portalproducts-portalproductid-productpages-productpageid-response-body-getproductpageresponsecontent-example"></a>

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

#### UpdateProductPageResponseContent schema
<a name="portalproducts-portalproductid-productpages-productpageid-response-body-updateproductpageresponsecontent-example"></a>

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
<a name="portalproducts-portalproductid-productpages-productpageid-response-body-badrequestexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedExceptionResponseContent schema
<a name="portalproducts-portalproductid-productpages-productpageid-response-body-accessdeniedexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundExceptionResponseContent schema
<a name="portalproducts-portalproductid-productpages-productpageid-response-body-notfoundexceptionresponsecontent-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededExceptionResponseContent schema
<a name="portalproducts-portalproductid-productpages-productpageid-response-body-limitexceededexceptionresponsecontent-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="portalproducts-portalproductid-productpages-productpageid-properties"></a>

### AccessDeniedExceptionResponseContent
<a name="portalproducts-portalproductid-productpages-productpageid-model-accessdeniedexceptionresponsecontent"></a>

The error message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The message. |

### BadRequestExceptionResponseContent
<a name="portalproducts-portalproductid-productpages-productpageid-model-badrequestexceptionresponsecontent"></a>

The response content for bad request exception.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The message of the bad request exception response content. |

### DisplayContent
<a name="portalproducts-portalproductid-productpages-productpageid-model-displaycontent"></a>

The content of the product page.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| body | string<br />MinLength: 1<br />MaxLength: 32768 | True | The body. |
| title | string<br />MinLength: 1<br />MaxLength: 255 | True | The title. |

### GetProductPageResponseContent
<a name="portalproducts-portalproductid-productpages-productpageid-model-getproductpageresponsecontent"></a>

Gets a product page.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| displayContent | [DisplayContent](#portalproducts-portalproductid-productpages-productpageid-model-displaycontent) | True | The content of the product page. |
| lastModified | string<br />Format: date-time | True | The timestamp when the product page was last modified. |
| productPageArn | string<br />MinLength: 20<br />MaxLength: 2048 | True | The ARN of the product page. |
| productPageId | string<br />Pattern: `^[a-z0-9]+$`<br />MinLength: 10<br />MaxLength: 30 | True | The product page identifier. |

### LimitExceededExceptionResponseContent
<a name="portalproducts-portalproductid-productpages-productpageid-model-limitexceededexceptionresponsecontent"></a>

The response content for limit exceeded exception.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type of the limit exceeded exception response content. |
| message | string | False | The message of the limit exceeded exception response content. |

### NotFoundExceptionResponseContent
<a name="portalproducts-portalproductid-productpages-productpageid-model-notfoundexceptionresponsecontent"></a>

The response content for not found exception.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The message of the not found exception response content. |
| resourceType | string | False | The resource type of the not found exception response content. |

### UpdateProductPageRequestContent
<a name="portalproducts-portalproductid-productpages-productpageid-model-updateproductpagerequestcontent"></a>

Update a product page.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| displayContent | [DisplayContent](#portalproducts-portalproductid-productpages-productpageid-model-displaycontent) | False | The content of the product page. |

### UpdateProductPageResponseContent
<a name="portalproducts-portalproductid-productpages-productpageid-model-updateproductpageresponsecontent"></a>

Updates a product page.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| displayContent | [DisplayContent](#portalproducts-portalproductid-productpages-productpageid-model-displaycontent) | False | The content of the product page. |
| lastModified | string<br />Format: date-time | True | The timestamp when the product page was last modified. |
| productPageArn | string<br />MinLength: 20<br />MaxLength: 2048 | True | The ARN of the product page. |
| productPageId | string<br />Pattern: `^[a-z0-9]+$`<br />MinLength: 10<br />MaxLength: 30 | True | The product page identifier. |

## See also
<a name="portalproducts-portalproductid-productpages-productpageid-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetProductPage
<a name="GetProductPage-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/GetProductPage)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/GetProductPage)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/GetProductPage)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/GetProductPage)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/GetProductPage)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/GetProductPage)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/GetProductPage)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/GetProductPage)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/GetProductPage)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/GetProductPage)

### DeleteProductPage
<a name="DeleteProductPage-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/DeleteProductPage)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/DeleteProductPage)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/DeleteProductPage)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/DeleteProductPage)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/DeleteProductPage)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/DeleteProductPage)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/DeleteProductPage)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/DeleteProductPage)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/DeleteProductPage)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/DeleteProductPage)

### UpdateProductPage
<a name="UpdateProductPage-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/UpdateProductPage)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/UpdateProductPage)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/UpdateProductPage)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/UpdateProductPage)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/UpdateProductPage)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/UpdateProductPage)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/UpdateProductPage)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/UpdateProductPage)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/UpdateProductPage)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/UpdateProductPage)
