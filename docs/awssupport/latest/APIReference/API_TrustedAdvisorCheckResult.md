---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_TrustedAdvisorCheckResult.html
---

# TrustedAdvisorCheckResult
<a name="API_TrustedAdvisorCheckResult"></a>

The results of a Trusted Advisor check returned by [DescribeTrustedAdvisorCheckResult](API_DescribeTrustedAdvisorCheckResult.md).

## Contents
<a name="API_TrustedAdvisorCheckResult_Contents"></a>

 ** categorySpecificSummary **   <a name="AWSSupport-Type-TrustedAdvisorCheckResult-categorySpecificSummary"></a>
Summary information that relates to the category of the check. Cost Optimizing is the only category that is currently supported.
Type: [TrustedAdvisorCategorySpecificSummary](API_TrustedAdvisorCategorySpecificSummary.md) object

 ** checkId **   <a name="AWSSupport-Type-TrustedAdvisorCheckResult-checkId"></a>
The unique identifier for the Trusted Advisor check.
Type: String

 ** flaggedResources **   <a name="AWSSupport-Type-TrustedAdvisorCheckResult-flaggedResources"></a>
The details about each resource listed in the check result.
Type: Array of [TrustedAdvisorResourceDetail](API_TrustedAdvisorResourceDetail.md) objects

 ** resourcesSummary **   <a name="AWSSupport-Type-TrustedAdvisorCheckResult-resourcesSummary"></a>
Details about AWS resources that were analyzed in a call to Trusted Advisor [DescribeTrustedAdvisorCheckSummaries](API_DescribeTrustedAdvisorCheckSummaries.md).
Type: [TrustedAdvisorResourcesSummary](API_TrustedAdvisorResourcesSummary.md) object

 ** status **   <a name="AWSSupport-Type-TrustedAdvisorCheckResult-status"></a>
The alert status of the check: "ok" (green), "warning" (yellow), "error" (red), or "not\_available".
Type: String

 ** timestamp **   <a name="AWSSupport-Type-TrustedAdvisorCheckResult-timestamp"></a>
The time of the last refresh of the check.
Type: String

## See Also
<a name="API_TrustedAdvisorCheckResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/TrustedAdvisorCheckResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/TrustedAdvisorCheckResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/TrustedAdvisorCheckResult)
