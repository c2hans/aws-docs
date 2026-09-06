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

 ** CreateAndUpdateFactSetAction **   <a name="QS-Type-Capabilities-CreateAndUpdateFactSetAction"></a>
The ability to create and update FactSet actions.
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

 ** CreateAndUpdateGoogleCalendarAction **   <a name="QS-Type-Capabilities-CreateAndUpdateGoogleCalendarAction"></a>
The ability to create and update Google Calendar actions.
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

 ** CreateAndUpdateQBusinessKnowledgeBase **   <a name="QS-Type-Capabilities-CreateAndUpdateQBusinessKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
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

 ** CreateAndUpdateWebCrawlerKnowledgeBase **   <a name="QS-Type-Capabilities-CreateAndUpdateWebCrawlerKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateAndUpdateZendeskAction **   <a name="QS-Type-Capabilities-CreateAndUpdateZendeskAction"></a>
The ability to create and update Zendesk actions.
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

 ** CreateSharedFolders **   <a name="QS-Type-Capabilities-CreateSharedFolders"></a>
The ability to create shared folders.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateSpaces **   <a name="QS-Type-Capabilities-CreateSpaces"></a>
The ability to create spaces.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** CreateSPICEDataset **   <a name="QS-Type-Capabilities-CreateSPICEDataset"></a>
The ability to create a SPICE dataset.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** Dashboard **   <a name="QS-Type-Capabilities-Dashboard"></a>
The ability to perform dashboard-related actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** EditVisualWithQ **   <a name="QS-Type-Capabilities-EditVisualWithQ"></a>
The ability to Edit Visual with AI
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

 ** GoogleCalendarAction **   <a name="QS-Type-Capabilities-GoogleCalendarAction"></a>
The ability to perform actions using Google Calendar connectors.
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

 ** OpenAPIAction **   <a name="QS-Type-Capabilities-OpenAPIAction"></a>
The ability to perform actions using OpenAPI Specification connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** PagerDutyAction **   <a name="QS-Type-Capabilities-PagerDutyAction"></a>
The ability to perform actions using PagerDuty Advance connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** PerformFlowUiTask **   <a name="QS-Type-Capabilities-PerformFlowUiTask"></a>
The ability to use UI Agent step to perform tasks on public websites.
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

 ** QuickEventTrigger **   <a name="QS-Type-Capabilities-QuickEventTrigger"></a>
The ability to create, view, edit, delete, and run Quick event triggers for flows and automations.
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

 ** S3KnowledgeBase **   <a name="QS-Type-Capabilities-S3KnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** SalesforceAction **   <a name="QS-Type-Capabilities-SalesforceAction"></a>
The ability to perform actions using Salesforce connectors.
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

 ** ShareFactSetAction **   <a name="QS-Type-Capabilities-ShareFactSetAction"></a>
The ability to share FactSet actions.
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

 ** ShareGoogleCalendarAction **   <a name="QS-Type-Capabilities-ShareGoogleCalendarAction"></a>
The ability to share Google Calendar actions.
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

 ** ShareOpenAPIAction **   <a name="QS-Type-Capabilities-ShareOpenAPIAction"></a>
The ability to share OpenAPI Specification actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** SharePagerDutyAction **   <a name="QS-Type-Capabilities-SharePagerDutyAction"></a>
The ability to share PagerDuty Advance actions.
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

 ** ShareQBusinessKnowledgeBase **   <a name="QS-Type-Capabilities-ShareQBusinessKnowledgeBase"></a>
The permission state of a capability in a custom permissions profile. Valid values:
+  `DENY` – Amazon Quick denies this capability for users assigned to the profile.
+  `ALLOW` – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always `ALLOW`. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.
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

 ** ShareSalesforceAction **   <a name="QS-Type-Capabilities-ShareSalesforceAction"></a>
The ability to share Salesforce actions.
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

 ** ShareSpaces **   <a name="QS-Type-Capabilities-ShareSpaces"></a>
The ability to share spaces with other users and groups.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ShareTextractAction **   <a name="QS-Type-Capabilities-ShareTextractAction"></a>
The ability to share Textract actions.
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

 ** ShareZendeskAction **   <a name="QS-Type-Capabilities-ShareZendeskAction"></a>
The ability to share Zendesk actions.
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

 ** Space **   <a name="QS-Type-Capabilities-Space"></a>
The ability to perform space-related actions.
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

 ** TextractAction **   <a name="QS-Type-Capabilities-TextractAction"></a>
The ability to perform actions using Textract connectors.
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

 ** UseAgentWebSearch **   <a name="QS-Type-Capabilities-UseAgentWebSearch"></a>
The ability to use internet to enhance results in Chat Agents, Flows, and Quick Research. Web search queries will be processed securely in an AWS region `us-east-1`.
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

 ** UseGoogleCalendarAction **   <a name="QS-Type-Capabilities-UseGoogleCalendarAction"></a>
The ability to use Google Calendar actions.
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

 ** UseTextractAction **   <a name="QS-Type-Capabilities-UseTextractAction"></a>
The ability to use Textract actions.
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

 ** UseWordAddInExtension **   <a name="QS-Type-Capabilities-UseWordAddInExtension"></a>
The ability to use Amazon Quick through the Microsoft Word add-in.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** UseZendeskAction **   <a name="QS-Type-Capabilities-UseZendeskAction"></a>
The ability to use Zendesk actions.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

 ** ViewAccountSPICECapacity **   <a name="QS-Type-Capabilities-ViewAccountSPICECapacity"></a>
The ability to view account SPICE capacity.
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

 ** ZendeskAction **   <a name="QS-Type-Capabilities-ZendeskAction"></a>
The ability to perform actions using Zendesk connectors.
Type: String
Valid Values: `DENY | ALLOW`
Required: No

## See Also
<a name="API_Capabilities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/Capabilities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/Capabilities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/Capabilities)
