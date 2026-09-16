---
source_url: https://docs.aws.amazon.com/mediapackage/latest/apireference/tags-resource-arn.html
---

# Tags resource-arn
<a name="tags-resource-arn"></a>

Manage tags for AWS Elemental MediaPackage channels and endpoints. Tags are key-value pairs that you can associate with Amazon resources. MediaPackage offers tagging support for channel and endpoint resources. For information about tagging, see [Tagging Resources in AWS Elemental MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/ug/tagging.html).

## URI
<a name="tags-resource-arn-url"></a>

`/tags/{{resource-arn}}`

## HTTP methods
<a name="tags-resource-arn-http-methods"></a>

### GET
<a name="tags-resource-arnget"></a>

**Operation ID:** `ListTagsForResource`

Returns a list of the tags assigned to the specified resource (either a channel or endpoint).

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resource-arn}} | String | True | The Amazon Resource Name (ARN) for the channel or endpoint. You can get this from the response to any request to the resource. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | tagsModel |  `200 OK` response<br />The list of tags is returned successfully. |

### POST
<a name="tags-resource-arnpost"></a>

**Operation ID:** `TagResource`

Adds tags to the specified channel or endpoint resource. You can specify one or more tags to add.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resource-arn}} | String | True | The Amazon Resource Name (ARN) for the channel or endpoint. You can get this from the response to any request to the resource. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | The request was successful. There is no content in the response. |

### DELETE
<a name="tags-resource-arndelete"></a>

**Operation ID:** `UntagResource`

Removes tags from the specified channel or endpoint resource. You can specify one or more tags to remove.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resource-arn}} | String | True | The Amazon Resource Name (ARN) for the channel or endpoint. You can get this from the response to any request to the resource. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| tagKeys | String | True | A comma-separated list of the tag keys to remove from the channel or endpoint. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | The request was successful. There is no content in the response. |

### OPTIONS
<a name="tags-resource-arnoptions"></a>

Enable CORS by returning correct headers.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resource-arn}} | String | True | The Amazon Resource Name (ARN) for the channel or endpoint. You can get this from the response to any request to the resource. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method. |

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

### tagsModel
<a name="tags-resource-arn-model-tagsmodel"></a>

The key:value pairs used in a tag.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| tags | object | True | A comma-separated list of tag key:value pairs. For example: <pre> {<br />   "Key1": "Value1",<br />   "Key2": "Value2"<br /> }</pre> |

## See also
<a name="tags-resource-arn-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListTagsForResource
<a name="ListTagsForResource-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediapackage-2017-10-12/ListTagsForResource)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediapackage-2017-10-12/ListTagsForResource)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediapackage-2017-10-12/ListTagsForResource)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediapackage-2017-10-12/ListTagsForResource)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediapackage-2017-10-12/ListTagsForResource)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediapackage-2017-10-12/ListTagsForResource)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediapackage-2017-10-12/ListTagsForResource)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediapackage-2017-10-12/ListTagsForResource)
+ [AWS SDK for Python (Boto3)](/goto/boto3/mediapackage-2017-10-12/ListTagsForResource)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediapackage-2017-10-12/ListTagsForResource)

### TagResource
<a name="TagResource-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediapackage-2017-10-12/TagResource)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediapackage-2017-10-12/TagResource)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediapackage-2017-10-12/TagResource)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediapackage-2017-10-12/TagResource)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediapackage-2017-10-12/TagResource)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediapackage-2017-10-12/TagResource)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediapackage-2017-10-12/TagResource)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediapackage-2017-10-12/TagResource)
+ [AWS SDK for Python (Boto3)](/goto/boto3/mediapackage-2017-10-12/TagResource)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediapackage-2017-10-12/TagResource)

### UntagResource
<a name="UntagResource-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediapackage-2017-10-12/UntagResource)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediapackage-2017-10-12/UntagResource)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediapackage-2017-10-12/UntagResource)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediapackage-2017-10-12/UntagResource)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediapackage-2017-10-12/UntagResource)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediapackage-2017-10-12/UntagResource)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediapackage-2017-10-12/UntagResource)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediapackage-2017-10-12/UntagResource)
+ [AWS SDK for Python (Boto3)](/goto/boto3/mediapackage-2017-10-12/UntagResource)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediapackage-2017-10-12/UntagResource)
