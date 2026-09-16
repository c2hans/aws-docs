---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_UpdatePullThroughCacheRule.html
---

# UpdatePullThroughCacheRule
<a name="API_UpdatePullThroughCacheRule"></a>

Updates an existing pull through cache rule.

## Request Syntax
<a name="API_UpdatePullThroughCacheRule_RequestSyntax"></a>

```
{
   "credentialArn": "{{string}}",
   "customRoleArn": "{{string}}",
   "ecrRepositoryPrefix": "{{string}}",
   "registryId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdatePullThroughCacheRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [credentialArn](#API_UpdatePullThroughCacheRule_RequestSyntax) **   <a name="ECR-UpdatePullThroughCacheRule-request-credentialArn"></a>
The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that identifies the credentials to authenticate to the upstream registry.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 612.
Pattern: `^arn:aws(-\w+)*:secretsmanager:[a-zA-Z0-9-:]+:secret:ecr\-pullthroughcache\/[a-zA-Z0-9\/_+=.@-]+$`
Required: No

 ** [customRoleArn](#API_UpdatePullThroughCacheRule_RequestSyntax) **   <a name="ECR-UpdatePullThroughCacheRule-request-customRoleArn"></a>
Amazon Resource Name (ARN) of the IAM role to be assumed by Amazon ECR to authenticate to the ECR upstream registry. This role must be in the same account as the registry that you are configuring.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** [ecrRepositoryPrefix](#API_UpdatePullThroughCacheRule_RequestSyntax) **   <a name="ECR-UpdatePullThroughCacheRule-request-ecrRepositoryPrefix"></a>
The repository name prefix to use when caching images from the source registry.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 30.
Pattern: `^([a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*\/?|ROOT)$`
Required: Yes

 ** [registryId](#API_UpdatePullThroughCacheRule_RequestSyntax) **   <a name="ECR-UpdatePullThroughCacheRule-request-registryId"></a>
The AWS account ID associated with the registry associated with the pull through cache rule. If you do not specify a registry, the default registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

## Response Syntax
<a name="API_UpdatePullThroughCacheRule_ResponseSyntax"></a>

```
{
   "credentialArn": "string",
   "customRoleArn": "string",
   "ecrRepositoryPrefix": "string",
   "registryId": "string",
   "updatedAt": number,
   "upstreamRepositoryPrefix": "string"
}
```

## Response Elements
<a name="API_UpdatePullThroughCacheRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [credentialArn](#API_UpdatePullThroughCacheRule_ResponseSyntax) **   <a name="ECR-UpdatePullThroughCacheRule-response-credentialArn"></a>
The Amazon Resource Name (ARN) of the AWS Secrets Manager secret associated with the pull through cache rule.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 612.
Pattern: `^arn:aws(-\w+)*:secretsmanager:[a-zA-Z0-9-:]+:secret:ecr\-pullthroughcache\/[a-zA-Z0-9\/_+=.@-]+$`

 ** [customRoleArn](#API_UpdatePullThroughCacheRule_ResponseSyntax) **   <a name="ECR-UpdatePullThroughCacheRule-response-customRoleArn"></a>
The ARN of the IAM role associated with the pull through cache rule.
Type: String
Length Constraints: Maximum length of 2048.

 ** [ecrRepositoryPrefix](#API_UpdatePullThroughCacheRule_ResponseSyntax) **   <a name="ECR-UpdatePullThroughCacheRule-response-ecrRepositoryPrefix"></a>
The Amazon ECR repository prefix associated with the pull through cache rule.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 30.
Pattern: `^([a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*\/?|ROOT)$`

 ** [registryId](#API_UpdatePullThroughCacheRule_ResponseSyntax) **   <a name="ECR-UpdatePullThroughCacheRule-response-registryId"></a>
The registry ID associated with the request.
Type: String
Pattern: `[0-9]{12}`

 ** [updatedAt](#API_UpdatePullThroughCacheRule_ResponseSyntax) **   <a name="ECR-UpdatePullThroughCacheRule-response-updatedAt"></a>
The date and time, in JavaScript date format, when the pull through cache rule was updated.
Type: Timestamp

 ** [upstreamRepositoryPrefix](#API_UpdatePullThroughCacheRule_ResponseSyntax) **   <a name="ECR-UpdatePullThroughCacheRule-response-upstreamRepositoryPrefix"></a>
The upstream repository prefix associated with the pull through cache rule.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 30.
Pattern: `^([a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*\/?|ROOT)$`

## Errors
<a name="API_UpdatePullThroughCacheRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** PullThroughCacheRuleNotFoundException **
The pull through cache rule was not found. Specify a valid pull through cache rule and try again.
HTTP Status Code: 400

 ** SecretNotFoundException **
The ARN of the secret specified in the pull through cache rule was not found. Update the pull through cache rule with a valid secret ARN and try again.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server-side issue.
 ** message **
The error message associated with the exception.
HTTP Status Code: 500

 ** UnableToAccessSecretException **
The secret is unable to be accessed. Verify the resource permissions for the secret and try again.
HTTP Status Code: 400

 ** UnableToDecryptSecretValueException **
The secret is accessible but is unable to be decrypted. Verify the resource permisisons and try again.
HTTP Status Code: 400

 ** ValidationException **
There was an exception validating this request.
HTTP Status Code: 400

## See Also
<a name="API_UpdatePullThroughCacheRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/UpdatePullThroughCacheRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/UpdatePullThroughCacheRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/UpdatePullThroughCacheRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/UpdatePullThroughCacheRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/UpdatePullThroughCacheRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/UpdatePullThroughCacheRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/UpdatePullThroughCacheRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/UpdatePullThroughCacheRule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/UpdatePullThroughCacheRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/UpdatePullThroughCacheRule)
