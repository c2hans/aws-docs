---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RuleSummary.html
---

# RuleSummary
<a name="API_RuleSummary"></a>

A list of `ActionTypes` associated with a rule.

## Contents
<a name="API_RuleSummary_Contents"></a>

 ** ActionSummaries **   <a name="connect-Type-RuleSummary-ActionSummaries"></a>
A list of ActionTypes associated with a rule.
Type: Array of [ActionSummary](API_ActionSummary.md) objects
Required: Yes

 ** CreatedTime **   <a name="connect-Type-RuleSummary-CreatedTime"></a>
The timestamp for when the rule was created.
Type: Timestamp
Required: Yes

 ** EventSourceName **   <a name="connect-Type-RuleSummary-EventSourceName"></a>
The name of the event source.
Type: String
Valid Values: `OnPostCallAnalysisAvailable | OnRealTimeCallAnalysisAvailable | OnRealTimeChatAnalysisAvailable | OnPostChatAnalysisAvailable | OnEmailAnalysisAvailable | OnZendeskTicketCreate | OnZendeskTicketStatusUpdate | OnSalesforceCaseCreate | OnContactEvaluationSubmit | OnMetricDataUpdate | OnCaseCreate | OnCaseUpdate | OnSlaBreach | OnAlertUpdate | OnSchedulePublish | OnScheduleUpdate | OnScheduleTimeOffRequestActivity`
Required: Yes

 ** LastUpdatedTime **   <a name="connect-Type-RuleSummary-LastUpdatedTime"></a>
The timestamp for when the rule was last updated.
Type: Timestamp
Required: Yes

 ** Name **   <a name="connect-Type-RuleSummary-Name"></a>
The name of the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^[0-9a-zA-Z._-]+`
Required: Yes

 ** PublishStatus **   <a name="connect-Type-RuleSummary-PublishStatus"></a>
The publish status of the rule.
Type: String
Valid Values: `DRAFT | PUBLISHED`
Required: Yes

 ** RuleArn **   <a name="connect-Type-RuleSummary-RuleArn"></a>
The Amazon Resource Name (ARN) of the rule.
Type: String
Required: Yes

 ** RuleId **   <a name="connect-Type-RuleSummary-RuleId"></a>
A unique identifier for the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** RuleCapabilityTiers **   <a name="connect-Type-RuleSummary-RuleCapabilityTiers"></a>
The list of capability tiers associated with the rule. Used for categorizing rules by capability (for example, `GenerativeAI`).
Type: Array of strings
Valid Values: `GenerativeAI`
Required: No

## See Also
<a name="API_RuleSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RuleSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RuleSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RuleSummary)
