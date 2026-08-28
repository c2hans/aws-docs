---
source_url: https://docs.aws.amazon.com/amazon-mq/latest/api-reference/tags-resource-arn.html
---

# Tag
<a name="tags-resource-arn"></a>

A tag is a key-value pair associated with a resource. You can use these metadata tags to identify the purpose of a broker or configuration. For more information see [Tagging resources](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-tagging.html) in the Amazon MQ Developer Guide.

## URI
<a name="tags-resource-arn-url"></a>

`/v1/tags/{{resource-arn}}`

## HTTP methods
<a name="tags-resource-arn-http-methods"></a>

### GET
<a name="tags-resource-arnget"></a>

**Operation ID:** `ListTags`

Lists tags for a resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resource-arn}} | String | True | The Amazon Resource Name (ARN) of the resource tag. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Tags | HTTP Status Code 200: OK. |
| 400 | Error | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 403 | Error | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 404 | Error | HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it. |
| 500 | Error | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |

### POST
<a name="tags-resource-arnpost"></a>

**Operation ID:** `CreateTags`

Add a tag to a resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resource-arn}} | String | True | The Amazon Resource Name (ARN) of the resource tag. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | HTTP Status Code 204: Successful response.  |
| 400 | Error | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 403 | Error | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 404 | Error | HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it. |
| 500 | Error | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |

### DELETE
<a name="tags-resource-arndelete"></a>

**Operation ID:** `DeleteTags`

Removes a tag from a resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resource-arn}} | String | True | The Amazon Resource Name (ARN) of the resource tag. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| tagKeys | String | True | An array of tag keys to delete |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | HTTP Status Code 204: Successful response.  |
| 400 | Error | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 403 | Error | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 404 | Error | HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it. |
| 500 | Error | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |

### OPTIONS
<a name="tags-resource-arnoptions"></a>

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resource-arn}} | String | True | The Amazon Resource Name (ARN) of the resource tag. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="tags-resource-arn-schemas"></a>

### Request bodies
<a name="tags-resource-arn-request-examples"></a>

#### POST schema
<a name="tags-resource-arn-request-body-post-example"></a>

```
{
  "tags": {
  }
}
```

### Response bodies
<a name="tags-resource-arn-response-examples"></a>

#### Tags schema
<a name="tags-resource-arn-response-body-tags-example"></a>

```
{
  "tags": {
  }
}
```

#### Error schema
<a name="tags-resource-arn-response-body-error-example"></a>

```
{
  "errorAttribute": "string",
  "message": "string"
}
```

## Properties
<a name="tags-resource-arn-properties"></a>

### Error
<a name="tags-resource-arn-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| errorAttribute | string | False | The attribute which caused the error. |
| message | string | False | The explanation of the error. |

### Tags
<a name="tags-resource-arn-model-tags"></a>

A map of the key-value pairs for the resource tag.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| tags | object | False | The key-value pair for the resource tag. |

## See also
<a name="tags-resource-arn-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListTags
<a name="ListTags-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mq-2017-11-27/ListTags)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mq-2017-11-27/ListTags)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mq-2017-11-27/ListTags)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mq-2017-11-27/ListTags)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mq-2017-11-27/ListTags)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mq-2017-11-27/ListTags)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mq-2017-11-27/ListTags)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mq-2017-11-27/ListTags)
+ [AWS SDK for Python](/goto/boto3/mq-2017-11-27/ListTags)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mq-2017-11-27/ListTags)

### CreateTags
<a name="CreateTags-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mq-2017-11-27/CreateTags)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mq-2017-11-27/CreateTags)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mq-2017-11-27/CreateTags)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mq-2017-11-27/CreateTags)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mq-2017-11-27/CreateTags)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mq-2017-11-27/CreateTags)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mq-2017-11-27/CreateTags)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mq-2017-11-27/CreateTags)
+ [AWS SDK for Python](/goto/boto3/mq-2017-11-27/CreateTags)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mq-2017-11-27/CreateTags)

### DeleteTags
<a name="DeleteTags-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mq-2017-11-27/DeleteTags)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mq-2017-11-27/DeleteTags)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mq-2017-11-27/DeleteTags)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mq-2017-11-27/DeleteTags)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mq-2017-11-27/DeleteTags)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mq-2017-11-27/DeleteTags)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mq-2017-11-27/DeleteTags)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mq-2017-11-27/DeleteTags)
+ [AWS SDK for Python](/goto/boto3/mq-2017-11-27/DeleteTags)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mq-2017-11-27/DeleteTags)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MQ. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazon-mq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
