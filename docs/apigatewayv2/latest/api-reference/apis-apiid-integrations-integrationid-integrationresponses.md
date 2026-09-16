---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/apis-apiid-integrations-integrationid-integrationresponses.html
---

# IntegrationResponses
<a name="apis-apiid-integrations-integrationid-integrationresponses"></a>

Represents the collection of responses for an integration. Supported only for WebSocket APIs.

## URI
<a name="apis-apiid-integrations-integrationid-integrationresponses-url"></a>

`/v2/apis/{{apiId}}/integrations/{{integrationId}}/integrationresponses`

## HTTP methods
<a name="apis-apiid-integrations-integrationid-integrationresponses-http-methods"></a>

### GET
<a name="apis-apiid-integrations-integrationid-integrationresponsesget"></a>

**Operation ID:** `GetIntegrationResponses`

Gets the `IntegrationResponses` for an `Integration`.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{integrationId}} | String | True | The integration ID. |
| {{apiId}} | String | True | The API identifier. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The next page of elements from this collection. Not valid for the last element of the collection. |
| maxResults | String | False | The maximum number of elements to be returned for this resource. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | IntegrationResponses | Success |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### POST
<a name="apis-apiid-integrations-integrationid-integrationresponsespost"></a>

**Operation ID:** `CreateIntegrationResponse`

Creates an `IntegrationResponses`.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{apiId}} | String | True | The API identifier. |
| {{integrationId}} | String | True | The integration ID. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | IntegrationResponse | The request has succeeded and has resulted in the creation of a resource. |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 409 | ConflictException | The resource already exists. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="apis-apiid-integrations-integrationid-integrationresponses-schemas"></a>

### Request bodies
<a name="apis-apiid-integrations-integrationid-integrationresponses-request-examples"></a>

#### POST schema
<a name="apis-apiid-integrations-integrationid-integrationresponses-request-body-post-example"></a>

```
{
  "integrationResponseKey": "string",
  "responseParameters": {
  },
  "responseTemplates": {
  },
  "templateSelectionExpression": "string",
  "contentHandlingStrategy": enum
}
```

### Response bodies
<a name="apis-apiid-integrations-integrationid-integrationresponses-response-examples"></a>

#### IntegrationResponses schema
<a name="apis-apiid-integrations-integrationid-integrationresponses-response-body-integrationresponses-example"></a>

```
{
  "items": [
    {
      "integrationResponseId": "string",
      "integrationResponseKey": "string",
      "responseParameters": {
      },
      "responseTemplates": {
      },
      "templateSelectionExpression": "string",
      "contentHandlingStrategy": enum
    }
  ],
  "nextToken": "string"
}
```

#### IntegrationResponse schema
<a name="apis-apiid-integrations-integrationid-integrationresponses-response-body-integrationresponse-example"></a>

```
{
  "integrationResponseId": "string",
  "integrationResponseKey": "string",
  "responseParameters": {
  },
  "responseTemplates": {
  },
  "templateSelectionExpression": "string",
  "contentHandlingStrategy": enum
}
```

#### BadRequestException schema
<a name="apis-apiid-integrations-integrationid-integrationresponses-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="apis-apiid-integrations-integrationid-integrationresponses-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### ConflictException schema
<a name="apis-apiid-integrations-integrationid-integrationresponses-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceededException schema
<a name="apis-apiid-integrations-integrationid-integrationresponses-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="apis-apiid-integrations-integrationid-integrationresponses-properties"></a>

### BadRequestException
<a name="apis-apiid-integrations-integrationid-integrationresponses-model-badrequestexception"></a>

The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### ConflictException
<a name="apis-apiid-integrations-integrationid-integrationresponses-model-conflictexception"></a>

The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### ContentHandlingStrategy
<a name="apis-apiid-integrations-integrationid-integrationresponses-model-contenthandlingstrategy"></a>

Specifies how to handle response payload content type conversions. Supported only for WebSocket APIs.
+ `CONVERT_TO_BINARY`
+ `CONVERT_TO_TEXT`

### CreateIntegrationResponseInput
<a name="apis-apiid-integrations-integrationid-integrationresponses-model-createintegrationresponseinput"></a>

