---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid.html
---

# Product REST endpoint page
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid"></a>

Represents a product REST endpoint page.

## URI
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-url"></a>

`/v2/portalproducts/{{portalProductId}}/productrestendpointpages/{{productRestEndpointPageId}}`

## HTTP methods
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-http-methods"></a>

### GET
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageidget"></a>

**Operation ID:** `GetProductRestEndpointPage`

Gets a product REST endpoint page.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{portalProductId}} | String | True | The portal product identifier. |
| {{productRestEndpointPageId}} | String | True | The product REST endpoint identifier. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| resourceOwnerAccountId | String | False | The account ID of the resource owner of the portal product. |
| includeRawDisplayContent | String | False | The query parameter to include raw display content. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetProductRestEndpointPageResponseContent | Success |
| 400 | BadRequestExceptionResponseContent | One of the parameters in the request is invalid. |
| 403 | AccessDeniedExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | The resource specified in the request was not found. |
| 429 | LimitExceededExceptionResponseContent | The client is sending more than the allowed number of requests per unit of time. |

### DELETE
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageiddelete"></a>

**Operation ID:** `DeleteProductRestEndpointPage`

Deletes a product REST endpoint page.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{productRestEndpointPageId}} | String | True | The product REST endpoint identifier. |
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
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageidpatch"></a>

**Operation ID:** `UpdateProductRestEndpointPage`

Updates a product REST endpoint page.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{productRestEndpointPageId}} | String | True | The product REST endpoint identifier. |
| {{portalProductId}} | String | True | The portal product identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | UpdateProductRestEndpointPageResponseContent | 200 response |
| 400 | BadRequestExceptionResponseContent | One of the parameters in the request is invalid. |
| 403 | AccessDeniedExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | The resource specified in the request was not found. |
| 429 | LimitExceededExceptionResponseContent | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-schemas"></a>

### Request bodies
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-request-examples"></a>

#### PATCH schema
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-request-body-patch-example"></a>

```
{
  "displayContent": {
    "none": {
    },
    "overrides": {
      "endpoint": "string",
      "operationName": "string",
      "body": "string"
    }
  },
  "tryItState": enum
}
```

### Response bodies
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-response-examples"></a>

#### GetProductRestEndpointPageResponseContent schema
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-response-body-getproductrestendpointpageresponsecontent-example"></a>

```
{
  "displayContent": {
    "endpoint": "string",
    "operationName": "string",
    "body": "string"
  },
  "tryItState": enum,
  "statusException": {
    "exception": "string",
    "message": "string"
  },
  "productRestEndpointPageId": "string",
  "lastModified": "string",
  "restEndpointIdentifier": {
    "identifierParts": {
      "path": "string",
      "stage": "string",
      "method": "string",
      "restApiId": "string"
    }
  },
  "rawDisplayContent": "string",
  "productRestEndpointPageArn": "string",
  "status": enum
}
```

#### UpdateProductRestEndpointPageResponseContent schema
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-response-body-updateproductrestendpointpageresponsecontent-example"></a>

```
{
  "displayContent": {
    "endpoint": "string",
    "operationName": "string",
    "body": "string"
  },
  "tryItState": enum,
  "statusException": {
    "exception": "string",
    "message": "string"
  },
  "productRestEndpointPageId": "string",
  "lastModified": "string",
  "restEndpointIdentifier": {
    "identifierParts": {
      "path": "string",
      "stage": "string",
      "method": "string",
      "restApiId": "string"
    }
  },
  "productRestEndpointPageArn": "string",
  "status": enum
}
```

#### BadRequestExceptionResponseContent schema
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-response-body-badrequestexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedExceptionResponseContent schema
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-response-body-accessdeniedexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundExceptionResponseContent schema
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-response-body-notfoundexceptionresponsecontent-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededExceptionResponseContent schema
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-response-body-limitexceededexceptionresponsecontent-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-properties"></a>

### AccessDeniedExceptionResponseContent
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-accessdeniedexceptionresponsecontent"></a>

The error message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The message. |

### BadRequestExceptionResponseContent
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-badrequestexceptionresponsecontent"></a>

The response content for bad request exception.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The message of the bad request exception response content. |

### DisplayContentOverrides
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-displaycontentoverrides"></a>

Contains any values that override the default configuration generated from API Gateway.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| body | string<br />MinLength: 1<br />MaxLength: 32768 | False | By default, this is the documentation of your REST API from API Gateway. You can provide custom documentation to override this value. |
| endpoint | string<br />MinLength: 1<br />MaxLength: 1024 | False | The URL for your REST API. By default, API Gateway uses the default execute API endpoint. You can provide a custom domain to override this value. |
| operationName | string<br />MinLength: 1<br />MaxLength: 255 | False | The operation name of the product REST endpoint. |

### EndpointDisplayContent
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-endpointdisplaycontent"></a>

