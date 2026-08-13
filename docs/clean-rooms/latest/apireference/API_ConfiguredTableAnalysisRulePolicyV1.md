---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ConfiguredTableAnalysisRulePolicyV1.html
---

# ConfiguredTableAnalysisRulePolicyV1
<a name="API_ConfiguredTableAnalysisRulePolicyV1"></a>

Controls on the query specifications that can be run on a configured table.

## Contents
<a name="API_ConfiguredTableAnalysisRulePolicyV1_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** aggregation **   <a name="API-Type-ConfiguredTableAnalysisRulePolicyV1-aggregation"></a>
Analysis rule type that enables only aggregation queries on a configured table.
Type: [AnalysisRuleAggregation](API_AnalysisRuleAggregation.md) object
Required: No

 ** custom **   <a name="API-Type-ConfiguredTableAnalysisRulePolicyV1-custom"></a>
A type of analysis rule that enables the table owner to approve custom SQL queries on their configured tables. It supports differential privacy, minimum aggregation thresholds, and comparison controls.
Type: [AnalysisRuleCustom](API_AnalysisRuleCustom.md) object
Required: No

 ** list **   <a name="API-Type-ConfiguredTableAnalysisRulePolicyV1-list"></a>
Analysis rule type that enables only list queries on a configured table.
Type: [AnalysisRuleList](API_AnalysisRuleList.md) object
Required: No

## See Also
<a name="API_ConfiguredTableAnalysisRulePolicyV1_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ConfiguredTableAnalysisRulePolicyV1)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ConfiguredTableAnalysisRulePolicyV1)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ConfiguredTableAnalysisRulePolicyV1)
