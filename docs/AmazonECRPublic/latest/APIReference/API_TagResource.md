---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_TagResource.html
---

# TagResource
<a name="API_TagResource"></a>

Associates the specified tags to a resource with the specified `resourceArn`. If existing tags on a resource aren't specified in the request parameters, they aren't changed. When a resource is deleted, the tags associated with that resource are also deleted.

## Request Syntax
<a name="API_TagResource_RequestSyntax"></a>

```
{
   "resourceArn": "{{string}}",
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_TagResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [resourceArn](#API_TagResource_RequestSyntax) **   <a name="ecrpublic-TagResource-request-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource to add tags to. Currently, the supported resource is an Amazon ECR Public repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [tags](#API_TagResource_RequestSyntax) **   <a name="ecrpublic-TagResource-request-tags"></a>
The tags to add to the resource. A tag is an array of key-value pairs. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: Yes

## Response Elements
<a name="API_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_TagResource_Errors"></a>

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
<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-public-2020-10-30/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-public-2020-10-30/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-public-2020-10-30/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-public-2020-10-30/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-public-2020-10-30/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-public-2020-10-30/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-public-2020-10-30/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/TagResource)
