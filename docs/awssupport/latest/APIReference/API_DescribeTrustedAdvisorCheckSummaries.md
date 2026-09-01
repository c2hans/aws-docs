---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeTrustedAdvisorCheckSummaries.html
---

# DescribeTrustedAdvisorCheckSummaries
<a name="API_DescribeTrustedAdvisorCheckSummaries"></a>

Returns the results for the AWS Trusted Advisor check summaries for the check IDs that you specified. You can get the check IDs by calling the [DescribeTrustedAdvisorChecks](API_DescribeTrustedAdvisorChecks.md) operation.

The response contains an array of [TrustedAdvisorCheckSummary](API_TrustedAdvisorCheckSummary.md) objects.

**Note**
You must have an AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan to use the AWS Support API. If you're in an AWS Region that doesn't offer one of these AWS Support plans, or if you haven't transitioned to one of these plans, you can use the AWS Support API with a Business, Enterprise On-Ramp, or Enterprise Support plan.
If you call the AWS Support API from an account that doesn't have an AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan, the `SubscriptionRequiredException` error message appears. For information about changing your support plan, see [AWS Support](http://aws.amazon.com/premiumsupport/).

To call the AWS Trusted Advisor operations in the AWS Support API, you must use the US East (N. Virginia) endpoint. Currently, the US West (Oregon) and Europe (Ireland) endpoints don't support the Trusted Advisor operations. For more information, see [About the AWS Support API](https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html#endpoint) in the * AWS Support User Guide*.

 **Understanding the Trusted Advisor Resources processed value**

The **Resources processed** value, `resourcesProcessed`, usually shows both flagged resources (those with warnings or errors) and resources in good standing (ok status resources). However, some checks report flagged resources only. To understand what a specific check reports, review the detailed check information in the [AWS Trusted Advisor check reference](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-check-reference.html). If you see a **Green** criterion listed in the **Alert criteria**, then the check reports all resources. If there's no **Green** criterion listed in the **Alert criteria**, then the check reports only flagged resources. For example, the [Amazon EC2 Reserved Instance optimization check (cX3c2R1chu)](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#amazon-ec2-reserved-instances-optimization) doesn't list a **Green** criterion in the **Alert criteria**. So, this check only reports flagged resources.

## Request Syntax
<a name="API_DescribeTrustedAdvisorCheckSummaries_RequestSyntax"></a>

```
{
   "checkIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeTrustedAdvisorCheckSummaries_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [checkIds](#API_DescribeTrustedAdvisorCheckSummaries_RequestSyntax) **   <a name="AWSSupport-DescribeTrustedAdvisorCheckSummaries-request-checkIds"></a>
The IDs of the Trusted Advisor checks.
Type: Array of strings

## Response Syntax
<a name="API_DescribeTrustedAdvisorCheckSummaries_ResponseSyntax"></a>

```
{
   "summaries": [
      {
         "categorySpecificSummary": {
            "costOptimizing": {
               "estimatedMonthlySavings": number,
               "estimatedPercentMonthlySavings": number
            }
         },
         "checkId": "string",
         "hasFlaggedResources": boolean,
         "resourcesSummary": {
            "resourcesFlagged": number,
            "resourcesIgnored": number,
            "resourcesProcessed": number,
            "resourcesSuppressed": number
         },
         "status": "string",
         "timestamp": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeTrustedAdvisorCheckSummaries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [summaries](#API_DescribeTrustedAdvisorCheckSummaries_ResponseSyntax) **   <a name="AWSSupport-DescribeTrustedAdvisorCheckSummaries-response-summaries"></a>
The summary information for the requested Trusted Advisor checks.
Type: Array of [TrustedAdvisorCheckSummary](API_TrustedAdvisorCheckSummary.md) objects

## Errors
<a name="API_DescribeTrustedAdvisorCheckSummaries_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An internal server error occurred.
 ** message **
An internal server error occurred.
HTTP Status Code: 500

 ** ThrottlingException **
 You have exceeded the maximum allowed TPS (Transactions Per Second) for the operations.
HTTP Status Code: 400

## See Also
<a name="API_DescribeTrustedAdvisorCheckSummaries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/support-2013-04-15/DescribeTrustedAdvisorCheckSummaries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/support-2013-04-15/DescribeTrustedAdvisorCheckSummaries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/DescribeTrustedAdvisorCheckSummaries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/support-2013-04-15/DescribeTrustedAdvisorCheckSummaries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/DescribeTrustedAdvisorCheckSummaries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/support-2013-04-15/DescribeTrustedAdvisorCheckSummaries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/support-2013-04-15/DescribeTrustedAdvisorCheckSummaries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/support-2013-04-15/DescribeTrustedAdvisorCheckSummaries)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/support-2013-04-15/DescribeTrustedAdvisorCheckSummaries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/DescribeTrustedAdvisorCheckSummaries)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awssupport` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
