---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_ListTagsForResource"></a>

Returns a list of all tags on an AWS PCS resource.

## Request Syntax
<a name="API_ListTagsForResource_RequestSyntax"></a>

```
{
   "resourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTagsForResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [resourceArn](#API_ListTagsForResource_RequestSyntax) **   <a name="PCS-ListTagsForResource-request-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource for which to list tags.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws.*:pcs:.*:[0-9]{12}:.*/[a-z0-9_\-]+`
Required: Yes

## Response Syntax
<a name="API_ListTagsForResource_ResponseSyntax"></a>

```
{
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [tags](#API_ListTagsForResource_ResponseSyntax) **   <a name="PCS-ListTagsForResource-response-tags"></a>
1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
The requested resource can't be found. The cluster, node group, or queue you're attempting to get, update, list, or delete doesn't exist.
 *Examples*
 ** resourceId **
 The unique identifier of the resource that was not found.
 ** resourceType **
 The type or category of the resource that was not found.
HTTP Status Code: 400

## See Also
<a name="API_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pcs-2023-02-10/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pcs-2023-02-10/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pcs-2023-02-10/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pcs-2023-02-10/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pcs-2023-02-10/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pcs-2023-02-10/ListTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pcs-2023-02-10/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/ListTagsForResource)
