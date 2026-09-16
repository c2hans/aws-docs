---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_SetRepositoryPolicy.html
---

# SetRepositoryPolicy
<a name="API_SetRepositoryPolicy"></a>

Applies a repository policy to the specified public repository to control access permissions. For more information, see [Amazon ECR repository policies](https://docs.aws.amazon.com/AmazonECR/latest/public/public-repository-policies.html) in the *Amazon Elastic Container Registry Public User Guide*.

## Request Syntax
<a name="API_SetRepositoryPolicy_RequestSyntax"></a>

```
{
   "force": {{boolean}},
   "policyText": "{{string}}",
   "registryId": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_SetRepositoryPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [force](#API_SetRepositoryPolicy_RequestSyntax) **   <a name="ecrpublic-SetRepositoryPolicy-request-force"></a>
If the policy that you want to set on a repository policy would prevent you from setting another policy in the future, you must force the [SetRepositoryPolicy](#API_SetRepositoryPolicy) operation. This prevents accidental repository lockouts.
Type: Boolean
Required: No

 ** [policyText](#API_SetRepositoryPolicy_RequestSyntax) **   <a name="ecrpublic-SetRepositoryPolicy-request-policyText"></a>
The JSON repository policy text to apply to the repository. For more information, see [Amazon ECR repository policies](https://docs.aws.amazon.com/AmazonECR/latest/public/public-repository-policies.html) in the *Amazon Elastic Container Registry Public User Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.
Required: Yes

 ** [registryId](#API_SetRepositoryPolicy_RequestSyntax) **   <a name="ecrpublic-SetRepositoryPolicy-request-registryId"></a>
The AWS account ID that's associated with the registry that contains the repository. If you do not specify a registry, the default public registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [repositoryName](#API_SetRepositoryPolicy_RequestSyntax) **   <a name="ecrpublic-SetRepositoryPolicy-request-repositoryName"></a>
The name of the repository to receive the policy.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 205.
Pattern: `(?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*`
Required: Yes

## Response Syntax
<a name="API_SetRepositoryPolicy_ResponseSyntax"></a>

```
{
   "policyText": "string",
   "registryId": "string",
   "repositoryName": "string"
}
```

## Response Elements
<a name="API_SetRepositoryPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policyText](#API_SetRepositoryPolicy_ResponseSyntax) **   <a name="ecrpublic-SetRepositoryPolicy-response-policyText"></a>
The JSON repository policy text that's applied to the repository.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.

 ** [registryId](#API_SetRepositoryPolicy_ResponseSyntax) **   <a name="ecrpublic-SetRepositoryPolicy-response-registryId"></a>
The registry ID that's associated with the request.
Type: String
Pattern: `[0-9]{12}`

 ** [repositoryName](#API_SetRepositoryPolicy_ResponseSyntax) **   <a name="ecrpublic-SetRepositoryPolicy-response-repositoryName"></a>
The repository name that's associated with the request.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 205.
Pattern: `(?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*`

## Errors
<a name="API_SetRepositoryPolicy_Errors"></a>

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
<a name="API_SetRepositoryPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-public-2020-10-30/SetRepositoryPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-public-2020-10-30/SetRepositoryPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/SetRepositoryPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-public-2020-10-30/SetRepositoryPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/SetRepositoryPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-public-2020-10-30/SetRepositoryPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-public-2020-10-30/SetRepositoryPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-public-2020-10-30/SetRepositoryPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecr-public-2020-10-30/SetRepositoryPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/SetRepositoryPolicy)
