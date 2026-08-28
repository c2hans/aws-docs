---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ValidatePullThroughCacheRule.html
---

# ValidatePullThroughCacheRule
<a name="API_ValidatePullThroughCacheRule"></a>

Validates an existing pull through cache rule for an upstream registry that requires authentication. This will retrieve the contents of the AWS Secrets Manager secret, verify the syntax, and then validate that authentication to the upstream registry is successful.

## Request Syntax
<a name="API_ValidatePullThroughCacheRule_RequestSyntax"></a>

```
{
   "ecrRepositoryPrefix": "{{string}}",
   "registryId": "{{string}}"
}
```

## Request Parameters
<a name="API_ValidatePullThroughCacheRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ecrRepositoryPrefix](#API_ValidatePullThroughCacheRule_RequestSyntax) **   <a name="ECR-ValidatePullThroughCacheRule-request-ecrRepositoryPrefix"></a>
The repository name prefix associated with the pull through cache rule.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 30.
Pattern: `^([a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*\/?|ROOT)$`
Required: Yes

 ** [registryId](#API_ValidatePullThroughCacheRule_RequestSyntax) **   <a name="ECR-ValidatePullThroughCacheRule-request-registryId"></a>
The registry ID associated with the pull through cache rule. If you do not specify a registry, the default registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

## Response Syntax
<a name="API_ValidatePullThroughCacheRule_ResponseSyntax"></a>

```
{
   "credentialArn": "string",
   "customRoleArn": "string",
   "ecrRepositoryPrefix": "string",
   "failure": "string",
   "isValid": boolean,
   "registryId": "string",
   "upstreamRegistryUrl": "string",
   "upstreamRepositoryPrefix": "string"
}
```

## Response Elements
<a name="API_ValidatePullThroughCacheRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [credentialArn](#API_ValidatePullThroughCacheRule_ResponseSyntax) **   <a name="ECR-ValidatePullThroughCacheRule-response-credentialArn"></a>
The Amazon Resource Name (ARN) of the AWS Secrets Manager secret associated with the pull through cache rule.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 612.
Pattern: `^arn:aws(-\w+)*:secretsmanager:[a-zA-Z0-9-:]+:secret:ecr\-pullthroughcache\/[a-zA-Z0-9\/_+=.@-]+$`

 ** [customRoleArn](#API_ValidatePullThroughCacheRule_ResponseSyntax) **   <a name="ECR-ValidatePullThroughCacheRule-response-customRoleArn"></a>
The ARN of the IAM role associated with the pull through cache rule.
Type: String
Length Constraints: Maximum length of 2048.

 ** [ecrRepositoryPrefix](#API_ValidatePullThroughCacheRule_ResponseSyntax) **   <a name="ECR-ValidatePullThroughCacheRule-response-ecrRepositoryPrefix"></a>
The Amazon ECR repository prefix associated with the pull through cache rule.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 30.
Pattern: `^([a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*\/?|ROOT)$`

 ** [failure](#API_ValidatePullThroughCacheRule_ResponseSyntax) **   <a name="ECR-ValidatePullThroughCacheRule-response-failure"></a>
The reason the validation failed. For more details about possible causes and how to address them, see [Using pull through cache rules](https://docs.aws.amazon.com/AmazonECR/latest/userguide/pull-through-cache.html) in the *Amazon Elastic Container Registry User Guide*.
Type: String

 ** [isValid](#API_ValidatePullThroughCacheRule_ResponseSyntax) **   <a name="ECR-ValidatePullThroughCacheRule-response-isValid"></a>
Whether or not the pull through cache rule was validated. If `true`, Amazon ECR was able to reach the upstream registry and authentication was successful. If `false`, there was an issue and validation failed. The `failure` reason indicates the cause.
Type: Boolean

 ** [registryId](#API_ValidatePullThroughCacheRule_ResponseSyntax) **   <a name="ECR-ValidatePullThroughCacheRule-response-registryId"></a>
The registry ID associated with the request.
Type: String
Pattern: `[0-9]{12}`

 ** [upstreamRegistryUrl](#API_ValidatePullThroughCacheRule_ResponseSyntax) **   <a name="ECR-ValidatePullThroughCacheRule-response-upstreamRegistryUrl"></a>
The upstream registry URL associated with the pull through cache rule.
Type: String

 ** [upstreamRepositoryPrefix](#API_ValidatePullThroughCacheRule_ResponseSyntax) **   <a name="ECR-ValidatePullThroughCacheRule-response-upstreamRepositoryPrefix"></a>
The upstream repository prefix associated with the pull through cache rule.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 30.
Pattern: `^([a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*\/?|ROOT)$`

## Errors
<a name="API_ValidatePullThroughCacheRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** PullThroughCacheRuleNotFoundException **
The pull through cache rule was not found. Specify a valid pull through cache rule and try again.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server-side issue.
 ** message **
The error message associated with the exception.
HTTP Status Code: 500

 ** ValidationException **
There was an exception validating this request.
HTTP Status Code: 400

## See Also
<a name="API_ValidatePullThroughCacheRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/ValidatePullThroughCacheRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/ValidatePullThroughCacheRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/ValidatePullThroughCacheRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/ValidatePullThroughCacheRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/ValidatePullThroughCacheRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/ValidatePullThroughCacheRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/ValidatePullThroughCacheRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/ValidatePullThroughCacheRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/ValidatePullThroughCacheRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/ValidatePullThroughCacheRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
