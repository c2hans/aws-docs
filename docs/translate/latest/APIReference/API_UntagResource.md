---
source_url: https://docs.aws.amazon.com/translate/latest/APIReference/API_UntagResource.html
---

# UntagResource
<a name="API_UntagResource"></a>

Removes a specific tag associated with an Amazon Translate resource. For more information, see [ Tagging your resources](https://docs.aws.amazon.com/translate/latest/dg/tagging.html) in the Amazon Translate Developer Guide.

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
{
   "ResourceArn": "{{string}}",
   "TagKeys": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_UntagResource_RequestSyntax) **   <a name="translate-UntagResource-request-ResourceArn"></a>
 The Amazon Resource Name (ARN) of the given Amazon Translate resource from which you want to remove the tags.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** [TagKeys](#API_UntagResource_RequestSyntax) **   <a name="translate-UntagResource-request-TagKeys"></a>
The initial part of a key-value pair that forms a tag being removed from a given resource. Keys must be unique and cannot be duplicated for a particular resource.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Response Elements
<a name="API_UntagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UntagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
Another modification is being made. That modification must complete before you can make your change.
HTTP Status Code: 400

 ** InternalServerException **
An internal server error occurred. Retry your request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
The value of the parameter is not valid. Review the value of the parameter you are using to correct it, and then retry your operation.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource you are looking for has not been found. Review the resource you're looking for and see if a different resource will accomplish your needs before retrying the revised request.
HTTP Status Code: 400

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/translate-2017-07-01/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/translate-2017-07-01/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/translate-2017-07-01/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/translate-2017-07-01/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/translate-2017-07-01/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/translate-2017-07-01/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/translate-2017-07-01/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/translate-2017-07-01/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/translate-2017-07-01/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/translate-2017-07-01/UntagResource)
