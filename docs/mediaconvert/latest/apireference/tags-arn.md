---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/apireference/tags-arn.html
---

# Tags arn
<a name="tags-arn"></a>

## URI
<a name="tags-arn-url"></a>

`/2017-08-29/tags/{{arn}}`

## HTTP methods
<a name="tags-arn-http-methods"></a>

### GET
<a name="tags-arnget"></a>

**Operation ID:** `ListTagsForResource`

Retrieve the tags for a MediaConvert resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{arn}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListTagsForResourceResponse | 200 response |
| 400 | ExceptionBody | The service can't process your request because of a problem in the request. Please check your request form and syntax. |
| 402 | ExceptionBody | You attempted to create more resources than the service allows based on service quotas. |
| 403 | ExceptionBody | You don't have permissions for this action with the credentials you sent. |
| 404 | ExceptionBody | The resource you requested does not exist. |
| 409 | ExceptionBody | The service could not complete your request because there is a conflict with the current state of the resource. |
| 429 | ExceptionBody | Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests. |
| 500 | ExceptionBody | The service encountered an unexpected condition and cannot fulfill your request. |

### PUT
<a name="tags-arnput"></a>

**Operation ID:** `UntagResource`

Remove tags from a MediaConvert queue, preset, or job template. For information about tagging, see the User Guide at https://docs.aws.amazon.com/mediaconvert/latest/ug/tagging-resources.html

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{arn}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | UntagResourceResponse | 200 response |
| 400 | ExceptionBody | The service can't process your request because of a problem in the request. Please check your request form and syntax. |
| 402 | ExceptionBody | You attempted to create more resources than the service allows based on service quotas. |
| 403 | ExceptionBody | You don't have permissions for this action with the credentials you sent. |
| 404 | ExceptionBody | The resource you requested does not exist. |
| 409 | ExceptionBody | The service could not complete your request because there is a conflict with the current state of the resource. |
| 429 | ExceptionBody | Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests. |
| 500 | ExceptionBody | The service encountered an unexpected condition and cannot fulfill your request. |

### OPTIONS
<a name="tags-arnoptions"></a>

Supports CORS preflight requests.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{arn}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request completed successfully. |

## Schemas
<a name="tags-arn-schemas"></a>

### Request bodies
<a name="tags-arn-request-examples"></a>

#### GET schema
<a name="tags-arn-request-body-get-example"></a>

```
{
  "arn": "string"
}
```

#### PUT schema
<a name="tags-arn-request-body-put-example"></a>

```
{
  "arn": "string",
  "tagKeys": [
    "string"
  ]
}
```

### Response bodies
<a name="tags-arn-response-examples"></a>

#### ListTagsForResourceResponse schema
<a name="tags-arn-response-body-listtagsforresourceresponse-example"></a>

```
{
  "resourceTags": {
    "arn": "string",
    "tags": {
    }
  }
}
```

#### UntagResourceResponse schema
<a name="tags-arn-response-body-untagresourceresponse-example"></a>

```
{
}
```

#### ExceptionBody schema
<a name="tags-arn-response-body-exceptionbody-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="tags-arn-properties"></a>

### ExceptionBody
<a name="tags-arn-model-exceptionbody"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ListTagsForResourceRequest
<a name="tags-arn-model-listtagsforresourcerequest"></a>

List the tags for your AWS Elemental MediaConvert resource by sending a request with the Amazon Resource Name (ARN) of the resource. To get the ARN, send a GET request with the resource name.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The Amazon Resource Name (ARN) of the resource that you want to list tags for. To get the ARN, send a GET request with the resource name. |

### ListTagsForResourceResponse
<a name="tags-arn-model-listtagsforresourceresponse"></a>

A successful request to list the tags for a resource returns a JSON map of tags.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| resourceTags | [ResourceTags](#tags-arn-model-resourcetags) | False | The Amazon Resource Name (ARN) and tags for an AWS Elemental MediaConvert resource. |

### ResourceTags
<a name="tags-arn-model-resourcetags"></a>

The Amazon Resource Name (ARN) and tags for an AWS Elemental MediaConvert resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The Amazon Resource Name (ARN) of the resource. |
| tags | object | False | The tags for the resource. |

### UntagResourceRequest
<a name="tags-arn-model-untagresourcerequest"></a>

To remove tags from a resource, send a request with the Amazon Resource Name (ARN) of the resource and the keys of the tags that you want to remove.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The Amazon Resource Name (ARN) of the resource that you want to remove tags from. To get the ARN, send a GET request with the resource name. |
| tagKeys | Array of type string | False | The keys of the tags that you want to remove from the resource. |

### UntagResourceResponse
<a name="tags-arn-model-untagresourceresponse"></a>

A successful request to remove tags from a resource returns an OK message.

## See also
<a name="tags-arn-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListTagsForResource
<a name="ListTagsForResource-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediaconvert-2017-08-29/ListTagsForResource)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediaconvert-2017-08-29/ListTagsForResource)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediaconvert-2017-08-29/ListTagsForResource)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediaconvert-2017-08-29/ListTagsForResource)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediaconvert-2017-08-29/ListTagsForResource)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediaconvert-2017-08-29/ListTagsForResource)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediaconvert-2017-08-29/ListTagsForResource)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediaconvert-2017-08-29/ListTagsForResource)
+ [AWS SDK for Python](/goto/boto3/mediaconvert-2017-08-29/ListTagsForResource)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediaconvert-2017-08-29/ListTagsForResource)

### UntagResource
<a name="UntagResource-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediaconvert-2017-08-29/UntagResource)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediaconvert-2017-08-29/UntagResource)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediaconvert-2017-08-29/UntagResource)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediaconvert-2017-08-29/UntagResource)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediaconvert-2017-08-29/UntagResource)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediaconvert-2017-08-29/UntagResource)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediaconvert-2017-08-29/UntagResource)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediaconvert-2017-08-29/UntagResource)
+ [AWS SDK for Python](/goto/boto3/mediaconvert-2017-08-29/UntagResource)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediaconvert-2017-08-29/UntagResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
