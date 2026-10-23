---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Capabilities.html
---

# Capabilities
<a name="API_Capabilities"></a>

A set of actions that correspond to Amazon Quick Sight permissions.

## Contents
<a name="API_Capabilities_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AccessAppsNativeDataStore **   <a name="QS-Type-Capabilities-AccessAppsNativeDataStore"></a>
The ability to access the native data store for new and existing apps.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** Action **   <a name="QS-Type-Capabilities-Action"></a>
The ability to perform actions in external services through Action connectors. Actions allow users to interact with third-party systems.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** AddOrRunAnomalyDetectionForAnalyses **   <a name="QS-Type-Capabilities-AddOrRunAnomalyDetectionForAnalyses"></a>
The ability to add or run anomaly detection.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** AdobeAction **   <a name="QS-Type-Capabilities-AdobeAction"></a>
The ability to perform actions using Adobe Marketing Agent connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** AdobeAnalyticsDataSource **   <a name="QS-Type-Capabilities-AdobeAnalyticsDataSource"></a>
The ability to create, update, and share Adobe Analytics data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** AirtableAction **   <a name="QS-Type-Capabilities-AirtableAction"></a>
The ability to perform actions using Airtable connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** AmazonBedrockARSAction **   <a name="QS-Type-Capabilities-AmazonBedrockARSAction"></a>
The ability to perform actions using Bedrock Agent connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** AmazonBedrockFSAction **   <a name="QS-Type-Capabilities-AmazonBedrockFSAction"></a>
The ability to perform actions using Bedrock Runtime connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** AmazonBedrockKRSAction **   <a name="QS-Type-Capabilities-AmazonBedrockKRSAction"></a>
The ability to perform actions using Bedrock Data Automation Runtime connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** AmazonSThreeAction **   <a name="QS-Type-Capabilities-AmazonSThreeAction"></a>
The ability to perform actions using Amazon S3 connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** Analysis **   <a name="QS-Type-Capabilities-Analysis"></a>
The ability to perform analysis-related actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ApproveFlowShareRequests **   <a name="QS-Type-Capabilities-ApproveFlowShareRequests"></a>
The ability to review and approve sharing requests of Flows.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** Apps **   <a name="QS-Type-Capabilities-Apps"></a>
The ability to perform apps-related actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** AsanaAction **   <a name="QS-Type-Capabilities-AsanaAction"></a>
The ability to perform actions using Asana connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** AthenaDataSource **   <a name="QS-Type-Capabilities-AthenaDataSource"></a>
The ability to create, update, and share Amazon Athena data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** AuroraDataSource **   <a name="QS-Type-Capabilities-AuroraDataSource"></a>
The ability to create, update, and share Amazon Aurora data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** Automate **   <a name="QS-Type-Capabilities-Automate"></a>
The ability to perform automate-related actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** BambooHRAction **   <a name="QS-Type-Capabilities-BambooHRAction"></a>
The ability to perform actions using BambooHR connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** BedrockManagedKnowledgeBase **   <a name="QS-Type-Capabilities-BedrockManagedKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** BeeAction **   <a name="QS-Type-Capabilities-BeeAction"></a>
The ability to perform actions using Bee connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** BoxAgentAction **   <a name="QS-Type-Capabilities-BoxAgentAction"></a>
The ability to perform actions using Box Agent connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** BoxKnowledgeBase **   <a name="QS-Type-Capabilities-BoxKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** BuildCalculatedFieldWithQ **   <a name="QS-Type-Capabilities-BuildCalculatedFieldWithQ"></a>
The ability to Build Calculation with AI
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CanvaAgentAction **   <a name="QS-Type-Capabilities-CanvaAgentAction"></a>
The ability to perform actions using Canva Agent connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ChatAgent **   <a name="QS-Type-Capabilities-ChatAgent"></a>
The ability to perform chat-related actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CiscoWebexMeetingsAction **   <a name="QS-Type-Capabilities-CiscoWebexMeetingsAction"></a>
The ability to perform actions using Cisco Webex Meetings connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CiscoWebexVidcastAction **   <a name="QS-Type-Capabilities-CiscoWebexVidcastAction"></a>
The ability to perform actions using Cisco Webex Video Messaging Agent connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ComprehendAction **   <a name="QS-Type-Capabilities-ComprehendAction"></a>
The ability to perform actions using Comprehend connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ComprehendMedicalAction **   <a name="QS-Type-Capabilities-ComprehendMedicalAction"></a>
The ability to perform actions using Comprehend Medical connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ConfluenceAction **   <a name="QS-Type-Capabilities-ConfluenceAction"></a>
The ability to perform actions using Atlassian Confluence Cloud connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ConfluenceKnowledgeBase **   <a name="QS-Type-Capabilities-ConfluenceKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAdobeAnalyticsDataSource **   <a name="QS-Type-Capabilities-CreateAdobeAnalyticsDataSource"></a>
The ability to create Adobe Analytics data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateAdobeAction **   <a name="QS-Type-Capabilities-CreateAndUpdateAdobeAction"></a>
The ability to create and update Adobe Marketing Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateAirtableAction **   <a name="QS-Type-Capabilities-CreateAndUpdateAirtableAction"></a>
The ability to create and update Airtable actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateAmazonBedrockARSAction **   <a name="QS-Type-Capabilities-CreateAndUpdateAmazonBedrockARSAction"></a>
The ability to create and update Bedrock Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateAmazonBedrockFSAction **   <a name="QS-Type-Capabilities-CreateAndUpdateAmazonBedrockFSAction"></a>
The ability to create and update Bedrock Runtime actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateAmazonBedrockKRSAction **   <a name="QS-Type-Capabilities-CreateAndUpdateAmazonBedrockKRSAction"></a>
The ability to create and update Bedrock Data Automation Runtime actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateAmazonSThreeAction **   <a name="QS-Type-Capabilities-CreateAndUpdateAmazonSThreeAction"></a>
The ability to create and update Amazon S3 actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateApps **   <a name="QS-Type-Capabilities-CreateAndUpdateApps"></a>
The ability to create or update apps.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateAsanaAction **   <a name="QS-Type-Capabilities-CreateAndUpdateAsanaAction"></a>
The ability to create and update Asana actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateBambooHRAction **   <a name="QS-Type-Capabilities-CreateAndUpdateBambooHRAction"></a>
The ability to create and update BambooHR actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateBedrockManagedKnowledgeBase **   <a name="QS-Type-Capabilities-CreateAndUpdateBedrockManagedKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateBeeAction **   <a name="QS-Type-Capabilities-CreateAndUpdateBeeAction"></a>
The ability to create and update Bee actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateBoxAgentAction **   <a name="QS-Type-Capabilities-CreateAndUpdateBoxAgentAction"></a>
The ability to create and update Box Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateBoxKnowledgeBase **   <a name="QS-Type-Capabilities-CreateAndUpdateBoxKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateCanvaAgentAction **   <a name="QS-Type-Capabilities-CreateAndUpdateCanvaAgentAction"></a>
The ability to create and update Canva Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateCiscoWebexMeetingsAction **   <a name="QS-Type-Capabilities-CreateAndUpdateCiscoWebexMeetingsAction"></a>
The ability to create and update Cisco Webex Meetings actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateCiscoWebexVidcastAction **   <a name="QS-Type-Capabilities-CreateAndUpdateCiscoWebexVidcastAction"></a>
The ability to create and update Cisco Webex Video Messaging Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateComprehendAction **   <a name="QS-Type-Capabilities-CreateAndUpdateComprehendAction"></a>
The ability to create and update Comprehend actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateComprehendMedicalAction **   <a name="QS-Type-Capabilities-CreateAndUpdateComprehendMedicalAction"></a>
The ability to create and update Comprehend Medical actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateConfluenceAction **   <a name="QS-Type-Capabilities-CreateAndUpdateConfluenceAction"></a>
The ability to create and update Atlassian Confluence Cloud actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateConfluenceKnowledgeBase **   <a name="QS-Type-Capabilities-CreateAndUpdateConfluenceKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateDashboardEmailReports **   <a name="QS-Type-Capabilities-CreateAndUpdateDashboardEmailReports"></a>
The ability to create and update email reports.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateDatasets **   <a name="QS-Type-Capabilities-CreateAndUpdateDatasets"></a>
The ability to create and update datasets.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateDataSources **   <a name="QS-Type-Capabilities-CreateAndUpdateDataSources"></a>
The ability to create and update data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateDropboxAction **   <a name="QS-Type-Capabilities-CreateAndUpdateDropboxAction"></a>
The ability to create and update Dropbox actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateDunAndBradstreetAction **   <a name="QS-Type-Capabilities-CreateAndUpdateDunAndBradstreetAction"></a>
The ability to create and update Dun and Bradstreet actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateFactSetAction **   <a name="QS-Type-Capabilities-CreateAndUpdateFactSetAction"></a>
The ability to create and update FactSet actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateFigmaAction **   <a name="QS-Type-Capabilities-CreateAndUpdateFigmaAction"></a>
The ability to create and update Figma actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateGenericHTTPAction **   <a name="QS-Type-Capabilities-CreateAndUpdateGenericHTTPAction"></a>
The ability to create and update REST API connection actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateGithubAction **   <a name="QS-Type-Capabilities-CreateAndUpdateGithubAction"></a>
The ability to create and update GitHub actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateGmailAction **   <a name="QS-Type-Capabilities-CreateAndUpdateGmailAction"></a>
The ability to create and update Gmail actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateGongAction **   <a name="QS-Type-Capabilities-CreateAndUpdateGongAction"></a>
The ability to create and update Gong actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateGoogleAnalyticsAction **   <a name="QS-Type-Capabilities-CreateAndUpdateGoogleAnalyticsAction"></a>
The ability to create and update Google Analytics actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateGoogleCalendarAction **   <a name="QS-Type-Capabilities-CreateAndUpdateGoogleCalendarAction"></a>
The ability to create and update Google Calendar actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateGoogleChatAction **   <a name="QS-Type-Capabilities-CreateAndUpdateGoogleChatAction"></a>
The ability to create and update Google Chat actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateGoogleDocsAction **   <a name="QS-Type-Capabilities-CreateAndUpdateGoogleDocsAction"></a>
The ability to create and update Google Docs actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateGoogleDriveAction **   <a name="QS-Type-Capabilities-CreateAndUpdateGoogleDriveAction"></a>
The ability to create and update Google Drive actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateGoogleDriveKnowledgeBase **   <a name="QS-Type-Capabilities-CreateAndUpdateGoogleDriveKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateGoogleMeetAction **   <a name="QS-Type-Capabilities-CreateAndUpdateGoogleMeetAction"></a>
The ability to create and update Google Meet actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateGoogleSheetsAction **   <a name="QS-Type-Capabilities-CreateAndUpdateGoogleSheetsAction"></a>
The ability to create and update Google Sheets actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateGoogleSlidesAction **   <a name="QS-Type-Capabilities-CreateAndUpdateGoogleSlidesAction"></a>
The ability to create and update Google Slides actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateHGInsightsAction **   <a name="QS-Type-Capabilities-CreateAndUpdateHGInsightsAction"></a>
The ability to create and update HG Insights Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateHubspotAction **   <a name="QS-Type-Capabilities-CreateAndUpdateHubspotAction"></a>
The ability to create and update Hubspot actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateHuggingFaceAction **   <a name="QS-Type-Capabilities-CreateAndUpdateHuggingFaceAction"></a>
The ability to create and update HuggingFace actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateIDCKnowledgeBase **   <a name="QS-Type-Capabilities-CreateAndUpdateIDCKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateIntercomAction **   <a name="QS-Type-Capabilities-CreateAndUpdateIntercomAction"></a>
The ability to create and update Intercom actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateJiraAction **   <a name="QS-Type-Capabilities-CreateAndUpdateJiraAction"></a>
The ability to create and update Jira actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateKnowledgeBases **   <a name="QS-Type-Capabilities-CreateAndUpdateKnowledgeBases"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateLinearAction **   <a name="QS-Type-Capabilities-CreateAndUpdateLinearAction"></a>
The ability to create and update Linear actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateMCPAction **   <a name="QS-Type-Capabilities-CreateAndUpdateMCPAction"></a>
The ability to create and update Model Context Protocol actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateMondayAction **   <a name="QS-Type-Capabilities-CreateAndUpdateMondayAction"></a>
The ability to create and update Monday actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateMoodysAction **   <a name="QS-Type-Capabilities-CreateAndUpdateMoodysAction"></a>
The ability to create and update Moody's GenAI Ready Data actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateMSExchangeAction **   <a name="QS-Type-Capabilities-CreateAndUpdateMSExchangeAction"></a>
The ability to create and update Microsoft Outlook actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateMSTeamsAction **   <a name="QS-Type-Capabilities-CreateAndUpdateMSTeamsAction"></a>
The ability to create and update Microsoft Teams actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateNewRelicAction **   <a name="QS-Type-Capabilities-CreateAndUpdateNewRelicAction"></a>
The ability to create and update New Relic actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateNotionAction **   <a name="QS-Type-Capabilities-CreateAndUpdateNotionAction"></a>
The ability to create and update Notion actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateOneDriveAction **   <a name="QS-Type-Capabilities-CreateAndUpdateOneDriveAction"></a>
The ability to create and update Microsoft OneDrive actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateOneDriveKnowledgeBase **   <a name="QS-Type-Capabilities-CreateAndUpdateOneDriveKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateOneNoteAction **   <a name="QS-Type-Capabilities-CreateAndUpdateOneNoteAction"></a>
The ability to create and update Microsoft OneNote actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateOpenAPIAction **   <a name="QS-Type-Capabilities-CreateAndUpdateOpenAPIAction"></a>
The ability to create and update OpenAPI Specification actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdatePagerDutyAction **   <a name="QS-Type-Capabilities-CreateAndUpdatePagerDutyAction"></a>
The ability to create and update PagerDuty Advance actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdatePagerDutyAgentAction **   <a name="QS-Type-Capabilities-CreateAndUpdatePagerDutyAgentAction"></a>
The ability to create and update PagerDuty Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateQBusinessKnowledgeBase **   <a name="QS-Type-Capabilities-CreateAndUpdateQBusinessKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateQuickBooksAction **   <a name="QS-Type-Capabilities-CreateAndUpdateQuickBooksAction"></a>
The ability to create and update QuickBooks actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateS3KnowledgeBase **   <a name="QS-Type-Capabilities-CreateAndUpdateS3KnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateSalesforceAction **   <a name="QS-Type-Capabilities-CreateAndUpdateSalesforceAction"></a>
The ability to create and update Salesforce actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateSandPGlobalEnergyAction **   <a name="QS-Type-Capabilities-CreateAndUpdateSandPGlobalEnergyAction"></a>
The ability to create and update S&P Global Energy actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateSandPGMIAction **   <a name="QS-Type-Capabilities-CreateAndUpdateSandPGMIAction"></a>
The ability to create and update S&P Global Market Intelligence actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateSAPBillOfMaterialAction **   <a name="QS-Type-Capabilities-CreateAndUpdateSAPBillOfMaterialAction"></a>
The ability to create and update SAP Bill of Materials actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateSAPBusinessPartnerAction **   <a name="QS-Type-Capabilities-CreateAndUpdateSAPBusinessPartnerAction"></a>
The ability to create and update SAP Business Partner actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateSAPMaterialStockAction **   <a name="QS-Type-Capabilities-CreateAndUpdateSAPMaterialStockAction"></a>
The ability to create and update SAP Material Stock actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateSAPPhysicalInventoryAction **   <a name="QS-Type-Capabilities-CreateAndUpdateSAPPhysicalInventoryAction"></a>
The ability to create and update SAP Physical Inventory actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateSAPProductMasterDataAction **   <a name="QS-Type-Capabilities-CreateAndUpdateSAPProductMasterDataAction"></a>
The ability to create and update SAP Product Master actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateServiceNowAction **   <a name="QS-Type-Capabilities-CreateAndUpdateServiceNowAction"></a>
The ability to create and update ServiceNow actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateSharePointAction **   <a name="QS-Type-Capabilities-CreateAndUpdateSharePointAction"></a>
The ability to create and update Microsoft SharePoint Online actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateSharePointKnowledgeBase **   <a name="QS-Type-Capabilities-CreateAndUpdateSharePointKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateShopifyAction **   <a name="QS-Type-Capabilities-CreateAndUpdateShopifyAction"></a>
The ability to create and update Shopify actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateSlackAction **   <a name="QS-Type-Capabilities-CreateAndUpdateSlackAction"></a>
The ability to create and update Slack actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateSmartsheetAction **   <a name="QS-Type-Capabilities-CreateAndUpdateSmartsheetAction"></a>
The ability to create and update Smartsheet actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateSnowFlakeAction **   <a name="QS-Type-Capabilities-CreateAndUpdateSnowFlakeAction"></a>
The ability to create and update Snowflake Cortex Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateTextractAction **   <a name="QS-Type-Capabilities-CreateAndUpdateTextractAction"></a>
The ability to create and update Textract actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateThemes **   <a name="QS-Type-Capabilities-CreateAndUpdateThemes"></a>
The ability to export to Create and Update themes.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateThresholdAlerts **   <a name="QS-Type-Capabilities-CreateAndUpdateThresholdAlerts"></a>
The ability to create and update threshold alerts.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateVisierAgentAction **   <a name="QS-Type-Capabilities-CreateAndUpdateVisierAgentAction"></a>
The ability to create and update Visier Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateWebCrawlerKnowledgeBase **   <a name="QS-Type-Capabilities-CreateAndUpdateWebCrawlerKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateWhatsAppAction **   <a name="QS-Type-Capabilities-CreateAndUpdateWhatsAppAction"></a>
The ability to create and update WhatsApp actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateZapierAction **   <a name="QS-Type-Capabilities-CreateAndUpdateZapierAction"></a>
The ability to create and update Zapier Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateZendeskAction **   <a name="QS-Type-Capabilities-CreateAndUpdateZendeskAction"></a>
The ability to create and update Zendesk actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateZoomAction **   <a name="QS-Type-Capabilities-CreateAndUpdateZoomAction"></a>
The ability to create and update Zoom actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateZoomInfoAction **   <a name="QS-Type-Capabilities-CreateAndUpdateZoomInfoAction"></a>
The ability to create and update ZoomInfo Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAthenaDataSource **   <a name="QS-Type-Capabilities-CreateAthenaDataSource"></a>
The ability to create Amazon Athena data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAuroraDataSource **   <a name="QS-Type-Capabilities-CreateAuroraDataSource"></a>
The ability to create Amazon Aurora data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateChatAgents **   <a name="QS-Type-Capabilities-CreateChatAgents"></a>
The ability to create chat agents.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateDashboardExecutiveSummaryWithQ **   <a name="QS-Type-Capabilities-CreateDashboardExecutiveSummaryWithQ"></a>
The ability to Create Executive Summary
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateDatabricksDataSource **   <a name="QS-Type-Capabilities-CreateDatabricksDataSource"></a>
The ability to create Databricks data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateDb2DataSource **   <a name="QS-Type-Capabilities-CreateDb2DataSource"></a>
The ability to create Db2 data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateDenodoDataSource **   <a name="QS-Type-Capabilities-CreateDenodoDataSource"></a>
The ability to create Denodo data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateDocumentDbDataSource **   <a name="QS-Type-Capabilities-CreateDocumentDbDataSource"></a>
The ability to create Amazon DocumentDB data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateDremioDataSource **   <a name="QS-Type-Capabilities-CreateDremioDataSource"></a>
The ability to create Dremio data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateDynamoDbDataSource **   <a name="QS-Type-Capabilities-CreateDynamoDbDataSource"></a>
The ability to create Amazon DynamoDB data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateExasolDataSource **   <a name="QS-Type-Capabilities-CreateExasolDataSource"></a>
The ability to create Exasol data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateFileDataSource **   <a name="QS-Type-Capabilities-CreateFileDataSource"></a>
The ability to create file data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateGitHubDataSource **   <a name="QS-Type-Capabilities-CreateGitHubDataSource"></a>
The ability to create GitHub data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateGoogleAnalyticsDataSource **   <a name="QS-Type-Capabilities-CreateGoogleAnalyticsDataSource"></a>
The ability to create Google Analytics data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateGoogleBigQueryDataSource **   <a name="QS-Type-Capabilities-CreateGoogleBigQueryDataSource"></a>
The ability to create Google BigQuery data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateGoogleSheetsDataSource **   <a name="QS-Type-Capabilities-CreateGoogleSheetsDataSource"></a>
The ability to create Google Sheets data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateImpalaDataSource **   <a name="QS-Type-Capabilities-CreateImpalaDataSource"></a>
The ability to create Impala data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateJiraDataSource **   <a name="QS-Type-Capabilities-CreateJiraDataSource"></a>
The ability to create Jira data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateMariaDbDataSource **   <a name="QS-Type-Capabilities-CreateMariaDbDataSource"></a>
The ability to create MariaDB data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateMongoAtlasDataSource **   <a name="QS-Type-Capabilities-CreateMongoAtlasDataSource"></a>
The ability to create MongoDB Atlas data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateMongoDbDataSource **   <a name="QS-Type-Capabilities-CreateMongoDbDataSource"></a>
The ability to create MongoDB data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateMySqlDataSource **   <a name="QS-Type-Capabilities-CreateMySqlDataSource"></a>
The ability to create MySQL data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateOpenSearchDataSource **   <a name="QS-Type-Capabilities-CreateOpenSearchDataSource"></a>
The ability to create Amazon OpenSearch Service data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateOracleDataSource **   <a name="QS-Type-Capabilities-CreateOracleDataSource"></a>
The ability to create Oracle data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreatePayPalDataSource **   <a name="QS-Type-Capabilities-CreatePayPalDataSource"></a>
The ability to create PayPal data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreatePostgreSqlDataSource **   <a name="QS-Type-Capabilities-CreatePostgreSqlDataSource"></a>
The ability to create PostgreSQL data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreatePrestoDataSource **   <a name="QS-Type-Capabilities-CreatePrestoDataSource"></a>
The ability to create Presto data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateRadiantDataSource **   <a name="QS-Type-Capabilities-CreateRadiantDataSource"></a>
The ability to create Amazon QuickSight data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateRdsDataSource **   <a name="QS-Type-Capabilities-CreateRdsDataSource"></a>
The ability to create auto-discovered Amazon RDS data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateRedshiftAutoDiscoveredDataSource **   <a name="QS-Type-Capabilities-CreateRedshiftAutoDiscoveredDataSource"></a>
The ability to create auto-discovered Amazon Redshift data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateRedshiftManualDataSource **   <a name="QS-Type-Capabilities-CreateRedshiftManualDataSource"></a>
The ability to create manually configured Amazon Redshift data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateS3AnalyticsDataSource **   <a name="QS-Type-Capabilities-CreateS3AnalyticsDataSource"></a>
The ability to create Amazon S3 Analytics data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateS3DataSource **   <a name="QS-Type-Capabilities-CreateS3DataSource"></a>
The ability to create Amazon S3 data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateS3TablesDataSource **   <a name="QS-Type-Capabilities-CreateS3TablesDataSource"></a>
The ability to create Amazon S3 Tables data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateSalesforceDataSource **   <a name="QS-Type-Capabilities-CreateSalesforceDataSource"></a>
The ability to create Salesforce data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateSapHanaDataSource **   <a name="QS-Type-Capabilities-CreateSapHanaDataSource"></a>
The ability to create SAP HANA data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateServiceNowDataSource **   <a name="QS-Type-Capabilities-CreateServiceNowDataSource"></a>
The ability to create ServiceNow data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateSharedFolders **   <a name="QS-Type-Capabilities-CreateSharedFolders"></a>
The ability to create shared folders.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateSnowflakeDataSource **   <a name="QS-Type-Capabilities-CreateSnowflakeDataSource"></a>
The ability to create Snowflake data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateSpaces **   <a name="QS-Type-Capabilities-CreateSpaces"></a>
The ability to create spaces.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateSparkDataSource **   <a name="QS-Type-Capabilities-CreateSparkDataSource"></a>
The ability to create Spark data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateSPICEDataset **   <a name="QS-Type-Capabilities-CreateSPICEDataset"></a>
The ability to create a SPICE dataset.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateSqlServerDataSource **   <a name="QS-Type-Capabilities-CreateSqlServerDataSource"></a>
The ability to create SQL Server data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateSquareDataSource **   <a name="QS-Type-Capabilities-CreateSquareDataSource"></a>
The ability to create Square data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateStarburstDataSource **   <a name="QS-Type-Capabilities-CreateStarburstDataSource"></a>
The ability to create Starburst data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateTeradataDataSource **   <a name="QS-Type-Capabilities-CreateTeradataDataSource"></a>
The ability to create Teradata data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateTimestreamDataSource **   <a name="QS-Type-Capabilities-CreateTimestreamDataSource"></a>
The ability to create Amazon Timestream data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateTrinoDataSource **   <a name="QS-Type-Capabilities-CreateTrinoDataSource"></a>
The ability to create Trino data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateTwitterDataSource **   <a name="QS-Type-Capabilities-CreateTwitterDataSource"></a>
The ability to create Twitter data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** Dashboard **   <a name="QS-Type-Capabilities-Dashboard"></a>
The ability to perform dashboard-related actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** DatabricksDataSource **   <a name="QS-Type-Capabilities-DatabricksDataSource"></a>
The ability to create, update, and share Databricks data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** Db2DataSource **   <a name="QS-Type-Capabilities-Db2DataSource"></a>
The ability to create, update, and share Db2 data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** DenodoDataSource **   <a name="QS-Type-Capabilities-DenodoDataSource"></a>
The ability to create, update, and share Denodo data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** DocumentDbDataSource **   <a name="QS-Type-Capabilities-DocumentDbDataSource"></a>
The ability to create, update, and share Amazon DocumentDB data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** DremioDataSource **   <a name="QS-Type-Capabilities-DremioDataSource"></a>
The ability to create, update, and share Dremio data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** DropboxAction **   <a name="QS-Type-Capabilities-DropboxAction"></a>
The ability to perform actions using Dropbox connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** DunAndBradstreetAction **   <a name="QS-Type-Capabilities-DunAndBradstreetAction"></a>
The ability to perform actions using Dun and Bradstreet connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** DynamoDbDataSource **   <a name="QS-Type-Capabilities-DynamoDbDataSource"></a>
The ability to create, update, and share Amazon DynamoDB data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** EditVisualWithQ **   <a name="QS-Type-Capabilities-EditVisualWithQ"></a>
The ability to Edit Visual with AI
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ExasolDataSource **   <a name="QS-Type-Capabilities-ExasolDataSource"></a>
The ability to create, update, and share Exasol data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ExportToCsv **   <a name="QS-Type-Capabilities-ExportToCsv"></a>
The ability to export to CSV files from the UI.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ExportToCsvInScheduledReports **   <a name="QS-Type-Capabilities-ExportToCsvInScheduledReports"></a>
The ability to export to CSV files in scheduled email reports.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ExportToExcel **   <a name="QS-Type-Capabilities-ExportToExcel"></a>
The ability to export to Excel files from the UI.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ExportToExcelInScheduledReports **   <a name="QS-Type-Capabilities-ExportToExcelInScheduledReports"></a>
The ability to export to Excel files in scheduled email reports.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ExportToPdf **   <a name="QS-Type-Capabilities-ExportToPdf"></a>
The ability to export to PDF files from the UI.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ExportToPdfInScheduledReports **   <a name="QS-Type-Capabilities-ExportToPdfInScheduledReports"></a>
The ability to export to PDF files in scheduled email reports.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** Extension **   <a name="QS-Type-Capabilities-Extension"></a>
The ability to perform Extension-related actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** FactSetAction **   <a name="QS-Type-Capabilities-FactSetAction"></a>
The ability to perform actions using FactSet connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** FigmaAction **   <a name="QS-Type-Capabilities-FigmaAction"></a>
The ability to perform actions using Figma connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** FileDataSource **   <a name="QS-Type-Capabilities-FileDataSource"></a>
The ability to create, update, and share file data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** Flow **   <a name="QS-Type-Capabilities-Flow"></a>
The ability to perform flow-related actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** GenerateAnalyses **   <a name="QS-Type-Capabilities-GenerateAnalyses"></a>
The ability to generate analysis using AI
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** GenericHTTPAction **   <a name="QS-Type-Capabilities-GenericHTTPAction"></a>
The ability to perform actions using REST API connection connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** GithubAction **   <a name="QS-Type-Capabilities-GithubAction"></a>
The ability to perform actions using GitHub connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** GitHubDataSource **   <a name="QS-Type-Capabilities-GitHubDataSource"></a>
The ability to create, update, and share GitHub data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** GmailAction **   <a name="QS-Type-Capabilities-GmailAction"></a>
The ability to perform actions using Gmail connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** GongAction **   <a name="QS-Type-Capabilities-GongAction"></a>
The ability to perform actions using Gong connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** GoogleAnalyticsAction **   <a name="QS-Type-Capabilities-GoogleAnalyticsAction"></a>
The ability to perform actions using Google Analytics connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** GoogleAnalyticsDataSource **   <a name="QS-Type-Capabilities-GoogleAnalyticsDataSource"></a>
The ability to create, update, and share Google Analytics data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** GoogleBigQueryDataSource **   <a name="QS-Type-Capabilities-GoogleBigQueryDataSource"></a>
The ability to create, update, and share Google BigQuery data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** GoogleCalendarAction **   <a name="QS-Type-Capabilities-GoogleCalendarAction"></a>
The ability to perform actions using Google Calendar connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** GoogleChatAction **   <a name="QS-Type-Capabilities-GoogleChatAction"></a>
The ability to perform actions using Google Chat connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** GoogleDocsAction **   <a name="QS-Type-Capabilities-GoogleDocsAction"></a>
The ability to perform actions using Google Docs connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** GoogleDriveAction **   <a name="QS-Type-Capabilities-GoogleDriveAction"></a>
The ability to perform actions using Google Drive connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** GoogleDriveKnowledgeBase **   <a name="QS-Type-Capabilities-GoogleDriveKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** GoogleMeetAction **   <a name="QS-Type-Capabilities-GoogleMeetAction"></a>
The ability to perform actions using Google Meet connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** GoogleSheetsAction **   <a name="QS-Type-Capabilities-GoogleSheetsAction"></a>
The ability to perform actions using Google Sheets connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** GoogleSheetsDataSource **   <a name="QS-Type-Capabilities-GoogleSheetsDataSource"></a>
The ability to create, update, and share Google Sheets data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** GoogleSlidesAction **   <a name="QS-Type-Capabilities-GoogleSlidesAction"></a>
The ability to perform actions using Google Slides connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** HGInsightsAction **   <a name="QS-Type-Capabilities-HGInsightsAction"></a>
The ability to perform actions using HG Insights Agent connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** HubspotAction **   <a name="QS-Type-Capabilities-HubspotAction"></a>
The ability to perform actions using Hubspot connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** HuggingFaceAction **   <a name="QS-Type-Capabilities-HuggingFaceAction"></a>
The ability to perform actions using HuggingFace connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** IDCKnowledgeBase **   <a name="QS-Type-Capabilities-IDCKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ImpalaDataSource **   <a name="QS-Type-Capabilities-ImpalaDataSource"></a>
The ability to create, update, and share Impala data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** InboundEmailTrigger **   <a name="QS-Type-Capabilities-InboundEmailTrigger"></a>
The ability to create, view, edit, delete, and run inbound email triggers for flows and automations.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** IncludeContentInScheduledReportsEmail **   <a name="QS-Type-Capabilities-IncludeContentInScheduledReportsEmail"></a>
The ability to include content in scheduled email reports.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** IntercomAction **   <a name="QS-Type-Capabilities-IntercomAction"></a>
The ability to perform actions using Intercom connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** InvokeAppsAIInference **   <a name="QS-Type-Capabilities-InvokeAppsAIInference"></a>
The ability to add and invoke AI inference in new and existing apps.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** JiraAction **   <a name="QS-Type-Capabilities-JiraAction"></a>
The ability to perform actions using Jira connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** JiraDataSource **   <a name="QS-Type-Capabilities-JiraDataSource"></a>
The ability to create, update, and share Jira data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** KnowledgeBase **   <a name="QS-Type-Capabilities-KnowledgeBase"></a>
The ability to use knowledge bases to specify content from external applications.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** LinearAction **   <a name="QS-Type-Capabilities-LinearAction"></a>
The ability to perform actions using Linear connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ManageSharedFolders **   <a name="QS-Type-Capabilities-ManageSharedFolders"></a>
The ability to create, update, delete and view shared folders (both restricted and unrestricted), ability to add any asset to shared folders, and ability to share the folders.
 **Note:** This does *not* prevent inheriting access to assets that others share with them through folder membership.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** MariaDbDataSource **   <a name="QS-Type-Capabilities-MariaDbDataSource"></a>
