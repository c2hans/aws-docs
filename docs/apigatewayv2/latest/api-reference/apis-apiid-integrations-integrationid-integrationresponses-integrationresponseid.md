---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid.html
---

# IntegrationResponse
<a name="apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid"></a>

Represents an integration response. Supported only for WebSocket APIs.

## URI
<a name="apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid-url"></a>

`/v2/apis/{{apiId}}/integrations/{{integrationId}}/integrationresponses/{{integrationResponseId}}`

## HTTP methods
<a name="apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid-http-methods"></a>

### GET
<a name="apis-apiid-integrations-integrationid-integrationresponses-integrationresponseidget"></a>

**Operation ID:** `GetIntegrationResponse`

Gets an `IntegrationResponses`.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{apiId}} | String | True | The API identifier. |
| {{integrationResponseId}} | String | True | The integration response ID. |
| {{integrationId}} | String | True | The integration ID. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | IntegrationResponse | Success |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### DELETE
<a name="apis-apiid-integrations-integrationid-integrationresponses-integrationresponseiddelete"></a>

**Operation ID:** `DeleteIntegrationResponse`

Deletes an `IntegrationResponses`.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{apiId}} | String | True | The API identifier. |
| {{integrationResponseId}} | String | True | The integration response ID. |
| {{integrationId}} | String | True | The integration ID. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | The request has succeeded, and there is no additional content to send in the response payload body. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### PATCH
<a name="apis-apiid-integrations-integrationid-integrationresponses-integrationresponseidpatch"></a>

**Operation ID:** `UpdateIntegrationResponse`

Updates an `IntegrationResponses`.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{apiId}} | String | True | The API identifier. |
| {{integrationResponseId}} | String | True | The integration response ID. |
| {{integrationId}} | String | True | The integration ID. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | IntegrationResponse | Success |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 409 | ConflictException | The resource already exists. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid-schemas"></a>

### Request bodies
<a name="apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid-request-examples"></a>

#### PATCH schema
<a name="apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid-request-body-patch-example"></a>

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
<a name="apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid-response-examples"></a>

#### IntegrationResponse schema
<a name="apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid-response-body-integrationresponse-example"></a>

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
<a name="apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### ConflictException schema
<a name="apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceededException schema
<a name="apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid-properties"></a>

### BadRequestException
<a name="apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid-model-badrequestexception"></a>

The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### ConflictException
<a name="apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid-model-conflictexception"></a>

The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### ContentHandlingStrategy
<a name="apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid-model-contenthandlingstrategy"></a>

Specifies how to handle response payload content type conversions. Supported only for WebSocket APIs.
+ `CONVERT_TO_BINARY`
+ `CONVERT_TO_TEXT`

### IntegrationParameters
<a name="apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid-model-integrationparameters"></a>

For WebSocket APIs, a key-value map specifying request parameters that are passed from the method request to the backend. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the backend. The method request parameter value must match the pattern of `method.request.{{{location}}}.{{{name}}} `, where ` {{{location}}} ` is `querystring`, `path`, or `header`; and ` {{{name}}} ` must be a valid and unique method request parameter name.

For HTTP API integrations with a specified `integrationSubtype`, request parameters are a key-value map specifying parameters that are passed to `AWS_PROXY` integrations. You can provide static values, or map request data, stage variables, or context variables that are evaluated at runtime. To learn more, see [Working with AWS service integrations for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services.html).

For HTTP API integrations without a specified `integrationSubtype` request parameters are a key-value map specifying how to transform HTTP requests before sending them to the backend. The key should follow the pattern <action>:<header\|querystring\|path>.<location> where action can be `append`, `overwrite` or` remove`. For values, you can provide static values, or map request data, stage variables, or context variables that are evaluated at runtime. To learn more, see [Transforming API requests and responses](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html).

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### IntegrationResponse
<a name="apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid-model-integrationresponse"></a>

