---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/tags-resource-arn.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Tags
<a name="tags-resource-arn"></a>

A *tag* is a label that you optionally define and associate with an application, campaign, message template, or segment in Amazon Pinpoint. Tags can help you categorize and manage these types of resources in different ways, such as by purpose, owner, environment, or other criteria. A resource can have as many as 50 tags.

Each tag consists of a required *tag key* and an associated *tag value*, both of which you define. A tag key is a general label that acts as a category for more specific tag values. A tag value acts as a descriptor within a tag key. For example, if you have two versions of an Amazon Pinpoint application, one for internal testing and another for external use, you might assign a `Stack` tag key to both applications. The value of the key might be `Test` for one version of the application and `Production` for the other version. For more information about tags, see [Tagging Amazon Pinpoint Resources](https://docs.aws.amazon.com/pinpoint/latest/developerguide/tagging-resources.html) in the *Amazon Pinpoint Developer Guide*.

You can use the Tags resource to add, retrieve, or remove tags from an application, campaign, message template, or segment.

## URI
<a name="tags-resource-arn-url"></a>

`/v1/tags/{{resource-arn}}`

## HTTP methods
<a name="tags-resource-arn-http-methods"></a>

### GET
<a name="tags-resource-arnget"></a>

**Operation ID:** `ListTagsForResource`

Retrieves all the tags (keys and values) that are associated with an application, campaign, message template, or segment.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resource-arn}} | String | True | The Amazon Resource Name (ARN) of the resource. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | tagsModel | The request succeeded. |

### POST
<a name="tags-resource-arnpost"></a>

**Operation ID:** `TagResource`

Adds one or more tags (keys and values) to an application, campaign, message template, or segment.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resource-arn}} | String | True | The Amazon Resource Name (ARN) of the resource. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | The request succeeded and there's no additional content to send in the body of the response (No Content). |

### DELETE
<a name="tags-resource-arndelete"></a>

**Operation ID:** `UntagResource`

Removes one or more tags (keys and values) from an application, campaign, message template, or segment.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resource-arn}} | String | True | The Amazon Resource Name (ARN) of the resource. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| tagKeys | String | True | The key of the tag to remove from the resource. To remove multiple tags, append the `tagKeys` parameter and argument for each additional tag to remove, separated by an ampersand (&). |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | The request succeeded and there's no additional content to send in the body of the response (No Content). |

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

Specifies the tags (keys and values) for an application, campaign, message template, or segment.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| tags | object | True | A string-to-string map of key-value pairs that defines the tags for an application, campaign, message template, or segment. Each of these resources can have a maximum of 50 tags.<br />Each tag consists of a required tag key and an associated tag value. The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters. |

## See also
<a name="tags-resource-arn-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListTagsForResource
<a name="ListTagsForResource-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/ListTagsForResource)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/ListTagsForResource)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/ListTagsForResource)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/ListTagsForResource)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/ListTagsForResource)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/ListTagsForResource)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/ListTagsForResource)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/ListTagsForResource)
+ [AWS SDK for Python (Boto3)](/goto/boto3/pinpoint-2016-12-01/ListTagsForResource)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/ListTagsForResource)

### TagResource
<a name="TagResource-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/TagResource)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/TagResource)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/TagResource)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/TagResource)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/TagResource)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/TagResource)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/TagResource)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/TagResource)
+ [AWS SDK for Python (Boto3)](/goto/boto3/pinpoint-2016-12-01/TagResource)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/TagResource)

### UntagResource
<a name="UntagResource-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/UntagResource)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/UntagResource)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/UntagResource)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/UntagResource)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/UntagResource)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/UntagResource)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/UntagResource)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/UntagResource)
+ [AWS SDK for Python (Boto3)](/goto/boto3/pinpoint-2016-12-01/UntagResource)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/UntagResource)
