---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ActionConnectorSummary.html
---

# ActionConnectorSummary
<a name="API_ActionConnectorSummary"></a>

Contains summary information about an action connector, used in list and search operations.

## Contents
<a name="API_ActionConnectorSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ActionConnectorId **   <a name="QS-Type-ActionConnectorSummary-ActionConnectorId"></a>
The unique identifier of the action connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** Arn **   <a name="QS-Type-ActionConnectorSummary-Arn"></a>
The Amazon Resource Name (ARN) of the action connector.
Type: String
Required: Yes

 ** LastUpdatedTime **   <a name="QS-Type-ActionConnectorSummary-LastUpdatedTime"></a>
The date and time when the action connector was last updated.
Type: Timestamp
Required: Yes

 ** Name **   <a name="QS-Type-ActionConnectorSummary-Name"></a>
The name of the action connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9](?:[\w- ]*[A-Za-z0-9])?`
Required: Yes

 ** Type **   <a name="QS-Type-ActionConnectorSummary-Type"></a>
The type of action connector (e.g., SALESFORCE, JIRA, CUSTOM, BEDROCK).
Type: String
Valid Values: `GENERIC_HTTP | SERVICENOW_NOW_PLATFORM | SALESFORCE_CRM | MICROSOFT_OUTLOOK | PAGERDUTY_ADVANCE | JIRA_CLOUD | ATLASSIAN_CONFLUENCE | AMAZON_S3 | AMAZON_BEDROCK_AGENT_RUNTIME | AMAZON_BEDROCK_RUNTIME | AMAZON_BEDROCK_DATA_AUTOMATION_RUNTIME | AMAZON_TEXTRACT | AMAZON_COMPREHEND | AMAZON_COMPREHEND_MEDICAL | MICROSOFT_ONEDRIVE | MICROSOFT_SHAREPOINT | MICROSOFT_TEAMS | SAP_BUSINESSPARTNER | SAP_PRODUCTMASTERDATA | SAP_PHYSICALINVENTORY | SAP_BILLOFMATERIALS | SAP_MATERIALSTOCK | ZENDESK_SUITE | SMARTSHEET | SLACK | ASANA | BAMBOO_HR`
Required: Yes

 ** CreatedTime **   <a name="QS-Type-ActionConnectorSummary-CreatedTime"></a>
The date and time when the action connector was created.
Type: Timestamp
Required: No

 ** Error **   <a name="QS-Type-ActionConnectorSummary-Error"></a>
Error information if the action connector is in an error state.
Type: [ActionConnectorError](API_ActionConnectorError.md) object
Required: No

 ** Status **   <a name="QS-Type-ActionConnectorSummary-Status"></a>
The current status of the action connector.
Type: String
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETED`
Required: No

## See Also
<a name="API_ActionConnectorSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ActionConnectorSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ActionConnectorSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ActionConnectorSummary)
