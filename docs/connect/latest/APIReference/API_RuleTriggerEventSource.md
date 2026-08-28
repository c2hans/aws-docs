---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RuleTriggerEventSource.html
---

# RuleTriggerEventSource
<a name="API_RuleTriggerEventSource"></a>

The name of the event source. This field is required if `TriggerEventSource` is one of the following values: `OnZendeskTicketCreate` \| `OnZendeskTicketStatusUpdate` \| `OnSalesforceCaseCreate` \| `OnContactEvaluationSubmit` \| `OnMetricDataUpdate`.

## Contents
<a name="API_RuleTriggerEventSource_Contents"></a>

 ** EventSourceName **   <a name="connect-Type-RuleTriggerEventSource-EventSourceName"></a>
The name of the event source.
Type: String
Valid Values: `OnPostCallAnalysisAvailable | OnRealTimeCallAnalysisAvailable | OnRealTimeChatAnalysisAvailable | OnPostChatAnalysisAvailable | OnAfterCallWorkAvailable | OnAfterChatWorkAvailable | OnEmailAnalysisAvailable | OnZendeskTicketCreate | OnZendeskTicketStatusUpdate | OnSalesforceCaseCreate | OnContactEvaluationSubmit | OnMetricDataUpdate | OnCaseCreate | OnCaseUpdate | OnSlaBreach | OnAlertUpdate | OnSchedulePublish | OnScheduleUpdate | OnScheduleTimeOffRequestActivity`
Required: Yes

 ** IntegrationAssociationId **   <a name="connect-Type-RuleTriggerEventSource-IntegrationAssociationId"></a>
The identifier for the integration association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

## See Also
<a name="API_RuleTriggerEventSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RuleTriggerEventSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RuleTriggerEventSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RuleTriggerEventSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
