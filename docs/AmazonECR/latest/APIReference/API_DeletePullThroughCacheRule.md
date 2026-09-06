---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DeletePullThroughCacheRule.html
---

# DeletePullThroughCacheRule
<a name="API_DeletePullThroughCacheRule"></a>

Deletes a pull through cache rule.

## Request Syntax
<a name="API_DeletePullThroughCacheRule_RequestSyntax"></a>

```
{
   "ecrRepositoryPrefix": "{{string}}",
   "registryId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeletePullThroughCacheRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ecrRepositoryPrefix](#API_DeletePullThroughCacheRule_RequestSyntax) **   <a name="ECR-DeletePullThroughCacheRule-request-ecrRepositoryPrefix"></a>
The Amazon ECR repository prefix associated with the pull through cache rule to delete.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 30.
Pattern: `^([a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*\/?|ROOT)$`
Required: Yes

 ** [registryId](#API_DeletePullThroughCacheRule_RequestSyntax) **   <a name="ECR-DeletePullThroughCacheRule-request-registryId"></a>
The AWS account ID associated with the registry that contains the pull through cache rule. If you do not specify a registry, the default registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

## Response Syntax
<a name="API_DeletePullThroughCacheRule_ResponseSyntax"></a>

```
{
   "createdAt": number,
   "credentialArn": "string",
   "customRoleArn": "string",
   "ecrRepositoryPrefix": "string",
   "registryId": "string",
   "upstreamRegistryUrl": "string",
   "upstreamRepositoryPrefix": "string"
}
```

## Response Elements
<a name="API_DeletePullThroughCacheRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_DeletePullThroughCacheRule_ResponseSyntax) **   <a name="ECR-DeletePullThroughCacheRule-response-createdAt"></a>
The timestamp associated with the pull through cache rule.
Type: Timestamp

 ** [credentialArn](#API_DeletePullThroughCacheRule_ResponseSyntax) **   <a name="ECR-DeletePullThroughCacheRule-response-credentialArn"></a>
The Amazon Resource Name (ARN) of the AWS Secrets Manager secret associated with the pull through cache rule.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 612.
Pattern: `^arn:aws(-\w+)*:secretsmanager:[a-zA-Z0-9-:]+:secret:ecr\-pullthroughcache\/[a-zA-Z0-9\/_+=.@-]+$`

 ** [customRoleArn](#API_DeletePullThroughCacheRule_ResponseSyntax) **   <a name="ECR-DeletePullThroughCacheRule-response-customRoleArn"></a>
The ARN of the IAM role associated with the pull through cache rule.
Type: String
Length Constraints: Maximum length of 2048.

 ** [ecrRepositoryPrefix](#API_DeletePullThroughCacheRule_ResponseSyntax) **   <a name="ECR-DeletePullThroughCacheRule-response-ecrRepositoryPrefix"></a>
The Amazon ECR repository prefix associated with the request.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 30.
Pattern: `^([a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*\/?|ROOT)$`

 ** [registryId](#API_DeletePullThroughCacheRule_ResponseSyntax) **   <a name="ECR-DeletePullThroughCacheRule-response-registryId"></a>
The registry ID associated with the request.
Type: String
Pattern: `[0-9]{12}`

 ** [upstreamRegistryUrl](#API_DeletePullThroughCacheRule_ResponseSyntax) **   <a name="ECR-DeletePullThroughCacheRule-response-upstreamRegistryUrl"></a>
The upstream registry URL associated with the pull through cache rule.
Type: String

 ** [upstreamRepositoryPrefix](#API_DeletePullThroughCacheRule_ResponseSyntax) **   <a name="ECR-DeletePullThroughCacheRule-response-upstreamRepositoryPrefix"></a>
The upstream repository prefix associated with the pull through cache rule.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 30.
Pattern: `^([a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*\/?|ROOT)$`

## Errors
<a name="API_DeletePullThroughCacheRule_Errors"></a>

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
<a name="API_DeletePullThroughCacheRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/DeletePullThroughCacheRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/DeletePullThroughCacheRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/DeletePullThroughCacheRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/DeletePullThroughCacheRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/DeletePullThroughCacheRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/DeletePullThroughCacheRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/DeletePullThroughCacheRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/DeletePullThroughCacheRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/DeletePullThroughCacheRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/DeletePullThroughCacheRule)
