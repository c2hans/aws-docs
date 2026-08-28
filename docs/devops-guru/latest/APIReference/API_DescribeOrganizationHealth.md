---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_DescribeOrganizationHealth.html
---

# DescribeOrganizationHealth
<a name="API_DescribeOrganizationHealth"></a>

Returns the number of metrics, insights, and resource hours DevOps Guru analyzed in the last hour.

There are two types of insights:
+  *Reactive*: A reactive insight identifies anomalous behavior as it occurs. It contains anomalies with recommendations, related metrics, and events to help you understand and address the issues now.
+  *Proactive*: A proactive insight lets you know about anomalous behavior before it occurs. It contains anomalies with recommendations to help you address the issues before they are predicted to happen.

## Request Syntax
<a name="API_DescribeOrganizationHealth_RequestSyntax"></a>

```
POST /organization/health HTTP/1.1
Content-type: application/json

{
   "AccountIds": [ "{{string}}" ],
   "OrganizationalUnitIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_DescribeOrganizationHealth_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeOrganizationHealth_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountIds](#API_DescribeOrganizationHealth_RequestSyntax) **   <a name="DevOpsGuru-DescribeOrganizationHealth-request-AccountIds"></a>
The ID of the AWS account.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: No

 ** [OrganizationalUnitIds](#API_DescribeOrganizationHealth_RequestSyntax) **   <a name="DevOpsGuru-DescribeOrganizationHealth-request-OrganizationalUnitIds"></a>
The ID of the organizational unit.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Maximum length of 68.
Pattern: `^ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}$`
Required: No

## Response Syntax
<a name="API_DescribeOrganizationHealth_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "MetricsAnalyzed": number,
   "OpenProactiveInsights": number,
   "OpenReactiveInsights": number,
   "ResourceHours": number
}
```

## Response Elements
<a name="API_DescribeOrganizationHealth_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MetricsAnalyzed](#API_DescribeOrganizationHealth_ResponseSyntax) **   <a name="DevOpsGuru-DescribeOrganizationHealth-response-MetricsAnalyzed"></a>
An integer that specifies the number of metrics that have been analyzed in your organization.
Type: Integer

 ** [OpenProactiveInsights](#API_DescribeOrganizationHealth_ResponseSyntax) **   <a name="DevOpsGuru-DescribeOrganizationHealth-response-OpenProactiveInsights"></a>
An integer that specifies the number of open proactive insights in your AWS account.
Type: Integer

 ** [OpenReactiveInsights](#API_DescribeOrganizationHealth_ResponseSyntax) **   <a name="DevOpsGuru-DescribeOrganizationHealth-response-OpenReactiveInsights"></a>
An integer that specifies the number of open reactive insights in your AWS account.
Type: Integer

 ** [ResourceHours](#API_DescribeOrganizationHealth_ResponseSyntax) **   <a name="DevOpsGuru-DescribeOrganizationHealth-response-ResourceHours"></a>
The number of Amazon DevOps Guru resource analysis hours billed to the current AWS account in the last hour.
Type: Long

## Errors
<a name="API_DescribeOrganizationHealth_Errors"></a>

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
<a name="API_DescribeOrganizationHealth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-guru-2020-12-01/DescribeOrganizationHealth)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-guru-2020-12-01/DescribeOrganizationHealth)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/DescribeOrganizationHealth)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-guru-2020-12-01/DescribeOrganizationHealth)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/DescribeOrganizationHealth)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-guru-2020-12-01/DescribeOrganizationHealth)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-guru-2020-12-01/DescribeOrganizationHealth)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-guru-2020-12-01/DescribeOrganizationHealth)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devops-guru-2020-12-01/DescribeOrganizationHealth)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/DescribeOrganizationHealth)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
