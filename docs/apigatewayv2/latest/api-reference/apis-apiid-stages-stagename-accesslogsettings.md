---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/apis-apiid-stages-stagename-accesslogsettings.html
---

# AccessLogSettings
<a name="apis-apiid-stages-stagename-accesslogsettings"></a>

Represents the access log settings for a stage.

## URI
<a name="apis-apiid-stages-stagename-accesslogsettings-url"></a>

`/v2/apis/{{apiId}}/stages/{{stageName}}/accesslogsettings`

## HTTP methods
<a name="apis-apiid-stages-stagename-accesslogsettings-http-methods"></a>

### DELETE
<a name="apis-apiid-stages-stagename-accesslogsettingsdelete"></a>

**Operation ID:** `DeleteAccessLogSettings`

Deletes the `AccessLogSettings` for a `Stage`. To disable access logging for a `Stage`, delete its `AccessLogSettings`.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{stageName}} | String | True | The stage name. Stage names can contain only alphanumeric characters, hyphens, and underscores, or be `$default`. Maximum length is 128 characters. |
| {{apiId}} | String | True | The API identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | The request has succeeded, and there is no additional content to send in the response payload body. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="apis-apiid-stages-stagename-accesslogsettings-schemas"></a>

### Response bodies
<a name="apis-apiid-stages-stagename-accesslogsettings-response-examples"></a>

#### NotFoundException schema
<a name="apis-apiid-stages-stagename-accesslogsettings-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededException schema
<a name="apis-apiid-stages-stagename-accesslogsettings-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="apis-apiid-stages-stagename-accesslogsettings-properties"></a>

### LimitExceededException
<a name="apis-apiid-stages-stagename-accesslogsettings-model-limitexceededexception"></a>

A limit has been exceeded. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type. |
| message | string | False | Describes the error encountered. |

### NotFoundException
<a name="apis-apiid-stages-stagename-accesslogsettings-model-notfoundexception"></a>

The resource specified in the request was not found. See the `message` field for more information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |
| resourceType | string | False | The resource type. |

## See also
<a name="apis-apiid-stages-stagename-accesslogsettings-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DeleteAccessLogSettings
<a name="DeleteAccessLogSettings-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/DeleteAccessLogSettings)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/DeleteAccessLogSettings)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/DeleteAccessLogSettings)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/DeleteAccessLogSettings)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/DeleteAccessLogSettings)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/DeleteAccessLogSettings)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/DeleteAccessLogSettings)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/DeleteAccessLogSettings)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/DeleteAccessLogSettings)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/DeleteAccessLogSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigatewayv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
