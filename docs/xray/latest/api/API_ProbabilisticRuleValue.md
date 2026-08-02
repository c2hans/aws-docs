---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_ProbabilisticRuleValue.html
---

# ProbabilisticRuleValue
<a name="API_ProbabilisticRuleValue"></a>

 The indexing rule configuration for probabilistic sampling.

## Contents
<a name="API_ProbabilisticRuleValue_Contents"></a>

 ** DesiredSamplingPercentage **   <a name="xray-Type-ProbabilisticRuleValue-DesiredSamplingPercentage"></a>
 Configured sampling percentage of traceIds. Note that sampling can be subject to limits to ensure completeness of data.
Type: Double
Required: Yes

 ** ActualSamplingPercentage **   <a name="xray-Type-ProbabilisticRuleValue-ActualSamplingPercentage"></a>
 Applied sampling percentage of traceIds.
Type: Double
Required: No

## See Also
<a name="API_ProbabilisticRuleValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/ProbabilisticRuleValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/ProbabilisticRuleValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/ProbabilisticRuleValue)