Represents the input parameters for a `CreateIntegrationResponse` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| contentHandlingStrategy | [ContentHandlingStrategy](#apis-apiid-integrations-integrationid-integrationresponses-model-contenthandlingstrategy) | False | Specifies how to handle response payload content type conversions. Supported values are `CONVERT_TO_BINARY` and `CONVERT_TO_TEXT`, with the following behaviors:<br /> `CONVERT_TO_BINARY`: Converts a response payload from a Base64-encoded string to the corresponding binary blob.<br /> `CONVERT_TO_TEXT`: Converts a response payload from a binary blob to a Base64-encoded string.<br />If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification. |
| integrationResponseKey | string | True | The integration response key. |
| responseParameters | [IntegrationParameters](#apis-apiid-integrations-integrationid-integrationresponses-model-integrationparameters) | False | A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of `method.response.header.{name}`, where `{name}` is a valid and unique header name. The mapped non-static value must match the pattern of `integration.response.header.{name}` or `integration.response.body.{JSON-expression}`, where `{name}` is a valid and unique response header name and {JSON-expression} is a valid JSON expression without the `$` prefix. |
| responseTemplates | [TemplateMap](#apis-apiid-integrations-integrationid-integrationresponses-model-templatemap) | False | The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key/value map, with a content-type as the key and a template as the value. |
| templateSelectionExpression | string | False | The template selection expression for the integration response. Supported only for WebSocket APIs. |

### IntegrationParameters
<a name="apis-apiid-integrations-integrationid-integrationresponses-model-integrationparameters"></a>

For WebSocket APIs, a key-value map specifying request parameters that are passed from the method request to the backend. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the backend. The method request parameter value must match the pattern of `method.request.{{{location}}}.{{{name}}} `, where ` {{{location}}} ` is `querystring`, `path`, or `header`; and ` {{{name}}} ` must be a valid and unique method request parameter name.

For HTTP API integrations with a specified `integrationSubtype`, request parameters are a key-value map specifying parameters that are passed to `AWS_PROXY` integrations. You can provide static values, or map request data, stage variables, or context variables that are evaluated at runtime. To learn more, see [Working with AWS service integrations for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services.html).

For HTTP API integrations without a specified `integrationSubtype` request parameters are a key-value map specifying how to transform HTTP requests before sending them to the backend. The key should follow the pattern <action>:<header\|querystring\|path>.<location> where action can be `append`, `overwrite` or` remove`. For values, you can provide static values, or map request data, stage variables, or context variables that are evaluated at runtime. To learn more, see [Transforming API requests and responses](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html).

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### IntegrationResponse
<a name="apis-apiid-integrations-integrationid-integrationresponses-model-integrationresponse"></a>

Represents an integration response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| contentHandlingStrategy | [ContentHandlingStrategy](#apis-apiid-integrations-integrationid-integrationresponses-model-contenthandlingstrategy) | False | Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are `CONVERT_TO_BINARY` and `CONVERT_TO_TEXT`, with the following behaviors:<br /> `CONVERT_TO_BINARY`: Converts a response payload from a Base64-encoded string to the corresponding binary blob.<br /> `CONVERT_TO_TEXT`: Converts a response payload from a binary blob to a Base64-encoded string.<br />If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification. |
| integrationResponseId | string | False | The integration response ID. |
| integrationResponseKey | string | True | The integration response key. |
| responseParameters | [IntegrationParameters](#apis-apiid-integrations-integrationid-integrationresponses-model-integrationparameters) | False | A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of method.response.header.{name}, where name is a valid and unique header name. The mapped non-static value must match the pattern of integration.response.header.{name} or integration.response.body.{JSON-expression}, where name is a valid and unique response header name and JSON-expression is a valid JSON expression without the $ prefix. |
| responseTemplates | [TemplateMap](#apis-apiid-integrations-integrationid-integrationresponses-model-templatemap) | False | The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key/value map, with a content-type as the key and a template as the value. |
| templateSelectionExpression | string | False | The template selection expressions for the integration response. |

### IntegrationResponses
<a name="apis-apiid-integrations-integrationid-integrationresponses-model-integrationresponses"></a>

Represents a collection of integration responses.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| items | Array of type [IntegrationResponse](#apis-apiid-integrations-integrationid-integrationresponses-model-integrationresponse) | False | The elements from this collection. |
| nextToken | string | False | The next page of elements from this collection. Not valid for the last element of the collection. |

### LimitExceededException
<a name="apis-apiid-integrations-integrationid-integrationresponses-model-limitexceededexception"></a>

A limit has been exceeded. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type. |
| message | string | False | Describes the error encountered. |

### NotFoundException
<a name="apis-apiid-integrations-integrationid-integrationresponses-model-notfoundexception"></a>

The resource specified in the request was not found. See the `message` field for more information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |
| resourceType | string | False | The resource type. |

### TemplateMap
<a name="apis-apiid-integrations-integrationid-integrationresponses-model-templatemap"></a>

A mapping of identifier keys to templates. The value is an actual template script. The key is typically a `SelectionKey` which is chosen based on evaluating a selection expression.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

## See also
<a name="apis-apiid-integrations-integrationid-integrationresponses-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetIntegrationResponses
<a name="GetIntegrationResponses-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/GetIntegrationResponses)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/GetIntegrationResponses)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/GetIntegrationResponses)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/GetIntegrationResponses)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/GetIntegrationResponses)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/GetIntegrationResponses)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/GetIntegrationResponses)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/GetIntegrationResponses)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/GetIntegrationResponses)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/GetIntegrationResponses)

### CreateIntegrationResponse
<a name="CreateIntegrationResponse-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/CreateIntegrationResponse)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/CreateIntegrationResponse)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/CreateIntegrationResponse)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/CreateIntegrationResponse)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/CreateIntegrationResponse)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/CreateIntegrationResponse)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/CreateIntegrationResponse)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/CreateIntegrationResponse)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/CreateIntegrationResponse)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/CreateIntegrationResponse)
