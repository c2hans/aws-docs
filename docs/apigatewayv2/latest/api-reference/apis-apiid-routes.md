---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/apis-apiid-routes.html
---

# Routes
<a name="apis-apiid-routes"></a>

Represents the collection of routes for an API.

## URI
<a name="apis-apiid-routes-url"></a>

`/v2/apis/{{apiId}}/routes`

## HTTP methods
<a name="apis-apiid-routes-http-methods"></a>

### GET
<a name="apis-apiid-routesget"></a>

**Operation ID:** `GetRoutes`

Gets the `Routes` for an API.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{apiId}} | String | True | The API identifier. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The next page of elements from this collection. Not valid for the last element of the collection. |
| maxResults | String | False | The maximum number of elements to be returned for this resource. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Routes | Success |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### POST
<a name="apis-apiid-routespost"></a>

**Operation ID:** `CreateRoute`

Creates a `Route` for an API.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{apiId}} | String | True | The API identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | Route | The request has succeeded and has resulted in the creation of a resource. |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 409 | ConflictException | The resource already exists. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="apis-apiid-routes-schemas"></a>

### Request bodies
<a name="apis-apiid-routes-request-examples"></a>

#### POST schema
<a name="apis-apiid-routes-request-body-post-example"></a>

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
<a name="apis-apiid-routes-response-examples"></a>

#### Routes schema
<a name="apis-apiid-routes-response-body-routes-example"></a>

```
{
  "items": [
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
  ],
  "nextToken": "string"
}
```

#### Route schema
<a name="apis-apiid-routes-response-body-route-example"></a>

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
<a name="apis-apiid-routes-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="apis-apiid-routes-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### ConflictException schema
<a name="apis-apiid-routes-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceededException schema
<a name="apis-apiid-routes-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="apis-apiid-routes-properties"></a>

### AuthorizationType
<a name="apis-apiid-routes-model-authorizationtype"></a>

The authorization type. For WebSocket APIs, valid values are `NONE` for open access, `AWS_IAM` for using AWS IAM permissions, and `CUSTOM` for using a Lambda authorizer. For HTTP APIs, valid values are `NONE` for open access, `JWT` for using JSON Web Tokens, `AWS_IAM` for using AWS IAM permissions, and `CUSTOM` for using a Lambda authorizer.
+ `NONE`
+ `AWS_IAM`
+ `CUSTOM`
+ `JWT`

### BadRequestException
<a name="apis-apiid-routes-model-badrequestexception"></a>

The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### ConflictException
<a name="apis-apiid-routes-model-conflictexception"></a>

The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### CreateRouteInput
<a name="apis-apiid-routes-model-createrouteinput"></a>

