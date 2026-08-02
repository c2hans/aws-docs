---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/tags-resource-arn.html
---

# Tags: list tags
<a name="tags-resource-arn"></a>

## URI
<a name="tags-resource-arn-url"></a>

`/prod/tags/{{resource-arn}}`

## HTTP methods
<a name="tags-resource-arn-http-methods"></a>

### DELETE
<a name="tags-resource-arndelete"></a>

**Operation ID:** `DeleteTags`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resource-arn}} | String | True |  |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| tagKeys | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | 204 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 404 | ResourceNotFound | 404 response |
| 500 | InternalServiceError | 500 response |

### GET
<a name="tags-resource-arnget"></a>

**Operation ID:** `ListTagsForResource`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resource-arn}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | TagsModel | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 404 | ResourceNotFound | 404 response |
| 500 | InternalServiceError | 500 response |

### POST
<a name="tags-resource-arnpost"></a>

**Operation ID:** `CreateTags`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resource-arn}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | 204 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 404 | ResourceNotFound | 404 response |
| 500 | InternalServiceError | 500 response |

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

#### TagsModel schema
<a name="tags-resource-arn-response-body-tagsmodel-example"></a>

```
{
  "tags": {
  }
}
```

#### InvalidRequest schema
<a name="tags-resource-arn-response-body-invalidrequest-example"></a>

```
{
  "message": "string"
}
```

#### AccessDenied schema
<a name="tags-resource-arn-response-body-accessdenied-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFound schema
<a name="tags-resource-arn-response-body-resourcenotfound-example"></a>

```
{
  "message": "string"
}
```

#### InternalServiceError schema
<a name="tags-resource-arn-response-body-internalserviceerror-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="tags-resource-arn-properties"></a>

### AccessDenied
<a name="tags-resource-arn-model-accessdenied"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InternalServiceError
<a name="tags-resource-arn-model-internalserviceerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InvalidRequest
<a name="tags-resource-arn-model-invalidrequest"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ResourceNotFound
<a name="tags-resource-arn-model-resourcenotfound"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### Tags
<a name="tags-resource-arn-model-tags"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### TagsModel
<a name="tags-resource-arn-model-tagsmodel"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| tags | [Tags](#tags-resource-arn-model-tags) | False |  |

## See also
<a name="tags-resource-arn-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DeleteTags
<a name="DeleteTags-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/DeleteTags)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/DeleteTags)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/DeleteTags)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/DeleteTags)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/DeleteTags)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/DeleteTags)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/DeleteTags)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/DeleteTags)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/DeleteTags)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/DeleteTags)

### ListTagsForResource
<a name="ListTagsForResource-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/ListTagsForResource)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/ListTagsForResource)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/ListTagsForResource)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/ListTagsForResource)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/ListTagsForResource)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/ListTagsForResource)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/ListTagsForResource)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/ListTagsForResource)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/ListTagsForResource)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/ListTagsForResource)

### CreateTags
<a name="CreateTags-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/CreateTags)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/CreateTags)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/CreateTags)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/CreateTags)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/CreateTags)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/CreateTags)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/CreateTags)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/CreateTags)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/CreateTags)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/CreateTags)
