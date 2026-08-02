---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_AnalysisRulePolicyV1.html
---

# AnalysisRulePolicyV1
<a name="API_AnalysisRulePolicyV1"></a>

Controls on the query specifications that can be run on configured table.

## Contents
<a name="API_AnalysisRulePolicyV1_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** aggregation **   <a name="API-Type-AnalysisRulePolicyV1-aggregation"></a>
Analysis rule type that enables only aggregation queries on a configured table.
Type: [AnalysisRuleAggregation](API_AnalysisRuleAggregation.md) object
Required: No

 ** custom **   <a name="API-Type-AnalysisRulePolicyV1-custom"></a>
Analysis rule type that enables custom SQL queries on a configured table.
Type: [AnalysisRuleCustom](API_AnalysisRuleCustom.md) object
Required: No

 ** idMappingTable **   <a name="API-Type-AnalysisRulePolicyV1-idMappingTable"></a>
The ID mapping table.
Type: [AnalysisRuleIdMappingTable](API_AnalysisRuleIdMappingTable.md) object
Required: No

 ** list **   <a name="API-Type-AnalysisRulePolicyV1-list"></a>
Analysis rule type that enables only list queries on a configured table.
Type: [AnalysisRuleList](API_AnalysisRuleList.md) object
Required: No

## See Also
<a name="API_AnalysisRulePolicyV1_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/AnalysisRulePolicyV1)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/AnalysisRulePolicyV1)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/AnalysisRulePolicyV1)
