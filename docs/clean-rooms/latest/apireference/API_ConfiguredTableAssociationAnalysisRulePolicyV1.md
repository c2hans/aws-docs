---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ConfiguredTableAssociationAnalysisRulePolicyV1.html
---

# ConfiguredTableAssociationAnalysisRulePolicyV1
<a name="API_ConfiguredTableAssociationAnalysisRulePolicyV1"></a>

 Controls on the query specifications that can be run on an associated configured table.

## Contents
<a name="API_ConfiguredTableAssociationAnalysisRulePolicyV1_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** aggregation **   <a name="API-Type-ConfiguredTableAssociationAnalysisRulePolicyV1-aggregation"></a>
 Analysis rule type that enables only aggregation queries on a configured table.
Type: [ConfiguredTableAssociationAnalysisRuleAggregation](API_ConfiguredTableAssociationAnalysisRuleAggregation.md) object
Required: No

 ** custom **   <a name="API-Type-ConfiguredTableAssociationAnalysisRulePolicyV1-custom"></a>
 Analysis rule type that enables the table owner to approve custom SQL queries on their configured tables. It supports differential privacy.
Type: [ConfiguredTableAssociationAnalysisRuleCustom](API_ConfiguredTableAssociationAnalysisRuleCustom.md) object
Required: No

 ** list **   <a name="API-Type-ConfiguredTableAssociationAnalysisRulePolicyV1-list"></a>
 Analysis rule type that enables only list queries on a configured table.
Type: [ConfiguredTableAssociationAnalysisRuleList](API_ConfiguredTableAssociationAnalysisRuleList.md) object
Required: No

## See Also
<a name="API_ConfiguredTableAssociationAnalysisRulePolicyV1_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ConfiguredTableAssociationAnalysisRulePolicyV1)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ConfiguredTableAssociationAnalysisRulePolicyV1)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ConfiguredTableAssociationAnalysisRulePolicyV1)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
