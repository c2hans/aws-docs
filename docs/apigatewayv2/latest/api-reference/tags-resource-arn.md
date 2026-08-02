---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/tags-resource-arn.html
---

# Tags
<a name="tags-resource-arn"></a>

Represents a collection of tags associated with the resource.

## URI
<a name="tags-resource-arn-url"></a>

`/v2/tags/{{resource-arn}}`

## HTTP methods
<a name="tags-resource-arn-http-methods"></a>

### GET
<a name="tags-resource-arnget"></a>

**Operation ID:** `GetTags`

Gets a collection of `Tag` resources.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resource-arn}} | String | True | The resource ARN for the tag. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Tags | Success |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 409 | ConflictException | The resource already exists. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### POST
<a name="tags-resource-arnpost"></a>

**Operation ID:** `TagResource`

Creates a new `Tag` resource to represent a tag.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resource-arn}} | String | True | The resource ARN for the tag. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | None | The request has succeeded and has resulted in the creation of a resource. |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 409 | ConflictException | The resource already exists. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### DELETE
<a name="tags-resource-arndelete"></a>

**Operation ID:** `UntagResource`

Deletes a `Tag`.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resource-arn}} | String | True | The resource ARN for the tag. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| tagKeys | String | True | The tag keys. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | The request has succeeded, and there is no additional content to send in the response payload body. |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 409 | ConflictException | The resource already exists. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

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
}
```

#### BadRequestException schema
<a name="tags-resource-arn-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="tags-resource-arn-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### ConflictException schema
<a name="tags-resource-arn-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceededException schema
<a name="tags-resource-arn-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="tags-resource-arn-properties"></a>

### BadRequestException
<a name="tags-resource-arn-model-badrequestexception"></a>

The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### ConflictException
<a name="tags-resource-arn-model-conflictexception"></a>

The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### LimitExceededException
<a name="tags-resource-arn-model-limitexceededexception"></a>

A limit has been exceeded. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type. |
| message | string | False | Describes the error encountered. |

### NotFoundException
<a name="tags-resource-arn-model-notfoundexception"></a>

The resource specified in the request was not found. See the `message` field for more information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |
| resourceType | string | False | The resource type. |

### TagResourceInput
<a name="tags-resource-arn-model-tagresourceinput"></a>

Represents the input parameters for a `TagResource` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| tags | [Tags](#tags-resource-arn-model-tags) | False | The collection of tags. Each tag element is associated with a given resource. |

### Tags
<a name="tags-resource-arn-model-tags"></a>

Represents a collection of tags associated with the resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

## See also
<a name="tags-resource-arn-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetTags
<a name="GetTags-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/GetTags)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/GetTags)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/GetTags)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/GetTags)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/GetTags)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/GetTags)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/GetTags)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/GetTags)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/GetTags)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/GetTags)

### TagResource
<a name="TagResource-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/TagResource)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/TagResource)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/TagResource)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/TagResource)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/TagResource)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/TagResource)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/TagResource)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/TagResource)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/TagResource)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/TagResource)

### UntagResource
<a name="UntagResource-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/UntagResource)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/UntagResource)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/UntagResource)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/UntagResource)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/UntagResource)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/UntagResource)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/UntagResource)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/UntagResource)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/UntagResource)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/UntagResource)
