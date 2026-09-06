---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Plugin.html
---

# Plugin
<a name="API_Plugin"></a>

Information about an Amazon Q Business plugin and its configuration.

## Contents
<a name="API_Plugin_Contents"></a>

 ** buildStatus **   <a name="qbusiness-Type-Plugin-buildStatus"></a>
The status of the plugin.
Type: String
Valid Values: `READY | CREATE_IN_PROGRESS | CREATE_FAILED | UPDATE_IN_PROGRESS | UPDATE_FAILED | DELETE_IN_PROGRESS | DELETE_FAILED`
Required: No

 ** createdAt **   <a name="qbusiness-Type-Plugin-createdAt"></a>
The timestamp for when the plugin was created.
Type: Timestamp
Required: No

 ** displayName **   <a name="qbusiness-Type-Plugin-displayName"></a>
The name of the plugin.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: No

 ** pluginId **   <a name="qbusiness-Type-Plugin-pluginId"></a>
The identifier of the plugin.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** serverUrl **   <a name="qbusiness-Type-Plugin-serverUrl"></a>
The plugin server URL used for configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(https?|ftp|file)://([^\s]*)`
Required: No

 ** state **   <a name="qbusiness-Type-Plugin-state"></a>
The current status of the plugin.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** type **   <a name="qbusiness-Type-Plugin-type"></a>
The type of the plugin.
Type: String
Valid Values: `SERVICE_NOW | SALESFORCE | JIRA | ZENDESK | CUSTOM | QUICKSIGHT | SERVICENOW_NOW_PLATFORM | JIRA_CLOUD | SALESFORCE_CRM | ZENDESK_SUITE | ATLASSIAN_CONFLUENCE | GOOGLE_CALENDAR | MICROSOFT_TEAMS | MICROSOFT_EXCHANGE | PAGERDUTY_ADVANCE | SMARTSHEET | ASANA`
Required: No

 ** updatedAt **   <a name="qbusiness-Type-Plugin-updatedAt"></a>
The timestamp for when the plugin was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_Plugin_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/Plugin)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/Plugin)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/Plugin)
