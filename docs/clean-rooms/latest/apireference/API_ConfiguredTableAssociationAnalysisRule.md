---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ConfiguredTableAssociationAnalysisRule.html
---

# ConfiguredTableAssociationAnalysisRule
<a name="API_ConfiguredTableAssociationAnalysisRule"></a>

An analysis rule for a configured table association. This analysis rule specifies how data from the table can be used within its associated collaboration. In the console, the `ConfiguredTableAssociationAnalysisRule` is referred to as the *collaboration analysis rule*.

## Contents
<a name="API_ConfiguredTableAssociationAnalysisRule_Contents"></a>

 ** configuredTableAssociationArn **   <a name="API-Type-ConfiguredTableAssociationAnalysisRule-configuredTableAssociationArn"></a>
 The Amazon Resource Name (ARN) of the configured table association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:configuredtableassociation/[\d\w-]+/[\d\w-]+`
Required: Yes

 ** configuredTableAssociationId **   <a name="API-Type-ConfiguredTableAssociationAnalysisRule-configuredTableAssociationId"></a>
 The unique identifier for the configured table association.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** createTime **   <a name="API-Type-ConfiguredTableAssociationAnalysisRule-createTime"></a>
 The creation time of the configured table association analysis rule.
Type: Timestamp
Required: Yes

 ** membershipIdentifier **   <a name="API-Type-ConfiguredTableAssociationAnalysisRule-membershipIdentifier"></a>
 The membership identifier for the configured table association analysis rule.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** policy **   <a name="API-Type-ConfiguredTableAssociationAnalysisRule-policy"></a>
 The policy of the configured table association analysis rule.
Type: [ConfiguredTableAssociationAnalysisRulePolicy](API_ConfiguredTableAssociationAnalysisRulePolicy.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** type **   <a name="API-Type-ConfiguredTableAssociationAnalysisRule-type"></a>
 The type of the configured table association analysis rule.
Type: String
Valid Values: `AGGREGATION | LIST | CUSTOM`
Required: Yes

 ** updateTime **   <a name="API-Type-ConfiguredTableAssociationAnalysisRule-updateTime"></a>
 The update time of the configured table association analysis rule.
Type: Timestamp
Required: Yes

## See Also
<a name="API_ConfiguredTableAssociationAnalysisRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ConfiguredTableAssociationAnalysisRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ConfiguredTableAssociationAnalysisRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ConfiguredTableAssociationAnalysisRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
