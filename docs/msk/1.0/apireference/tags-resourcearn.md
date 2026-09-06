---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/tags-resourcearn.html
---

# Tags
<a name="tags-resourcearn"></a>

Represents the set of tags for an MSK resource. A tag is a key-value pair that you define for the cluster. Using tags is a simple yet powerful way to manage Amazon resources and organize data, including billing data.

## URI
<a name="tags-resourcearn-url"></a>

`/v1/tags/{{resourceArn}}`

## HTTP methods
<a name="tags-resourcearn-http-methods"></a>

### GET
<a name="tags-resourcearnget"></a>

**Operation ID:** `ListTagsForResource`

Returns a list of the tags associated with the specified resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resourceArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the resource that's associated with the tags. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  ListTagsForResourceResponse | Success response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### POST
<a name="tags-resourcearnpost"></a>

**Operation ID:** `TagResource`

Adds tags to the specified MSK resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resourceArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the resource that's associated with the tags. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | 204 response |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### DELETE
<a name="tags-resourcearndelete"></a>

**Operation ID:** `UntagResource`

Removes the tags associated with the keys that are provided in the query.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resourceArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the resource that's associated with the tags. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| tagKeys | String | True | Tag keys must be unique for a given cluster. In addition, the following restrictions apply:+  Each tag key must be unique. If you add a tag with a key that's already in use, your new tag overwrites the existing key-value pair.  <br />+  You can't start a tag key with `aws:` because this prefix is reserved for use by Amazon. Amazon creates tags that begin with this prefix on your behalf, but you can't edit or delete them. <br />+  Tag keys must be between 1 and 128 Unicode characters in length. <br />+  Tag keys must consist of the following characters: Unicode letters, digits, white space, and the following special characters: `_ . / = + - @`.  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | 204 response |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="tags-resourcearnoptions"></a>

Enable CORS by returning the correct headers.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{resourceArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the resource that's associated with the tags. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

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

#### Error schema
<a name="tags-resourcearn-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="tags-resourcearn-properties"></a>

### Error
<a name="tags-resourcearn-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### ListTagsForResourceResponse
<a name="tags-resourcearn-model-listtagsforresourceresponse"></a>

Response of listing tags for a resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| tags | object | True | The key-value pair for the resource tag. |

### TagResourceRequest
<a name="tags-resourcearn-model-tagresourcerequest"></a>

Tag a resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| tags | object | True | The key-value pair for the resource tag. |

## See also
<a name="tags-resourcearn-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListTagsForResource
<a name="ListTagsForResource-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/ListTagsForResource)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/ListTagsForResource)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/ListTagsForResource)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/ListTagsForResource)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/ListTagsForResource)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/ListTagsForResource)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/ListTagsForResource)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/ListTagsForResource)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/ListTagsForResource)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/ListTagsForResource)

### TagResource
<a name="TagResource-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/TagResource)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/TagResource)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/TagResource)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/TagResource)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/TagResource)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/TagResource)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/TagResource)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/TagResource)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/TagResource)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/TagResource)

### UntagResource
<a name="UntagResource-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/UntagResource)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/UntagResource)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/UntagResource)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/UntagResource)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/UntagResource)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/UntagResource)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/UntagResource)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/UntagResource)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/UntagResource)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/UntagResource)
