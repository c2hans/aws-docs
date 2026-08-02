---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ConformancePackComplianceScore.html
---

# ConformancePackComplianceScore
<a name="API_ConformancePackComplianceScore"></a>

A compliance score is the percentage of the number of compliant rule-resource combinations in a conformance pack compared to the number of total possible rule-resource combinations in the conformance pack. This metric provides you with a high-level view of the compliance state of your conformance packs. You can use it to identify, investigate, and understand the level of compliance in your conformance packs.

## Contents
<a name="API_ConformancePackComplianceScore_Contents"></a>

 ** ConformancePackName **   <a name="config-Type-ConformancePackComplianceScore-ConformancePackName"></a>
The name of the conformance pack.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z][-a-zA-Z0-9]*`
Required: No

 ** LastUpdatedTime **   <a name="config-Type-ConformancePackComplianceScore-LastUpdatedTime"></a>
The time that the conformance pack compliance score was last updated.
Type: Timestamp
Required: No

 ** Score **   <a name="config-Type-ConformancePackComplianceScore-Score"></a>
Compliance score for the conformance pack. Conformance packs with no evaluation results will have a compliance score of `INSUFFICIENT_DATA`.
Type: String
Required: No

## See Also
<a name="API_ConformancePackComplianceScore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ConformancePackComplianceScore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ConformancePackComplianceScore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ConformancePackComplianceScore)
