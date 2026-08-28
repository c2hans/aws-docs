---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_IntermediateTableAnalysisRule.html
---

# IntermediateTableAnalysisRule
<a name="API_IntermediateTableAnalysisRule"></a>

Contains the details of an analysis rule for an intermediate table.

## Contents
<a name="API_IntermediateTableAnalysisRule_Contents"></a>

 ** analysisRulePolicy **   <a name="API-Type-IntermediateTableAnalysisRule-analysisRulePolicy"></a>
The policy of the analysis rule.
Type: [IntermediateTableAnalysisRulePolicy](API_IntermediateTableAnalysisRulePolicy.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** analysisRuleType **   <a name="API-Type-IntermediateTableAnalysisRule-analysisRuleType"></a>
The type of the analysis rule.
Type: String
Valid Values: `CUSTOM`
Required: Yes

 ** createTime **   <a name="API-Type-IntermediateTableAnalysisRule-createTime"></a>
The time the analysis rule was created.
Type: Timestamp
Required: Yes

 ** intermediateTableArn **   <a name="API-Type-IntermediateTableAnalysisRule-intermediateTableArn"></a>
The Amazon Resource Name (ARN) of the intermediate table associated with this analysis rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership\/[\d\w-]+\/intermediatetable\/[\d\w-]+`
Required: Yes

 ** intermediateTableIdentifier **   <a name="API-Type-IntermediateTableAnalysisRule-intermediateTableIdentifier"></a>
The unique identifier of the intermediate table associated with this analysis rule.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** updateTime **   <a name="API-Type-IntermediateTableAnalysisRule-updateTime"></a>
The time the analysis rule was last updated.
Type: Timestamp
Required: Yes

## See Also
<a name="API_IntermediateTableAnalysisRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/IntermediateTableAnalysisRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/IntermediateTableAnalysisRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/IntermediateTableAnalysisRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
