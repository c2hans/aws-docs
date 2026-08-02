---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_AnalysisRule.html
---

# AnalysisRule
<a name="API_AnalysisRule"></a>

A specification about how data from the configured table can be used in a query.

## Contents
<a name="API_AnalysisRule_Contents"></a>

 ** collaborationId **   <a name="API-Type-AnalysisRule-collaborationId"></a>
The unique ID for the associated collaboration.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** createTime **   <a name="API-Type-AnalysisRule-createTime"></a>
The time the analysis rule was created.
Type: Timestamp
Required: Yes

 ** name **   <a name="API-Type-AnalysisRule-name"></a>
The name for the analysis rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?`
Required: Yes

 ** policy **   <a name="API-Type-AnalysisRule-policy"></a>
A policy that describes the associated data usage limitations.
Type: [AnalysisRulePolicy](API_AnalysisRulePolicy.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** type **   <a name="API-Type-AnalysisRule-type"></a>
The type of analysis rule.
Type: String
Valid Values: `AGGREGATION | LIST | CUSTOM | ID_MAPPING_TABLE`
Required: Yes

 ** updateTime **   <a name="API-Type-AnalysisRule-updateTime"></a>
The time the analysis rule was last updated.
Type: Timestamp
Required: Yes

 ** collaborationPolicy **   <a name="API-Type-AnalysisRule-collaborationPolicy"></a>
 Controls on the query specifications that can be run on an associated configured table.
Type: [ConfiguredTableAssociationAnalysisRulePolicy](API_ConfiguredTableAssociationAnalysisRulePolicy.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** consolidatedPolicy **   <a name="API-Type-AnalysisRule-consolidatedPolicy"></a>
 The consolidated policy for the analysis rule.
Type: [ConsolidatedPolicy](API_ConsolidatedPolicy.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_AnalysisRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/AnalysisRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/AnalysisRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/AnalysisRule)
