---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/apis-apiid-models-modelid-template.html
---

# ModelTemplate
<a name="apis-apiid-models-modelid-template"></a>

Represents a model template. Supported only for WebSocket APIs.

## URI
<a name="apis-apiid-models-modelid-template-url"></a>

`/v2/apis/{{apiId}}/models/{{modelId}}/template`

## HTTP methods
<a name="apis-apiid-models-modelid-template-http-methods"></a>

### GET
<a name="apis-apiid-models-modelid-templateget"></a>

**Operation ID:** `GetModelTemplate`

Gets a model template.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{modelId}} | String | True | The model ID. |
| {{apiId}} | String | True | The API identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Template | Success |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="apis-apiid-models-modelid-template-schemas"></a>

### Response bodies
<a name="apis-apiid-models-modelid-template-response-examples"></a>

#### Template schema
<a name="apis-apiid-models-modelid-template-response-body-template-example"></a>

```
{
  "value": "string"
}
```

#### NotFoundException schema
<a name="apis-apiid-models-modelid-template-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededException schema
<a name="apis-apiid-models-modelid-template-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="apis-apiid-models-modelid-template-properties"></a>

### LimitExceededException
<a name="apis-apiid-models-modelid-template-model-limitexceededexception"></a>

A limit has been exceeded. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type. |
| message | string | False | Describes the error encountered. |

### NotFoundException
<a name="apis-apiid-models-modelid-template-model-notfoundexception"></a>

The resource specified in the request was not found. See the `message` field for more information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |
| resourceType | string | False | The resource type. |

### Template
<a name="apis-apiid-models-modelid-template-model-template"></a>

Represents a template.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| value | string | False | The template value. |

## See also
<a name="apis-apiid-models-modelid-template-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetModelTemplate
<a name="GetModelTemplate-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/GetModelTemplate)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/GetModelTemplate)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/GetModelTemplate)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/GetModelTemplate)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/GetModelTemplate)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/GetModelTemplate)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/GetModelTemplate)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/GetModelTemplate)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/GetModelTemplate)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/GetModelTemplate)
