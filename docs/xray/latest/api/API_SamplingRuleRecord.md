---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_SamplingRuleRecord.html
---

# SamplingRuleRecord
<a name="API_SamplingRuleRecord"></a>

A [SamplingRule](https://docs.aws.amazon.com/xray/latest/api/API_SamplingRule.html) and its metadata.

## Contents
<a name="API_SamplingRuleRecord_Contents"></a>

 ** CreatedAt **   <a name="xray-Type-SamplingRuleRecord-CreatedAt"></a>
When the rule was created, in Unix time seconds.
Type: Timestamp
Required: No

 ** ModifiedAt **   <a name="xray-Type-SamplingRuleRecord-ModifiedAt"></a>
When the rule was last modified, in Unix time seconds.
Type: Timestamp
Required: No

 ** SamplingRule **   <a name="xray-Type-SamplingRuleRecord-SamplingRule"></a>
The sampling rule.
Type: [SamplingRule](API_SamplingRule.md) object
Required: No

## See Also
<a name="API_SamplingRuleRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/SamplingRuleRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/SamplingRuleRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/SamplingRuleRecord)
