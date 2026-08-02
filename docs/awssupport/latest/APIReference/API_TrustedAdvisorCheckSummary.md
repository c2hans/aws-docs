---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_TrustedAdvisorCheckSummary.html
---

# TrustedAdvisorCheckSummary
<a name="API_TrustedAdvisorCheckSummary"></a>

A summary of a Trusted Advisor check result, including the alert status, last refresh, and number of resources examined.

## Contents
<a name="API_TrustedAdvisorCheckSummary_Contents"></a>

 ** categorySpecificSummary **   <a name="AWSSupport-Type-TrustedAdvisorCheckSummary-categorySpecificSummary"></a>
Summary information that relates to the category of the check. Cost Optimizing is the only category that is currently supported.
Type: [TrustedAdvisorCategorySpecificSummary](API_TrustedAdvisorCategorySpecificSummary.md) object

 ** checkId **   <a name="AWSSupport-Type-TrustedAdvisorCheckSummary-checkId"></a>
The unique identifier for the Trusted Advisor check.
Type: String

 ** resourcesSummary **   <a name="AWSSupport-Type-TrustedAdvisorCheckSummary-resourcesSummary"></a>
Details about AWS resources that were analyzed in a call to Trusted Advisor [DescribeTrustedAdvisorCheckSummaries](API_DescribeTrustedAdvisorCheckSummaries.md).
Type: [TrustedAdvisorResourcesSummary](API_TrustedAdvisorResourcesSummary.md) object

 ** status **   <a name="AWSSupport-Type-TrustedAdvisorCheckSummary-status"></a>
The alert status of the check: "ok" (green), "warning" (yellow), "error" (red), or "not\_available".
Type: String

 ** timestamp **   <a name="AWSSupport-Type-TrustedAdvisorCheckSummary-timestamp"></a>
The time of the last refresh of the check.
Type: String

 ** hasFlaggedResources **   <a name="AWSSupport-Type-TrustedAdvisorCheckSummary-hasFlaggedResources"></a>
Specifies whether the Trusted Advisor check has flagged resources.
Type: Boolean

## See Also
<a name="API_TrustedAdvisorCheckSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/TrustedAdvisorCheckSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/TrustedAdvisorCheckSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/TrustedAdvisorCheckSummary)
