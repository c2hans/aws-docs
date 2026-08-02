---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_DeleteRepository.html
---

# DeleteRepository
<a name="API_DeleteRepository"></a>

Deletes a repository in a public registry. If the repository contains images, you must either manually delete all images in the repository or use the `force` option. This option deletes all images on your behalf before deleting the repository.

## Request Syntax
<a name="API_DeleteRepository_RequestSyntax"></a>

```
{
   "force": {{boolean}},
   "registryId": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteRepository_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [force](#API_DeleteRepository_RequestSyntax) **   <a name="ecrpublic-DeleteRepository-request-force"></a>
 The force option can be used to delete a repository that contains images. If the force option is not used, the repository must be empty prior to deletion.
Type: Boolean
Required: No

 ** [registryId](#API_DeleteRepository_RequestSyntax) **   <a name="ecrpublic-DeleteRepository-request-registryId"></a>
The AWS account ID that's associated with the public registry that contains the repository to delete. If you do not specify a registry, the default public registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [repositoryName](#API_DeleteRepository_RequestSyntax) **   <a name="ecrpublic-DeleteRepository-request-repositoryName"></a>
The name of the repository to delete.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 205.
Pattern: `(?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*`
Required: Yes

## Response Syntax
<a name="API_DeleteRepository_ResponseSyntax"></a>

```
{
   "repository": {
      "createdAt": number,
      "registryId": "string",
      "repositoryArn": "string",
      "repositoryName": "string",
      "repositoryUri": "string"
   }
}
```

## Response Elements
<a name="API_DeleteRepository_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [repository](#API_DeleteRepository_ResponseSyntax) **   <a name="ecrpublic-DeleteRepository-response-repository"></a>
The repository that was deleted.
Type: [Repository](API_Repository.md) object

## Errors
<a name="API_DeleteRepository_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
HTTP Status Code: 400

 ** RepositoryNotEmptyException **
The specified repository contains images. To delete a repository that contains images, you must force the deletion with the `force` parameter.
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
<a name="API_DeleteRepository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-public-2020-10-30/DeleteRepository)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-public-2020-10-30/DeleteRepository)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/DeleteRepository)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-public-2020-10-30/DeleteRepository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/DeleteRepository)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-public-2020-10-30/DeleteRepository)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-public-2020-10-30/DeleteRepository)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-public-2020-10-30/DeleteRepository)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-public-2020-10-30/DeleteRepository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/DeleteRepository)
