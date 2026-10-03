---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_RemediationSummaryDetail.html
---

# RemediationSummaryDetail
<a name="API_RemediationSummaryDetail"></a>

A summary of the remediation target.

## Contents
<a name="API_RemediationSummaryDetail_Contents"></a>

 ** Action **   <a name="securityhub-Type-RemediationSummaryDetail-Action"></a>
A summarized action to take for the remediation target.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** IsImmediate **   <a name="securityhub-Type-RemediationSummaryDetail-IsImmediate"></a>
Specifies whether the effect of this target is immediate.
Type: Boolean
Required: Yes

 ** Description **   <a name="securityhub-Type-RemediationSummaryDetail-Description"></a>
A description of the remediation target.
Type: String
Pattern: `.*\S.*`
Required: No

 ** KbArticles **   <a name="securityhub-Type-RemediationSummaryDetail-KbArticles"></a>
An array of `KbArticle` objects.
Type: Array of [KbArticle](API_KbArticle.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** PostRemediationSteps **   <a name="securityhub-Type-RemediationSummaryDetail-PostRemediationSteps"></a>
An array of steps to be taken after remediation.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_RemediationSummaryDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/RemediationSummaryDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/RemediationSummaryDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/RemediationSummaryDetail)
