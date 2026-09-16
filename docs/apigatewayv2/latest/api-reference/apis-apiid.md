---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/apis-apiid.html
---

# Api
<a name="apis-apiid"></a>

Represents an API.

## URI
<a name="apis-apiid-url"></a>

`/v2/apis/{{apiId}}`

## HTTP methods
<a name="apis-apiid-http-methods"></a>

### GET
<a name="apis-apiidget"></a>

**Operation ID:** `GetApi`

Gets an `Api` resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{apiId}} | String | True | The API identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Api | Success |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### PUT
<a name="apis-apiidput"></a>

**Operation ID:** `ReimportApi`

Puts an `Api` resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{apiId}} | String | True | The API identifier. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| failOnWarnings | String | False | Specifies whether to rollback the API creation when a warning is encountered. By default, API creation continues if a warning is encountered. |
| basepath | String | False | Specifies how to interpret the base path of the API during import. Valid values are `ignore`, `prepend`, and `split`. The default value is `ignore`. To learn more, see [Set the OpenAPI basePath Property](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api-basePath.html). Supported only for HTTP APIs. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | Api | The request has succeeded and has resulted in the creation of a resource. |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 409 | ConflictException | The resource already exists. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### DELETE
<a name="apis-apiiddelete"></a>

**Operation ID:** `DeleteApi`

Deletes an `Api` resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{apiId}} | String | True | The API identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | The request has succeeded, and there is no additional content to send in the response payload body. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### PATCH
<a name="apis-apiidpatch"></a>

**Operation ID:** `UpdateApi`

Updates an `Api` resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{apiId}} | String | True | The API identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Api | Success |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 409 | ConflictException | The resource already exists. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="apis-apiid-schemas"></a>

### Request bodies
<a name="apis-apiid-request-examples"></a>

#### PUT schema
<a name="apis-apiid-request-body-put-example"></a>

```
{
  "body": "string"
}
```

#### PATCH schema
<a name="apis-apiid-request-body-patch-example"></a>

```
{
  "name": "string",
  "description": "string",
  "version": "string",
  "routeSelectionExpression": "string",
  "apiKeySelectionExpression": "string",
  "disableSchemaValidation": boolean,
  "target": "string",
  "credentialsArn": "string",
  "routeKey": "string",
  "corsConfiguration": {
    "allowOrigins": [
      "string"
    ],
    "allowCredentials": boolean,
    "exposeHeaders": [
      "string"
    ],
    "maxAge": integer,
    "allowMethods": [
      "string"
    ],
    "allowHeaders": [
      "string"
    ]
  },
  "disableExecuteApiEndpoint": boolean,
  "ipAddressType": enum
}
```

### Response bodies
<a name="apis-apiid-response-examples"></a>

#### Api schema
<a name="apis-apiid-response-body-api-example"></a>

```
{
  "apiId": "string",
  "name": "string",
  "description": "string",
  "version": "string",
  "protocolType": enum,
  "ipAddressType": enum,
  "routeSelectionExpression": "string",
  "apiKeySelectionExpression": "string",
  "disableSchemaValidation": boolean,
  "warnings": [
    "string"
  ],
  "importInfo": [
    "string"
  ],
  "apiEndpoint": "string",
  "apiGatewayManaged": boolean,
  "createdDate": "string",
  "tags": {
  },
  "corsConfiguration": {
    "allowOrigins": [
      "string"
    ],
    "allowCredentials": boolean,
    "exposeHeaders": [
      "string"
    ],
    "maxAge": integer,
    "allowMethods": [
      "string"
    ],
    "allowHeaders": [
      "string"
    ]
  },
  "disableExecuteApiEndpoint": boolean
}
```

#### BadRequestException schema
<a name="apis-apiid-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="apis-apiid-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### ConflictException schema
<a name="apis-apiid-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceededException schema
<a name="apis-apiid-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="apis-apiid-properties"></a>

