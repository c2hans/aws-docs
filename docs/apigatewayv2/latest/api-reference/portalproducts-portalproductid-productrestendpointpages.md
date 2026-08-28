---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portalproducts-portalproductid-productrestendpointpages.html
---

# Product REST endpoint pages
<a name="portalproducts-portalproductid-productrestendpointpages"></a>

Represents the collection of product REST endpoint pages for a portal product.

## URI
<a name="portalproducts-portalproductid-productrestendpointpages-url"></a>

`/v2/portalproducts/{{portalProductId}}/productrestendpointpages`

## HTTP methods
<a name="portalproducts-portalproductid-productrestendpointpages-http-methods"></a>

### GET
<a name="portalproducts-portalproductid-productrestendpointpagesget"></a>

**Operation ID:** `ListProductRestEndpointPages`

Lists the product REST endpoint pages of a portal product.

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
| 200 | ListProductRestEndpointPagesResponseContent | Success |
| 400 | BadRequestExceptionResponseContent | One of the parameters in the request is invalid. |
| 403 | AccessDeniedExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | The resource specified in the request was not found. |
| 429 | LimitExceededExceptionResponseContent | The client is sending more than the allowed number of requests per unit of time. |

### POST
<a name="portalproducts-portalproductid-productrestendpointpagespost"></a>

**Operation ID:** `CreateProductRestEndpointPage`

Creates a product REST endpoint page for a portal product.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{portalProductId}} | String | True | The portal product identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | CreateProductRestEndpointPageResponseContent | The request has succeeded and has resulted in the creation of a resource. |
| 400 | BadRequestExceptionResponseContent | One of the parameters in the request is invalid. |
| 403 | AccessDeniedExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | The resource specified in the request was not found. |
| 429 | LimitExceededExceptionResponseContent | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="portalproducts-portalproductid-productrestendpointpages-schemas"></a>

### Request bodies
<a name="portalproducts-portalproductid-productrestendpointpages-request-examples"></a>

