---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/apis-apiid-routes-routeid-requestparameters-requestparameterkey.html
---

# RouteRequestParameter
<a name="apis-apiid-routes-routeid-requestparameters-requestparameterkey"></a>

Represents a route request parameter.

## URI
<a name="apis-apiid-routes-routeid-requestparameters-requestparameterkey-url"></a>

`/v2/apis/{{apiId}}/routes/{{routeId}}/requestparameters/{{requestParameterKey}}`

## HTTP methods
<a name="apis-apiid-routes-routeid-requestparameters-requestparameterkey-http-methods"></a>

### DELETE
<a name="apis-apiid-routes-routeid-requestparameters-requestparameterkeydelete"></a>

**Operation ID:** `DeleteRouteRequestParameter`

Deletes a route request parameter. Supported only for WebSocket APIs.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{requestParameterKey}} | String | True | The route request parameter key. |
| {{apiId}} | String | True | The API identifier. |
| {{routeId}} | String | True | The route ID. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | The request has succeeded, and there is no additional content to send in the response payload body. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="apis-apiid-routes-routeid-requestparameters-requestparameterkey-schemas"></a>

### Response bodies
<a name="apis-apiid-routes-routeid-requestparameters-requestparameterkey-response-examples"></a>

#### NotFoundException schema
<a name="apis-apiid-routes-routeid-requestparameters-requestparameterkey-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededException schema
<a name="apis-apiid-routes-routeid-requestparameters-requestparameterkey-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="apis-apiid-routes-routeid-requestparameters-requestparameterkey-properties"></a>

### LimitExceededException
<a name="apis-apiid-routes-routeid-requestparameters-requestparameterkey-model-limitexceededexception"></a>

A limit has been exceeded. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type. |
| message | string | False | Describes the error encountered. |

### NotFoundException
<a name="apis-apiid-routes-routeid-requestparameters-requestparameterkey-model-notfoundexception"></a>

The resource specified in the request was not found. See the `message` field for more information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |
| resourceType | string | False | The resource type. |

## See also
<a name="apis-apiid-routes-routeid-requestparameters-requestparameterkey-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DeleteRouteRequestParameter
<a name="DeleteRouteRequestParameter-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/DeleteRouteRequestParameter)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/DeleteRouteRequestParameter)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/DeleteRouteRequestParameter)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/DeleteRouteRequestParameter)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/DeleteRouteRequestParameter)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/DeleteRouteRequestParameter)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/DeleteRouteRequestParameter)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/DeleteRouteRequestParameter)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/DeleteRouteRequestParameter)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/DeleteRouteRequestParameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigatewayv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