The ability to create, update, and share MariaDB data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** MCPAction **   <a name="QS-Type-Capabilities-MCPAction"></a>
The ability to perform actions using Model Context Protocol connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** MondayAction **   <a name="QS-Type-Capabilities-MondayAction"></a>
The ability to perform actions using Monday connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** MongoAtlasDataSource **   <a name="QS-Type-Capabilities-MongoAtlasDataSource"></a>
The ability to create, update, and share MongoDB Atlas data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** MongoDbDataSource **   <a name="QS-Type-Capabilities-MongoDbDataSource"></a>
The ability to create, update, and share MongoDB data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** MoodysAction **   <a name="QS-Type-Capabilities-MoodysAction"></a>
The ability to perform actions using Moody's GenAI Ready Data connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** MSExchangeAction **   <a name="QS-Type-Capabilities-MSExchangeAction"></a>
The ability to perform actions using Microsoft Outlook connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** MSTeamsAction **   <a name="QS-Type-Capabilities-MSTeamsAction"></a>
The ability to perform actions using Microsoft Teams connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** MySqlDataSource **   <a name="QS-Type-Capabilities-MySqlDataSource"></a>
The ability to create, update, and share MySQL data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** NewRelicAction **   <a name="QS-Type-Capabilities-NewRelicAction"></a>
The ability to perform actions using New Relic connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** NotionAction **   <a name="QS-Type-Capabilities-NotionAction"></a>
The ability to perform actions using Notion connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** OneDriveAction **   <a name="QS-Type-Capabilities-OneDriveAction"></a>
The ability to perform actions using Microsoft OneDrive connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** OneDriveKnowledgeBase **   <a name="QS-Type-Capabilities-OneDriveKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** OneNoteAction **   <a name="QS-Type-Capabilities-OneNoteAction"></a>
The ability to perform actions using Microsoft OneNote connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** OpenAPIAction **   <a name="QS-Type-Capabilities-OpenAPIAction"></a>
The ability to perform actions using OpenAPI Specification connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** OpenSearchDataSource **   <a name="QS-Type-Capabilities-OpenSearchDataSource"></a>
The ability to create, update, and share Amazon OpenSearch Service data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** OracleDataSource **   <a name="QS-Type-Capabilities-OracleDataSource"></a>
The ability to create, update, and share Oracle data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** PagerDutyAction **   <a name="QS-Type-Capabilities-PagerDutyAction"></a>
The ability to perform actions using PagerDuty Advance connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** PagerDutyAgentAction **   <a name="QS-Type-Capabilities-PagerDutyAgentAction"></a>
The ability to perform actions using PagerDuty Agent connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** PayPalDataSource **   <a name="QS-Type-Capabilities-PayPalDataSource"></a>
The ability to create, update, and share PayPal data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** PerformFlowUiTask **   <a name="QS-Type-Capabilities-PerformFlowUiTask"></a>
The ability to use UI Agent step to perform tasks on public websites.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** PostgreSqlDataSource **   <a name="QS-Type-Capabilities-PostgreSqlDataSource"></a>
The ability to create, update, and share PostgreSQL data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** PrestoDataSource **   <a name="QS-Type-Capabilities-PrestoDataSource"></a>
The ability to create, update, and share Presto data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** PrintReports **   <a name="QS-Type-Capabilities-PrintReports"></a>
The ability to print reports.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** PublishWithoutApproval **   <a name="QS-Type-Capabilities-PublishWithoutApproval"></a>
The ability to enable approvals for flow share.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** QBusinessKnowledgeBase **   <a name="QS-Type-Capabilities-QBusinessKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** QuickBooksAction **   <a name="QS-Type-Capabilities-QuickBooksAction"></a>
The ability to perform actions using QuickBooks connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** QuickEventTrigger **   <a name="QS-Type-Capabilities-QuickEventTrigger"></a>
The ability to create, view, edit, delete, and run Quick event triggers for flows and automations.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** RadiantDataSource **   <a name="QS-Type-Capabilities-RadiantDataSource"></a>
The ability to create, update, and share Amazon QuickSight data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** RdsDataSource **   <a name="QS-Type-Capabilities-RdsDataSource"></a>
The ability to create, update, and share auto-discovered Amazon RDS data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** RedshiftAutoDiscoveredDataSource **   <a name="QS-Type-Capabilities-RedshiftAutoDiscoveredDataSource"></a>
The ability to create, update, and share auto-discovered Amazon Redshift data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** RedshiftManualDataSource **   <a name="QS-Type-Capabilities-RedshiftManualDataSource"></a>
The ability to create, update, and share manually configured Amazon Redshift data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** RenameSharedFolders **   <a name="QS-Type-Capabilities-RenameSharedFolders"></a>
The ability to rename shared folders.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** Research **   <a name="QS-Type-Capabilities-Research"></a>
The ability to perform research-related actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** S3AnalyticsDataSource **   <a name="QS-Type-Capabilities-S3AnalyticsDataSource"></a>
The ability to create, update, and share Amazon S3 Analytics data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** S3DataSource **   <a name="QS-Type-Capabilities-S3DataSource"></a>
The ability to create, update, and share Amazon S3 data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** S3KnowledgeBase **   <a name="QS-Type-Capabilities-S3KnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** S3TablesDataSource **   <a name="QS-Type-Capabilities-S3TablesDataSource"></a>
The ability to create, update, and share Amazon S3 Tables data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** SalesforceAction **   <a name="QS-Type-Capabilities-SalesforceAction"></a>
The ability to perform actions using Salesforce connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** SalesforceDataSource **   <a name="QS-Type-Capabilities-SalesforceDataSource"></a>
The ability to create, update, and share Salesforce data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** SandPGlobalEnergyAction **   <a name="QS-Type-Capabilities-SandPGlobalEnergyAction"></a>
The ability to perform actions using S&P Global Energy connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** SandPGMIAction **   <a name="QS-Type-Capabilities-SandPGMIAction"></a>
The ability to perform actions using S&P Global Market Intelligence connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** SAPBillOfMaterialAction **   <a name="QS-Type-Capabilities-SAPBillOfMaterialAction"></a>
The ability to perform actions using SAP Bill of Materials connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** SAPBusinessPartnerAction **   <a name="QS-Type-Capabilities-SAPBusinessPartnerAction"></a>
The ability to perform actions using SAP Business Partner connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** SapHanaDataSource **   <a name="QS-Type-Capabilities-SapHanaDataSource"></a>
The ability to create, update, and share SAP HANA data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** SAPMaterialStockAction **   <a name="QS-Type-Capabilities-SAPMaterialStockAction"></a>
The ability to perform actions using SAP Material Stock connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** SAPPhysicalInventoryAction **   <a name="QS-Type-Capabilities-SAPPhysicalInventoryAction"></a>
The ability to perform actions using SAP Physical Inventory connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** SAPProductMasterDataAction **   <a name="QS-Type-Capabilities-SAPProductMasterDataAction"></a>
The ability to perform actions using SAP Product Master connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** Scenario **   <a name="QS-Type-Capabilities-Scenario"></a>
The ability to perform Scenario-related actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ScheduleTrigger **   <a name="QS-Type-Capabilities-ScheduleTrigger"></a>
The ability to create, view, edit, delete, and run schedule triggers for flows and automations.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** SelfUpgradeUserRole **   <a name="QS-Type-Capabilities-SelfUpgradeUserRole"></a>
The ability to enable users to upgrade their user role.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ServiceNowAction **   <a name="QS-Type-Capabilities-ServiceNowAction"></a>
The ability to perform actions using ServiceNow connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ServiceNowDataSource **   <a name="QS-Type-Capabilities-ServiceNowDataSource"></a>
The ability to create, update, and share ServiceNow data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareAdobeAction **   <a name="QS-Type-Capabilities-ShareAdobeAction"></a>
The ability to share Adobe Marketing Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareAdobeAnalyticsDataSource **   <a name="QS-Type-Capabilities-ShareAdobeAnalyticsDataSource"></a>
The ability to share Adobe Analytics data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareAirtableAction **   <a name="QS-Type-Capabilities-ShareAirtableAction"></a>
The ability to share Airtable actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareAmazonBedrockARSAction **   <a name="QS-Type-Capabilities-ShareAmazonBedrockARSAction"></a>
The ability to share Bedrock Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareAmazonBedrockFSAction **   <a name="QS-Type-Capabilities-ShareAmazonBedrockFSAction"></a>
The ability to share Bedrock Runtime actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareAmazonBedrockKRSAction **   <a name="QS-Type-Capabilities-ShareAmazonBedrockKRSAction"></a>
The ability to share Bedrock Data Automation Runtime actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareAmazonSThreeAction **   <a name="QS-Type-Capabilities-ShareAmazonSThreeAction"></a>
The ability to share Amazon S3 actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareAnalyses **   <a name="QS-Type-Capabilities-ShareAnalyses"></a>
The ability to share analyses.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareApps **   <a name="QS-Type-Capabilities-ShareApps"></a>
The ability to share apps with other users.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareAsanaAction **   <a name="QS-Type-Capabilities-ShareAsanaAction"></a>
The ability to share Asana actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareAthenaDataSource **   <a name="QS-Type-Capabilities-ShareAthenaDataSource"></a>
The ability to share Amazon Athena data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareAuroraDataSource **   <a name="QS-Type-Capabilities-ShareAuroraDataSource"></a>
The ability to share Amazon Aurora data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareBambooHRAction **   <a name="QS-Type-Capabilities-ShareBambooHRAction"></a>
The ability to share BambooHR actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareBedrockManagedKnowledgeBase **   <a name="QS-Type-Capabilities-ShareBedrockManagedKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareBeeAction **   <a name="QS-Type-Capabilities-ShareBeeAction"></a>
The ability to share Bee actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareBoxAgentAction **   <a name="QS-Type-Capabilities-ShareBoxAgentAction"></a>
The ability to share Box Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareBoxKnowledgeBase **   <a name="QS-Type-Capabilities-ShareBoxKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareCanvaAgentAction **   <a name="QS-Type-Capabilities-ShareCanvaAgentAction"></a>
The ability to share Canva Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareChatAgents **   <a name="QS-Type-Capabilities-ShareChatAgents"></a>
The ability to share chat agents with other users and groups.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareCiscoWebexMeetingsAction **   <a name="QS-Type-Capabilities-ShareCiscoWebexMeetingsAction"></a>
The ability to share Cisco Webex Meetings actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareCiscoWebexVidcastAction **   <a name="QS-Type-Capabilities-ShareCiscoWebexVidcastAction"></a>
The ability to share Cisco Webex Video Messaging Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareComprehendAction **   <a name="QS-Type-Capabilities-ShareComprehendAction"></a>
The ability to share Comprehend actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareComprehendMedicalAction **   <a name="QS-Type-Capabilities-ShareComprehendMedicalAction"></a>
The ability to share Comprehend Medical actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareConfluenceAction **   <a name="QS-Type-Capabilities-ShareConfluenceAction"></a>
The ability to share Atlassian Confluence Cloud actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareConfluenceKnowledgeBase **   <a name="QS-Type-Capabilities-ShareConfluenceKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareDashboards **   <a name="QS-Type-Capabilities-ShareDashboards"></a>
The ability to share dashboards.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareDatabricksDataSource **   <a name="QS-Type-Capabilities-ShareDatabricksDataSource"></a>
The ability to share Databricks data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareDatasets **   <a name="QS-Type-Capabilities-ShareDatasets"></a>
The ability to share datasets.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareDataSources **   <a name="QS-Type-Capabilities-ShareDataSources"></a>
The ability to share data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareDb2DataSource **   <a name="QS-Type-Capabilities-ShareDb2DataSource"></a>
The ability to share Db2 data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareDenodoDataSource **   <a name="QS-Type-Capabilities-ShareDenodoDataSource"></a>
The ability to share Denodo data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareDocumentDbDataSource **   <a name="QS-Type-Capabilities-ShareDocumentDbDataSource"></a>
The ability to share Amazon DocumentDB data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareDremioDataSource **   <a name="QS-Type-Capabilities-ShareDremioDataSource"></a>
The ability to share Dremio data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareDropboxAction **   <a name="QS-Type-Capabilities-ShareDropboxAction"></a>
The ability to share Dropbox actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareDunAndBradstreetAction **   <a name="QS-Type-Capabilities-ShareDunAndBradstreetAction"></a>
The ability to share Dun and Bradstreet actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareDynamoDbDataSource **   <a name="QS-Type-Capabilities-ShareDynamoDbDataSource"></a>
The ability to share Amazon DynamoDB data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareExasolDataSource **   <a name="QS-Type-Capabilities-ShareExasolDataSource"></a>
The ability to share Exasol data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareFactSetAction **   <a name="QS-Type-Capabilities-ShareFactSetAction"></a>
The ability to share FactSet actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareFigmaAction **   <a name="QS-Type-Capabilities-ShareFigmaAction"></a>
The ability to share Figma actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareFileDataSource **   <a name="QS-Type-Capabilities-ShareFileDataSource"></a>
The ability to share file data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareGenericHTTPAction **   <a name="QS-Type-Capabilities-ShareGenericHTTPAction"></a>
The ability to share REST API connection actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareGithubAction **   <a name="QS-Type-Capabilities-ShareGithubAction"></a>
The ability to share GitHub actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareGitHubDataSource **   <a name="QS-Type-Capabilities-ShareGitHubDataSource"></a>
The ability to share GitHub data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareGmailAction **   <a name="QS-Type-Capabilities-ShareGmailAction"></a>
The ability to share Gmail actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareGongAction **   <a name="QS-Type-Capabilities-ShareGongAction"></a>
The ability to share Gong actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareGoogleAnalyticsAction **   <a name="QS-Type-Capabilities-ShareGoogleAnalyticsAction"></a>
The ability to share Google Analytics actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareGoogleAnalyticsDataSource **   <a name="QS-Type-Capabilities-ShareGoogleAnalyticsDataSource"></a>
The ability to share Google Analytics data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareGoogleBigQueryDataSource **   <a name="QS-Type-Capabilities-ShareGoogleBigQueryDataSource"></a>
The ability to share Google BigQuery data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareGoogleCalendarAction **   <a name="QS-Type-Capabilities-ShareGoogleCalendarAction"></a>
The ability to share Google Calendar actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareGoogleChatAction **   <a name="QS-Type-Capabilities-ShareGoogleChatAction"></a>
The ability to share Google Chat actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareGoogleDocsAction **   <a name="QS-Type-Capabilities-ShareGoogleDocsAction"></a>
The ability to share Google Docs actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareGoogleDriveAction **   <a name="QS-Type-Capabilities-ShareGoogleDriveAction"></a>
The ability to share Google Drive actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareGoogleDriveKnowledgeBase **   <a name="QS-Type-Capabilities-ShareGoogleDriveKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareGoogleMeetAction **   <a name="QS-Type-Capabilities-ShareGoogleMeetAction"></a>
The ability to share Google Meet actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareGoogleSheetsAction **   <a name="QS-Type-Capabilities-ShareGoogleSheetsAction"></a>
The ability to share Google Sheets actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareGoogleSheetsDataSource **   <a name="QS-Type-Capabilities-ShareGoogleSheetsDataSource"></a>
The ability to share Google Sheets data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareGoogleSlidesAction **   <a name="QS-Type-Capabilities-ShareGoogleSlidesAction"></a>
The ability to share Google Slides actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareHGInsightsAction **   <a name="QS-Type-Capabilities-ShareHGInsightsAction"></a>
The ability to share HG Insights Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareHubspotAction **   <a name="QS-Type-Capabilities-ShareHubspotAction"></a>
The ability to share Hubspot actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareHuggingFaceAction **   <a name="QS-Type-Capabilities-ShareHuggingFaceAction"></a>
The ability to share HuggingFace actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareIDCKnowledgeBase **   <a name="QS-Type-Capabilities-ShareIDCKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareImpalaDataSource **   <a name="QS-Type-Capabilities-ShareImpalaDataSource"></a>
The ability to share Impala data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareIntercomAction **   <a name="QS-Type-Capabilities-ShareIntercomAction"></a>
The ability to share Intercom actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareJiraAction **   <a name="QS-Type-Capabilities-ShareJiraAction"></a>
The ability to share Jira actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareJiraDataSource **   <a name="QS-Type-Capabilities-ShareJiraDataSource"></a>
The ability to share Jira data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareKnowledgeBases **   <a name="QS-Type-Capabilities-ShareKnowledgeBases"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareLinearAction **   <a name="QS-Type-Capabilities-ShareLinearAction"></a>
The ability to share Linear actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareMariaDbDataSource **   <a name="QS-Type-Capabilities-ShareMariaDbDataSource"></a>
The ability to share MariaDB data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareMCPAction **   <a name="QS-Type-Capabilities-ShareMCPAction"></a>
The ability to share Model Context Protocol actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareMondayAction **   <a name="QS-Type-Capabilities-ShareMondayAction"></a>
The ability to share Monday actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareMongoAtlasDataSource **   <a name="QS-Type-Capabilities-ShareMongoAtlasDataSource"></a>
The ability to share MongoDB Atlas data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareMongoDbDataSource **   <a name="QS-Type-Capabilities-ShareMongoDbDataSource"></a>
The ability to share MongoDB data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareMoodysAction **   <a name="QS-Type-Capabilities-ShareMoodysAction"></a>
The ability to share Moody's GenAI Ready Data actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareMSExchangeAction **   <a name="QS-Type-Capabilities-ShareMSExchangeAction"></a>
The ability to share Microsoft Outlook actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareMSTeamsAction **   <a name="QS-Type-Capabilities-ShareMSTeamsAction"></a>
The ability to share Microsoft Teams actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareMySqlDataSource **   <a name="QS-Type-Capabilities-ShareMySqlDataSource"></a>
The ability to share MySQL data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareNewRelicAction **   <a name="QS-Type-Capabilities-ShareNewRelicAction"></a>
The ability to share New Relic actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareNotionAction **   <a name="QS-Type-Capabilities-ShareNotionAction"></a>
The ability to share Notion actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareOneDriveAction **   <a name="QS-Type-Capabilities-ShareOneDriveAction"></a>
The ability to share Microsoft OneDrive actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareOneDriveKnowledgeBase **   <a name="QS-Type-Capabilities-ShareOneDriveKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareOneNoteAction **   <a name="QS-Type-Capabilities-ShareOneNoteAction"></a>
The ability to share Microsoft OneNote actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareOpenAPIAction **   <a name="QS-Type-Capabilities-ShareOpenAPIAction"></a>
The ability to share OpenAPI Specification actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareOpenSearchDataSource **   <a name="QS-Type-Capabilities-ShareOpenSearchDataSource"></a>
The ability to share Amazon OpenSearch Service data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareOracleDataSource **   <a name="QS-Type-Capabilities-ShareOracleDataSource"></a>
The ability to share Oracle data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** SharePagerDutyAction **   <a name="QS-Type-Capabilities-SharePagerDutyAction"></a>
The ability to share PagerDuty Advance actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** SharePagerDutyAgentAction **   <a name="QS-Type-Capabilities-SharePagerDutyAgentAction"></a>
The ability to share PagerDuty Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** SharePayPalDataSource **   <a name="QS-Type-Capabilities-SharePayPalDataSource"></a>
The ability to share PayPal data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** SharePointAction **   <a name="QS-Type-Capabilities-SharePointAction"></a>
The ability to perform actions using Microsoft SharePoint Online connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** SharePointKnowledgeBase **   <a name="QS-Type-Capabilities-SharePointKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** SharePostgreSqlDataSource **   <a name="QS-Type-Capabilities-SharePostgreSqlDataSource"></a>
The ability to share PostgreSQL data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** SharePrestoDataSource **   <a name="QS-Type-Capabilities-SharePrestoDataSource"></a>
The ability to share Presto data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareQBusinessKnowledgeBase **   <a name="QS-Type-Capabilities-ShareQBusinessKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareQuickBooksAction **   <a name="QS-Type-Capabilities-ShareQuickBooksAction"></a>
The ability to share QuickBooks actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareRadiantDataSource **   <a name="QS-Type-Capabilities-ShareRadiantDataSource"></a>
The ability to share Amazon QuickSight data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareRdsDataSource **   <a name="QS-Type-Capabilities-ShareRdsDataSource"></a>
The ability to share auto-discovered Amazon RDS data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareRedshiftAutoDiscoveredDataSource **   <a name="QS-Type-Capabilities-ShareRedshiftAutoDiscoveredDataSource"></a>
The ability to share auto-discovered Amazon Redshift data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareRedshiftManualDataSource **   <a name="QS-Type-Capabilities-ShareRedshiftManualDataSource"></a>
The ability to share manually configured Amazon Redshift data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareS3AnalyticsDataSource **   <a name="QS-Type-Capabilities-ShareS3AnalyticsDataSource"></a>
The ability to share Amazon S3 Analytics data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareS3DataSource **   <a name="QS-Type-Capabilities-ShareS3DataSource"></a>
The ability to share Amazon S3 data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareS3KnowledgeBase **   <a name="QS-Type-Capabilities-ShareS3KnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareS3TablesDataSource **   <a name="QS-Type-Capabilities-ShareS3TablesDataSource"></a>
The ability to share Amazon S3 Tables data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareSalesforceAction **   <a name="QS-Type-Capabilities-ShareSalesforceAction"></a>
The ability to share Salesforce actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareSalesforceDataSource **   <a name="QS-Type-Capabilities-ShareSalesforceDataSource"></a>
The ability to share Salesforce data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareSandPGlobalEnergyAction **   <a name="QS-Type-Capabilities-ShareSandPGlobalEnergyAction"></a>
The ability to share S&P Global Energy actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareSandPGMIAction **   <a name="QS-Type-Capabilities-ShareSandPGMIAction"></a>
The ability to share S&P Global Market Intelligence actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareSAPBillOfMaterialAction **   <a name="QS-Type-Capabilities-ShareSAPBillOfMaterialAction"></a>
The ability to share SAP Bill of Materials actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareSAPBusinessPartnerAction **   <a name="QS-Type-Capabilities-ShareSAPBusinessPartnerAction"></a>
The ability to share SAP Business Partner actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareSapHanaDataSource **   <a name="QS-Type-Capabilities-ShareSapHanaDataSource"></a>
The ability to share SAP HANA data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareSAPMaterialStockAction **   <a name="QS-Type-Capabilities-ShareSAPMaterialStockAction"></a>
The ability to share SAP Material Stock actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareSAPPhysicalInventoryAction **   <a name="QS-Type-Capabilities-ShareSAPPhysicalInventoryAction"></a>
The ability to share SAP Physical Inventory actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareSAPProductMasterDataAction **   <a name="QS-Type-Capabilities-ShareSAPProductMasterDataAction"></a>
The ability to share SAP Product Master actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareServiceNowAction **   <a name="QS-Type-Capabilities-ShareServiceNowAction"></a>
The ability to share ServiceNow actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareServiceNowDataSource **   <a name="QS-Type-Capabilities-ShareServiceNowDataSource"></a>
The ability to share ServiceNow data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareSharePointAction **   <a name="QS-Type-Capabilities-ShareSharePointAction"></a>
The ability to share Microsoft SharePoint Online actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareSharePointKnowledgeBase **   <a name="QS-Type-Capabilities-ShareSharePointKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareShopifyAction **   <a name="QS-Type-Capabilities-ShareShopifyAction"></a>
The ability to share Shopify actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareSlackAction **   <a name="QS-Type-Capabilities-ShareSlackAction"></a>
The ability to share Slack actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareSmartsheetAction **   <a name="QS-Type-Capabilities-ShareSmartsheetAction"></a>
The ability to share Smartsheet actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareSnowFlakeAction **   <a name="QS-Type-Capabilities-ShareSnowFlakeAction"></a>
The ability to share Snowflake Cortex Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareSnowflakeDataSource **   <a name="QS-Type-Capabilities-ShareSnowflakeDataSource"></a>
The ability to share Snowflake data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareSpaces **   <a name="QS-Type-Capabilities-ShareSpaces"></a>
The ability to share spaces with other users and groups.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareSparkDataSource **   <a name="QS-Type-Capabilities-ShareSparkDataSource"></a>
The ability to share Spark data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareSqlServerDataSource **   <a name="QS-Type-Capabilities-ShareSqlServerDataSource"></a>
The ability to share SQL Server data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareSquareDataSource **   <a name="QS-Type-Capabilities-ShareSquareDataSource"></a>
The ability to share Square data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareStarburstDataSource **   <a name="QS-Type-Capabilities-ShareStarburstDataSource"></a>
The ability to share Starburst data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareTeradataDataSource **   <a name="QS-Type-Capabilities-ShareTeradataDataSource"></a>
The ability to share Teradata data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareTextractAction **   <a name="QS-Type-Capabilities-ShareTextractAction"></a>
The ability to share Textract actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareTimestreamDataSource **   <a name="QS-Type-Capabilities-ShareTimestreamDataSource"></a>
The ability to share Amazon Timestream data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareTrinoDataSource **   <a name="QS-Type-Capabilities-ShareTrinoDataSource"></a>
The ability to share Trino data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareTwitterDataSource **   <a name="QS-Type-Capabilities-ShareTwitterDataSource"></a>
The ability to share Twitter data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareVisierAgentAction **   <a name="QS-Type-Capabilities-ShareVisierAgentAction"></a>
The ability to share Visier Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareWebCrawlerKnowledgeBase **   <a name="QS-Type-Capabilities-ShareWebCrawlerKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareWhatsAppAction **   <a name="QS-Type-Capabilities-ShareWhatsAppAction"></a>
The ability to share WhatsApp actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareZapierAction **   <a name="QS-Type-Capabilities-ShareZapierAction"></a>
The ability to share Zapier Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareZendeskAction **   <a name="QS-Type-Capabilities-ShareZendeskAction"></a>
The ability to share Zendesk actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareZoomAction **   <a name="QS-Type-Capabilities-ShareZoomAction"></a>
The ability to share Zoom actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareZoomInfoAction **   <a name="QS-Type-Capabilities-ShareZoomInfoAction"></a>
The ability to share ZoomInfo Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShopifyAction **   <a name="QS-Type-Capabilities-ShopifyAction"></a>
The ability to perform actions using Shopify connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** SlackAction **   <a name="QS-Type-Capabilities-SlackAction"></a>
The ability to perform actions using Slack connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** SmartsheetAction **   <a name="QS-Type-Capabilities-SmartsheetAction"></a>
The ability to perform actions using Smartsheet connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** SnowFlakeAction **   <a name="QS-Type-Capabilities-SnowFlakeAction"></a>
The ability to perform actions using Snowflake Cortex Agent connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** SnowflakeDataSource **   <a name="QS-Type-Capabilities-SnowflakeDataSource"></a>
The ability to create, update, and share Snowflake data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** Space **   <a name="QS-Type-Capabilities-Space"></a>
The ability to perform space-related actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** SparkDataSource **   <a name="QS-Type-Capabilities-SparkDataSource"></a>
The ability to create, update, and share Spark data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** SqlServerDataSource **   <a name="QS-Type-Capabilities-SqlServerDataSource"></a>
The ability to create, update, and share SQL Server data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** SquareDataSource **   <a name="QS-Type-Capabilities-SquareDataSource"></a>
The ability to create, update, and share Square data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** StarburstDataSource **   <a name="QS-Type-Capabilities-StarburstDataSource"></a>
The ability to create, update, and share Starburst data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** Story **   <a name="QS-Type-Capabilities-Story"></a>
The ability to perform Story-related actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** SubscribeDashboardEmailReports **   <a name="QS-Type-Capabilities-SubscribeDashboardEmailReports"></a>
The ability to subscribe to email reports.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** TeradataDataSource **   <a name="QS-Type-Capabilities-TeradataDataSource"></a>
The ability to create, update, and share Teradata data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** TextractAction **   <a name="QS-Type-Capabilities-TextractAction"></a>
The ability to perform actions using Textract connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** TimestreamDataSource **   <a name="QS-Type-Capabilities-TimestreamDataSource"></a>
The ability to create, update, and share Amazon Timestream data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** Topic **   <a name="QS-Type-Capabilities-Topic"></a>
The ability to perform Topic-related actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** Trigger **   <a name="QS-Type-Capabilities-Trigger"></a>
The ability to manage trigger-related settings for flows and automations.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** TrinoDataSource **   <a name="QS-Type-Capabilities-TrinoDataSource"></a>
The ability to create, update, and share Trino data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** TwitterDataSource **   <a name="QS-Type-Capabilities-TwitterDataSource"></a>
The ability to create, update, and share Twitter data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateAdobeAnalyticsDataSource **   <a name="QS-Type-Capabilities-UpdateAdobeAnalyticsDataSource"></a>
The ability to update Adobe Analytics data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateAthenaDataSource **   <a name="QS-Type-Capabilities-UpdateAthenaDataSource"></a>
The ability to update Amazon Athena data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateAuroraDataSource **   <a name="QS-Type-Capabilities-UpdateAuroraDataSource"></a>
The ability to update Amazon Aurora data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateDatabricksDataSource **   <a name="QS-Type-Capabilities-UpdateDatabricksDataSource"></a>
The ability to update Databricks data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateDb2DataSource **   <a name="QS-Type-Capabilities-UpdateDb2DataSource"></a>
The ability to update Db2 data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateDenodoDataSource **   <a name="QS-Type-Capabilities-UpdateDenodoDataSource"></a>
The ability to update Denodo data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateDocumentDbDataSource **   <a name="QS-Type-Capabilities-UpdateDocumentDbDataSource"></a>
The ability to update Amazon DocumentDB data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateDremioDataSource **   <a name="QS-Type-Capabilities-UpdateDremioDataSource"></a>
The ability to update Dremio data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateDynamoDbDataSource **   <a name="QS-Type-Capabilities-UpdateDynamoDbDataSource"></a>
The ability to update Amazon DynamoDB data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateExasolDataSource **   <a name="QS-Type-Capabilities-UpdateExasolDataSource"></a>
The ability to update Exasol data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateFileDataSource **   <a name="QS-Type-Capabilities-UpdateFileDataSource"></a>
The ability to update file data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateGitHubDataSource **   <a name="QS-Type-Capabilities-UpdateGitHubDataSource"></a>
The ability to update GitHub data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateGoogleAnalyticsDataSource **   <a name="QS-Type-Capabilities-UpdateGoogleAnalyticsDataSource"></a>
The ability to update Google Analytics data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateGoogleBigQueryDataSource **   <a name="QS-Type-Capabilities-UpdateGoogleBigQueryDataSource"></a>
The ability to update Google BigQuery data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateGoogleSheetsDataSource **   <a name="QS-Type-Capabilities-UpdateGoogleSheetsDataSource"></a>
The ability to update Google Sheets data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateImpalaDataSource **   <a name="QS-Type-Capabilities-UpdateImpalaDataSource"></a>
The ability to update Impala data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateJiraDataSource **   <a name="QS-Type-Capabilities-UpdateJiraDataSource"></a>
The ability to update Jira data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateMariaDbDataSource **   <a name="QS-Type-Capabilities-UpdateMariaDbDataSource"></a>
The ability to update MariaDB data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateMongoAtlasDataSource **   <a name="QS-Type-Capabilities-UpdateMongoAtlasDataSource"></a>
The ability to update MongoDB Atlas data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateMongoDbDataSource **   <a name="QS-Type-Capabilities-UpdateMongoDbDataSource"></a>
The ability to update MongoDB data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateMySqlDataSource **   <a name="QS-Type-Capabilities-UpdateMySqlDataSource"></a>
The ability to update MySQL data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateOpenSearchDataSource **   <a name="QS-Type-Capabilities-UpdateOpenSearchDataSource"></a>
The ability to update Amazon OpenSearch Service data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateOracleDataSource **   <a name="QS-Type-Capabilities-UpdateOracleDataSource"></a>
The ability to update Oracle data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdatePayPalDataSource **   <a name="QS-Type-Capabilities-UpdatePayPalDataSource"></a>
The ability to update PayPal data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdatePostgreSqlDataSource **   <a name="QS-Type-Capabilities-UpdatePostgreSqlDataSource"></a>
The ability to update PostgreSQL data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdatePrestoDataSource **   <a name="QS-Type-Capabilities-UpdatePrestoDataSource"></a>
The ability to update Presto data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateRadiantDataSource **   <a name="QS-Type-Capabilities-UpdateRadiantDataSource"></a>
The ability to update Amazon QuickSight data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateRdsDataSource **   <a name="QS-Type-Capabilities-UpdateRdsDataSource"></a>
The ability to update auto-discovered Amazon RDS data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateRedshiftAutoDiscoveredDataSource **   <a name="QS-Type-Capabilities-UpdateRedshiftAutoDiscoveredDataSource"></a>
The ability to update auto-discovered Amazon Redshift data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateRedshiftManualDataSource **   <a name="QS-Type-Capabilities-UpdateRedshiftManualDataSource"></a>
The ability to update manually configured Amazon Redshift data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateS3AnalyticsDataSource **   <a name="QS-Type-Capabilities-UpdateS3AnalyticsDataSource"></a>
The ability to update Amazon S3 Analytics data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateS3DataSource **   <a name="QS-Type-Capabilities-UpdateS3DataSource"></a>
The ability to update Amazon S3 data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateS3TablesDataSource **   <a name="QS-Type-Capabilities-UpdateS3TablesDataSource"></a>
The ability to update Amazon S3 Tables data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateSalesforceDataSource **   <a name="QS-Type-Capabilities-UpdateSalesforceDataSource"></a>
The ability to update Salesforce data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateSapHanaDataSource **   <a name="QS-Type-Capabilities-UpdateSapHanaDataSource"></a>
The ability to update SAP HANA data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateServiceNowDataSource **   <a name="QS-Type-Capabilities-UpdateServiceNowDataSource"></a>
The ability to update ServiceNow data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateSnowflakeDataSource **   <a name="QS-Type-Capabilities-UpdateSnowflakeDataSource"></a>
The ability to update Snowflake data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateSparkDataSource **   <a name="QS-Type-Capabilities-UpdateSparkDataSource"></a>
The ability to update Spark data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateSqlServerDataSource **   <a name="QS-Type-Capabilities-UpdateSqlServerDataSource"></a>
The ability to update SQL Server data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateSquareDataSource **   <a name="QS-Type-Capabilities-UpdateSquareDataSource"></a>
The ability to update Square data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateStarburstDataSource **   <a name="QS-Type-Capabilities-UpdateStarburstDataSource"></a>
The ability to update Starburst data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateTeradataDataSource **   <a name="QS-Type-Capabilities-UpdateTeradataDataSource"></a>
The ability to update Teradata data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateTimestreamDataSource **   <a name="QS-Type-Capabilities-UpdateTimestreamDataSource"></a>
The ability to update Amazon Timestream data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateTrinoDataSource **   <a name="QS-Type-Capabilities-UpdateTrinoDataSource"></a>
The ability to update Trino data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UpdateTwitterDataSource **   <a name="QS-Type-Capabilities-UpdateTwitterDataSource"></a>
The ability to update Twitter data sources.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseAdobeAction **   <a name="QS-Type-Capabilities-UseAdobeAction"></a>
The ability to use Adobe Marketing Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseAgentWebSearch **   <a name="QS-Type-Capabilities-UseAgentWebSearch"></a>
The ability to use internet to enhance results in Chat Agents, Flows, and Quick Research. Web search queries will be processed securely in an AWS region `us-east-1`.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseAirtableAction **   <a name="QS-Type-Capabilities-UseAirtableAction"></a>
The ability to use Airtable actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseAmazonBedrockARSAction **   <a name="QS-Type-Capabilities-UseAmazonBedrockARSAction"></a>
The ability to use Bedrock Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseAmazonBedrockFSAction **   <a name="QS-Type-Capabilities-UseAmazonBedrockFSAction"></a>
The ability to use Bedrock Runtime actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseAmazonBedrockKRSAction **   <a name="QS-Type-Capabilities-UseAmazonBedrockKRSAction"></a>
The ability to use Bedrock Data Automation Runtime actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseAmazonSThreeAction **   <a name="QS-Type-Capabilities-UseAmazonSThreeAction"></a>
The ability to use Amazon S3 actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseAsanaAction **   <a name="QS-Type-Capabilities-UseAsanaAction"></a>
The ability to use Asana actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseBambooHRAction **   <a name="QS-Type-Capabilities-UseBambooHRAction"></a>
The ability to use BambooHR actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseBedrockManagedKnowledgeBase **   <a name="QS-Type-Capabilities-UseBedrockManagedKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseBedrockModels **   <a name="QS-Type-Capabilities-UseBedrockModels"></a>
The ability to use Bedrock models for general knowledge step in flows.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseBeeAction **   <a name="QS-Type-Capabilities-UseBeeAction"></a>
The ability to use Bee actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseBoxAgentAction **   <a name="QS-Type-Capabilities-UseBoxAgentAction"></a>
The ability to use Box Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseBoxKnowledgeBase **   <a name="QS-Type-Capabilities-UseBoxKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseBrowserExtension **   <a name="QS-Type-Capabilities-UseBrowserExtension"></a>
The ability to use Amazon Quick through the browser extension for Chrome, Firefox, and Edge.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseCanvaAgentAction **   <a name="QS-Type-Capabilities-UseCanvaAgentAction"></a>
The ability to use Canva Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseCiscoWebexMeetingsAction **   <a name="QS-Type-Capabilities-UseCiscoWebexMeetingsAction"></a>
The ability to use Cisco Webex Meetings actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseCiscoWebexVidcastAction **   <a name="QS-Type-Capabilities-UseCiscoWebexVidcastAction"></a>
The ability to use Cisco Webex Video Messaging Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseComprehendAction **   <a name="QS-Type-Capabilities-UseComprehendAction"></a>
The ability to use Comprehend actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseComprehendMedicalAction **   <a name="QS-Type-Capabilities-UseComprehendMedicalAction"></a>
The ability to use Comprehend Medical actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseConfluenceAction **   <a name="QS-Type-Capabilities-UseConfluenceAction"></a>
The ability to use Atlassian Confluence Cloud actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseConfluenceKnowledgeBase **   <a name="QS-Type-Capabilities-UseConfluenceKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseDropboxAction **   <a name="QS-Type-Capabilities-UseDropboxAction"></a>
The ability to use Dropbox actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseDunAndBradstreetAction **   <a name="QS-Type-Capabilities-UseDunAndBradstreetAction"></a>
The ability to use Dun and Bradstreet actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseExcelAddInExtension **   <a name="QS-Type-Capabilities-UseExcelAddInExtension"></a>
The ability to use Amazon Quick through the Microsoft Excel add-in.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseFactSetAction **   <a name="QS-Type-Capabilities-UseFactSetAction"></a>
The ability to use FactSet actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseFigmaAction **   <a name="QS-Type-Capabilities-UseFigmaAction"></a>
The ability to use Figma actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseGenericHTTPAction **   <a name="QS-Type-Capabilities-UseGenericHTTPAction"></a>
The ability to use REST API connection actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseGithubAction **   <a name="QS-Type-Capabilities-UseGithubAction"></a>
The ability to use GitHub actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseGmailAction **   <a name="QS-Type-Capabilities-UseGmailAction"></a>
The ability to use Gmail actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseGongAction **   <a name="QS-Type-Capabilities-UseGongAction"></a>
The ability to use Gong actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseGoogleAnalyticsAction **   <a name="QS-Type-Capabilities-UseGoogleAnalyticsAction"></a>
The ability to use Google Analytics actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseGoogleCalendarAction **   <a name="QS-Type-Capabilities-UseGoogleCalendarAction"></a>
The ability to use Google Calendar actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseGoogleChatAction **   <a name="QS-Type-Capabilities-UseGoogleChatAction"></a>
The ability to use Google Chat actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseGoogleDocsAction **   <a name="QS-Type-Capabilities-UseGoogleDocsAction"></a>
The ability to use Google Docs actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseGoogleDriveAction **   <a name="QS-Type-Capabilities-UseGoogleDriveAction"></a>
The ability to use Google Drive actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseGoogleDriveKnowledgeBase **   <a name="QS-Type-Capabilities-UseGoogleDriveKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseGoogleMeetAction **   <a name="QS-Type-Capabilities-UseGoogleMeetAction"></a>
The ability to use Google Meet actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseGoogleSheetsAction **   <a name="QS-Type-Capabilities-UseGoogleSheetsAction"></a>
The ability to use Google Sheets actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseGoogleSlidesAction **   <a name="QS-Type-Capabilities-UseGoogleSlidesAction"></a>
The ability to use Google Slides actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseHGInsightsAction **   <a name="QS-Type-Capabilities-UseHGInsightsAction"></a>
The ability to use HG Insights Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseHubspotAction **   <a name="QS-Type-Capabilities-UseHubspotAction"></a>
The ability to use Hubspot actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseHuggingFaceAction **   <a name="QS-Type-Capabilities-UseHuggingFaceAction"></a>
The ability to use HuggingFace actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseIDCKnowledgeBase **   <a name="QS-Type-Capabilities-UseIDCKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseIntercomAction **   <a name="QS-Type-Capabilities-UseIntercomAction"></a>
The ability to use Intercom actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseJiraAction **   <a name="QS-Type-Capabilities-UseJiraAction"></a>
The ability to use Jira actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseLinearAction **   <a name="QS-Type-Capabilities-UseLinearAction"></a>
The ability to use Linear actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseMCPAction **   <a name="QS-Type-Capabilities-UseMCPAction"></a>
The ability to use Model Context Protocol actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseMondayAction **   <a name="QS-Type-Capabilities-UseMondayAction"></a>
The ability to use Monday actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseMoodysAction **   <a name="QS-Type-Capabilities-UseMoodysAction"></a>
The ability to use Moody's GenAI Ready Data actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseMSExchangeAction **   <a name="QS-Type-Capabilities-UseMSExchangeAction"></a>
The ability to use Microsoft Outlook actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseMSTeamsAction **   <a name="QS-Type-Capabilities-UseMSTeamsAction"></a>
The ability to use Microsoft Teams actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseNewRelicAction **   <a name="QS-Type-Capabilities-UseNewRelicAction"></a>
The ability to use New Relic actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseNotionAction **   <a name="QS-Type-Capabilities-UseNotionAction"></a>
The ability to use Notion actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseOneDriveAction **   <a name="QS-Type-Capabilities-UseOneDriveAction"></a>
The ability to use Microsoft OneDrive actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseOneDriveKnowledgeBase **   <a name="QS-Type-Capabilities-UseOneDriveKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseOneNoteAction **   <a name="QS-Type-Capabilities-UseOneNoteAction"></a>
The ability to use Microsoft OneNote actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseOpenAPIAction **   <a name="QS-Type-Capabilities-UseOpenAPIAction"></a>
The ability to use OpenAPI Specification actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseOutlookAddInExtension **   <a name="QS-Type-Capabilities-UseOutlookAddInExtension"></a>
The ability to use Amazon Quick through the Microsoft Outlook add-in.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UsePagerDutyAction **   <a name="QS-Type-Capabilities-UsePagerDutyAction"></a>
The ability to use PagerDuty Advance actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UsePagerDutyAgentAction **   <a name="QS-Type-Capabilities-UsePagerDutyAgentAction"></a>
The ability to use PagerDuty Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UsePowerpointAddInExtension **   <a name="QS-Type-Capabilities-UsePowerpointAddInExtension"></a>
The ability to use Amazon Quick through the Microsoft PowerPoint add-in.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseQBusinessKnowledgeBase **   <a name="QS-Type-Capabilities-UseQBusinessKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseQuickBooksAction **   <a name="QS-Type-Capabilities-UseQuickBooksAction"></a>
The ability to use QuickBooks actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseS3KnowledgeBase **   <a name="QS-Type-Capabilities-UseS3KnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseSalesforceAction **   <a name="QS-Type-Capabilities-UseSalesforceAction"></a>
The ability to use Salesforce actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseSandPGlobalEnergyAction **   <a name="QS-Type-Capabilities-UseSandPGlobalEnergyAction"></a>
The ability to use S&P Global Energy actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseSandPGMIAction **   <a name="QS-Type-Capabilities-UseSandPGMIAction"></a>
The ability to use S&P Global Market Intelligence actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseSAPBillOfMaterialAction **   <a name="QS-Type-Capabilities-UseSAPBillOfMaterialAction"></a>
The ability to use SAP Bill of Materials actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseSAPBusinessPartnerAction **   <a name="QS-Type-Capabilities-UseSAPBusinessPartnerAction"></a>
The ability to use SAP Business Partner actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseSAPMaterialStockAction **   <a name="QS-Type-Capabilities-UseSAPMaterialStockAction"></a>
The ability to use SAP Material Stock actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseSAPPhysicalInventoryAction **   <a name="QS-Type-Capabilities-UseSAPPhysicalInventoryAction"></a>
The ability to use SAP Physical Inventory actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseSAPProductMasterDataAction **   <a name="QS-Type-Capabilities-UseSAPProductMasterDataAction"></a>
The ability to use SAP Product Master actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseServiceNowAction **   <a name="QS-Type-Capabilities-UseServiceNowAction"></a>
The ability to use ServiceNow actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseSharePointAction **   <a name="QS-Type-Capabilities-UseSharePointAction"></a>
The ability to use Microsoft SharePoint Online actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseSharePointKnowledgeBase **   <a name="QS-Type-Capabilities-UseSharePointKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseShopifyAction **   <a name="QS-Type-Capabilities-UseShopifyAction"></a>
The ability to use Shopify actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseSlackAction **   <a name="QS-Type-Capabilities-UseSlackAction"></a>
The ability to use Slack actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseSmartsheetAction **   <a name="QS-Type-Capabilities-UseSmartsheetAction"></a>
The ability to use Smartsheet actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseSnowFlakeAction **   <a name="QS-Type-Capabilities-UseSnowFlakeAction"></a>
The ability to use Snowflake Cortex Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseTextractAction **   <a name="QS-Type-Capabilities-UseTextractAction"></a>
The ability to use Textract actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseVisierAgentAction **   <a name="QS-Type-Capabilities-UseVisierAgentAction"></a>
The ability to use Visier Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseWebCrawlerKnowledgeBase **   <a name="QS-Type-Capabilities-UseWebCrawlerKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseWhatsAppAction **   <a name="QS-Type-Capabilities-UseWhatsAppAction"></a>
The ability to use WhatsApp actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseWordAddInExtension **   <a name="QS-Type-Capabilities-UseWordAddInExtension"></a>
The ability to use Amazon Quick through the Microsoft Word add-in.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseZapierAction **   <a name="QS-Type-Capabilities-UseZapierAction"></a>
The ability to use Zapier Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseZendeskAction **   <a name="QS-Type-Capabilities-UseZendeskAction"></a>
The ability to use Zendesk actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseZoomAction **   <a name="QS-Type-Capabilities-UseZoomAction"></a>
The ability to use Zoom actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseZoomInfoAction **   <a name="QS-Type-Capabilities-UseZoomInfoAction"></a>
The ability to use ZoomInfo Agent actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ViewAccountSPICECapacity **   <a name="QS-Type-Capabilities-ViewAccountSPICECapacity"></a>
The ability to view account SPICE capacity.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** VisierAgentAction **   <a name="QS-Type-Capabilities-VisierAgentAction"></a>
The ability to perform actions using Visier Agent connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** WebCrawlerKnowledgeBase **   <a name="QS-Type-Capabilities-WebCrawlerKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** WhatsAppAction **   <a name="QS-Type-Capabilities-WhatsAppAction"></a>
The ability to perform actions using WhatsApp connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ZapierAction **   <a name="QS-Type-Capabilities-ZapierAction"></a>
The ability to perform actions using Zapier Agent connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ZendeskAction **   <a name="QS-Type-Capabilities-ZendeskAction"></a>
The ability to perform actions using Zendesk connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ZoomAction **   <a name="QS-Type-Capabilities-ZoomAction"></a>
The ability to perform actions using Zoom connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ZoomInfoAction **   <a name="QS-Type-Capabilities-ZoomInfoAction"></a>
The ability to perform actions using ZoomInfo Agent connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

## See Also
<a name="API_Capabilities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/Capabilities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/Capabilities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/Capabilities)
