---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_PluginTypeMetadataSummary.html
---

# PluginTypeMetadataSummary
<a name="API_PluginTypeMetadataSummary"></a>

Summary metadata information for a Amazon Q Business plugin.

## Contents
<a name="API_PluginTypeMetadataSummary_Contents"></a>

 ** category **   <a name="qbusiness-Type-PluginTypeMetadataSummary-category"></a>
The category of the plugin type.
Type: String
Valid Values: `Customer relationship management (CRM) | Project management | Communication | Productivity | Ticketing and incident management`
Required: No

 ** description **   <a name="qbusiness-Type-PluginTypeMetadataSummary-description"></a>
The description assigned by Amazon Q Business to a plugin. You can't modify this value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** type **   <a name="qbusiness-Type-PluginTypeMetadataSummary-type"></a>
The type of the plugin.
Type: String
Valid Values: `SERVICE_NOW | SALESFORCE | JIRA | ZENDESK | CUSTOM | QUICKSIGHT | SERVICENOW_NOW_PLATFORM | JIRA_CLOUD | SALESFORCE_CRM | ZENDESK_SUITE | ATLASSIAN_CONFLUENCE | GOOGLE_CALENDAR | MICROSOFT_TEAMS | MICROSOFT_EXCHANGE | PAGERDUTY_ADVANCE | SMARTSHEET | ASANA`
Required: No

## See Also
<a name="API_PluginTypeMetadataSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/PluginTypeMetadataSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/PluginTypeMetadataSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/PluginTypeMetadataSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
