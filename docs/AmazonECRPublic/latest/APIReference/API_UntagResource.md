---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_UntagResource.html
---

# UntagResource
<a name="API_UntagResource"></a>

Deletes specified tags from a resource.

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
{
   "resourceArn": "{{string}}",
   "tagKeys": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [resourceArn](#API_UntagResource_RequestSyntax) **   <a name="ecrpublic-UntagResource-request-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource to delete tags from. Currently, the supported resource is an Amazon ECR Public repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [tagKeys](#API_UntagResource_RequestSyntax) **   <a name="ecrpublic-UntagResource-request-tagKeys"></a>
The keys of the tags to be removed.
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

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
HTTP Status Code: 400

 ** InvalidTagParameterException **
An invalid parameter has been specified. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
HTTP Status Code: 400

 ** RepositoryNotFoundException **
The specified repository can't be found. Check the spelling of the specified repository and ensure that you're performing operations on the correct registry.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server-side issue.
HTTP Status Code: 500

 ** TooManyTagsException **
The list of tags on the repository is over the limit. The maximum number of tags that can be applied to a repository is 50.
HTTP Status Code: 400

 ** UnsupportedCommandException **
The action isn't supported in this Region.
HTTP Status Code: 400

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-public-2020-10-30/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-public-2020-10-30/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-public-2020-10-30/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-public-2020-10-30/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-public-2020-10-30/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-public-2020-10-30/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-public-2020-10-30/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/UntagResource)
