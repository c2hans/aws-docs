---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ListPullTimeUpdateExclusions.html
---

# ListPullTimeUpdateExclusions
<a name="API_ListPullTimeUpdateExclusions"></a>

Lists the IAM principals that are excluded from having their image pull times recorded.

## Request Syntax
<a name="API_ListPullTimeUpdateExclusions_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListPullTimeUpdateExclusions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListPullTimeUpdateExclusions_RequestSyntax) **   <a name="ECR-ListPullTimeUpdateExclusions-request-maxResults"></a>
The maximum number of pull time update exclusion results returned by `ListPullTimeUpdateExclusions` in paginated output. When this parameter is used, `ListPullTimeUpdateExclusions` only returns `maxResults` results in a single page along with a `nextToken` response element. The remaining results of the initial request can be seen by sending another `ListPullTimeUpdateExclusions` request with the returned `nextToken` value. This value can be between 1 and 1000. If this parameter is not used, then `ListPullTimeUpdateExclusions` returns up to 100 results and a `nextToken` value, if applicable.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListPullTimeUpdateExclusions_RequestSyntax) **   <a name="ECR-ListPullTimeUpdateExclusions-request-nextToken"></a>
The `nextToken` value returned from a previous paginated `ListPullTimeUpdateExclusions` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value. This value is `null` when there are no more results to return.
This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
Type: String
Required: No

## Response Syntax
<a name="API_ListPullTimeUpdateExclusions_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "pullTimeUpdateExclusions": [ "string" ]
}
```

## Response Elements
<a name="API_ListPullTimeUpdateExclusions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListPullTimeUpdateExclusions_ResponseSyntax) **   <a name="ECR-ListPullTimeUpdateExclusions-response-nextToken"></a>
The `nextToken` value to include in a future `ListPullTimeUpdateExclusions` request. When the results of a `ListPullTimeUpdateExclusions` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 ** [pullTimeUpdateExclusions](#API_ListPullTimeUpdateExclusions_ResponseSyntax) **   <a name="ECR-ListPullTimeUpdateExclusions-response-pullTimeUpdateExclusions"></a>
The list of IAM principal ARNs that are excluded from having their image pull times recorded.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Maximum length of 200.
Pattern: `^arn:aws(-[a-z]+)*:iam::[0-9]{12}:(role|user)/[\w+=,.@-]+(/[\w+=,.@-]+)*$`

## Errors
<a name="API_ListPullTimeUpdateExclusions_Errors"></a>

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

 ** ServerException **
These errors are usually caused by a server-side issue.
 ** message **
The error message associated with the exception.
HTTP Status Code: 500

 ** ValidationException **
There was an exception validating this request.
HTTP Status Code: 400

## Examples
<a name="API_ListPullTimeUpdateExclusions_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### To list all pull time update exclusions
<a name="API_ListPullTimeUpdateExclusions_Example_1"></a>

This example lists all IAM principals that are excluded from having their image pull timestamps recorded in the registry.

#### Sample Request
<a name="API_ListPullTimeUpdateExclusions_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: api.ecr.us-west-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonEC2ContainerRegistry_V20150921.ListPullTimeUpdateExclusions
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0 Python/3.8.0 Darwin/20.0.0 botocore/2.0.0
X-Amz-Date: 20251117T220830Z
Authorization: AUTHPARAMS
Content-Length: 2

{}
```

#### Sample Response
<a name="API_ListPullTimeUpdateExclusions_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f
Content-Type: application/x-amz-json-1.1
Content-Length: 95
Connection: keep-alive

{
   "pullTimeUpdateExclusions": [
      "arn:aws:iam::012345678910:role/ECRAccess"
   ]
}
```

## See Also
<a name="API_ListPullTimeUpdateExclusions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/ListPullTimeUpdateExclusions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/ListPullTimeUpdateExclusions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/ListPullTimeUpdateExclusions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/ListPullTimeUpdateExclusions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/ListPullTimeUpdateExclusions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/ListPullTimeUpdateExclusions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/ListPullTimeUpdateExclusions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/ListPullTimeUpdateExclusions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/ListPullTimeUpdateExclusions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/ListPullTimeUpdateExclusions)