### Api
<a name="apis-apiid-model-api"></a>

Represents an API.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| apiEndpoint | string<br />Format: uri | False | The URI of the API, of the form {api-id}.execute-api.{region}.amazonaws.com. The stage name is typically appended to this URI to form a complete path to a deployed API stage. |
| apiGatewayManaged | boolean | False | Specifies whether an API is managed by API Gateway. You can't update or delete a managed API by using API Gateway. A managed API can be deleted only through the tooling or service that created it. |
| apiId | string | False | The API ID. |
| apiKeySelectionExpression | string | False | An API key selection expression. Supported only for WebSocket APIs. See [API Key Selection Expressions](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions). |
| corsConfiguration | [Cors](#apis-apiid-model-cors) | False | A CORS configuration. Supported only for HTTP APIs. |
| createdDate | string<br />Format: date-time | False | The timestamp when the API was created. |
| description | string | False | The description of the API. |
| disableExecuteApiEndpoint | boolean | False | Specifies whether clients can invoke your API by using the default `execute-api` endpoint. By default, clients can invoke your API with the default https://{api\_id}.execute-api.{region}.amazonaws.com endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint. |
| disableSchemaValidation | boolean | False | Avoid validating models when creating a deployment. Supported only for WebSocket APIs. |
| importInfo | Array of type string | False | The validation information during API import. This may include particular properties of your OpenAPI definition which are ignored during import. Supported only for HTTP APIs. |
| ipAddressType | [IpAddressType](#apis-apiid-model-ipaddresstype) | False | The IP address types that can invoke the API. |
| name | string | True | The name of the API. |
| protocolType | [ProtocolType](#apis-apiid-model-protocoltype) | True | The API protocol. |
| routeSelectionExpression | string | True | The route selection expression for the API. For HTTP APIs, the `routeSelectionExpression` must be `${request.method} ${request.path}`. If not provided, this will be the default for HTTP APIs. This property is required for WebSocket APIs. |
| tags | [Tags](#apis-apiid-model-tags) | False | A collection of tags associated with the API. |
| version | string | False | A version identifier for the API. |
| warnings | Array of type string | False | The warning messages reported when `failonwarnings` is turned on during API import. |

### BadRequestException
<a name="apis-apiid-model-badrequestexception"></a>

The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### ConflictException
<a name="apis-apiid-model-conflictexception"></a>

The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### Cors
<a name="apis-apiid-model-cors"></a>

Represents a CORS configuration. Supported only for HTTP APIs. See [Configuring CORS](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-cors.html) for more information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| allowCredentials | boolean | False | Specifies whether credentials are included in the CORS request. Supported only for HTTP APIs. |
| allowHeaders | Array of type string | False | Represents a collection of allowed headers. Supported only for HTTP APIs. |
| allowMethods | Array of type string | False | Represents a collection of allowed HTTP methods. Supported only for HTTP APIs. |
| allowOrigins | Array of type string | False | Represents a collection of allowed origins. Supported only for HTTP APIs. |
| exposeHeaders | Array of type string | False | Represents a collection of exposed headers. Supported only for HTTP APIs. |
| maxAge | integer | False | The number of seconds that the browser should cache preflight request results. Supported only for HTTP APIs. |

### IpAddressType
<a name="apis-apiid-model-ipaddresstype"></a>

The IP address types that can invoke your API or domain name.
+ `ipv4`
+ `dualstack`

### LimitExceededException
<a name="apis-apiid-model-limitexceededexception"></a>

A limit has been exceeded. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type. |
| message | string | False | Describes the error encountered. |

### NotFoundException
<a name="apis-apiid-model-notfoundexception"></a>

The resource specified in the request was not found. See the `message` field for more information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |
| resourceType | string | False | The resource type. |

### ProtocolType
<a name="apis-apiid-model-protocoltype"></a>

Represents a protocol type.
+ `WEBSOCKET`
+ `HTTP`

### ReimportApiInput
<a name="apis-apiid-model-reimportapiinput"></a>

Overwrites the configuration of an existing API using the provided definition. Supported only for HTTP APIs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| body | string | True | The OpenAPI definition. Supported only for HTTP APIs. |

### Tags
<a name="apis-apiid-model-tags"></a>

Represents a collection of tags associated with the resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### UpdateApiInput
<a name="apis-apiid-model-updateapiinput"></a>

Represents the input parameters for an `UpdateApi` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| apiKeySelectionExpression | string | False | An API key selection expression. Supported only for WebSocket APIs. See [API Key Selection Expressions](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions). |
| corsConfiguration | [Cors](#apis-apiid-model-cors) | False | A CORS configuration. Supported only for HTTP APIs. |
| credentialsArn | string | False | This property is part of quick create. It specifies the credentials required for the integration, if any. For a Lambda integration, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify `arn:aws:iam::*:user/*`. To use resource-based permissions on supported AWS services, don't specify this parameter. Currently, this property is not used for HTTP integrations. If provided, this value replaces the credentials associated with the quick create integration. Supported only for HTTP APIs. |
| description | string | False | The description of the API. |
| disableExecuteApiEndpoint | boolean | False | Specifies whether clients can invoke your API by using the default `execute-api` endpoint. By default, clients can invoke your API with the default https://{api\_id}.execute-api.{region}.amazonaws.com endpoint. To require that clients use a custom domain name to invoke your API, disable the default `execute-api` endpoint. |
| disableSchemaValidation | boolean | False | Avoid validating models when creating a deployment. Supported only for WebSocket APIs. |
| ipAddressType | [IpAddressType](#apis-apiid-model-ipaddresstype) | False | The IP address types that can invoke the API. Use `ipv4` to allow only IPv4 addresses to invoke your API, or use `dualstack` to allow both IPv4 and IPv6 addresses to invoke your API. |
| name | string | False | The name of the API. |
| routeKey | string | False | This property is part of quick create. If not specified, the route created using quick create is kept. Otherwise, this value replaces the route key of the quick create route. Additional routes may still be added after the API is updated. Supported only for HTTP APIs. |
| routeSelectionExpression | string | False | The route selection expression for the API. For HTTP APIs, the `routeSelectionExpression` must be `${request.method} ${request.path}`. If not provided, this will be the default for HTTP APIs. This property is required for WebSocket APIs. |
| target | string | False | This property is part of quick create. For HTTP integrations, specify a fully qualified URL. For Lambda integrations, specify a function ARN. The type of the integration will be HTTP\_PROXY or AWS\_PROXY, respectively. The value provided updates the integration URI and integration type. You can update a quick-created target, but you can't remove it from an API. Supported only for HTTP APIs. |
| version | string | False | A version identifier for the API. |

## See also
<a name="apis-apiid-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetApi
<a name="GetApi-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/GetApi)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/GetApi)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/GetApi)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/GetApi)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/GetApi)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/GetApi)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/GetApi)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/GetApi)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/GetApi)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/GetApi)

### ReimportApi
<a name="ReimportApi-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/ReimportApi)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/ReimportApi)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/ReimportApi)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/ReimportApi)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/ReimportApi)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/ReimportApi)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/ReimportApi)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/ReimportApi)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/ReimportApi)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/ReimportApi)

### DeleteApi
<a name="DeleteApi-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/DeleteApi)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/DeleteApi)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/DeleteApi)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/DeleteApi)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/DeleteApi)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/DeleteApi)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/DeleteApi)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/DeleteApi)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/DeleteApi)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/DeleteApi)

### UpdateApi
<a name="UpdateApi-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/UpdateApi)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/UpdateApi)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/UpdateApi)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/UpdateApi)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/UpdateApi)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/UpdateApi)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/UpdateApi)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/UpdateApi)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/UpdateApi)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/UpdateApi)