Represents an integration response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| contentHandlingStrategy | [ContentHandlingStrategy](#apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid-model-contenthandlingstrategy) | False | Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are `CONVERT_TO_BINARY` and `CONVERT_TO_TEXT`, with the following behaviors:<br /> `CONVERT_TO_BINARY`: Converts a response payload from a Base64-encoded string to the corresponding binary blob.<br /> `CONVERT_TO_TEXT`: Converts a response payload from a binary blob to a Base64-encoded string.<br />If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification. |
| integrationResponseId | string | False | The integration response ID. |
| integrationResponseKey | string | True | The integration response key. |
| responseParameters | [IntegrationParameters](#apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid-model-integrationparameters) | False | A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of method.response.header.{name}, where name is a valid and unique header name. The mapped non-static value must match the pattern of integration.response.header.{name} or integration.response.body.{JSON-expression}, where name is a valid and unique response header name and JSON-expression is a valid JSON expression without the $ prefix. |
| responseTemplates | [TemplateMap](#apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid-model-templatemap) | False | The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key/value map, with a content-type as the key and a template as the value. |
| templateSelectionExpression | string | False | The template selection expressions for the integration response. |

### LimitExceededException
<a name="apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid-model-limitexceededexception"></a>

A limit has been exceeded. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type. |
| message | string | False | Describes the error encountered. |

### NotFoundException
<a name="apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid-model-notfoundexception"></a>

The resource specified in the request was not found. See the `message` field for more information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |
| resourceType | string | False | The resource type. |

### TemplateMap
<a name="apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid-model-templatemap"></a>

A mapping of identifier keys to templates. The value is an actual template script. The key is typically a `SelectionKey` which is chosen based on evaluating a selection expression.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### UpdateIntegrationResponseInput
<a name="apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid-model-updateintegrationresponseinput"></a>

Represents the input parameters for an `UpdateIntegrationResponse` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| contentHandlingStrategy | [ContentHandlingStrategy](#apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid-model-contenthandlingstrategy) | False | Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are `CONVERT_TO_BINARY` and `CONVERT_TO_TEXT`, with the following behaviors:<br /> `CONVERT_TO_BINARY`: Converts a response payload from a Base64-encoded string to the corresponding binary blob.<br /> `CONVERT_TO_TEXT`: Converts a response payload from a binary blob to a Base64-encoded string.<br />If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification. |
| integrationResponseKey | string | False | The integration response key. |
| responseParameters | [IntegrationParameters](#apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid-model-integrationparameters) | False | A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of `method.response.header.{{{name}}} `, where name is a valid and unique header name. The mapped non-static value must match the pattern of `integration.response.header.{{{name}}} ` or `integration.response.body.{{{JSON-expression}}} `, where ` {{{name}}} ` is a valid and unique response header name and ` {{{JSON-expression}}} ` is a valid JSON expression without the `$` prefix. |
| responseTemplates | [TemplateMap](#apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid-model-templatemap) | False | The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key/value map, with a content-type as the key and a template as the value. |
| templateSelectionExpression | string | False | The template selection expression for the integration response. Supported only for WebSocket APIs. |

## See also
<a name="apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetIntegrationResponse
<a name="GetIntegrationResponse-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/GetIntegrationResponse)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/GetIntegrationResponse)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/GetIntegrationResponse)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/GetIntegrationResponse)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/GetIntegrationResponse)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/GetIntegrationResponse)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/GetIntegrationResponse)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/GetIntegrationResponse)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/GetIntegrationResponse)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/GetIntegrationResponse)

### DeleteIntegrationResponse
<a name="DeleteIntegrationResponse-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/DeleteIntegrationResponse)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/DeleteIntegrationResponse)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/DeleteIntegrationResponse)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/DeleteIntegrationResponse)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/DeleteIntegrationResponse)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/DeleteIntegrationResponse)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/DeleteIntegrationResponse)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/DeleteIntegrationResponse)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/DeleteIntegrationResponse)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/DeleteIntegrationResponse)

### UpdateIntegrationResponse
<a name="UpdateIntegrationResponse-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/UpdateIntegrationResponse)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/UpdateIntegrationResponse)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/UpdateIntegrationResponse)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/UpdateIntegrationResponse)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/UpdateIntegrationResponse)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/UpdateIntegrationResponse)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/UpdateIntegrationResponse)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/UpdateIntegrationResponse)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/UpdateIntegrationResponse)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/UpdateIntegrationResponse)
