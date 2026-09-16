---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/tags-resourcearn.html
---

# ListTagsForResource, TagResource, UntagResource
<a name="tags-resourcearn"></a>

## URI
<a name="tags-resourcearn-url"></a>

`/tags/{{ResourceArn}}`

## HTTP methods
<a name="tags-resourcearn-http-methods"></a>

### GET
<a name="tags-resourcearnget"></a>

**Operation ID:** `ListTagsForResource`

Lists the tags for a resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{ResourceArn}} | String | True | The Amazon Resource Name (ARN) for the resource. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListTagsForResourceResponse | 200 response - Success. |
| 400 | ValidationException | 400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you used parameters together incorrectly. |
| 404 | ResourceNotFoundException | 404 response - MalformedQueryString. The query string contains a syntax error or resource not found. |
| 500 | InternalServerException | 500 response - InternalServiceError. Temporary service error. Retry the request. |

### POST
<a name="tags-resourcearnpost"></a>

**Operation ID:** `TagResource`

Adds a tag to a resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{ResourceArn}} | String | True | The Amazon Resource Name (ARN) for the resource. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | TagResourceResponse | 200 response - Success. |
| 400 | ValidationException | 400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you used parameters together incorrectly. |
| 404 | ResourceNotFoundException | 404 response - MalformedQueryString. The query string contains a syntax error or resource not found. |
| 500 | InternalServerException | 500 response - InternalServiceError. Temporary service error. Retry the request. |

### DELETE
<a name="tags-resourcearndelete"></a>

**Operation ID:** `UntagResource`

Removes a tag from a resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{ResourceArn}} | String | True | The Amazon Resource Name (ARN) for the resource. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| TagKeys | String | True | Keys for the tags to be removed. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | UntagResourceResponse | 200 response - Success. |
| 400 | ValidationException | 400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you used parameters together incorrectly. |
| 404 | ResourceNotFoundException | 404 response - MalformedQueryString. The query string contains a syntax error or resource not found. |
| 500 | InternalServerException | 500 response - InternalServiceError. Temporary service error. Retry the request. |

### OPTIONS
<a name="tags-resourcearnoptions"></a>

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{ResourceArn}} | String | True | The Amazon Resource Name (ARN) for the resource. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method. |

## Schemas
<a name="tags-resourcearn-schemas"></a>

### Request bodies
<a name="tags-resourcearn-request-examples"></a>

#### POST schema
<a name="tags-resourcearn-request-body-post-example"></a>

```
{
  "Tags": {
  }
}
```

### Response bodies
<a name="tags-resourcearn-response-examples"></a>

#### ListTagsForResourceResponse schema
<a name="tags-resourcearn-response-body-listtagsforresourceresponse-example"></a>

```
{
  "Tags": {
  }
}
```

#### TagResourceResponse schema
<a name="tags-resourcearn-response-body-tagresourceresponse-example"></a>

```
{
}
```

#### UntagResourceResponse schema
<a name="tags-resourcearn-response-body-untagresourceresponse-example"></a>

```
{
}
```

#### ValidationException schema
<a name="tags-resourcearn-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="tags-resourcearn-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="tags-resourcearn-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="tags-resourcearn-properties"></a>

### InternalServerException
<a name="tags-resourcearn-model-internalserverexception"></a>

500 response - InternalServiceError. Temporary service error. Retry the request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### ListTagsForResourceResponse
<a name="tags-resourcearn-model-listtagsforresourceresponse"></a>

The result of a successful `ListTagsForResource` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Tags | object | False | The tags associated with the resource. |

### ResourceNotFoundException
<a name="tags-resourcearn-model-resourcenotfoundexception"></a>

404 response - MalformedQueryString. The query string contains a syntax error or resource not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### TagResourceRequest
<a name="tags-resourcearn-model-tagresourcerequest"></a>

Request to tag a resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Tags | object | True | The tags associated with the resource. |

### TagResourceResponse
<a name="tags-resourcearn-model-tagresourceresponse"></a>

The result of a successful `TagResource` request.

### UntagResourceResponse
<a name="tags-resourcearn-model-untagresourceresponse"></a>

The result of a successful `UntagResource` request.

### ValidationException
<a name="tags-resourcearn-model-validationexception"></a>

400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

## See also
<a name="tags-resourcearn-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListTagsForResource
<a name="ListTagsForResource-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/route53-recovery-control-config-2020-11-02/ListTagsForResource)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/route53-recovery-control-config-2020-11-02/ListTagsForResource)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/route53-recovery-control-config-2020-11-02/ListTagsForResource)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/route53-recovery-control-config-2020-11-02/ListTagsForResource)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/route53-recovery-control-config-2020-11-02/ListTagsForResource)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/route53-recovery-control-config-2020-11-02/ListTagsForResource)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/route53-recovery-control-config-2020-11-02/ListTagsForResource)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/route53-recovery-control-config-2020-11-02/ListTagsForResource)
+ [AWS SDK for Python (Boto3)](/goto/boto3/route53-recovery-control-config-2020-11-02/ListTagsForResource)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/route53-recovery-control-config-2020-11-02/ListTagsForResource)

### TagResource
<a name="TagResource-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/route53-recovery-control-config-2020-11-02/TagResource)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/route53-recovery-control-config-2020-11-02/TagResource)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/route53-recovery-control-config-2020-11-02/TagResource)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/route53-recovery-control-config-2020-11-02/TagResource)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/route53-recovery-control-config-2020-11-02/TagResource)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/route53-recovery-control-config-2020-11-02/TagResource)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/route53-recovery-control-config-2020-11-02/TagResource)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/route53-recovery-control-config-2020-11-02/TagResource)
+ [AWS SDK for Python (Boto3)](/goto/boto3/route53-recovery-control-config-2020-11-02/TagResource)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/route53-recovery-control-config-2020-11-02/TagResource)

### UntagResource
<a name="UntagResource-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/route53-recovery-control-config-2020-11-02/UntagResource)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/route53-recovery-control-config-2020-11-02/UntagResource)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/route53-recovery-control-config-2020-11-02/UntagResource)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/route53-recovery-control-config-2020-11-02/UntagResource)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/route53-recovery-control-config-2020-11-02/UntagResource)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/route53-recovery-control-config-2020-11-02/UntagResource)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/route53-recovery-control-config-2020-11-02/UntagResource)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/route53-recovery-control-config-2020-11-02/UntagResource)
+ [AWS SDK for Python (Boto3)](/goto/boto3/route53-recovery-control-config-2020-11-02/UntagResource)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/route53-recovery-control-config-2020-11-02/UntagResource)
