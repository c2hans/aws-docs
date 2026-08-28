---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_TrustedAdvisorResourcesSummary.html
---

# TrustedAdvisorResourcesSummary
<a name="API_TrustedAdvisorResourcesSummary"></a>

Details about AWS resources that were analyzed in a call to Trusted Advisor [DescribeTrustedAdvisorCheckSummaries](API_DescribeTrustedAdvisorCheckSummaries.md).

## Contents
<a name="API_TrustedAdvisorResourcesSummary_Contents"></a>

 ** resourcesFlagged **   <a name="AWSSupport-Type-TrustedAdvisorResourcesSummary-resourcesFlagged"></a>
The number of AWS resources that were flagged (listed) by the Trusted Advisor check.
Type: Long

 ** resourcesIgnored **   <a name="AWSSupport-Type-TrustedAdvisorResourcesSummary-resourcesIgnored"></a>
The number of AWS resources ignored by Trusted Advisor because information was unavailable.
Type: Long

 ** resourcesProcessed **   <a name="AWSSupport-Type-TrustedAdvisorResourcesSummary-resourcesProcessed"></a>
The number of AWS resources that were analyzed by the Trusted Advisor check.
Type: Long

 ** resourcesSuppressed **   <a name="AWSSupport-Type-TrustedAdvisorResourcesSummary-resourcesSuppressed"></a>
The number of AWS resources ignored by Trusted Advisor because they were marked as suppressed by the user.
Type: Long

## See Also
<a name="API_TrustedAdvisorResourcesSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/TrustedAdvisorResourcesSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/TrustedAdvisorResourcesSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/TrustedAdvisorResourcesSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awssupport` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