#### POST schema
<a name="portalproducts-portalproductid-productrestendpointpages-request-body-post-example"></a>

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
  "tryItState": enum,
  "restEndpointIdentifier": {
    "identifierParts": {
      "path": "string",
      "stage": "string",
      "method": "string",
      "restApiId": "string"
    }
  }
}
```

### Response bodies
<a name="portalproducts-portalproductid-productrestendpointpages-response-examples"></a>

#### ListProductRestEndpointPagesResponseContent schema
<a name="portalproducts-portalproductid-productrestendpointpages-response-body-listproductrestendpointpagesresponsecontent-example"></a>

```
{
  "nextToken": "string",
  "items": [
    {
      "endpoint": "string",
      "tryItState": enum,
      "statusException": {
        "exception": "string",
        "message": "string"
      },
      "productRestEndpointPageId": "string",
      "operationName": "string",
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
  ]
}
```

#### CreateProductRestEndpointPageResponseContent schema
<a name="portalproducts-portalproductid-productrestendpointpages-response-body-createproductrestendpointpageresponsecontent-example"></a>

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
<a name="portalproducts-portalproductid-productrestendpointpages-response-body-badrequestexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedExceptionResponseContent schema
<a name="portalproducts-portalproductid-productrestendpointpages-response-body-accessdeniedexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundExceptionResponseContent schema
<a name="portalproducts-portalproductid-productrestendpointpages-response-body-notfoundexceptionresponsecontent-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededExceptionResponseContent schema
<a name="portalproducts-portalproductid-productrestendpointpages-response-body-limitexceededexceptionresponsecontent-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="portalproducts-portalproductid-productrestendpointpages-properties"></a>

### AccessDeniedExceptionResponseContent
<a name="portalproducts-portalproductid-productrestendpointpages-model-accessdeniedexceptionresponsecontent"></a>

The error message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The message. |

### BadRequestExceptionResponseContent
<a name="portalproducts-portalproductid-productrestendpointpages-model-badrequestexceptionresponsecontent"></a>

The response content for bad request exception.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The message of the bad request exception response content. |

### CreateProductRestEndpointPageRequestContent
<a name="portalproducts-portalproductid-productrestendpointpages-model-createproductrestendpointpagerequestcontent"></a>

Creates a product REST endpoint page.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| displayContent | [EndpointDisplayContent](#portalproducts-portalproductid-productrestendpointpages-model-endpointdisplaycontent) | False | The content of the product REST endpoint page. |
| restEndpointIdentifier | [RestEndpointIdentifier](#portalproducts-portalproductid-productrestendpointpages-model-restendpointidentifier) | True | The REST endpoint identifier. |
| tryItState | [TryItState](#portalproducts-portalproductid-productrestendpointpages-model-tryitstate) | False | The try it state of the product REST endpoint page. |

### CreateProductRestEndpointPageResponseContent
<a name="portalproducts-portalproductid-productrestendpointpages-model-createproductrestendpointpageresponsecontent"></a>

Creates a product REST endpoint page.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| displayContent | [EndpointDisplayContentResponse](#portalproducts-portalproductid-productrestendpointpages-model-endpointdisplaycontentresponse) | True | The display content. |
| lastModified | string<br />Format: date-time | True | The timestamp when the product REST endpoint page was last modified. |
| productRestEndpointPageArn | string<br />MinLength: 20<br />MaxLength: 2048 | True | The ARN of the product REST endpoint page. |
| productRestEndpointPageId | string<br />Pattern: `^[a-z0-9]+$`<br />MinLength: 10<br />MaxLength: 30 | True | The product REST endpoint page identifier. |
| restEndpointIdentifier | [RestEndpointIdentifier](#portalproducts-portalproductid-productrestendpointpages-model-restendpointidentifier) | True | The REST endpoint identifier. |
| status | [Status](#portalproducts-portalproductid-productrestendpointpages-model-status) | True | The status. |
| statusException | [StatusException](#portalproducts-portalproductid-productrestendpointpages-model-statusexception) | False | The status exception information. |
| tryItState | [TryItState](#portalproducts-portalproductid-productrestendpointpages-model-tryitstate) | True | The try it state. |

### DisplayContentOverrides
<a name="portalproducts-portalproductid-productrestendpointpages-model-displaycontentoverrides"></a>

Contains any values that override the default configuration generated from API Gateway.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| body | string<br />MinLength: 1<br />MaxLength: 32768 | False | By default, this is the documentation of your REST API from API Gateway. You can provide custom documentation to override this value. |
| endpoint | string<br />MinLength: 1<br />MaxLength: 1024 | False | The URL for your REST API. By default, API Gateway uses the default execute API endpoint. You can provide a custom domain to override this value. |
| operationName | string<br />MinLength: 1<br />MaxLength: 255 | False | The operation name of the product REST endpoint. |

### EndpointDisplayContent
<a name="portalproducts-portalproductid-productrestendpointpages-model-endpointdisplaycontent"></a>

Represents the endpoint display content.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| none | [None](#portalproducts-portalproductid-productrestendpointpages-model-none) | False | If your product REST endpoint contains no overrides, the none object is returned. |
| overrides | [DisplayContentOverrides](#portalproducts-portalproductid-productrestendpointpages-model-displaycontentoverrides) | False | The overrides for endpoint display content. |

### EndpointDisplayContentResponse
<a name="portalproducts-portalproductid-productrestendpointpages-model-endpointdisplaycontentresponse"></a>

The product REST endpoint page.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| body | string<br />MinLength: 1<br />MaxLength: 32768 | False | The API documentation. |
| endpoint | string<br />MinLength: 1<br />MaxLength: 1024 | True | The URL to invoke your REST API. |
| operationName | string<br />MinLength: 1<br />MaxLength: 255 | False | The operation name. |

### IdentifierParts
<a name="portalproducts-portalproductid-productrestendpointpages-model-identifierparts"></a>

The identifier parts of a product REST endpoint.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| method | string<br />MinLength: 1<br />MaxLength: 20 | True | The method of the product REST endpoint. |
| path | string<br />MinLength: 1<br />MaxLength: 4096 | True | The path of the product REST endpoint. |
| restApiId | string<br />MinLength: 1<br />MaxLength: 50 | True | The REST API ID of the product REST endpoint. |
| stage | string<br />MinLength: 1<br />MaxLength: 128 | True | The stage of the product REST endpoint. |

### LimitExceededExceptionResponseContent
<a name="portalproducts-portalproductid-productrestendpointpages-model-limitexceededexceptionresponsecontent"></a>

The response content for limit exceeded exception.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type of the limit exceeded exception response content. |
| message | string | False | The message of the limit exceeded exception response content. |

### ListProductRestEndpointPagesResponseContent
<a name="portalproducts-portalproductid-productrestendpointpages-model-listproductrestendpointpagesresponsecontent"></a>

Lists the product rest endpoint pages in a portal product.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| items | Array of type [ProductRestEndpointPageSummaryNoBody](#portalproducts-portalproductid-productrestendpointpages-model-productrestendpointpagesummarynobody) | True | The elements from this collection. |
| nextToken | string | False | The next page of elements from this collection. Not valid for the last element of the collection. |

### None
<a name="portalproducts-portalproductid-productrestendpointpages-model-none"></a>

The none option.

### NotFoundExceptionResponseContent
<a name="portalproducts-portalproductid-productrestendpointpages-model-notfoundexceptionresponsecontent"></a>

The response content for not found exception.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The message of the not found exception response content. |
| resourceType | string | False | The resource type of the not found exception response content. |

### ProductRestEndpointPageSummaryNoBody
<a name="portalproducts-portalproductid-productrestendpointpages-model-productrestendpointpagesummarynobody"></a>

A summary of a product REST endpoint page, without providing the page content.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| endpoint | string<br />MinLength: 1<br />MaxLength: 1024 | True | The endpoint of the product REST endpoint page. |
| lastModified | string<br />Format: date-time | True | The timestamp when the product REST endpoint page was last modified. |
| operationName | string<br />MinLength: 1<br />MaxLength: 255 | False | The operation name of the product REST endpoint. |
| productRestEndpointPageArn | string<br />MinLength: 20<br />MaxLength: 2048 | True | The ARN of the product REST endpoint page. |
| productRestEndpointPageId | string<br />Pattern: `^[a-z0-9]+$`<br />MinLength: 10<br />MaxLength: 30 | True | The product REST endpoint page identifier. |
| restEndpointIdentifier | [RestEndpointIdentifier](#portalproducts-portalproductid-productrestendpointpages-model-restendpointidentifier) | True | The REST endpoint identifier. |
| status | [Status](#portalproducts-portalproductid-productrestendpointpages-model-status) | True | The status. |
| statusException | [StatusException](#portalproducts-portalproductid-productrestendpointpages-model-statusexception) | False | The status exception information. |
| tryItState | [TryItState](#portalproducts-portalproductid-productrestendpointpages-model-tryitstate) | True | The try it state of a product REST endpoint page. |

### RestEndpointIdentifier
<a name="portalproducts-portalproductid-productrestendpointpages-model-restendpointidentifier"></a>

The REST API endpoint identifier.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| identifierParts | [IdentifierParts](#portalproducts-portalproductid-productrestendpointpages-model-identifierparts) | False | The identifier parts of the REST endpoint identifier. |

### Status
<a name="portalproducts-portalproductid-productrestendpointpages-model-status"></a>

The status.
+ `AVAILABLE`
+ `IN_PROGRESS`
+ `FAILED`

### StatusException
<a name="portalproducts-portalproductid-productrestendpointpages-model-statusexception"></a>

Represents a StatusException.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| exception | string<br />MinLength: 1<br />MaxLength: 256 | False | The exception. |
| message | string<br />MinLength: 1<br />MaxLength: 2048 | False | The error message. |

### TryItState
<a name="portalproducts-portalproductid-productrestendpointpages-model-tryitstate"></a>

Represents the try it state for a product REST endpoint page.
+ `ENABLED`
+ `DISABLED`

## See also
<a name="portalproducts-portalproductid-productrestendpointpages-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListProductRestEndpointPages
<a name="ListProductRestEndpointPages-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/ListProductRestEndpointPages)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/ListProductRestEndpointPages)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/ListProductRestEndpointPages)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/ListProductRestEndpointPages)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/ListProductRestEndpointPages)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/ListProductRestEndpointPages)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/ListProductRestEndpointPages)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/ListProductRestEndpointPages)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/ListProductRestEndpointPages)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/ListProductRestEndpointPages)

### CreateProductRestEndpointPage
<a name="CreateProductRestEndpointPage-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/CreateProductRestEndpointPage)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/CreateProductRestEndpointPage)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/CreateProductRestEndpointPage)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/CreateProductRestEndpointPage)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/CreateProductRestEndpointPage)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/CreateProductRestEndpointPage)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/CreateProductRestEndpointPage)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/CreateProductRestEndpointPage)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/CreateProductRestEndpointPage)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/CreateProductRestEndpointPage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigatewayv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