Represents the input parameters for a `CreateRoute` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| apiKeyRequired | boolean | False | Specifies whether an API key is required for the route. Supported only for WebSocket APIs. |
| authorizationScopes | Array of type string | False | The authorization scopes supported by this route. |
| authorizationType | [AuthorizationType](#apis-apiid-routes-model-authorizationtype) | False | The authorization type for the route. For WebSocket APIs, valid values are `NONE` for open access, `AWS_IAM` for using AWS IAM permissions, and `CUSTOM` for using a Lambda authorizer. For HTTP APIs, valid values are `NONE` for open access, `JWT` for using JSON Web Tokens, `AWS_IAM` for using AWS IAM permissions, and `CUSTOM` for using a Lambda authorizer. |
| authorizerId | string | False | The identifier of the `Authorizer` resource to be associated with this route. The authorizer identifier is generated by API Gateway when you created the authorizer. |
| modelSelectionExpression | string | False | The model selection expression for the route. Supported only for WebSocket APIs. |
| operationName | string | False | The operation name for the route. |
| requestModels | [RouteModels](#apis-apiid-routes-model-routemodels) | False | The request models for the route. Supported only for WebSocket APIs. |
| requestParameters | [RouteParameters](#apis-apiid-routes-model-routeparameters) | False | The request parameters for the route. Supported only for WebSocket APIs. |
| routeKey | string | True | The route key for the route. For HTTP APIs, the route key can be either `$default`, or a combination of an HTTP method and resource path, for example, `GET /pets`. |
| routeResponseSelectionExpression | string | False | The route response selection expression for the route. Supported only for WebSocket APIs. |
| target | string | False | The target for the route. |

### LimitExceededException
<a name="apis-apiid-routes-model-limitexceededexception"></a>

A limit has been exceeded. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type. |
| message | string | False | Describes the error encountered. |

### NotFoundException
<a name="apis-apiid-routes-model-notfoundexception"></a>

The resource specified in the request was not found. See the `message` field for more information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |
| resourceType | string | False | The resource type. |

### ParameterConstraints
<a name="apis-apiid-routes-model-parameterconstraints"></a>

Validation constraints imposed on parameters of a request (path, query string, headers).

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| required | boolean | False | Whether or not the parameter is required. |

### Route
<a name="apis-apiid-routes-model-route"></a>

Represents a route.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| apiGatewayManaged | boolean | False | Specifies whether a route is managed by API Gateway. If you created an API using quick create, the `$default` route is managed by API Gateway. You can't modify the `$default` route key. |
| apiKeyRequired | boolean | False | Specifies whether an API key is required for this route. Supported only for WebSocket APIs. |
| authorizationScopes | Array of type string | False | A list of authorization scopes configured on a route. The scopes are used with a `JWT` authorizer to authorize the method invocation. The authorization works by matching the route scopes against the scopes parsed from the access token in the incoming request. The method invocation is authorized if any route scope matches a claimed scope in the access token. Otherwise, the invocation is not authorized. When the route scope is configured, the client must provide an access token instead of an identity token for authorization purposes. |
| authorizationType | [AuthorizationType](#apis-apiid-routes-model-authorizationtype) | False | The authorization type for the route. For WebSocket APIs, valid values are `NONE` for open access, `AWS_IAM` for using AWS IAM permissions, and `CUSTOM` for using a Lambda authorizer. For HTTP APIs, valid values are `NONE` for open access, `JWT` for using JSON Web Tokens, `AWS_IAM` for using AWS IAM permissions, and `CUSTOM` for using a Lambda authorizer. |
| authorizerId | string | False | The identifier of the `Authorizer` resource to be associated with this route. The authorizer identifier is generated by API Gateway when you created the authorizer. |
| modelSelectionExpression | string | False | The model selection expression for the route. Supported only for WebSocket APIs. |
| operationName | string | False | The operation name for the route. |
| requestModels | [RouteModels](#apis-apiid-routes-model-routemodels) | False | The request models for the route. Supported only for WebSocket APIs. |
| requestParameters | [RouteParameters](#apis-apiid-routes-model-routeparameters) | False | The request parameters for the route. Supported only for WebSocket APIs. |
| routeId | string | False | The route ID. |
| routeKey | string | True | The route key for the route. For HTTP APIs, the route key can be either `$default`, or a combination of an HTTP method and resource path, for example, `GET /pets`. |
| routeResponseSelectionExpression | string | False | The route response selection expression for the route. Supported only for WebSocket APIs. |
| target | string | False | The target for the route. |

### RouteModels
<a name="apis-apiid-routes-model-routemodels"></a>

The route models.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### RouteParameters
<a name="apis-apiid-routes-model-routeparameters"></a>

The route parameters.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | object | False |  |

### Routes
<a name="apis-apiid-routes-model-routes"></a>

Represents a collection of routes.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| items | Array of type [Route](#apis-apiid-routes-model-route) | False | The elements from this collection. |
| nextToken | string | False | The next page of elements from this collection. Not valid for the last element of the collection. |

## See also
<a name="apis-apiid-routes-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetRoutes
<a name="GetRoutes-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/GetRoutes)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/GetRoutes)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/GetRoutes)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/GetRoutes)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/GetRoutes)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/GetRoutes)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/GetRoutes)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/GetRoutes)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/GetRoutes)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/GetRoutes)

### CreateRoute
<a name="CreateRoute-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/CreateRoute)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/CreateRoute)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/CreateRoute)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/CreateRoute)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/CreateRoute)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/CreateRoute)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/CreateRoute)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/CreateRoute)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/CreateRoute)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/CreateRoute)
