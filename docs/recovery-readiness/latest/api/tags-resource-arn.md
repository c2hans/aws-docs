---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/tags-resource-arn.html
---

# ListTagsForResources, TagResource, UntagResource
<a name="tags-resource-arn"></a>

## URI
<a name="tags-resource-arn-url"></a>

`/tags/{{resource-arn}}`

## HTTP methods
<a name="tags-resource-arn-http-methods"></a>

### GET
<a name="tags-resource-arnget"></a>

**Operation ID:** `ListTagsForResources`

Lists the tags for a resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resource-arn}} | String | True | The Amazon Resource Name (ARN) for a resource. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | tagsModel | 200 response - Success. |
| 204 | None | 204 response - Successful deletion |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 404 | None | 404 response - Malformed query string. The query string contains a syntax error or resource not found. |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

### POST
<a name="tags-resource-arnpost"></a>

**Operation ID:** `TagResource`

Adds a tag to a resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resource-arn}} | String | True | The Amazon Resource Name (ARN) for a resource. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response - Success. |
| 204 | None | 204 response - Successful deletion |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 404 | None | 404 response - Malformed query string. The query string contains a syntax error or resource not found. |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

### DELETE
<a name="tags-resource-arndelete"></a>

**Operation ID:** `UntagResource`

Removes a tag from a resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resource-arn}} | String | True | The Amazon Resource Name (ARN) for a resource. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| tagKeys | String | True | The keys for tags you add to resources. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | 204 response - Successful deletion |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 404 | None | 404 response - Malformed query string. The query string contains a syntax error or resource not found. |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

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

#### tagsModel schema
<a name="tags-resource-arn-response-body-tagsmodel-example"></a>

```
{
  "tags": {
  }
}
```

## Properties
<a name="tags-resource-arn-properties"></a>

### Tags
<a name="tags-resource-arn-model-tags"></a>

A collection of tags associated with a resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### tagsModel
<a name="tags-resource-arn-model-tagsmodel"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| tags | [Tags](#tags-resource-arn-model-tags) | True |  |

## See also
<a name="tags-resource-arn-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListTagsForResources
<a name="ListTagsForResources-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/ListTagsForResources)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/ListTagsForResources)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/ListTagsForResources)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/ListTagsForResources)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/ListTagsForResources)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/ListTagsForResources)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/ListTagsForResources)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/ListTagsForResources)
+ [AWS SDK for Python](/goto/boto3/aws-meridian-beta-2019-12-02/ListTagsForResources)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/ListTagsForResources)

### TagResource
<a name="TagResource-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/TagResource)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/TagResource)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/TagResource)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/TagResource)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/TagResource)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/TagResource)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/TagResource)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/TagResource)
+ [AWS SDK for Python](/goto/boto3/aws-meridian-beta-2019-12-02/TagResource)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/TagResource)

### UntagResource
<a name="UntagResource-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/UntagResource)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/UntagResource)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/UntagResource)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/UntagResource)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/UntagResource)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/UntagResource)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/UntagResource)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/UntagResource)
+ [AWS SDK for Python](/goto/boto3/aws-meridian-beta-2019-12-02/UntagResource)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/UntagResource)
