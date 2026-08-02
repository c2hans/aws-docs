---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/apis-apiid-routes-routeid.html
---

# Route
<a name="apis-apiid-routes-routeid"></a>

Represents a route for an API.

## URI
<a name="apis-apiid-routes-routeid-url"></a>

`/v2/apis/{{apiId}}/routes/{{routeId}}`

## HTTP methods
<a name="apis-apiid-routes-routeid-http-methods"></a>

### GET
<a name="apis-apiid-routes-routeidget"></a>

**Operation ID:** `GetRoute`

Gets a `Route`.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{apiId}} | String | True | The API identifier. |
| {{routeId}} | String | True | The route ID. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Route | Success |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### DELETE
<a name="apis-apiid-routes-routeiddelete"></a>

**Operation ID:** `DeleteRoute`

Deletes a `Route`.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{apiId}} | String | True | The API identifier. |
| {{routeId}} | String | True | The route ID. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | The request has succeeded, and there is no additional content to send in the response payload body. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### PATCH
<a name="apis-apiid-routes-routeidpatch"></a>

**Operation ID:** `UpdateRoute`

Updates a `Route`.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{apiId}} | String | True | The API identifier. |
| {{routeId}} | String | True | The route ID. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Route | Success |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 409 | ConflictException | The resource already exists. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="apis-apiid-routes-routeid-schemas"></a>

### Request bodies
<a name="apis-apiid-routes-routeid-request-examples"></a>

#### PATCH schema
<a name="apis-apiid-routes-routeid-request-body-patch-example"></a>

```
{
  "routeKey": "string",
  "authorizationType": enum,
  "authorizerId": "string",
  "authorizationScopes": [
    "string"
  ],
  "apiKeyRequired": boolean,
  "requestParameters": {
  },
  "requestModels": {
  },
  "modelSelectionExpression": "string",
  "target": "string",
  "operationName": "string",
  "routeResponseSelectionExpression": "string"
}
```

### Response bodies
<a name="apis-apiid-routes-routeid-response-examples"></a>

#### Route schema
<a name="apis-apiid-routes-routeid-response-body-route-example"></a>

```
{
  "routeId": "string",
  "routeKey": "string",
  "authorizationType": enum,
  "authorizerId": "string",
  "authorizationScopes": [
    "string"
  ],
  "apiKeyRequired": boolean,
  "requestParameters": {
  },
  "requestModels": {
  },
  "modelSelectionExpression": "string",
  "target": "string",
  "operationName": "string",
  "routeResponseSelectionExpression": "string",
  "apiGatewayManaged": boolean
}
```

#### BadRequestException schema
<a name="apis-apiid-routes-routeid-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="apis-apiid-routes-routeid-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### ConflictException schema
<a name="apis-apiid-routes-routeid-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceededException schema
<a name="apis-apiid-routes-routeid-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="apis-apiid-routes-routeid-properties"></a>

### AuthorizationType
<a name="apis-apiid-routes-routeid-model-authorizationtype"></a>

The authorization type. For WebSocket APIs, valid values are `NONE` for open access, `AWS_IAM` for using AWS IAM permissions, and `CUSTOM` for using a Lambda authorizer. For HTTP APIs, valid values are `NONE` for open access, `JWT` for using JSON Web Tokens, `AWS_IAM` for using AWS IAM permissions, and `CUSTOM` for using a Lambda authorizer.
+ `NONE`
+ `AWS_IAM`
+ `CUSTOM`
+ `JWT`

### BadRequestException
<a name="apis-apiid-routes-routeid-model-badrequestexception"></a>

The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### ConflictException
<a name="apis-apiid-routes-routeid-model-conflictexception"></a>

The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### LimitExceededException
<a name="apis-apiid-routes-routeid-model-limitexceededexception"></a>

A limit has been exceeded. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type. |
| message | string | False | Describes the error encountered. |

### NotFoundException
<a name="apis-apiid-routes-routeid-model-notfoundexception"></a>

The resource specified in the request was not found. See the `message` field for more information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |
| resourceType | string | False | The resource type. |

### ParameterConstraints
<a name="apis-apiid-routes-routeid-model-parameterconstraints"></a>

Validation constraints imposed on parameters of a request (path, query string, headers).

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| required | boolean | False | Whether or not the parameter is required. |

### Route
<a name="apis-apiid-routes-routeid-model-route"></a>

