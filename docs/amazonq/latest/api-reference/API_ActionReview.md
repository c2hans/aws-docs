---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ActionReview.html
---

# ActionReview
<a name="API_ActionReview"></a>

An output event that Amazon Q Business returns to an user who wants to perform a plugin action during a non-streaming chat conversation. It contains information about the selected action with a list of possible user input fields, some pre-populated by Amazon Q Business.

## Contents
<a name="API_ActionReview_Contents"></a>

 ** payload **   <a name="qbusiness-Type-ActionReview-payload"></a>
Field values that an end user needs to provide to Amazon Q Business for Amazon Q Business to perform the requested plugin action.
Type: String to [ActionReviewPayloadField](API_ActionReviewPayloadField.md) object map
Key Length Constraints: Minimum length of 1.
Required: No

 ** payloadFieldNameSeparator **   <a name="qbusiness-Type-ActionReview-payloadFieldNameSeparator"></a>
A string used to retain information about the hierarchical contexts within an action review payload.
Type: String
Length Constraints: Fixed length of 1.
Required: No

 ** pluginId **   <a name="qbusiness-Type-ActionReview-pluginId"></a>
The identifier of the plugin associated with the action review.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** pluginType **   <a name="qbusiness-Type-ActionReview-pluginType"></a>
The type of plugin.
Type: String
Valid Values: `SERVICE_NOW | SALESFORCE | JIRA | ZENDESK | CUSTOM | QUICKSIGHT | SERVICENOW_NOW_PLATFORM | JIRA_CLOUD | SALESFORCE_CRM | ZENDESK_SUITE | ATLASSIAN_CONFLUENCE | GOOGLE_CALENDAR | MICROSOFT_TEAMS | MICROSOFT_EXCHANGE | PAGERDUTY_ADVANCE | SMARTSHEET | ASANA`
Required: No

## See Also
<a name="API_ActionReview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/ActionReview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/ActionReview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/ActionReview)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
