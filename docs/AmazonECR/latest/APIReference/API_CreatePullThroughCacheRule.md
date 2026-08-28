---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_CreatePullThroughCacheRule.html
---

# CreatePullThroughCacheRule
<a name="API_CreatePullThroughCacheRule"></a>

Creates a pull through cache rule. A pull through cache rule provides a way to cache images from an upstream registry source in your Amazon ECR private registry. For more information, see [Using pull through cache rules](https://docs.aws.amazon.com/AmazonECR/latest/userguide/pull-through-cache.html) in the *Amazon Elastic Container Registry User Guide*.

## Request Syntax
<a name="API_CreatePullThroughCacheRule_RequestSyntax"></a>

```
{
   "credentialArn": "{{string}}",
   "customRoleArn": "{{string}}",
   "ecrRepositoryPrefix": "{{string}}",
   "registryId": "{{string}}",
   "upstreamRegistry": "{{string}}",
   "upstreamRegistryUrl": "{{string}}",
   "upstreamRepositoryPrefix": "{{string}}"
}
```

## Request Parameters
<a name="API_CreatePullThroughCacheRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [credentialArn](#API_CreatePullThroughCacheRule_RequestSyntax) **   <a name="ECR-CreatePullThroughCacheRule-request-credentialArn"></a>
The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that identifies the credentials to authenticate to the upstream registry.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 612.
Pattern: `^arn:aws(-\w+)*:secretsmanager:[a-zA-Z0-9-:]+:secret:ecr\-pullthroughcache\/[a-zA-Z0-9\/_+=.@-]+$`
Required: No

 ** [customRoleArn](#API_CreatePullThroughCacheRule_RequestSyntax) **   <a name="ECR-CreatePullThroughCacheRule-request-customRoleArn"></a>
Amazon Resource Name (ARN) of the IAM role to be assumed by Amazon ECR to authenticate to the ECR upstream registry. This role must be in the same account as the registry that you are configuring.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** [ecrRepositoryPrefix](#API_CreatePullThroughCacheRule_RequestSyntax) **   <a name="ECR-CreatePullThroughCacheRule-request-ecrRepositoryPrefix"></a>
The repository name prefix to use when caching images from the source registry.
There is always an assumed `/` applied to the end of the prefix. If you specify `ecr-public` as the prefix, Amazon ECR treats that as `ecr-public/`.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 30.
Pattern: `^([a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*\/?|ROOT)$`
Required: Yes

 ** [registryId](#API_CreatePullThroughCacheRule_RequestSyntax) **   <a name="ECR-CreatePullThroughCacheRule-request-registryId"></a>
The AWS account ID associated with the registry to create the pull through cache rule for. If you do not specify a registry, the default registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [upstreamRegistry](#API_CreatePullThroughCacheRule_RequestSyntax) **   <a name="ECR-CreatePullThroughCacheRule-request-upstreamRegistry"></a>
The name of the upstream registry.
Type: String
Valid Values: `ecr | ecr-public | quay | k8s | docker-hub | github-container-registry | azure-container-registry | gitlab-container-registry | chainguard`
Required: No

 ** [upstreamRegistryUrl](#API_CreatePullThroughCacheRule_RequestSyntax) **   <a name="ECR-CreatePullThroughCacheRule-request-upstreamRegistryUrl"></a>
The registry URL of the upstream public registry to use as the source for the pull through cache rule. The following is the syntax to use for each supported upstream registry.
+ Amazon ECR (`ecr`) – `<accountId>.dkr.ecr.<region>.amazonaws.com`
+ Amazon ECR Public (`ecr-public`) – `public.ecr.aws`
+ Docker Hub (`docker-hub`) – `registry-1.docker.io`
+ GitHub Container Registry (`github-container-registry`) – `ghcr.io`
+ GitLab Container Registry (`gitlab-container-registry`) – `registry.gitlab.com`
+ Kubernetes (`k8s`) – `registry.k8s.io`
+ Microsoft Azure Container Registry (`azure-container-registry`) – `<custom>.azurecr.io`
+ Quay (`quay`) – `quay.io`
Type: String
Required: Yes

 ** [upstreamRepositoryPrefix](#API_CreatePullThroughCacheRule_RequestSyntax) **   <a name="ECR-CreatePullThroughCacheRule-request-upstreamRepositoryPrefix"></a>
The repository name prefix of the upstream registry to match with the upstream repository name. When this field isn't specified, Amazon ECR will use the `ROOT`.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 30.
Pattern: `^([a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*\/?|ROOT)$`
Required: No

## Response Syntax
<a name="API_CreatePullThroughCacheRule_ResponseSyntax"></a>

```
{
   "createdAt": number,
   "credentialArn": "string",
   "customRoleArn": "string",
   "ecrRepositoryPrefix": "string",
   "registryId": "string",
   "upstreamRegistry": "string",
   "upstreamRegistryUrl": "string",
   "upstreamRepositoryPrefix": "string"
}
```

## Response Elements
<a name="API_CreatePullThroughCacheRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreatePullThroughCacheRule_ResponseSyntax) **   <a name="ECR-CreatePullThroughCacheRule-response-createdAt"></a>
The date and time, in JavaScript date format, when the pull through cache rule was created.
Type: Timestamp

 ** [credentialArn](#API_CreatePullThroughCacheRule_ResponseSyntax) **   <a name="ECR-CreatePullThroughCacheRule-response-credentialArn"></a>
The Amazon Resource Name (ARN) of the AWS Secrets Manager secret associated with the pull through cache rule.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 612.
Pattern: `^arn:aws(-\w+)*:secretsmanager:[a-zA-Z0-9-:]+:secret:ecr\-pullthroughcache\/[a-zA-Z0-9\/_+=.@-]+$`

 ** [customRoleArn](#API_CreatePullThroughCacheRule_ResponseSyntax) **   <a name="ECR-CreatePullThroughCacheRule-response-customRoleArn"></a>
The ARN of the IAM role associated with the pull through cache rule.
Type: String
Length Constraints: Maximum length of 2048.

 ** [ecrRepositoryPrefix](#API_CreatePullThroughCacheRule_ResponseSyntax) **   <a name="ECR-CreatePullThroughCacheRule-response-ecrRepositoryPrefix"></a>
The Amazon ECR repository prefix associated with the pull through cache rule.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 30.
Pattern: `^([a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*\/?|ROOT)$`

 ** [registryId](#API_CreatePullThroughCacheRule_ResponseSyntax) **   <a name="ECR-CreatePullThroughCacheRule-response-registryId"></a>
The registry ID associated with the request.
Type: String
Pattern: `[0-9]{12}`

 ** [upstreamRegistry](#API_CreatePullThroughCacheRule_ResponseSyntax) **   <a name="ECR-CreatePullThroughCacheRule-response-upstreamRegistry"></a>
The name of the upstream registry associated with the pull through cache rule.
Type: String
Valid Values: `ecr | ecr-public | quay | k8s | docker-hub | github-container-registry | azure-container-registry | gitlab-container-registry | chainguard`

 ** [upstreamRegistryUrl](#API_CreatePullThroughCacheRule_ResponseSyntax) **   <a name="ECR-CreatePullThroughCacheRule-response-upstreamRegistryUrl"></a>
The upstream registry URL associated with the pull through cache rule.
Type: String

 ** [upstreamRepositoryPrefix](#API_CreatePullThroughCacheRule_ResponseSyntax) **   <a name="ECR-CreatePullThroughCacheRule-response-upstreamRepositoryPrefix"></a>
The upstream repository prefix associated with the pull through cache rule.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 30.
Pattern: `^([a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*\/?|ROOT)$`

## Errors
<a name="API_CreatePullThroughCacheRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** LimitExceededException **
The operation did not succeed because it would have exceeded a service limit for your account. For more information, see [Amazon ECR service quotas](https://docs.aws.amazon.com/AmazonECR/latest/userguide/service-quotas.html) in the Amazon Elastic Container Registry User Guide.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** PullThroughCacheRuleAlreadyExistsException **
A pull through cache rule with these settings already exists for the private registry.
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

 ** UnsupportedUpstreamRegistryException **
The specified upstream registry isn't supported.
HTTP Status Code: 400

 ** ValidationException **
There was an exception validating this request.
HTTP Status Code: 400

## Examples
<a name="API_CreatePullThroughCacheRule_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_CreatePullThroughCacheRule_Example_1"></a>

This example creates a pull through cache rule for Docker Hub in the default registry for an account.

#### Sample Request
<a name="API_CreatePullThroughCacheRule_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: api.ecr.us-west-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonEC2ContainerRegistry_V20150921.CreatePullThroughCacheRule
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.13.22 Python/3.11.5 Darwin/16.7.0 botocore/1.12.180
X-Amz-Date: 20231003T155747Z
Authorization: AUTHPARAMS
Content-Length: 268

{
   "ecrRepositoryPrefix":"docker_hub",
   "upstreamRegistryUrl":"registry-1.docker.io",
   "credentialArn":"arn:aws:secretsmanager:us-west-2:012345678910:secret:ECRPTCDockerHub-EXAMPLE"
}
```

#### Sample Response
<a name="API_CreatePullThroughCacheRule_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f
Content-Type: application/x-amz-json-1.1
Content-Length: 180
Connection: keep-alive

{
    "ecrRepositoryPrefix": "docker_hub",
    "upstreamRegistryUrl": "registry-1.docker.io",
    "createdAt": "2023-10-03T15:57:48.411000+00:00",
    "registryId": "012345678910",
    "upstreamRegistry": "docker-hub",
    "credentialArn": "arn:aws:secretsmanager:us-west-2:012345678910:secret:ECRPTCDockerHub-EXAMPLE"
}
```

## See Also
<a name="API_CreatePullThroughCacheRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/CreatePullThroughCacheRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/CreatePullThroughCacheRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/CreatePullThroughCacheRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/CreatePullThroughCacheRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/CreatePullThroughCacheRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/CreatePullThroughCacheRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/CreatePullThroughCacheRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/CreatePullThroughCacheRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/CreatePullThroughCacheRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/CreatePullThroughCacheRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