Represents a route.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| apiGatewayManaged | boolean | False | Specifies whether a route is managed by API Gateway. If you created an API using quick create, the `$default` route is managed by API Gateway. You can't modify the `$default` route key. |
| apiKeyRequired | boolean | False | Specifies whether an API key is required for this route. Supported only for WebSocket APIs. |
| authorizationScopes | Array of type string | False | A list of authorization scopes configured on a route. The scopes are used with a `JWT` authorizer to authorize the method invocation. The authorization works by matching the route scopes against the scopes parsed from the access token in the incoming request. The method invocation is authorized if any route scope matches a claimed scope in the access token. Otherwise, the invocation is not authorized. When the route scope is configured, the client must provide an access token instead of an identity token for authorization purposes. |
| authorizationType | [AuthorizationType](#apis-apiid-routes-routeid-model-authorizationtype) | False | The authorization type for the route. For WebSocket APIs, valid values are `NONE` for open access, `AWS_IAM` for using AWS IAM permissions, and `CUSTOM` for using a Lambda authorizer. For HTTP APIs, valid values are `NONE` for open access, `JWT` for using JSON Web Tokens, `AWS_IAM` for using AWS IAM permissions, and `CUSTOM` for using a Lambda authorizer. |
| authorizerId | string | False | The identifier of the `Authorizer` resource to be associated with this route. The authorizer identifier is generated by API Gateway when you created the authorizer. |
| modelSelectionExpression | string | False | The model selection expression for the route. Supported only for WebSocket APIs. |
| operationName | string | False | The operation name for the route. |
| requestModels | [RouteModels](#apis-apiid-routes-routeid-model-routemodels) | False | The request models for the route. Supported only for WebSocket APIs. |
| requestParameters | [RouteParameters](#apis-apiid-routes-routeid-model-routeparameters) | False | The request parameters for the route. Supported only for WebSocket APIs. |
| routeId | string | False | The route ID. |
| routeKey | string | True | The route key for the route. For HTTP APIs, the route key can be either `$default`, or a combination of an HTTP method and resource path, for example, `GET /pets`. |
| routeResponseSelectionExpression | string | False | The route response selection expression for the route. Supported only for WebSocket APIs. |
| target | string | False | The target for the route. |

### RouteModels
<a name="apis-apiid-routes-routeid-model-routemodels"></a>

The route models.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### RouteParameters
<a name="apis-apiid-routes-routeid-model-routeparameters"></a>

The route parameters.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | object | False |  |

### UpdateRouteInput
<a name="apis-apiid-routes-routeid-model-updaterouteinput"></a>

Represents the input parameters for an `UpdateRoute` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| apiKeyRequired | boolean | False | Specifies whether an API key is required for the route. Supported only for WebSocket APIs. |
| authorizationScopes | Array of type string | False | The authorization scopes supported by this route. |
| authorizationType | [AuthorizationType](#apis-apiid-routes-routeid-model-authorizationtype) | False | The authorization type for the route. For WebSocket APIs, valid values are `NONE` for open access, `AWS_IAM` for using AWS IAM permissions, and `CUSTOM` for using a Lambda authorizer. For HTTP APIs, valid values are `NONE` for open access, `JWT` for using JSON Web Tokens, `AWS_IAM` for using AWS IAM permissions, and `CUSTOM` for using a Lambda authorizer. |
| authorizerId | string | False | The identifier of the `Authorizer` resource to be associated with this route. The authorizer identifier is generated by API Gateway when you created the authorizer. |
| modelSelectionExpression | string | False | The model selection expression for the route. Supported only for WebSocket APIs. |
| operationName | string | False | The operation name for the route. |
| requestModels | [RouteModels](#apis-apiid-routes-routeid-model-routemodels) | False | The request models for the route. Supported only for WebSocket APIs. |
| requestParameters | [RouteParameters](#apis-apiid-routes-routeid-model-routeparameters) | False | The request parameters for the route. Supported only for WebSocket APIs. |
| routeKey | string | False | The route key for the route. For HTTP APIs, the route key can be either `$default`, or a combination of an HTTP method and resource path, for example, `GET /pets`. |
| routeResponseSelectionExpression | string | False | The route response selection expression for the route. Supported only for WebSocket APIs. |
| target | string | False | The target for the route. |

## See also
<a name="apis-apiid-routes-routeid-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetRoute
<a name="GetRoute-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/GetRoute)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/GetRoute)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/GetRoute)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/GetRoute)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/GetRoute)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/GetRoute)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/GetRoute)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/GetRoute)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/GetRoute)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/GetRoute)

### DeleteRoute
<a name="DeleteRoute-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/DeleteRoute)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/DeleteRoute)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/DeleteRoute)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/DeleteRoute)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/DeleteRoute)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/DeleteRoute)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/DeleteRoute)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/DeleteRoute)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/DeleteRoute)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/DeleteRoute)

### UpdateRoute
<a name="UpdateRoute-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/UpdateRoute)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/UpdateRoute)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/UpdateRoute)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/UpdateRoute)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/UpdateRoute)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/UpdateRoute)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/UpdateRoute)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/UpdateRoute)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/UpdateRoute)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/UpdateRoute)
