---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/apireference/tags.html
---

# Tags
<a name="tags"></a>

## URI
<a name="tags-url"></a>

`/2017-08-29/tags`

## HTTP methods
<a name="tags-http-methods"></a>

### POST
<a name="tagspost"></a>

**Operation ID:** `TagResource`

Add tags to a MediaConvert queue, preset, or job template. For information about tagging, see the User Guide at https://docs.aws.amazon.com/mediaconvert/latest/ug/tagging-resources.html

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | TagResourceResponse | 200 response |
| 400 | ExceptionBody | The service can't process your request because of a problem in the request. Please check your request form and syntax. |
| 402 | ExceptionBody | You attempted to create more resources than the service allows based on service quotas. |
| 403 | ExceptionBody | You don't have permissions for this action with the credentials you sent. |
| 404 | ExceptionBody | The resource you requested does not exist. |
| 409 | ExceptionBody | The service could not complete your request because there is a conflict with the current state of the resource. |
| 429 | ExceptionBody | Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests. |
| 500 | ExceptionBody | The service encountered an unexpected condition and cannot fulfill your request. |

### OPTIONS
<a name="tagsoptions"></a>

Supports CORS preflight requests.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request completed successfully. |

## Schemas
<a name="tags-schemas"></a>

### Request bodies
<a name="tags-request-examples"></a>

#### POST schema
<a name="tags-request-body-post-example"></a>

```
{
  "arn": "string",
  "tags": {
  }
}
```

### Response bodies
<a name="tags-response-examples"></a>

#### TagResourceResponse schema
<a name="tags-response-body-tagresourceresponse-example"></a>

```
{
}
```

#### ExceptionBody schema
<a name="tags-response-body-exceptionbody-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="tags-properties"></a>

### ExceptionBody
<a name="tags-model-exceptionbody"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### TagResourceRequest
<a name="tags-model-tagresourcerequest"></a>

To add tags to a queue, preset, or job template, send a request with the Amazon Resource Name (ARN) of the resource and the tags that you want to add.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | True | The Amazon Resource Name (ARN) of the resource that you want to tag. To get the ARN, send a GET request with the resource name. |
| tags | object | True | The tags that you want to add to the resource. You can tag resources with a key-value pair or with only a key. |

### TagResourceResponse
<a name="tags-model-tagresourceresponse"></a>

A successful request to add tags to a resource returns an OK message.

## See also
<a name="tags-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### TagResource
<a name="TagResource-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediaconvert-2017-08-29/TagResource)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediaconvert-2017-08-29/TagResource)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediaconvert-2017-08-29/TagResource)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediaconvert-2017-08-29/TagResource)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediaconvert-2017-08-29/TagResource)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediaconvert-2017-08-29/TagResource)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediaconvert-2017-08-29/TagResource)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediaconvert-2017-08-29/TagResource)
+ [AWS SDK for Python (Boto3)](/goto/boto3/mediaconvert-2017-08-29/TagResource)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediaconvert-2017-08-29/TagResource)
