---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_ListTagsForResource"></a>

Lists the tags for an Amazon EVS resource.

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

**Note**
In the following list, the required parameters are described first.

 ** [resourceArn](#API_ListTagsForResource_RequestSyntax) **   <a name="evs-ListTagsForResource-request-resourceArn"></a>
The Amazon Resource Name (ARN) that identifies the resource to list tags for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws:evs:[a-z]{2}-[a-z]+-[0-9]:[0-9]{12}:environment/[a-zA-Z0-9_-]+`
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

 ** [tags](#API_ListTagsForResource_ResponseSyntax) **   <a name="evs-ListTagsForResource-response-tags"></a>
The tags for the resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\w.:/=+-@]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[\w.:/=+-@]+|`

## Errors
<a name="API_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [ResourceNotFoundException](API_ResourceNotFoundException.md)
A service resource associated with the request could not be found. The resource might not be specified correctly, or it may have a `state` of `DELETED`.
 ** message **
Describes the error encountered.
 ** resourceId **
The ID of the resource that could not be found.
 ** resourceType **
The type of the resource that is associated with the error.
HTTP Status Code: 400

## See Also
<a name="API_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/evs-2023-07-27/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/evs-2023-07-27/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/evs-2023-07-27/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/evs-2023-07-27/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/evs-2023-07-27/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/evs-2023-07-27/ListTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/evs-2023-07-27/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/ListTagsForResource)
