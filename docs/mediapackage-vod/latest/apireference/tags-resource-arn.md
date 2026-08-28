---
source_url: https://docs.aws.amazon.com/mediapackage-vod/latest/apireference/tags-resource-arn.html
---

# Tags resource-arn
<a name="tags-resource-arn"></a>

Manage tags for AWS Elemental MediaPackage packaging group. Tags are key-value pairs that you can associate with Amazon resources. MediaPackage offers tagging support for assets, packaging configurations, and packaging groups resources. For information about tagging, see [Tagging Resources in AWS Elemental MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/ug/tagging.html).

## URI
<a name="tags-resource-arn-url"></a>

`/tags/{{resource-arn}}`

## HTTP methods
<a name="tags-resource-arn-http-methods"></a>

### GET
<a name="tags-resource-arnget"></a>

**Operation ID:** `ListTagsForResource`

Returns a list of the tags assigned to the specified resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resource-arn}} | String | True | The Amazon Resource Name (ARN) for the resource. You can get this from the response to any request to the resource. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | tagsModel | 200 response |

### POST
<a name="tags-resource-arnpost"></a>

**Operation ID:** `TagResource`

Adds tags to the specified resource. You can specify one or more tags to add.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resource-arn}} | String | True | The Amazon Resource Name (ARN) for the resource. You can get this from the response to any request to the resource. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | 204 response |

### DELETE
<a name="tags-resource-arndelete"></a>

**Operation ID:** `UntagResource`

Removes tags from the specified resource. You can specify one or more tags to remove.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resource-arn}} | String | True | The Amazon Resource Name (ARN) for the resource. You can get this from the response to any request to the resource. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| tagKeys | String | True | A comma-separated list of the tag keys to remove from the resource. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | 204 response |

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
| tags | object | True | A comma-separated list of tag key:value pairs. For example: <pre> {<br />  "Key1": "Value1",<br />  "Key2": "Value2"<br />}</pre> |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage VOD. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage-vod` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
