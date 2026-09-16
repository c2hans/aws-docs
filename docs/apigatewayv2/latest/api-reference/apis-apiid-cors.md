---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/apis-apiid-cors.html
---

# Cors
<a name="apis-apiid-cors"></a>

Represents a CORS configuration. Supported only for HTTP APIs.

## URI
<a name="apis-apiid-cors-url"></a>

`/v2/apis/{{apiId}}/cors`

## HTTP methods
<a name="apis-apiid-cors-http-methods"></a>

### DELETE
<a name="apis-apiid-corsdelete"></a>

**Operation ID:** `DeleteCorsConfiguration`

Deletes a CORS configuration.

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

## Schemas
<a name="apis-apiid-cors-schemas"></a>

### Response bodies
<a name="apis-apiid-cors-response-examples"></a>

#### NotFoundException schema
<a name="apis-apiid-cors-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededException schema
<a name="apis-apiid-cors-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="apis-apiid-cors-properties"></a>

### LimitExceededException
<a name="apis-apiid-cors-model-limitexceededexception"></a>

A limit has been exceeded. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type. |
| message | string | False | Describes the error encountered. |

### NotFoundException
<a name="apis-apiid-cors-model-notfoundexception"></a>

The resource specified in the request was not found. See the `message` field for more information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |
| resourceType | string | False | The resource type. |

## See also
<a name="apis-apiid-cors-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DeleteCorsConfiguration
<a name="DeleteCorsConfiguration-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/DeleteCorsConfiguration)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/DeleteCorsConfiguration)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/DeleteCorsConfiguration)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/DeleteCorsConfiguration)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/DeleteCorsConfiguration)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/DeleteCorsConfiguration)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/DeleteCorsConfiguration)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/DeleteCorsConfiguration)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/DeleteCorsConfiguration)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/DeleteCorsConfiguration)
