---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/tags-resourcearn.html
---

# Tags
<a name="tags-resourcearn"></a>

A *tag* is a label that you can define and associate with AWS resources, including certain types of Amazon Macie resources. Tags can help you identify, categorize, and manage resources in different ways, such as by purpose, owner, environment, or other criteria. For example, you can use tags to: apply policies, allocate costs, distinguish between versions of resources, or identify resources that support certain compliance requirements or workflows.

You can associate tags with the following types of Macie resources:
+ Allow lists
+ Classification jobs
+ Custom data identifiers
+ Findings filters
+ Member accounts

A resource can have as many as 50 tags. Each tag consists of a *tag key* and an associated *tag value*, both of which you define. A *tag key* is a general label that acts as a category for more specific tag values. A *tag value* acts as a descriptor for a tag key. For more information, see [Tagging resources](https://docs.aws.amazon.com/macie/latest/user/tagging-resources.html) in the *Amazon Macie User Guide*.

You can use the Tags resource to add, retrieve, update, or remove tags from an allow list, classification job, custom data identifier, findings filter, or member account.

## URI
<a name="tags-resourcearn-url"></a>

`/tags/{{resourceArn}}`

## HTTP methods
<a name="tags-resourcearn-http-methods"></a>

### DELETE
<a name="tags-resourcearndelete"></a>

**Operation ID:** `UntagResource`

Removes one or more tags (keys and values) from an Amazon Macie resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resourceArn}} | String | True | The Amazon Resource Name (ARN) of the resource. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| tagKeys | String | True | One or more tags (keys) to remove from the resource. In an HTTP request to remove multiple tags, append the `tagKeys` parameter and argument for each tag to remove, separated by an ampersand (&). |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | UntagResourceResponse | The request succeeded and there isn't any content to include in the body of the response (No Content). |

### GET
<a name="tags-resourcearnget"></a>

**Operation ID:** `ListTagsForResource`

Retrieves the tags (keys and values) that are associated with an Amazon Macie resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resourceArn}} | String | True | The Amazon Resource Name (ARN) of the resource. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListTagsForResourceResponse | The request succeeded. |

### POST
<a name="tags-resourcearnpost"></a>

**Operation ID:** `TagResource`

Adds or updates one or more tags (keys and values) that are associated with an Amazon Macie resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resourceArn}} | String | True | The Amazon Resource Name (ARN) of the resource. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | TagResourceResponse | The request succeeded and there isn't any content to include in the body of the response (No Content). |

## Schemas
<a name="tags-resourcearn-schemas"></a>

### Request bodies
<a name="tags-resourcearn-request-examples"></a>

#### POST schema
<a name="tags-resourcearn-request-body-post-example"></a>

```
{
  "tags": {
  }
}
```

### Response bodies
<a name="tags-resourcearn-response-examples"></a>

#### ListTagsForResourceResponse schema
<a name="tags-resourcearn-response-body-listtagsforresourceresponse-example"></a>

```
{
  "tags": {
  }
}
```

#### UntagResourceResponse schema
<a name="tags-resourcearn-response-body-untagresourceresponse-example"></a>

```
{
}
```

#### TagResourceResponse schema
<a name="tags-resourcearn-response-body-tagresourceresponse-example"></a>

```
{
}
```

## Properties
<a name="tags-resourcearn-properties"></a>

### ListTagsForResourceResponse
<a name="tags-resourcearn-model-listtagsforresourceresponse"></a>

Provides information about the tags (keys and values) that are associated with an Amazon Macie resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| tags | [TagMap](#tags-resourcearn-model-tagmap) | False | A map of key-value pairs that specifies which tags (keys and values) are associated with the resource. |

### TagMap
<a name="tags-resourcearn-model-tagmap"></a>

A string-to-string map of key-value pairs that specifies the tags (keys and values) for an Amazon Macie resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### TagResourceRequest
<a name="tags-resourcearn-model-tagresourcerequest"></a>

Specifies the tags (keys and values) to associate with an Amazon Macie resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| tags | [TagMap](#tags-resourcearn-model-tagmap) | True | A map of key-value pairs that specifies the tags to associate with the resource.<br />A resource can have a maximum of 50 tags. Each tag consists of a tag key and an associated tag value. The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters. |

### TagResourceResponse
<a name="tags-resourcearn-model-tagresourceresponse"></a>

The request succeeded. The specified tags were added or updated for the resource.

### UntagResourceResponse
<a name="tags-resourcearn-model-untagresourceresponse"></a>

The request succeeded. The specified tags were removed from the resource.

## See also
<a name="tags-resourcearn-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### UntagResource
<a name="UntagResource-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/UntagResource)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/UntagResource)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/UntagResource)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/UntagResource)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/UntagResource)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/UntagResource)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/UntagResource)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/UntagResource)
+ [AWS SDK for Python (Boto3)](/goto/boto3/macie2-2020-01-01/UntagResource)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/UntagResource)

### ListTagsForResource
<a name="ListTagsForResource-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/ListTagsForResource)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/ListTagsForResource)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/ListTagsForResource)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/ListTagsForResource)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/ListTagsForResource)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/ListTagsForResource)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/ListTagsForResource)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/ListTagsForResource)
+ [AWS SDK for Python (Boto3)](/goto/boto3/macie2-2020-01-01/ListTagsForResource)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/ListTagsForResource)

### TagResource
<a name="TagResource-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/TagResource)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/TagResource)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/TagResource)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/TagResource)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/TagResource)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/TagResource)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/TagResource)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/TagResource)
+ [AWS SDK for Python (Boto3)](/goto/boto3/macie2-2020-01-01/TagResource)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/TagResource)
