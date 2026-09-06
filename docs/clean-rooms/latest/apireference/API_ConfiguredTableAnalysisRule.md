---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ConfiguredTableAnalysisRule.html
---

# ConfiguredTableAnalysisRule
<a name="API_ConfiguredTableAnalysisRule"></a>

A configured table analysis rule, which limits how data for this table can be used.

## Contents
<a name="API_ConfiguredTableAnalysisRule_Contents"></a>

 ** configuredTableArn **   <a name="API-Type-ConfiguredTableAnalysisRule-configuredTableArn"></a>
The unique ARN for the configured table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:configuredtable/[\d\w-]+`
Required: Yes

 ** configuredTableId **   <a name="API-Type-ConfiguredTableAnalysisRule-configuredTableId"></a>
The unique ID for the configured table.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** createTime **   <a name="API-Type-ConfiguredTableAnalysisRule-createTime"></a>
The time the configured table analysis rule was created.
Type: Timestamp
Required: Yes

 ** policy **   <a name="API-Type-ConfiguredTableAnalysisRule-policy"></a>
The policy that controls SQL query rules.
Type: [ConfiguredTableAnalysisRulePolicy](API_ConfiguredTableAnalysisRulePolicy.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** type **   <a name="API-Type-ConfiguredTableAnalysisRule-type"></a>
The type of configured table analysis rule.
Type: String
Valid Values: `AGGREGATION | LIST | CUSTOM`
Required: Yes

 ** updateTime **   <a name="API-Type-ConfiguredTableAnalysisRule-updateTime"></a>
The time the configured table analysis rule was last updated.
Type: Timestamp
Required: Yes

## See Also
<a name="API_ConfiguredTableAnalysisRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ConfiguredTableAnalysisRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ConfiguredTableAnalysisRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ConfiguredTableAnalysisRule)
