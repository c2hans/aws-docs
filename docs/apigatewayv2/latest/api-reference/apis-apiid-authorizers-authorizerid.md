---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/apis-apiid-authorizers-authorizerid.html
---

# Authorizer
<a name="apis-apiid-authorizers-authorizerid"></a>

Represents an authorizer. `JWT` authorizers are supported only for HTTP APIs.

## URI
<a name="apis-apiid-authorizers-authorizerid-url"></a>

`/v2/apis/{{apiId}}/authorizers/{{authorizerId}}`

## HTTP methods
<a name="apis-apiid-authorizers-authorizerid-http-methods"></a>

### GET
<a name="apis-apiid-authorizers-authorizeridget"></a>

**Operation ID:** `GetAuthorizer`

Gets an `Authorizer`.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{authorizerId}} | String | True | The authorizer identifier. |
| {{apiId}} | String | True | The API identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Authorizer | Success |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### DELETE
<a name="apis-apiid-authorizers-authorizeriddelete"></a>

**Operation ID:** `DeleteAuthorizer`

Deletes an `Authorizer`.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{authorizerId}} | String | True | The authorizer identifier. |
| {{apiId}} | String | True | The API identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | The request has succeeded, and there is no additional content to send in the response payload body. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### PATCH
<a name="apis-apiid-authorizers-authorizeridpatch"></a>

**Operation ID:** `UpdateAuthorizer`

Updates an `Authorizer`.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{authorizerId}} | String | True | The authorizer identifier. |
| {{apiId}} | String | True | The API identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Authorizer | Success |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 409 | ConflictException | The resource already exists. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="apis-apiid-authorizers-authorizerid-schemas"></a>

### Request bodies
<a name="apis-apiid-authorizers-authorizerid-request-examples"></a>

#### PATCH schema
<a name="apis-apiid-authorizers-authorizerid-request-body-patch-example"></a>

```
{
  "name": "string",
  "authorizerType": enum,
  "authorizerUri": "string",
  "authorizerCredentialsArn": "string",
  "identitySource": [
    "string"
  ],
  "identityValidationExpression": "string",
  "authorizerResultTtlInSeconds": integer,
  "jwtConfiguration": {
    "issuer": "string",
    "audience": [
      "string"
    ]
  },
  "authorizerPayloadFormatVersion": "string",
  "enableSimpleResponses": boolean
}
```

### Response bodies
<a name="apis-apiid-authorizers-authorizerid-response-examples"></a>

#### Authorizer schema
<a name="apis-apiid-authorizers-authorizerid-response-body-authorizer-example"></a>

```
{
  "authorizerId": "string",
  "name": "string",
  "authorizerType": enum,
  "authorizerUri": "string",
  "authorizerCredentialsArn": "string",
  "identitySource": [
    "string"
  ],
  "identityValidationExpression": "string",
  "authorizerResultTtlInSeconds": integer,
  "jwtConfiguration": {
    "issuer": "string",
    "audience": [
      "string"
    ]
  },
  "authorizerPayloadFormatVersion": "string",
  "enableSimpleResponses": boolean
}
```

#### BadRequestException schema
<a name="apis-apiid-authorizers-authorizerid-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="apis-apiid-authorizers-authorizerid-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### ConflictException schema
<a name="apis-apiid-authorizers-authorizerid-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceededException schema
<a name="apis-apiid-authorizers-authorizerid-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="apis-apiid-authorizers-authorizerid-properties"></a>

### Authorizer
<a name="apis-apiid-authorizers-authorizerid-model-authorizer"></a>

