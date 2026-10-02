---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RuleAction.html
---

# RuleAction
<a name="API_RuleAction"></a>

Information about the action to be performed when a rule is triggered.

## Contents
<a name="API_RuleAction_Contents"></a>

 ** ActionType **   <a name="connect-Type-RuleAction-ActionType"></a>
The type of action that creates a rule.
Type: String
Valid Values: `CREATE_TASK | ASSIGN_CONTACT_CATEGORY | GENERATE_EVENTBRIDGE_EVENT | SEND_NOTIFICATION | CREATE_CASE | UPDATE_CASE | ASSIGN_SLA | END_ASSOCIATED_TASKS | SUBMIT_AUTO_EVALUATION | EXTRACT_INFORMATION | SEND_IN_APP_NOTIFICATION`
Required: Yes

 ** AssignContactCategoryAction **   <a name="connect-Type-RuleAction-AssignContactCategoryAction"></a>
Information about the contact category action.
Supported only for `TriggerEventSource` values: `OnPostCallAnalysisAvailable` \| `OnRealTimeCallAnalysisAvailable` \| `OnRealTimeChatAnalysisAvailable` \| `OnPostChatAnalysisAvailable` \| `OnZendeskTicketCreate` \| `OnZendeskTicketStatusUpdate` \| `OnSalesforceCaseCreate`
Type: [AssignContactCategoryActionDefinition](API_AssignContactCategoryActionDefinition.md) object
Required: No

 ** AssignSlaAction **   <a name="connect-Type-RuleAction-AssignSlaAction"></a>
Information about the assign SLA action.
Type: [AssignSlaActionDefinition](API_AssignSlaActionDefinition.md) object
Required: No

 ** CreateCaseAction **   <a name="connect-Type-RuleAction-CreateCaseAction"></a>
Information about the create case action.
Supported only for `TriggerEventSource` values: `OnPostCallAnalysisAvailable` \| `OnPostChatAnalysisAvailable`.
Type: [CreateCaseActionDefinition](API_CreateCaseActionDefinition.md) object
Required: No

 ** EndAssociatedTasksAction **   <a name="connect-Type-RuleAction-EndAssociatedTasksAction"></a>
Information about the end associated tasks action.
Supported only for `TriggerEventSource` values: `OnCaseUpdate`.
Type: [EndAssociatedTasksActionDefinition](API_EndAssociatedTasksActionDefinition.md) object
Required: No

 ** EventBridgeAction **   <a name="connect-Type-RuleAction-EventBridgeAction"></a>
Information about the EventBridge action.
Supported only for `TriggerEventSource` values: `OnPostCallAnalysisAvailable` \| `OnRealTimeCallAnalysisAvailable` \| `OnRealTimeChatAnalysisAvailable` \| `OnPostChatAnalysisAvailable` \| `OnContactEvaluationSubmit` \| `OnMetricDataUpdate`
Type: [EventBridgeActionDefinition](API_EventBridgeActionDefinition.md) object
Required: No

 ** ExtractInformationAction **   <a name="connect-Type-RuleAction-ExtractInformationAction"></a>
Information about the extract information action.
Type: [ExtractInformationActionDefinition](API_ExtractInformationActionDefinition.md) object
Required: No

 ** SendInAppNotificationAction **   <a name="connect-Type-RuleAction-SendInAppNotificationAction"></a>
Information about the send in-app notification action.
Supported only for `TriggerEventSource` values: `OnPostCallAnalysisAvailable` \| `OnRealTimeCallAnalysisAvailable` \| `OnRealTimeChatAnalysisAvailable` \| `OnPostChatAnalysisAvailable` \| `OnAfterCallWorkAvailable` \| `OnAfterChatWorkAvailable` \| `OnEmailAnalysisAvailable` \| `OnContactEvaluationSubmit` \| `OnCaseCreate` \| `OnCaseUpdate` \| `OnSlaBreach` \| `OnSchedulePublish` \| `OnScheduleUpdate` \| `OnScheduleTimeOffRequestActivity`
Type: [SendInAppNotificationActionDefinition](API_SendInAppNotificationActionDefinition.md) object
Required: No

 ** SendNotificationAction **   <a name="connect-Type-RuleAction-SendNotificationAction"></a>
Information about the send notification action.
Supported only for `TriggerEventSource` values: `OnPostCallAnalysisAvailable` \| `OnRealTimeCallAnalysisAvailable` \| `OnRealTimeChatAnalysisAvailable` \| `OnPostChatAnalysisAvailable` \| `OnContactEvaluationSubmit` \| `OnMetricDataUpdate`
Type: [SendNotificationActionDefinition](API_SendNotificationActionDefinition.md) object
Required: No

 ** SubmitAutoEvaluationAction **   <a name="connect-Type-RuleAction-SubmitAutoEvaluationAction"></a>
Information about the submit automated evaluation action.
Type: [SubmitAutoEvaluationActionDefinition](API_SubmitAutoEvaluationActionDefinition.md) object
Required: No

 ** TaskAction **   <a name="connect-Type-RuleAction-TaskAction"></a>
Information about the task action. This field is required if `TriggerEventSource` is one of the following values: `OnZendeskTicketCreate` \| `OnZendeskTicketStatusUpdate` \| `OnSalesforceCaseCreate`
Type: [TaskActionDefinition](API_TaskActionDefinition.md) object
Required: No

 ** UpdateCaseAction **   <a name="connect-Type-RuleAction-UpdateCaseAction"></a>
Information about the update case action.
Supported only for `TriggerEventSource` values: `OnCaseCreate` \| `OnCaseUpdate`.
Type: [UpdateCaseActionDefinition](API_UpdateCaseActionDefinition.md) object
Required: No

## See Also
<a name="API_RuleAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RuleAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RuleAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RuleAction)
