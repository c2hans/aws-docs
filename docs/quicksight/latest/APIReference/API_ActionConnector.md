---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ActionConnector.html
---

# ActionConnector
<a name="API_ActionConnector"></a>

Contains detailed information about an action connector, including its configuration, status, and enabled actions.

## Contents
<a name="API_ActionConnector_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ActionConnectorId **   <a name="QS-Type-ActionConnector-ActionConnectorId"></a>
The unique identifier of the action connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** Arn **   <a name="QS-Type-ActionConnector-Arn"></a>
The Amazon Resource Name (ARN) of the action connector.
Type: String
Required: Yes

 ** LastUpdatedTime **   <a name="QS-Type-ActionConnector-LastUpdatedTime"></a>
The date and time when the action connector was last updated.
Type: Timestamp
Required: Yes

 ** Name **   <a name="QS-Type-ActionConnector-Name"></a>
The name of the action connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9](?:[\w- ]*[A-Za-z0-9])?`
Required: Yes

 ** Type **   <a name="QS-Type-ActionConnector-Type"></a>
The type of action connector.
Type: String
Valid Values: `GENERIC_HTTP | SERVICENOW_NOW_PLATFORM | SALESFORCE_CRM | MICROSOFT_OUTLOOK | PAGERDUTY_ADVANCE | JIRA_CLOUD | ATLASSIAN_CONFLUENCE | AMAZON_S3 | AMAZON_BEDROCK_AGENT_RUNTIME | AMAZON_BEDROCK_RUNTIME | AMAZON_BEDROCK_DATA_AUTOMATION_RUNTIME | AMAZON_TEXTRACT | AMAZON_COMPREHEND | AMAZON_COMPREHEND_MEDICAL | MICROSOFT_ONEDRIVE | MICROSOFT_SHAREPOINT | MICROSOFT_TEAMS | SAP_BUSINESSPARTNER | SAP_PRODUCTMASTERDATA | SAP_PHYSICALINVENTORY | SAP_BILLOFMATERIALS | SAP_MATERIALSTOCK | ZENDESK_SUITE | SMARTSHEET | SLACK | ASANA | BAMBOO_HR`
Required: Yes

 ** AuthenticationConfig **   <a name="QS-Type-ActionConnector-AuthenticationConfig"></a>
The authentication configuration used to connect to the external service.
Type: [ReadAuthConfig](API_ReadAuthConfig.md) object
Required: No

 ** CreatedTime **   <a name="QS-Type-ActionConnector-CreatedTime"></a>
The timestamp when the action connector was created.
Type: Timestamp
Required: No

 ** Description **   <a name="QS-Type-ActionConnector-Description"></a>
The description of the action connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[A-Za-z0-9 _.,!?-]*`
Required: No

 ** EnabledActions **   <a name="QS-Type-ActionConnector-EnabledActions"></a>
The list of actions that are enabled for this connector.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Pattern: `[\w@:_.,!?+-/]+`
Required: No

 ** Error **   <a name="QS-Type-ActionConnector-Error"></a>
Error information if the action connector is in an error state.
Type: [ActionConnectorError](API_ActionConnectorError.md) object
Required: No

 ** Status **   <a name="QS-Type-ActionConnector-Status"></a>
The current status of the action connector.
Type: String
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETED`
Required: No

 ** VpcConnectionArn **   <a name="QS-Type-ActionConnector-VpcConnectionArn"></a>
The ARN of the VPC connection used for secure connectivity to the external service.
Type: String
Required: No

## See Also
<a name="API_ActionConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ActionConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ActionConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ActionConnector)
