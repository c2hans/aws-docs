---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_PutImage.html
---

# PutImage
<a name="API_PutImage"></a>

Creates or updates the image manifest and tags that are associated with an image.

When an image is pushed and all new image layers have been uploaded, the PutImage API is called once to create or update the image manifest and the tags that are associated with the image.

**Note**
This operation is used by the Amazon ECR proxy and is not generally used by customers for pulling and pushing images. In most cases, you should use the `docker` CLI to pull, tag, and push images.

## Request Syntax
<a name="API_PutImage_RequestSyntax"></a>

```
{
   "imageDigest": "{{string}}",
   "imageManifest": "{{string}}",
   "imageManifestMediaType": "{{string}}",
   "imageTag": "{{string}}",
   "registryId": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_PutImage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [imageDigest](#API_PutImage_RequestSyntax) **   <a name="ecrpublic-PutImage-request-imageDigest"></a>
The image digest of the image manifest that corresponds to the image.
Type: String
Required: No

 ** [imageManifest](#API_PutImage_RequestSyntax) **   <a name="ecrpublic-PutImage-request-imageManifest"></a>
The image manifest that corresponds to the image to be uploaded.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4194304.
Required: Yes

 ** [imageManifestMediaType](#API_PutImage_RequestSyntax) **   <a name="ecrpublic-PutImage-request-imageManifestMediaType"></a>
The media type of the image manifest. If you push an image manifest that doesn't contain the `mediaType` field, you must specify the `imageManifestMediaType` in the request.
Type: String
Required: No

 ** [imageTag](#API_PutImage_RequestSyntax) **   <a name="ecrpublic-PutImage-request-imageTag"></a>
The tag to associate with the image. This parameter is optional.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

 ** [registryId](#API_PutImage_RequestSyntax) **   <a name="ecrpublic-PutImage-request-registryId"></a>
The AWS account ID, or registry alias, that's associated with the public registry that contains the repository where the image is put. If you do not specify a registry, the default public registry is assumed.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 50.
Required: No

 ** [repositoryName](#API_PutImage_RequestSyntax) **   <a name="ecrpublic-PutImage-request-repositoryName"></a>
The name of the repository where the image is put.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 205.
Pattern: `(?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*`
Required: Yes

## Response Syntax
<a name="API_PutImage_ResponseSyntax"></a>

```
{
   "image": {
      "imageId": {
         "imageDigest": "string",
         "imageTag": "string"
      },
      "imageManifest": "string",
      "imageManifestMediaType": "string",
      "registryId": "string",
      "repositoryName": "string"
   }
}
```

## Response Elements
<a name="API_PutImage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [image](#API_PutImage_ResponseSyntax) **   <a name="ecrpublic-PutImage-response-image"></a>
Details of the image uploaded.
Type: [Image](API_Image.md) object

## Errors
<a name="API_PutImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ImageAlreadyExistsException **
The specified image has already been pushed, and there were no changes to the manifest or image tag after the last push.
HTTP Status Code: 400

 ** ImageDigestDoesNotMatchException **
The specified image digest doesn't match the digest that Amazon ECR calculated for the image.
HTTP Status Code: 400

 ** ImageTagAlreadyExistsException **
The specified image is tagged with a tag that already exists. The repository is configured for tag immutability.
HTTP Status Code: 400

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
HTTP Status Code: 400

 ** LayersNotFoundException **
The specified layers can't be found, or the specified layer isn't valid for this repository.
HTTP Status Code: 400

 ** LimitExceededException **
The operation didn't succeed because it would have exceeded a service limit for your account. For more information, see [Amazon ECR Public service quotas](https://docs.aws.amazon.com/AmazonECR/latest/public/public-service-quotas.html) in the Amazon Elastic Container Registry Public User Guide.
HTTP Status Code: 400

 ** ReferencedImagesNotFoundException **
The manifest list is referencing an image that doesn't exist.
HTTP Status Code: 400

 ** RegistryNotFoundException **
The registry doesn't exist.
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
<a name="API_PutImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-public-2020-10-30/PutImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-public-2020-10-30/PutImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/PutImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-public-2020-10-30/PutImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/PutImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-public-2020-10-30/PutImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-public-2020-10-30/PutImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-public-2020-10-30/PutImage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-public-2020-10-30/PutImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/PutImage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECRPublic` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
