---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_DeleteRepositoryPolicy.html
---

# DeleteRepositoryPolicy
<a name="API_DeleteRepositoryPolicy"></a>

Deletes the repository policy that's associated with the specified repository.

## Request Syntax
<a name="API_DeleteRepositoryPolicy_RequestSyntax"></a>

```
{
   "registryId": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteRepositoryPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [registryId](#API_DeleteRepositoryPolicy_RequestSyntax) **   <a name="ecrpublic-DeleteRepositoryPolicy-request-registryId"></a>
The AWS account ID that's associated with the public registry that contains the repository policy to delete. If you do not specify a registry, the default public registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [repositoryName](#API_DeleteRepositoryPolicy_RequestSyntax) **   <a name="ecrpublic-DeleteRepositoryPolicy-request-repositoryName"></a>
The name of the repository that's associated with the repository policy to delete.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 205.
Pattern: `(?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*`
Required: Yes

## Response Syntax
<a name="API_DeleteRepositoryPolicy_ResponseSyntax"></a>

```
{
   "policyText": "string",
   "registryId": "string",
   "repositoryName": "string"
}
```

## Response Elements
<a name="API_DeleteRepositoryPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policyText](#API_DeleteRepositoryPolicy_ResponseSyntax) **   <a name="ecrpublic-DeleteRepositoryPolicy-response-policyText"></a>
The JSON repository policy that was deleted from the repository.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.

 ** [registryId](#API_DeleteRepositoryPolicy_ResponseSyntax) **   <a name="ecrpublic-DeleteRepositoryPolicy-response-registryId"></a>
The registry ID that's associated with the request.
Type: String
Pattern: `[0-9]{12}`

 ** [repositoryName](#API_DeleteRepositoryPolicy_ResponseSyntax) **   <a name="ecrpublic-DeleteRepositoryPolicy-response-repositoryName"></a>
The repository name that's associated with the request.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 205.
Pattern: `(?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*`

## Errors
<a name="API_DeleteRepositoryPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
HTTP Status Code: 400

 ** RepositoryNotFoundException **
The specified repository can't be found. Check the spelling of the specified repository and ensure that you're performing operations on the correct registry.
HTTP Status Code: 400

 ** RepositoryPolicyNotFoundException **
The specified repository and registry combination doesn't have an associated repository policy.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server-side issue.
HTTP Status Code: 500

 ** UnsupportedCommandException **
The action isn't supported in this Region.
HTTP Status Code: 400

## See Also
<a name="API_DeleteRepositoryPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-public-2020-10-30/DeleteRepositoryPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-public-2020-10-30/DeleteRepositoryPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/DeleteRepositoryPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-public-2020-10-30/DeleteRepositoryPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/DeleteRepositoryPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-public-2020-10-30/DeleteRepositoryPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-public-2020-10-30/DeleteRepositoryPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-public-2020-10-30/DeleteRepositoryPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-public-2020-10-30/DeleteRepositoryPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/DeleteRepositoryPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECRPublic` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
