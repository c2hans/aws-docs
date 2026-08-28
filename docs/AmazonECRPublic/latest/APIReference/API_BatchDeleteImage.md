---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_BatchDeleteImage.html
---

# BatchDeleteImage
<a name="API_BatchDeleteImage"></a>

Deletes a list of specified images that are within a repository in a public registry. Images are specified with either an `imageTag` or `imageDigest`.

You can remove a tag from an image by specifying the image's tag in your request. When you remove the last tag from an image, the image is deleted from your repository.

You can completely delete an image (and all of its tags) by specifying the digest of the image in your request.

## Request Syntax
<a name="API_BatchDeleteImage_RequestSyntax"></a>

```
{
   "imageIds": [
      {
         "imageDigest": "{{string}}",
         "imageTag": "{{string}}"
      }
   ],
   "registryId": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_BatchDeleteImage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [imageIds](#API_BatchDeleteImage_RequestSyntax) **   <a name="ecrpublic-BatchDeleteImage-request-imageIds"></a>
A list of image ID references that correspond to images to delete. The format of the `imageIds` reference is `imageTag=tag` or `imageDigest=digest`.
Type: Array of [ImageIdentifier](API_ImageIdentifier.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

 ** [registryId](#API_BatchDeleteImage_RequestSyntax) **   <a name="ecrpublic-BatchDeleteImage-request-registryId"></a>
The AWS account ID, or registry alias, that's associated with the registry that contains the image to delete. If you do not specify a registry, the default public registry is assumed.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 50.
Required: No

 ** [repositoryName](#API_BatchDeleteImage_RequestSyntax) **   <a name="ecrpublic-BatchDeleteImage-request-repositoryName"></a>
The repository in a public registry that contains the image to delete.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 205.
Pattern: `(?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*`
Required: Yes

## Response Syntax
<a name="API_BatchDeleteImage_ResponseSyntax"></a>

```
{
   "failures": [
      {
         "failureCode": "string",
         "failureReason": "string",
         "imageId": {
            "imageDigest": "string",
            "imageTag": "string"
         }
      }
   ],
   "imageIds": [
      {
         "imageDigest": "string",
         "imageTag": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchDeleteImage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failures](#API_BatchDeleteImage_ResponseSyntax) **   <a name="ecrpublic-BatchDeleteImage-response-failures"></a>
Any failures associated with the call.
Type: Array of [ImageFailure](API_ImageFailure.md) objects

 ** [imageIds](#API_BatchDeleteImage_ResponseSyntax) **   <a name="ecrpublic-BatchDeleteImage-response-imageIds"></a>
The image IDs of the deleted images.
Type: Array of [ImageIdentifier](API_ImageIdentifier.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.

## Errors
<a name="API_BatchDeleteImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
HTTP Status Code: 400

 ** RepositoryNotFoundException **
The specified repository can't be found. Check the spelling of the specified repository and ensure that you're performing operations on the correct registry.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server-side issue.
HTTP Status Code: 500

 ** UnsupportedCommandException **
The action isn't supported in this Region.
HTTP Status Code: 400

## See Also
<a name="API_BatchDeleteImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-public-2020-10-30/BatchDeleteImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-public-2020-10-30/BatchDeleteImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/BatchDeleteImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-public-2020-10-30/BatchDeleteImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/BatchDeleteImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-public-2020-10-30/BatchDeleteImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-public-2020-10-30/BatchDeleteImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-public-2020-10-30/BatchDeleteImage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-public-2020-10-30/BatchDeleteImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/BatchDeleteImage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECRPublic` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
