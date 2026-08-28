---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/apis-apiid-routes-routeid-routeresponses.html
---

# RouteResponses
<a name="apis-apiid-routes-routeid-routeresponses"></a>

Represents the collection of responses for a route. Supported only for WebSocket APIs.

## URI
<a name="apis-apiid-routes-routeid-routeresponses-url"></a>

`/v2/apis/{{apiId}}/routes/{{routeId}}/routeresponses`

## HTTP methods
<a name="apis-apiid-routes-routeid-routeresponses-http-methods"></a>

### GET
<a name="apis-apiid-routes-routeid-routeresponsesget"></a>

**Operation ID:** `GetRouteResponses`

Gets the `RouteResponses` for a `Route`.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{routeId}} | String | True | The route ID. |
| {{apiId}} | String | True | The API identifier. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The next page of elements from this collection. Not valid for the last element of the collection. |
| maxResults | String | False | The maximum number of elements to be returned for this resource. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | RouteResponses | Success |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### POST
<a name="apis-apiid-routes-routeid-routeresponsespost"></a>

**Operation ID:** `CreateRouteResponse`

Creates a `RouteResponse` for a `Route`.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{apiId}} | String | True | The API identifier. |
| {{routeId}} | String | True | The route ID. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | RouteResponse | The request has succeeded and has resulted in the creation of a resource. |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 409 | ConflictException | The resource already exists. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="apis-apiid-routes-routeid-routeresponses-schemas"></a>

### Request bodies
<a name="apis-apiid-routes-routeid-routeresponses-request-examples"></a>

#### POST schema
<a name="apis-apiid-routes-routeid-routeresponses-request-body-post-example"></a>

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
<a name="apis-apiid-routes-routeid-routeresponses-response-examples"></a>

#### RouteResponses schema
<a name="apis-apiid-routes-routeid-routeresponses-response-body-routeresponses-example"></a>

```
{
  "items": [
    {
      "routeResponseId": "string",
      "routeResponseKey": "string",
      "responseParameters": {
      },
      "responseModels": {
      },
      "modelSelectionExpression": "string"
    }
  ],
  "nextToken": "string"
}
```

#### RouteResponse schema
<a name="apis-apiid-routes-routeid-routeresponses-response-body-routeresponse-example"></a>

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
<a name="apis-apiid-routes-routeid-routeresponses-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="apis-apiid-routes-routeid-routeresponses-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### ConflictException schema
<a name="apis-apiid-routes-routeid-routeresponses-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceededException schema
<a name="apis-apiid-routes-routeid-routeresponses-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="apis-apiid-routes-routeid-routeresponses-properties"></a>

### BadRequestException
<a name="apis-apiid-routes-routeid-routeresponses-model-badrequestexception"></a>

The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### ConflictException
<a name="apis-apiid-routes-routeid-routeresponses-model-conflictexception"></a>

The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### CreateRouteResponseInput
<a name="apis-apiid-routes-routeid-routeresponses-model-createrouteresponseinput"></a>

Represents the input parameters for an `CreateRouteResponse` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| modelSelectionExpression | string | False | The model selection expression for the route response. Supported only for WebSocket APIs. |
| responseModels | [RouteModels](#apis-apiid-routes-routeid-routeresponses-model-routemodels) | False | The response models for the route response. |
| responseParameters | [RouteParameters](#apis-apiid-routes-routeid-routeresponses-model-routeparameters) | False | The route response parameters. |
| routeResponseKey | string | True | The route response key. |

### LimitExceededException
<a name="apis-apiid-routes-routeid-routeresponses-model-limitexceededexception"></a>

A limit has been exceeded. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type. |
| message | string | False | Describes the error encountered. |

### NotFoundException
<a name="apis-apiid-routes-routeid-routeresponses-model-notfoundexception"></a>

The resource specified in the request was not found. See the `message` field for more information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |
| resourceType | string | False | The resource type. |

### ParameterConstraints
<a name="apis-apiid-routes-routeid-routeresponses-model-parameterconstraints"></a>

Validation constraints imposed on parameters of a request (path, query string, headers).

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| required | boolean | False | Whether or not the parameter is required. |

### RouteModels
<a name="apis-apiid-routes-routeid-routeresponses-model-routemodels"></a>

The route models.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### RouteParameters
<a name="apis-apiid-routes-routeid-routeresponses-model-routeparameters"></a>

The route parameters.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | object | False |  |

### RouteResponse
<a name="apis-apiid-routes-routeid-routeresponses-model-routeresponse"></a>

Represents a route response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| modelSelectionExpression | string | False | Represents the model selection expression of a route response. Supported only for WebSocket APIs. |
| responseModels | [RouteModels](#apis-apiid-routes-routeid-routeresponses-model-routemodels) | False | Represents the response models of a route response. |
| responseParameters | [RouteParameters](#apis-apiid-routes-routeid-routeresponses-model-routeparameters) | False | Represents the response parameters of a route response. |
| routeResponseId | string | False | Represents the identifier of a route response. |
| routeResponseKey | string | True | Represents the route response key of a route response. |

### RouteResponses
<a name="apis-apiid-routes-routeid-routeresponses-model-routeresponses"></a>

Represents a collection of route responses.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| items | Array of type [RouteResponse](#apis-apiid-routes-routeid-routeresponses-model-routeresponse) | False | The elements from this collection. |
| nextToken | string | False | The next page of elements from this collection. Not valid for the last element of the collection. |

## See also
<a name="apis-apiid-routes-routeid-routeresponses-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetRouteResponses
<a name="GetRouteResponses-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/GetRouteResponses)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/GetRouteResponses)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/GetRouteResponses)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/GetRouteResponses)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/GetRouteResponses)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/GetRouteResponses)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/GetRouteResponses)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/GetRouteResponses)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/GetRouteResponses)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/GetRouteResponses)

### CreateRouteResponse
<a name="CreateRouteResponse-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/CreateRouteResponse)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/CreateRouteResponse)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/CreateRouteResponse)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/CreateRouteResponse)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/CreateRouteResponse)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/CreateRouteResponse)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/CreateRouteResponse)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/CreateRouteResponse)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/CreateRouteResponse)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/CreateRouteResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigatewayv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
