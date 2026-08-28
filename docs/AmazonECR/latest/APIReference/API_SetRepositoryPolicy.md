---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_SetRepositoryPolicy.html
---

# SetRepositoryPolicy
<a name="API_SetRepositoryPolicy"></a>

Applies a repository policy to the specified repository to control access permissions. For more information, see [Amazon ECR Repository policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-policies.html) in the *Amazon Elastic Container Registry User Guide*.

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

 ** [force](#API_SetRepositoryPolicy_RequestSyntax) **   <a name="ECR-SetRepositoryPolicy-request-force"></a>
If the policy you are attempting to set on a repository policy would prevent you from setting another policy in the future, you must force the [SetRepositoryPolicy](#API_SetRepositoryPolicy) operation. This is intended to prevent accidental repository lock outs.
Type: Boolean
Required: No

 ** [policyText](#API_SetRepositoryPolicy_RequestSyntax) **   <a name="ECR-SetRepositoryPolicy-request-policyText"></a>
The JSON repository policy text to apply to the repository. For more information, see [Amazon ECR repository policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-policy-examples.html) in the *Amazon Elastic Container Registry User Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.
Required: Yes

 ** [registryId](#API_SetRepositoryPolicy_RequestSyntax) **   <a name="ECR-SetRepositoryPolicy-request-registryId"></a>
The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [repositoryName](#API_SetRepositoryPolicy_RequestSyntax) **   <a name="ECR-SetRepositoryPolicy-request-repositoryName"></a>
The name of the repository to receive the policy.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`
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

 ** [policyText](#API_SetRepositoryPolicy_ResponseSyntax) **   <a name="ECR-SetRepositoryPolicy-response-policyText"></a>
The JSON repository policy text applied to the repository.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.

 ** [registryId](#API_SetRepositoryPolicy_ResponseSyntax) **   <a name="ECR-SetRepositoryPolicy-response-registryId"></a>
The registry ID associated with the request.
Type: String
Pattern: `[0-9]{12}`

 ** [repositoryName](#API_SetRepositoryPolicy_ResponseSyntax) **   <a name="ECR-SetRepositoryPolicy-response-repositoryName"></a>
The repository name associated with the request.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`

## Errors
<a name="API_SetRepositoryPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** RepositoryNotFoundException **
The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server-side issue.
 ** message **
The error message associated with the exception.
HTTP Status Code: 500

## Examples
<a name="API_SetRepositoryPolicy_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_SetRepositoryPolicy_Example_1"></a>

The following example sets a repository policy on the `ubuntu` repository that allows all AWS accounts to pull from it.

#### Sample Request
<a name="API_SetRepositoryPolicy_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecr.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 223
X-Amz-Target: AmazonEC2ContainerRegistry_V20150921.SetRepositoryPolicy
X-Amz-Date: 20151214T235302Z
User-Agent: aws-cli/1.9.10 Python/2.7.10 Darwin/14.5.0 botocore/1.3.10
Content-Type: application/x-amz-json-1.1
Authorization: AWUTHPARAMS

{
  "policyText": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Sid\":\"AllowPull\",\"Effect\":\"Allow\",\"Action\":[\"ecr:BatchGetImage\",\"ecr:GetDownloadUrlForLayer\"],\"Principal\":\"*\"}]}\n",
  "repositoryName": "ubuntu"
}
```

#### Sample Response
<a name="API_SetRepositoryPolicy_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Mon, 14 Dec 2015 23:53:02 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 301
Connection: keep-alive
x-amzn-RequestId: cfc3ead9-a2bd-11e5-91c7-7126cb670c2b

{
  "policyText": "{\n  \"Version\" : \"2012-10-17\",\n  \"Statement\" : [ {\n    \"Sid\" : \"AllowPull\",\n    \"Effect\" : \"Allow\",\n    \"Principal\" : \"*\",\n    \"Action\" : [ \"ecr:BatchGetImage\", \"ecr:GetDownloadUrlForLayer\" ]\n  } ]\n}",
  "registryId": "012345678910",
  "repositoryName": "ubuntu"
}
```

## See Also
<a name="API_SetRepositoryPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/SetRepositoryPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/SetRepositoryPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/SetRepositoryPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/SetRepositoryPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/SetRepositoryPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/SetRepositoryPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/SetRepositoryPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/SetRepositoryPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/SetRepositoryPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/SetRepositoryPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
