---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ActionReviewEvent.html
---

# ActionReviewEvent
<a name="API_ActionReviewEvent"></a>

An output event that Amazon Q Business returns to an user who wants to perform a plugin action during a streaming chat conversation. It contains information about the selected action with a list of possible user input fields, some pre-populated by Amazon Q Business.

## Contents
<a name="API_ActionReviewEvent_Contents"></a>

 ** conversationId **   <a name="qbusiness-Type-ActionReviewEvent-conversationId"></a>
The identifier of the conversation with which the action review event is associated.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: No

 ** payload **   <a name="qbusiness-Type-ActionReviewEvent-payload"></a>
Field values that an end user needs to provide to Amazon Q Business for Amazon Q Business to perform the requested plugin action.
Type: String to [ActionReviewPayloadField](API_ActionReviewPayloadField.md) object map
Key Length Constraints: Minimum length of 1.
Required: No

 ** payloadFieldNameSeparator **   <a name="qbusiness-Type-ActionReviewEvent-payloadFieldNameSeparator"></a>
A string used to retain information about the hierarchical contexts within an action review event payload.
Type: String
Length Constraints: Fixed length of 1.
Required: No

 ** pluginId **   <a name="qbusiness-Type-ActionReviewEvent-pluginId"></a>
The identifier of the plugin associated with the action review event.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** pluginType **   <a name="qbusiness-Type-ActionReviewEvent-pluginType"></a>
The type of plugin.
Type: String
Valid Values: `SERVICE_NOW | SALESFORCE | JIRA | ZENDESK | CUSTOM | QUICKSIGHT | SERVICENOW_NOW_PLATFORM | JIRA_CLOUD | SALESFORCE_CRM | ZENDESK_SUITE | ATLASSIAN_CONFLUENCE | GOOGLE_CALENDAR | MICROSOFT_TEAMS | MICROSOFT_EXCHANGE | PAGERDUTY_ADVANCE | SMARTSHEET | ASANA`
Required: No

 ** systemMessageId **   <a name="qbusiness-Type-ActionReviewEvent-systemMessageId"></a>
The identifier of an Amazon Q Business AI generated associated with the action review event.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: No

 ** userMessageId **   <a name="qbusiness-Type-ActionReviewEvent-userMessageId"></a>
The identifier of the conversation with which the plugin action is associated.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: No

## See Also
<a name="API_ActionReviewEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/ActionReviewEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/ActionReviewEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/ActionReviewEvent)
