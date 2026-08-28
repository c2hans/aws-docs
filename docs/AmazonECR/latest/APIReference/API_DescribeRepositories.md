---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeRepositories.html
---

# DescribeRepositories
<a name="API_DescribeRepositories"></a>

Describes image repositories in a registry.

## Request Syntax
<a name="API_DescribeRepositories_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "registryId": "{{string}}",
   "repositoryNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeRepositories_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_DescribeRepositories_RequestSyntax) **   <a name="ECR-DescribeRepositories-request-maxResults"></a>
The maximum number of repository results returned by `DescribeRepositories` in paginated output. When this parameter is used, `DescribeRepositories` only returns `maxResults` results in a single page along with a `nextToken` response element. The remaining results of the initial request can be seen by sending another `DescribeRepositories` request with the returned `nextToken` value. This value can be between 1 and 1000. If this parameter is not used, then `DescribeRepositories` returns up to 100 results and a `nextToken` value, if applicable. This option cannot be used when you specify repositories with `repositoryNames`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_DescribeRepositories_RequestSyntax) **   <a name="ECR-DescribeRepositories-request-nextToken"></a>
The `nextToken` value returned from a previous paginated `DescribeRepositories` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value. This value is `null` when there are no more results to return. This option cannot be used when you specify repositories with `repositoryNames`.
This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
Type: String
Required: No

 ** [registryId](#API_DescribeRepositories_RequestSyntax) **   <a name="ECR-DescribeRepositories-request-registryId"></a>
The AWS account ID associated with the registry that contains the repositories to be described. If you do not specify a registry, the default registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [repositoryNames](#API_DescribeRepositories_RequestSyntax) **   <a name="ECR-DescribeRepositories-request-repositoryNames"></a>
A list of repositories to describe. If this parameter is omitted, then all repositories in a registry are described.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`
Required: No

## Response Syntax
<a name="API_DescribeRepositories_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "repositories": [
      {
         "createdAt": number,
         "encryptionConfiguration": {
            "encryptionType": "string",
            "kmsKey": "string"
         },
         "imageScanningConfiguration": {
            "scanOnPush": boolean
         },
         "imageTagMutability": "string",
         "imageTagMutabilityExclusionFilters": [
            {
               "filter": "string",
               "filterType": "string"
            }
         ],
         "registryId": "string",
         "repositoryArn": "string",
         "repositoryName": "string",
         "repositoryUri": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeRepositories_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_DescribeRepositories_ResponseSyntax) **   <a name="ECR-DescribeRepositories-response-nextToken"></a>
The `nextToken` value to include in a future `DescribeRepositories` request. When the results of a `DescribeRepositories` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 ** [repositories](#API_DescribeRepositories_ResponseSyntax) **   <a name="ECR-DescribeRepositories-response-repositories"></a>
A list of repository objects corresponding to valid repositories.
Type: Array of [Repository](API_Repository.md) objects

## Errors
<a name="API_DescribeRepositories_Errors"></a>

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
<a name="API_DescribeRepositories_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_DescribeRepositories_Example_1"></a>

This example describes the repositories in the default registry for an account.

#### Sample Request
<a name="API_DescribeRepositories_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: api.ecr.us-west-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonEC2ContainerRegistry_V20150921.DescribeRepositories
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.16.190 Python/3.6.1 Darwin/16.7.0 botocore/1.12.180
X-Amz-Date: 20190715T205400Z
Authorization: AUTHPARAMS
Content-Length: 2

{}
```

#### Sample Response
<a name="API_DescribeRepositories_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f
Content-Type: application/x-amz-json-1.1
Content-Length: 1061
Connection: keep-alive

{
   "repositories":[
      {
         "createdAt":1.563223656E9,
         "imageTagMutability":"MUTABLE",
         "registryId":"012345678910",
         "repositoryArn":"arn:aws:ecr:us-west-2:012345678910:repository/sample-repo",
         "repositoryName":"sample-repo",
         "repositoryUri":"012345678910.dkr.ecr.us-west-2.amazonaws.com/sample-repo"
      },
      {
         "createdAt":1.554824595E9,
         "imageTagMutability":"IMMUTABLE",
         "registryId":"012345678910",
         "repositoryArn":"arn:aws:ecr:us-west-2:012345678910:repository/tagging-test",
         "repositoryName":"tagging-test",
         "repositoryUri":"012345678910.dkr.ecr.us-west-2.amazonaws.com/tagging-test"
      }
   ]
}
```

## See Also
<a name="API_DescribeRepositories_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/DescribeRepositories)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/DescribeRepositories)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/DescribeRepositories)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/DescribeRepositories)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/DescribeRepositories)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/DescribeRepositories)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/DescribeRepositories)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/DescribeRepositories)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/DescribeRepositories)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/DescribeRepositories)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
