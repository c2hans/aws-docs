---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/apis-apiid-routes-routeid-routeresponses-routeresponseid.html
---

# RouteResponse
<a name="apis-apiid-routes-routeid-routeresponses-routeresponseid"></a>

Represents a route response. Supported only for WebSocket APIs.

## URI
<a name="apis-apiid-routes-routeid-routeresponses-routeresponseid-url"></a>

`/v2/apis/{{apiId}}/routes/{{routeId}}/routeresponses/{{routeResponseId}}`

## HTTP methods
<a name="apis-apiid-routes-routeid-routeresponses-routeresponseid-http-methods"></a>

### GET
<a name="apis-apiid-routes-routeid-routeresponses-routeresponseidget"></a>

**Operation ID:** `GetRouteResponse`

Gets a `RouteResponse`.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{routeResponseId}} | String | True | The route response ID. |
| {{apiId}} | String | True | The API identifier. |
| {{routeId}} | String | True | The route ID. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | RouteResponse | Success |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### DELETE
<a name="apis-apiid-routes-routeid-routeresponses-routeresponseiddelete"></a>

**Operation ID:** `DeleteRouteResponse`

Deletes a `RouteResponse`.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{routeResponseId}} | String | True | The route response ID. |
| {{apiId}} | String | True | The API identifier. |
| {{routeId}} | String | True | The route ID. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | The request has succeeded, and there is no additional content to send in the response payload body. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### PATCH
<a name="apis-apiid-routes-routeid-routeresponses-routeresponseidpatch"></a>

**Operation ID:** `UpdateRouteResponse`

Updates a `RouteResponse`.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{routeResponseId}} | String | True | The route response ID. |
| {{apiId}} | String | True | The API identifier. |
| {{routeId}} | String | True | The route ID. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | RouteResponse | Success |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 409 | ConflictException | The resource already exists. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="apis-apiid-routes-routeid-routeresponses-routeresponseid-schemas"></a>

### Request bodies
<a name="apis-apiid-routes-routeid-routeresponses-routeresponseid-request-examples"></a>

#### PATCH schema
<a name="apis-apiid-routes-routeid-routeresponses-routeresponseid-request-body-patch-example"></a>

```
{
  "routeResponseKey": "string",
  "responseParameters": {
  },
  "responseModels": {
  },
  "modelSelectionExpression": "string"
}
```

### Response bodies
<a name="apis-apiid-routes-routeid-routeresponses-routeresponseid-response-examples"></a>

#### RouteResponse schema
<a name="apis-apiid-routes-routeid-routeresponses-routeresponseid-response-body-routeresponse-example"></a>

```
{
  "routeResponseId": "string",
  "routeResponseKey": "string",
  "responseParameters": {
  },
  "responseModels": {
  },
  "modelSelectionExpression": "string"
}
```

#### BadRequestException schema
<a name="apis-apiid-routes-routeid-routeresponses-routeresponseid-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="apis-apiid-routes-routeid-routeresponses-routeresponseid-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### ConflictException schema
<a name="apis-apiid-routes-routeid-routeresponses-routeresponseid-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceededException schema
<a name="apis-apiid-routes-routeid-routeresponses-routeresponseid-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="apis-apiid-routes-routeid-routeresponses-routeresponseid-properties"></a>

### BadRequestException
<a name="apis-apiid-routes-routeid-routeresponses-routeresponseid-model-badrequestexception"></a>

The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### ConflictException
<a name="apis-apiid-routes-routeid-routeresponses-routeresponseid-model-conflictexception"></a>

The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### LimitExceededException
<a name="apis-apiid-routes-routeid-routeresponses-routeresponseid-model-limitexceededexception"></a>

A limit has been exceeded. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type. |
| message | string | False | Describes the error encountered. |

### NotFoundException
<a name="apis-apiid-routes-routeid-routeresponses-routeresponseid-model-notfoundexception"></a>

The resource specified in the request was not found. See the `message` field for more information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |
| resourceType | string | False | The resource type. |

### ParameterConstraints
<a name="apis-apiid-routes-routeid-routeresponses-routeresponseid-model-parameterconstraints"></a>

Validation constraints imposed on parameters of a request (path, query string, headers).

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| required | boolean | False | Whether or not the parameter is required. |

### RouteModels
<a name="apis-apiid-routes-routeid-routeresponses-routeresponseid-model-routemodels"></a>

The route models.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### RouteParameters
<a name="apis-apiid-routes-routeid-routeresponses-routeresponseid-model-routeparameters"></a>

The route parameters.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | object | False |  |

### RouteResponse
<a name="apis-apiid-routes-routeid-routeresponses-routeresponseid-model-routeresponse"></a>

Represents a route response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| modelSelectionExpression | string | False | Represents the model selection expression of a route response. Supported only for WebSocket APIs. |
| responseModels | [RouteModels](#apis-apiid-routes-routeid-routeresponses-routeresponseid-model-routemodels) | False | Represents the response models of a route response. |
| responseParameters | [RouteParameters](#apis-apiid-routes-routeid-routeresponses-routeresponseid-model-routeparameters) | False | Represents the response parameters of a route response. |
| routeResponseId | string | False | Represents the identifier of a route response. |
| routeResponseKey | string | True | Represents the route response key of a route response. |

### UpdateRouteResponseInput
<a name="apis-apiid-routes-routeid-routeresponses-routeresponseid-model-updaterouteresponseinput"></a>

Represents the input parameters for an `UpdateRouteResponse` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| modelSelectionExpression | string | False | The model selection expression for the route response. Supported only for WebSocket APIs. |
| responseModels | [RouteModels](#apis-apiid-routes-routeid-routeresponses-routeresponseid-model-routemodels) | False | The response models for the route response. |
| responseParameters | [RouteParameters](#apis-apiid-routes-routeid-routeresponses-routeresponseid-model-routeparameters) | False | The route response parameters. |
| routeResponseKey | string | False | The route response key. |

## See also
<a name="apis-apiid-routes-routeid-routeresponses-routeresponseid-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetRouteResponse
<a name="GetRouteResponse-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/GetRouteResponse)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/GetRouteResponse)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/GetRouteResponse)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/GetRouteResponse)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/GetRouteResponse)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/GetRouteResponse)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/GetRouteResponse)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/GetRouteResponse)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/GetRouteResponse)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/GetRouteResponse)

### DeleteRouteResponse
<a name="DeleteRouteResponse-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/DeleteRouteResponse)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/DeleteRouteResponse)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/DeleteRouteResponse)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/DeleteRouteResponse)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/DeleteRouteResponse)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/DeleteRouteResponse)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/DeleteRouteResponse)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/DeleteRouteResponse)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/DeleteRouteResponse)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/DeleteRouteResponse)

### UpdateRouteResponse
<a name="UpdateRouteResponse-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/UpdateRouteResponse)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/UpdateRouteResponse)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/UpdateRouteResponse)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/UpdateRouteResponse)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/UpdateRouteResponse)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/UpdateRouteResponse)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/UpdateRouteResponse)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/UpdateRouteResponse)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/UpdateRouteResponse)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/UpdateRouteResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigatewayv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
