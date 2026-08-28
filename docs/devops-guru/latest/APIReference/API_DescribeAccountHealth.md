---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_DescribeAccountHealth.html
---

# DescribeAccountHealth
<a name="API_DescribeAccountHealth"></a>

 Returns the number of open reactive insights, the number of open proactive insights, and the number of metrics analyzed in your AWS account. Use these numbers to gauge the health of operations in your AWS account.

## Request Syntax
<a name="API_DescribeAccountHealth_RequestSyntax"></a>

```
GET /accounts/health HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeAccountHealth_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeAccountHealth_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeAccountHealth_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AnalyzedResourceCount": number,
   "MetricsAnalyzed": number,
   "OpenProactiveInsights": number,
   "OpenReactiveInsights": number,
   "ResourceHours": number
}
```

## Response Elements
<a name="API_DescribeAccountHealth_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AnalyzedResourceCount](#API_DescribeAccountHealth_ResponseSyntax) **   <a name="DevOpsGuru-DescribeAccountHealth-response-AnalyzedResourceCount"></a>
 Number of resources that DevOps Guru is monitoring in your AWS account.
Type: Long

 ** [MetricsAnalyzed](#API_DescribeAccountHealth_ResponseSyntax) **   <a name="DevOpsGuru-DescribeAccountHealth-response-MetricsAnalyzed"></a>
 An integer that specifies the number of metrics that have been analyzed in your AWS account.
Type: Integer

 ** [OpenProactiveInsights](#API_DescribeAccountHealth_ResponseSyntax) **   <a name="DevOpsGuru-DescribeAccountHealth-response-OpenProactiveInsights"></a>
 An integer that specifies the number of open proactive insights in your AWS account.
Type: Integer

 ** [OpenReactiveInsights](#API_DescribeAccountHealth_ResponseSyntax) **   <a name="DevOpsGuru-DescribeAccountHealth-response-OpenReactiveInsights"></a>
 An integer that specifies the number of open reactive insights in your AWS account.
Type: Integer

 ** [ResourceHours](#API_DescribeAccountHealth_ResponseSyntax) **   <a name="DevOpsGuru-DescribeAccountHealth-response-ResourceHours"></a>
The number of Amazon DevOps Guru resource analysis hours billed to the current AWS account in the last hour.
Type: Long

## Errors
<a name="API_DescribeAccountHealth_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see [Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *IAM User Guide*.
HTTP Status Code: 403

 ** InternalServerException **
An internal failure in an Amazon service occurred.
 ** RetryAfterSeconds **
 The number of seconds after which the action that caused the internal server exception can be retried.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to a request throttling.
 ** QuotaCode **
 The code of the quota that was exceeded, causing the throttling exception.
 ** RetryAfterSeconds **
 The number of seconds after which the action that caused the throttling exception can be retried.
 ** ServiceCode **
 The code of the service that caused the throttling exception.
HTTP Status Code: 429

 ** ValidationException **
 Contains information about data passed in to a field during a request that is not valid.
 ** Fields **
 An array of fields that are associated with the validation exception.
 ** Message **
 A message that describes the validation exception.
 ** Reason **
 The reason the validation exception was thrown.
HTTP Status Code: 400

## See Also
<a name="API_DescribeAccountHealth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-guru-2020-12-01/DescribeAccountHealth)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-guru-2020-12-01/DescribeAccountHealth)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/DescribeAccountHealth)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-guru-2020-12-01/DescribeAccountHealth)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/DescribeAccountHealth)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-guru-2020-12-01/DescribeAccountHealth)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-guru-2020-12-01/DescribeAccountHealth)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-guru-2020-12-01/DescribeAccountHealth)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devops-guru-2020-12-01/DescribeAccountHealth)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/DescribeAccountHealth)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
