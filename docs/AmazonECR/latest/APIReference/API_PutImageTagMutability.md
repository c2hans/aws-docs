---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PutImageTagMutability.html
---

# PutImageTagMutability
<a name="API_PutImageTagMutability"></a>

Updates the image tag mutability settings for the specified repository. For more information, see [Image tag mutability](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-tag-mutability.html) in the *Amazon Elastic Container Registry User Guide*.

## Request Syntax
<a name="API_PutImageTagMutability_RequestSyntax"></a>

```
{
   "imageTagMutability": "{{string}}",
   "imageTagMutabilityExclusionFilters": [
      {
         "filter": "{{string}}",
         "filterType": "{{string}}"
      }
   ],
   "registryId": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_PutImageTagMutability_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [imageTagMutability](#API_PutImageTagMutability_RequestSyntax) **   <a name="ECR-PutImageTagMutability-request-imageTagMutability"></a>
The tag mutability setting for the repository. If `MUTABLE` is specified, image tags can be overwritten. If `IMMUTABLE` is specified, all image tags within the repository will be immutable which will prevent them from being overwritten.
Type: String
Valid Values: `MUTABLE | IMMUTABLE | IMMUTABLE_WITH_EXCLUSION | MUTABLE_WITH_EXCLUSION`
Required: Yes

 ** [imageTagMutabilityExclusionFilters](#API_PutImageTagMutability_RequestSyntax) **   <a name="ECR-PutImageTagMutability-request-imageTagMutabilityExclusionFilters"></a>
A list of filters that specify which image tags should be excluded from the image tag mutability setting being applied.
Type: Array of [ImageTagMutabilityExclusionFilter](API_ImageTagMutabilityExclusionFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** [registryId](#API_PutImageTagMutability_RequestSyntax) **   <a name="ECR-PutImageTagMutability-request-registryId"></a>
The AWS account ID associated with the registry that contains the repository in which to update the image tag mutability settings. If you do not specify a registry, the default registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [repositoryName](#API_PutImageTagMutability_RequestSyntax) **   <a name="ECR-PutImageTagMutability-request-repositoryName"></a>
The name of the repository in which to update the image tag mutability settings.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`
Required: Yes

## Response Syntax
<a name="API_PutImageTagMutability_ResponseSyntax"></a>

```
{
   "imageTagMutability": "string",
   "imageTagMutabilityExclusionFilters": [
      {
         "filter": "string",
         "filterType": "string"
      }
   ],
   "registryId": "string",
   "repositoryName": "string"
}
```

## Response Elements
<a name="API_PutImageTagMutability_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [imageTagMutability](#API_PutImageTagMutability_ResponseSyntax) **   <a name="ECR-PutImageTagMutability-response-imageTagMutability"></a>
The image tag mutability setting for the repository.
Type: String
Valid Values: `MUTABLE | IMMUTABLE | IMMUTABLE_WITH_EXCLUSION | MUTABLE_WITH_EXCLUSION`

 ** [imageTagMutabilityExclusionFilters](#API_PutImageTagMutability_ResponseSyntax) **   <a name="ECR-PutImageTagMutability-response-imageTagMutabilityExclusionFilters"></a>
The list of filters that specify which image tags are excluded from the repository's image tag mutability setting.
Type: Array of [ImageTagMutabilityExclusionFilter](API_ImageTagMutabilityExclusionFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.

 ** [registryId](#API_PutImageTagMutability_ResponseSyntax) **   <a name="ECR-PutImageTagMutability-response-registryId"></a>
The registry ID associated with the request.
Type: String
Pattern: `[0-9]{12}`

 ** [repositoryName](#API_PutImageTagMutability_ResponseSyntax) **   <a name="ECR-PutImageTagMutability-response-repositoryName"></a>
The repository name associated with the request.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`

## Errors
<a name="API_PutImageTagMutability_Errors"></a>

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
<a name="API_PutImageTagMutability_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_PutImageTagMutability_Example_1"></a>

This example updates the image tag mutability setting for the `sample-repo` repository.

#### Sample Request
<a name="API_PutImageTagMutability_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecr.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 73
X-Amz-Target: AmazonEC2ContainerRegistry_V20150921.PutImageTagMutability
X-Amz-Date: 20161216T201255Z
User-Agent: aws-cli/1.16.310 Python/3.6.1 Darwin/18.7.0 botocore/1.13.46
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
    "repositoryName": "sample-repo",
    "imageTagMutability": "IMMUTABLE"
}
```

#### Sample Response
<a name="API_PutImageTagMutability_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Fri, 24 Jan 2020 03:48:07 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 98
Connection: keep-alive
x-amzn-RequestId: 3081a92b-2066-41f8-8a47-0580288ada9e

{
    "registryId": "012345678910",
    "repositoryName": "sample-repo",
    "imageTagMutability": "IMMUTABLE"
}
```

## See Also
<a name="API_PutImageTagMutability_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/PutImageTagMutability)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/PutImageTagMutability)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/PutImageTagMutability)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/PutImageTagMutability)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/PutImageTagMutability)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/PutImageTagMutability)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/PutImageTagMutability)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/PutImageTagMutability)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/PutImageTagMutability)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/PutImageTagMutability)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