Represents the endpoint display content.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| none | [None](#portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-none) | False | If your product REST endpoint contains no overrides, the none object is returned. |
| overrides | [DisplayContentOverrides](#portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-displaycontentoverrides) | False | The overrides for endpoint display content. |

### EndpointDisplayContentResponse
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-endpointdisplaycontentresponse"></a>

The product REST endpoint page.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| body | string<br />MinLength: 1<br />MaxLength: 32768 | False | The API documentation. |
| endpoint | string<br />MinLength: 1<br />MaxLength: 1024 | True | The URL to invoke your REST API. |
| operationName | string<br />MinLength: 1<br />MaxLength: 255 | False | The operation name. |

### GetProductRestEndpointPageResponseContent
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-getproductrestendpointpageresponsecontent"></a>

Gets a product REST endpoint page.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| displayContent | [EndpointDisplayContentResponse](#portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-endpointdisplaycontentresponse) | True | The content of the product REST endpoint page. |
| lastModified | string<br />Format: date-time | True | The timestamp when the product REST endpoint page was last modified. |
| productRestEndpointPageArn | string<br />MinLength: 20<br />MaxLength: 2048 | True | The ARN of the product REST endpoint page. |
| productRestEndpointPageId | string<br />Pattern: `^[a-z0-9]+$`<br />MinLength: 10<br />MaxLength: 30 | True | The product REST endpoint page identifier. |
| rawDisplayContent | string | False | The raw display content of the product REST endpoint page. |
| restEndpointIdentifier | [RestEndpointIdentifier](#portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-restendpointidentifier) | True | The REST endpoint identifier. |
| status | [Status](#portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-status) | True | The status of the product REST endpoint page. |
| statusException | [StatusException](#portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-statusexception) | False | The status exception information. |
| tryItState | [TryItState](#portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-tryitstate) | True | The try it state. |

### IdentifierParts
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-identifierparts"></a>

The identifier parts of a product REST endpoint.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| method | string<br />MinLength: 1<br />MaxLength: 20 | True | The method of the product REST endpoint. |
| path | string<br />MinLength: 1<br />MaxLength: 4096 | True | The path of the product REST endpoint. |
| restApiId | string<br />MinLength: 1<br />MaxLength: 50 | True | The REST API ID of the product REST endpoint. |
| stage | string<br />MinLength: 1<br />MaxLength: 128 | True | The stage of the product REST endpoint. |

### LimitExceededExceptionResponseContent
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-limitexceededexceptionresponsecontent"></a>

The response content for limit exceeded exception.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type of the limit exceeded exception response content. |
| message | string | False | The message of the limit exceeded exception response content. |

### None
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-none"></a>

The none option.

### NotFoundExceptionResponseContent
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-notfoundexceptionresponsecontent"></a>

The response content for not found exception.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The message of the not found exception response content. |
| resourceType | string | False | The resource type of the not found exception response content. |

### RestEndpointIdentifier
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-restendpointidentifier"></a>

The REST API endpoint identifier.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| identifierParts | [IdentifierParts](#portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-identifierparts) | False | The identifier parts of the REST endpoint identifier. |

### Status
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-status"></a>

The status.
+ `AVAILABLE`
+ `IN_PROGRESS`
+ `FAILED`

### StatusException
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-statusexception"></a>

Represents a StatusException.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| exception | string<br />MinLength: 1<br />MaxLength: 256 | False | The exception. |
| message | string<br />MinLength: 1<br />MaxLength: 2048 | False | The error message. |

### TryItState
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-tryitstate"></a>

Represents the try it state for a product REST endpoint page.
+ `ENABLED`
+ `DISABLED`

### UpdateProductRestEndpointPageRequestContent
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-updateproductrestendpointpagerequestcontent"></a>

Updates a product REST endpoint page.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| displayContent | [EndpointDisplayContent](#portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-endpointdisplaycontent) | False | The display content. |
| tryItState | [TryItState](#portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-tryitstate) | False | The try it state of a product REST endpoint page. |

### UpdateProductRestEndpointPageResponseContent
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-updateproductrestendpointpageresponsecontent"></a>

Update a product REST endpoint page.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| displayContent | [EndpointDisplayContentResponse](#portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-endpointdisplaycontentresponse) | True | The content of the product REST endpoint page. |
| lastModified | string<br />Format: date-time | True | The timestamp when the product REST endpoint page was last modified. |
| productRestEndpointPageArn | string<br />MinLength: 20<br />MaxLength: 2048 | True | The ARN of the product REST endpoint page. |
| productRestEndpointPageId | string<br />Pattern: `^[a-z0-9]+$`<br />MinLength: 10<br />MaxLength: 30 | True | The product REST endpoint page identifier. |
| restEndpointIdentifier | [RestEndpointIdentifier](#portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-restendpointidentifier) | True | The REST endpoint identifier. |
| status | [Status](#portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-status) | True | The status. |
| statusException | [StatusException](#portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-statusexception) | False | The status exception information. |
| tryItState | [TryItState](#portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-model-tryitstate) | True | The try it state of a product REST endpoint page. |

## See also
<a name="portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetProductRestEndpointPage
<a name="GetProductRestEndpointPage-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/GetProductRestEndpointPage)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/GetProductRestEndpointPage)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/GetProductRestEndpointPage)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/GetProductRestEndpointPage)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/GetProductRestEndpointPage)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/GetProductRestEndpointPage)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/GetProductRestEndpointPage)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/GetProductRestEndpointPage)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/GetProductRestEndpointPage)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/GetProductRestEndpointPage)

### DeleteProductRestEndpointPage
<a name="DeleteProductRestEndpointPage-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/DeleteProductRestEndpointPage)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/DeleteProductRestEndpointPage)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/DeleteProductRestEndpointPage)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/DeleteProductRestEndpointPage)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/DeleteProductRestEndpointPage)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/DeleteProductRestEndpointPage)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/DeleteProductRestEndpointPage)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/DeleteProductRestEndpointPage)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/DeleteProductRestEndpointPage)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/DeleteProductRestEndpointPage)

### UpdateProductRestEndpointPage
<a name="UpdateProductRestEndpointPage-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/UpdateProductRestEndpointPage)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/UpdateProductRestEndpointPage)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/UpdateProductRestEndpointPage)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/UpdateProductRestEndpointPage)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/UpdateProductRestEndpointPage)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/UpdateProductRestEndpointPage)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/UpdateProductRestEndpointPage)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/UpdateProductRestEndpointPage)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/UpdateProductRestEndpointPage)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/UpdateProductRestEndpointPage)
