---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/apis-apiid-exports-specification.html
---

# ExportedAPI
<a name="apis-apiid-exports-specification"></a>

Represents an exported definition of an API in a particular output format, for example, YAML. The API is serialized to the requested specification, for example, OpenAPI 3.0.

## URI
<a name="apis-apiid-exports-specification-url"></a>

`/v2/apis/{{apiId}}/exports/{{specification}}`

## HTTP methods
<a name="apis-apiid-exports-specification-http-methods"></a>

### GET
<a name="apis-apiid-exports-specificationget"></a>

**Operation ID:** `ExportApi`

Exports a definition of an API in a particular output format and specification.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{specification}} | String | True | The version of the API specification to use. `OAS30`, for OpenAPI 3.0, is the only supported value. |
| {{apiId}} | String | True | The API identifier. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| includeExtensions | String | False | Specifies whether to include [ API Gateway extensions](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions.html) in the exported API definition. API Gateway extensions are included by default.  |
| stageName | String | False | The name of the API stage to export. If you don't specify this property, a representation of the latest API configuration is exported. |
| exportVersion | String | False | The version of the API Gateway export algorithm. API Gateway uses the latest version by default. Currently, the only supported version is `1.0`. |
| outputType | String | True | The output type of the exported definition file. Valid values are `JSON` and `YAML`. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ExportedApi | Success |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="apis-apiid-exports-specification-schemas"></a>

### Response bodies
<a name="apis-apiid-exports-specification-response-examples"></a>

#### ExportedApi schema
<a name="apis-apiid-exports-specification-response-body-exportedapi-example"></a>

```
"string"
```

#### BadRequestException schema
<a name="apis-apiid-exports-specification-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="apis-apiid-exports-specification-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededException schema
<a name="apis-apiid-exports-specification-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="apis-apiid-exports-specification-properties"></a>

### BadRequestException
<a name="apis-apiid-exports-specification-model-badrequestexception"></a>

The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### LimitExceededException
<a name="apis-apiid-exports-specification-model-limitexceededexception"></a>

A limit has been exceeded. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type. |
| message | string | False | Describes the error encountered. |

### NotFoundException
<a name="apis-apiid-exports-specification-model-notfoundexception"></a>

The resource specified in the request was not found. See the `message` field for more information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |
| resourceType | string | False | The resource type. |

## See also
<a name="apis-apiid-exports-specification-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ExportApi
<a name="ExportApi-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/ExportApi)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/ExportApi)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/ExportApi)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/ExportApi)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/ExportApi)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/ExportApi)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/ExportApi)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/ExportApi)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/ExportApi)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/ExportApi)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigatewayv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
