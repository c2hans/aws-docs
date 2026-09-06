---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_QPluginCard.html
---

# QPluginCard
<a name="API_qapps_QPluginCard"></a>

A card in an Q App that integrates with a third-party plugin or service.

## Contents
<a name="API_qapps_QPluginCard_Contents"></a>

 ** dependencies **   <a name="qbusiness-Type-qapps_QPluginCard-dependencies"></a>
Any dependencies or requirements for the plugin card.
Type: Array of strings
Required: Yes

 ** id **   <a name="qbusiness-Type-qapps_QPluginCard-id"></a>
The unique identifier of the plugin card.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

 ** pluginId **   <a name="qbusiness-Type-qapps_QPluginCard-pluginId"></a>
The unique identifier of the plugin used by the card.
Type: String
Required: Yes

 ** pluginType **   <a name="qbusiness-Type-qapps_QPluginCard-pluginType"></a>
The type or category of the plugin used by the card.
Type: String
Valid Values: `SERVICE_NOW | SALESFORCE | JIRA | ZENDESK | CUSTOM | ASANA | ATLASSIAN_CONFLUENCE | GOOGLE_CALENDAR | JIRA_CLOUD | MICROSOFT_EXCHANGE | MICROSOFT_TEAMS | PAGERDUTY_ADVANCE | SALESFORCE_CRM | SERVICENOW_NOW_PLATFORM | SMARTSHEET | ZENDESK_SUITE`
Required: Yes

 ** prompt **   <a name="qbusiness-Type-qapps_QPluginCard-prompt"></a>
The prompt or instructions displayed for the plugin card.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50000.
Required: Yes

 ** title **   <a name="qbusiness-Type-qapps_QPluginCard-title"></a>
The title or label of the plugin card.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `[^{}\\"<>]+`
Required: Yes

 ** type **   <a name="qbusiness-Type-qapps_QPluginCard-type"></a>
The type of the card.
Type: String
Valid Values: `text-input | q-query | file-upload | q-plugin | form-input`
Required: Yes

 ** actionIdentifier **   <a name="qbusiness-Type-qapps_QPluginCard-actionIdentifier"></a>
The action identifier of the action to be performed by the plugin card.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_qapps_QPluginCard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/QPluginCard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/QPluginCard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/QPluginCard)
