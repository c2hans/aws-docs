---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_CreateRepository.html
---

# CreateRepository
<a name="API_CreateRepository"></a>

Creates a repository in a public registry. For more information, see [Public repositories](https://docs.aws.amazon.com/AmazonECR/latest/public/public-repositories.html) in the *Amazon Elastic Container Registry Public User Guide*.

## Request Syntax
<a name="API_CreateRepository_RequestSyntax"></a>

```
{
   "catalogData": {
      "aboutText": "{{string}}",
      "architectures": [ "{{string}}" ],
      "description": "{{string}}",
      "logoImageBlob": {{blob}},
      "operatingSystems": [ "{{string}}" ],
      "usageText": "{{string}}"
   },
   "repositoryName": "{{string}}",
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateRepository_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [catalogData](#API_CreateRepository_RequestSyntax) **   <a name="ecrpublic-CreateRepository-request-catalogData"></a>
The details about the repository that are publicly visible in the Amazon ECR Public Gallery.
Type: [RepositoryCatalogDataInput](API_RepositoryCatalogDataInput.md) object
Required: No

 ** [repositoryName](#API_CreateRepository_RequestSyntax) **   <a name="ecrpublic-CreateRepository-request-repositoryName"></a>
The name to use for the repository. This appears publicly in the Amazon ECR Public Gallery. The repository name can be specified on its own (for example `nginx-web-app`) or prepended with a namespace to group the repository into a category (for example `project-a/nginx-web-app`).
Type: String
Length Constraints: Minimum length of 2. Maximum length of 205.
Pattern: `(?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*`
Required: Yes

 ** [tags](#API_CreateRepository_RequestSyntax) **   <a name="ecrpublic-CreateRepository-request-tags"></a>
The metadata that you apply to each repository to help categorize and organize your repositories. Each tag consists of a key and an optional value. You define both of them. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateRepository_ResponseSyntax"></a>

```
{
   "catalogData": {
      "aboutText": "string",
      "architectures": [ "string" ],
      "description": "string",
      "logoUrl": "string",
      "marketplaceCertified": boolean,
      "operatingSystems": [ "string" ],
      "usageText": "string"
   },
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
<a name="API_CreateRepository_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [catalogData](#API_CreateRepository_ResponseSyntax) **   <a name="ecrpublic-CreateRepository-response-catalogData"></a>
The catalog data for a repository. This data is publicly visible in the Amazon ECR Public Gallery.
Type: [RepositoryCatalogData](API_RepositoryCatalogData.md) object

 ** [repository](#API_CreateRepository_ResponseSyntax) **   <a name="ecrpublic-CreateRepository-response-repository"></a>
The repository that was created.
Type: [Repository](API_Repository.md) object

## Errors
<a name="API_CreateRepository_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
HTTP Status Code: 400

 ** InvalidTagParameterException **
An invalid parameter has been specified. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
HTTP Status Code: 400

 ** LimitExceededException **
The operation didn't succeed because it would have exceeded a service limit for your account. For more information, see [Amazon ECR Public service quotas](https://docs.aws.amazon.com/AmazonECR/latest/public/public-service-quotas.html) in the Amazon Elastic Container Registry Public User Guide.
HTTP Status Code: 400

 ** RepositoryAlreadyExistsException **
The specified repository already exists in the specified registry.
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
<a name="API_CreateRepository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-public-2020-10-30/CreateRepository)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-public-2020-10-30/CreateRepository)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/CreateRepository)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-public-2020-10-30/CreateRepository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/CreateRepository)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-public-2020-10-30/CreateRepository)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-public-2020-10-30/CreateRepository)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-public-2020-10-30/CreateRepository)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-public-2020-10-30/CreateRepository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/CreateRepository)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECRPublic` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