Represents an authorizer.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| authorizerCredentialsArn | string | False | Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, don't specify this parameter. Supported only for `REQUEST` authorizers. |
| authorizerId | string | False | The authorizer identifier. |
| authorizerPayloadFormatVersion | string | False | Specifies the format of the payload sent to an HTTP API Lambda authorizer. Required for HTTP API Lambda authorizers. Supported values are `1.0` and `2.0`. To learn more, see [Working with AWS Lambda authorizers for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html). |
| authorizerResultTtlInSeconds | integer | False | The time to live (TTL) for cached authorizer results, in seconds. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway caches authorizer responses. The maximum value is 3600, or 1 hour. Supported only for HTTP API Lambda authorizers. |
| authorizerType | [AuthorizerType](#apis-apiid-authorizers-authorizerid-model-authorizertype) | False | The authorizer type. Specify `REQUEST` for a Lambda function using incoming request parameters. Specify `JWT` to use JSON Web Tokens (supported only for HTTP APIs). |
| authorizerUri | string | False | The authorizer's Uniform Resource Identifier (URI). For`REQUEST` authorizers, this must be a well-formed Lambda function URI, for example, `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{{{account_id}}}:function:{{{lambda_function_name}}}/invocations`. In general, the URI has this form: `arn:aws:apigateway:{{{region}}}:lambda:path/{{{service_api}}} `, where {{}}{region} is the same as the region hosting the Lambda function, path indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial `/`. For Lambda functions, this is usually of the form `/2015-03-31/functions/[FunctionARN]/invocations`. Supported only for `REQUEST` authorizers. |
| enableSimpleResponses | boolean | False | Specifies whether a Lambda authorizer returns a response in a simple format. If enabled, the Lambda authorizer can return a boolean value instead of an IAM policy. Supported only for HTTP APIs. To learn more, see [Working with AWS Lambda authorizers for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html). |
| identitySource | Array of type string | False | The identity source for which authorization is requested.<br />For a `REQUEST` authorizer, this is optional. The value is a set of one or more mapping expressions of the specified request parameters. The identity source can be headers, query string parameters, stage variables, and context parameters. For example, if an Auth header and a Name query string parameter are defined as identity sources, this value is route.request.header.Auth, route.request.querystring.Name for WebSocket APIs. For HTTP APIs, use selection expressions prefixed with `$`, for example, `$request.header.Auth`, `$request.querystring.Name`. These parameters are used to perform runtime validation for Lambda-based authorizers by verifying all of the identity-related request parameters are present in the request, not null, and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function. Otherwise, it returns a 401 Unauthorized response without calling the Lambda function. For HTTP APIs, identity sources are also used as the cache key when caching is enabled. To learn more, see [Working with AWS Lambda authorizers for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html).<br />For `JWT`, a single entry that specifies where to extract the JSON Web Token (JWT) from inbound requests. Currently only header-based and query parameter-based selections are supported, for example `$request.header.Authorization`. |
| identityValidationExpression | string | False | The validation expression does not apply to the `REQUEST` authorizer. |
| jwtConfiguration | [JWTConfiguration](#apis-apiid-authorizers-authorizerid-model-jwtconfiguration) | False | Represents the configuration of a JWT authorizer. Required for the `JWT` authorizer type. Supported only for HTTP APIs. |
| name | string | True | The name of the authorizer. |

### AuthorizerType
<a name="apis-apiid-authorizers-authorizerid-model-authorizertype"></a>

The authorizer type. Specify `REQUEST` for a Lambda function using incoming request parameters. Specify `JWT` to use JSON Web Tokens (supported only for HTTP APIs).
+ `REQUEST`
+ `JWT`

### BadRequestException
<a name="apis-apiid-authorizers-authorizerid-model-badrequestexception"></a>

The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### ConflictException
<a name="apis-apiid-authorizers-authorizerid-model-conflictexception"></a>

The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### JWTConfiguration
<a name="apis-apiid-authorizers-authorizerid-model-jwtconfiguration"></a>

Represents the configuration of a JWT authorizer. Required for the `JWT` authorizer type. Supported only for HTTP APIs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audience | Array of type string | False | A list of the intended recipients of the JWT. A valid JWT must provide an `aud` that matches at least one entry in this list. See [RFC 7519](https://tools.ietf.org/html/rfc7519#section-4.1.3). Required for the `JWT` authorizer type. Supported only for HTTP APIs. |
| issuer | string | False | The base domain of the identity provider that issues JSON Web Tokens. For example, an Amazon Cognito user pool has the following format: `https://cognito-idp.{{{region}}}.amazonaws.com/{{{userPoolId}}} `. Required for the `JWT` authorizer type. Supported only for HTTP APIs. |

### LimitExceededException
<a name="apis-apiid-authorizers-authorizerid-model-limitexceededexception"></a>

A limit has been exceeded. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type. |
| message | string | False | Describes the error encountered. |

### NotFoundException
<a name="apis-apiid-authorizers-authorizerid-model-notfoundexception"></a>

The resource specified in the request was not found. See the `message` field for more information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |
| resourceType | string | False | The resource type. |

### UpdateAuthorizerInput
<a name="apis-apiid-authorizers-authorizerid-model-updateauthorizerinput"></a>

The input parameters for an `UpdateAuthorizer` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| authorizerCredentialsArn | string | False | Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, don't specify this parameter. |
| authorizerPayloadFormatVersion | string | False | Specifies the format of the payload sent to an HTTP API Lambda authorizer. Required for HTTP API Lambda authorizers. Supported values are `1.0` and `2.0`. To learn more, see [Working with AWS Lambda authorizers for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html). |
| authorizerResultTtlInSeconds | integer | False | The time to live (TTL) for cached authorizer results, in seconds. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway caches authorizer responses. The maximum value is 3600, or 1 hour. Supported only for HTTP API Lambda authorizers. |
| authorizerType | [AuthorizerType](#apis-apiid-authorizers-authorizerid-model-authorizertype) | False | The authorizer type. Specify `REQUEST` for a Lambda function using incoming request parameters. Specify `JWT` to use JSON Web Tokens (supported only for HTTP APIs). |
| authorizerUri | string | False | The authorizer's Uniform Resource Identifier (URI). For `REQUEST` authorizers, this must be a well-formed Lambda function URI, for example, `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{{{account_id}}}:function:{{{lambda_function_name}}}/invocations`. In general, the URI has this form: `arn:aws:apigateway:{{{region}}}:lambda:path/{{{service_api}}} `, where {{}}{region} is the same as the region hosting the Lambda function, path indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial `/`. For Lambda functions, this is usually of the form `/2015-03-31/functions/[FunctionARN]/invocations`. Supported only for `REQUEST` authorizers. |
| enableSimpleResponses | boolean | False | Specifies whether a Lambda authorizer returns a response in a simple format. By default, a Lambda authorizer must return an IAM policy. If enabled, the Lambda authorizer can return a boolean value instead of an IAM policy. Supported only for HTTP APIs. To learn more, see [Working with AWS Lambda authorizers for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html). |
| identitySource | Array of type string | False | The identity source for which authorization is requested.<br />For a `REQUEST` authorizer, this is optional. The value is a set of one or more mapping expressions of the specified request parameters. The identity source can be headers, query string parameters, stage variables, and context parameters. For example, if an Auth header and a Name query string parameter are defined as identity sources, this value is route.request.header.Auth, route.request.querystring.Name for WebSocket APIs. For HTTP APIs, use selection expressions prefixed with `$`, for example, `$request.header.Auth`, `$request.querystring.Name`. These parameters are used to perform runtime validation for Lambda-based authorizers by verifying all of the identity-related request parameters are present in the request, not null, and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function. Otherwise, it returns a 401 Unauthorized response without calling the Lambda function. For HTTP APIs, identity sources are also used as the cache key when caching is enabled. To learn more, see [Working with AWS Lambda authorizers for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html).<br />For `JWT`, a single entry that specifies where to extract the JSON Web Token (JWT) from inbound requests. Currently only header-based and query parameter-based selections are supported, for example `$request.header.Authorization`. |
| identityValidationExpression | string | False | This parameter is not used. |
| jwtConfiguration | [JWTConfiguration](#apis-apiid-authorizers-authorizerid-model-jwtconfiguration) | False | Represents the configuration of a JWT authorizer. Required for the `JWT` authorizer type. Supported only for HTTP APIs.  |
| name | string | False | The name of the authorizer. |

## See also
<a name="apis-apiid-authorizers-authorizerid-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetAuthorizer
<a name="GetAuthorizer-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/GetAuthorizer)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/GetAuthorizer)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/GetAuthorizer)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/GetAuthorizer)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/GetAuthorizer)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/GetAuthorizer)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/GetAuthorizer)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/GetAuthorizer)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/GetAuthorizer)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/GetAuthorizer)

### DeleteAuthorizer
<a name="DeleteAuthorizer-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/DeleteAuthorizer)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/DeleteAuthorizer)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/DeleteAuthorizer)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/DeleteAuthorizer)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/DeleteAuthorizer)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/DeleteAuthorizer)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/DeleteAuthorizer)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/DeleteAuthorizer)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/DeleteAuthorizer)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/DeleteAuthorizer)

### UpdateAuthorizer
<a name="UpdateAuthorizer-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/UpdateAuthorizer)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/UpdateAuthorizer)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/UpdateAuthorizer)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/UpdateAuthorizer)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/UpdateAuthorizer)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/UpdateAuthorizer)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/UpdateAuthorizer)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/UpdateAuthorizer)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/UpdateAuthorizer)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/UpdateAuthorizer)
