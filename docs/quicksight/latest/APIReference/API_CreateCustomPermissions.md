---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateCustomPermissions.html
---

# CreateCustomPermissions
<a name="API_CreateCustomPermissions"></a>

Creates a custom permissions profile.

## Request Syntax
<a name="API_CreateCustomPermissions_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/custom-permissions HTTP/1.1
Content-type: application/json

{
   "Capabilities": {
      "AccessAppsNativeDataStore": "{{string}}",
      "Action": "{{string}}",
      "AddOrRunAnomalyDetectionForAnalyses": "{{string}}",
      "AdobeAction": "{{string}}",
      "AdobeAnalyticsDataSource": "{{string}}",
      "AirtableAction": "{{string}}",
      "AmazonBedrockARSAction": "{{string}}",
      "AmazonBedrockFSAction": "{{string}}",
      "AmazonBedrockKRSAction": "{{string}}",
      "AmazonSThreeAction": "{{string}}",
      "Analysis": "{{string}}",
      "ApproveFlowShareRequests": "{{string}}",
      "Apps": "{{string}}",
      "AsanaAction": "{{string}}",
      "AthenaDataSource": "{{string}}",
      "AuroraDataSource": "{{string}}",
      "Automate": "{{string}}",
      "BambooHRAction": "{{string}}",
      "BedrockManagedKnowledgeBase": "{{string}}",
      "BeeAction": "{{string}}",
      "BoxAgentAction": "{{string}}",
      "BoxKnowledgeBase": "{{string}}",
      "BuildCalculatedFieldWithQ": "{{string}}",
      "CanvaAgentAction": "{{string}}",
      "ChatAgent": "{{string}}",
      "CiscoWebexMeetingsAction": "{{string}}",
      "CiscoWebexVidcastAction": "{{string}}",
      "ComprehendAction": "{{string}}",
      "ComprehendMedicalAction": "{{string}}",
      "ConfluenceAction": "{{string}}",
      "ConfluenceKnowledgeBase": "{{string}}",
      "CreateAdobeAnalyticsDataSource": "{{string}}",
      "CreateAndUpdateAdobeAction": "{{string}}",
      "CreateAndUpdateAirtableAction": "{{string}}",
      "CreateAndUpdateAmazonBedrockARSAction": "{{string}}",
      "CreateAndUpdateAmazonBedrockFSAction": "{{string}}",
      "CreateAndUpdateAmazonBedrockKRSAction": "{{string}}",
      "CreateAndUpdateAmazonSThreeAction": "{{string}}",
      "CreateAndUpdateApps": "{{string}}",
      "CreateAndUpdateAsanaAction": "{{string}}",
      "CreateAndUpdateBambooHRAction": "{{string}}",
      "CreateAndUpdateBedrockManagedKnowledgeBase": "{{string}}",
      "CreateAndUpdateBeeAction": "{{string}}",
      "CreateAndUpdateBoxAgentAction": "{{string}}",
      "CreateAndUpdateBoxKnowledgeBase": "{{string}}",
      "CreateAndUpdateCanvaAgentAction": "{{string}}",
      "CreateAndUpdateCiscoWebexMeetingsAction": "{{string}}",
      "CreateAndUpdateCiscoWebexVidcastAction": "{{string}}",
      "CreateAndUpdateComprehendAction": "{{string}}",
      "CreateAndUpdateComprehendMedicalAction": "{{string}}",
      "CreateAndUpdateConfluenceAction": "{{string}}",
      "CreateAndUpdateConfluenceKnowledgeBase": "{{string}}",
      "CreateAndUpdateDashboardEmailReports": "{{string}}",
      "CreateAndUpdateDatasets": "{{string}}",
      "CreateAndUpdateDataSources": "{{string}}",
      "CreateAndUpdateDropboxAction": "{{string}}",
      "CreateAndUpdateDunAndBradstreetAction": "{{string}}",
      "CreateAndUpdateFactSetAction": "{{string}}",
      "CreateAndUpdateFigmaAction": "{{string}}",
      "CreateAndUpdateGenericHTTPAction": "{{string}}",
      "CreateAndUpdateGithubAction": "{{string}}",
      "CreateAndUpdateGmailAction": "{{string}}",
      "CreateAndUpdateGongAction": "{{string}}",
      "CreateAndUpdateGoogleAnalyticsAction": "{{string}}",
      "CreateAndUpdateGoogleCalendarAction": "{{string}}",
      "CreateAndUpdateGoogleChatAction": "{{string}}",
      "CreateAndUpdateGoogleDocsAction": "{{string}}",
      "CreateAndUpdateGoogleDriveAction": "{{string}}",
      "CreateAndUpdateGoogleDriveKnowledgeBase": "{{string}}",
      "CreateAndUpdateGoogleMeetAction": "{{string}}",
      "CreateAndUpdateGoogleSheetsAction": "{{string}}",
      "CreateAndUpdateGoogleSlidesAction": "{{string}}",
      "CreateAndUpdateHGInsightsAction": "{{string}}",
      "CreateAndUpdateHubspotAction": "{{string}}",
      "CreateAndUpdateHuggingFaceAction": "{{string}}",
      "CreateAndUpdateIDCKnowledgeBase": "{{string}}",
      "CreateAndUpdateIntercomAction": "{{string}}",
      "CreateAndUpdateJiraAction": "{{string}}",
      "CreateAndUpdateKnowledgeBases": "{{string}}",
      "CreateAndUpdateLinearAction": "{{string}}",
      "CreateAndUpdateMCPAction": "{{string}}",
      "CreateAndUpdateMondayAction": "{{string}}",
      "CreateAndUpdateMoodysAction": "{{string}}",
      "CreateAndUpdateMSExchangeAction": "{{string}}",
      "CreateAndUpdateMSTeamsAction": "{{string}}",
      "CreateAndUpdateNewRelicAction": "{{string}}",
      "CreateAndUpdateNotionAction": "{{string}}",
      "CreateAndUpdateOneDriveAction": "{{string}}",
      "CreateAndUpdateOneDriveKnowledgeBase": "{{string}}",
      "CreateAndUpdateOneNoteAction": "{{string}}",
      "CreateAndUpdateOpenAPIAction": "{{string}}",
      "CreateAndUpdatePagerDutyAction": "{{string}}",
      "CreateAndUpdatePagerDutyAgentAction": "{{string}}",
      "CreateAndUpdateQBusinessKnowledgeBase": "{{string}}",
      "CreateAndUpdateQuickBooksAction": "{{string}}",
      "CreateAndUpdateS3KnowledgeBase": "{{string}}",
      "CreateAndUpdateSalesforceAction": "{{string}}",
      "CreateAndUpdateSandPGlobalEnergyAction": "{{string}}",
      "CreateAndUpdateSandPGMIAction": "{{string}}",
      "CreateAndUpdateSAPBillOfMaterialAction": "{{string}}",
      "CreateAndUpdateSAPBusinessPartnerAction": "{{string}}",
      "CreateAndUpdateSAPMaterialStockAction": "{{string}}",
      "CreateAndUpdateSAPPhysicalInventoryAction": "{{string}}",
      "CreateAndUpdateSAPProductMasterDataAction": "{{string}}",
      "CreateAndUpdateServiceNowAction": "{{string}}",
      "CreateAndUpdateSharePointAction": "{{string}}",
      "CreateAndUpdateSharePointKnowledgeBase": "{{string}}",
      "CreateAndUpdateShopifyAction": "{{string}}",
      "CreateAndUpdateSlackAction": "{{string}}",
      "CreateAndUpdateSmartsheetAction": "{{string}}",
      "CreateAndUpdateSnowFlakeAction": "{{string}}",
      "CreateAndUpdateTextractAction": "{{string}}",
      "CreateAndUpdateThemes": "{{string}}",
      "CreateAndUpdateThresholdAlerts": "{{string}}",
      "CreateAndUpdateVisierAgentAction": "{{string}}",
      "CreateAndUpdateWebCrawlerKnowledgeBase": "{{string}}",
      "CreateAndUpdateWhatsAppAction": "{{string}}",
      "CreateAndUpdateZapierAction": "{{string}}",
      "CreateAndUpdateZendeskAction": "{{string}}",
      "CreateAndUpdateZoomAction": "{{string}}",
      "CreateAndUpdateZoomInfoAction": "{{string}}",
      "CreateAthenaDataSource": "{{string}}",
      "CreateAuroraDataSource": "{{string}}",
      "CreateChatAgents": "{{string}}",
      "CreateDashboardExecutiveSummaryWithQ": "{{string}}",
      "CreateDatabricksDataSource": "{{string}}",
      "CreateDb2DataSource": "{{string}}",
      "CreateDenodoDataSource": "{{string}}",
      "CreateDocumentDbDataSource": "{{string}}",
      "CreateDremioDataSource": "{{string}}",
      "CreateDynamoDbDataSource": "{{string}}",
      "CreateExasolDataSource": "{{string}}",
      "CreateFileDataSource": "{{string}}",
      "CreateGitHubDataSource": "{{string}}",
      "CreateGoogleAnalyticsDataSource": "{{string}}",
      "CreateGoogleBigQueryDataSource": "{{string}}",
      "CreateGoogleSheetsDataSource": "{{string}}",
      "CreateImpalaDataSource": "{{string}}",
      "CreateJiraDataSource": "{{string}}",
      "CreateMariaDbDataSource": "{{string}}",
      "CreateMongoAtlasDataSource": "{{string}}",
      "CreateMongoDbDataSource": "{{string}}",
      "CreateMySqlDataSource": "{{string}}",
      "CreateOpenSearchDataSource": "{{string}}",
      "CreateOracleDataSource": "{{string}}",
      "CreatePayPalDataSource": "{{string}}",
      "CreatePostgreSqlDataSource": "{{string}}",
      "CreatePrestoDataSource": "{{string}}",
      "CreateRadiantDataSource": "{{string}}",
      "CreateRdsDataSource": "{{string}}",
      "CreateRedshiftAutoDiscoveredDataSource": "{{string}}",
      "CreateRedshiftManualDataSource": "{{string}}",
      "CreateS3AnalyticsDataSource": "{{string}}",
      "CreateS3DataSource": "{{string}}",
      "CreateS3TablesDataSource": "{{string}}",
      "CreateSalesforceDataSource": "{{string}}",
      "CreateSapHanaDataSource": "{{string}}",
      "CreateServiceNowDataSource": "{{string}}",
      "CreateSharedFolders": "{{string}}",
      "CreateSnowflakeDataSource": "{{string}}",
      "CreateSpaces": "{{string}}",
      "CreateSparkDataSource": "{{string}}",
      "CreateSPICEDataset": "{{string}}",
      "CreateSqlServerDataSource": "{{string}}",
      "CreateSquareDataSource": "{{string}}",
      "CreateStarburstDataSource": "{{string}}",
      "CreateTeradataDataSource": "{{string}}",
      "CreateTimestreamDataSource": "{{string}}",
      "CreateTrinoDataSource": "{{string}}",
      "CreateTwitterDataSource": "{{string}}",
      "Dashboard": "{{string}}",
      "DatabricksDataSource": "{{string}}",
      "Db2DataSource": "{{string}}",
      "DenodoDataSource": "{{string}}",
      "DocumentDbDataSource": "{{string}}",
      "DremioDataSource": "{{string}}",
      "DropboxAction": "{{string}}",
      "DunAndBradstreetAction": "{{string}}",
      "DynamoDbDataSource": "{{string}}",
      "EditVisualWithQ": "{{string}}",
      "ExasolDataSource": "{{string}}",
      "ExportToCsv": "{{string}}",
      "ExportToCsvInScheduledReports": "{{string}}",
      "ExportToExcel": "{{string}}",
      "ExportToExcelInScheduledReports": "{{string}}",
      "ExportToPdf": "{{string}}",
      "ExportToPdfInScheduledReports": "{{string}}",
      "Extension": "{{string}}",
      "FactSetAction": "{{string}}",
      "FigmaAction": "{{string}}",
      "FileDataSource": "{{string}}",
      "Flow": "{{string}}",
      "GenerateAnalyses": "{{string}}",
      "GenericHTTPAction": "{{string}}",
      "GithubAction": "{{string}}",
      "GitHubDataSource": "{{string}}",
      "GmailAction": "{{string}}",
      "GongAction": "{{string}}",
      "GoogleAnalyticsAction": "{{string}}",
      "GoogleAnalyticsDataSource": "{{string}}",
      "GoogleBigQueryDataSource": "{{string}}",
      "GoogleCalendarAction": "{{string}}",
      "GoogleChatAction": "{{string}}",
      "GoogleDocsAction": "{{string}}",
      "GoogleDriveAction": "{{string}}",
      "GoogleDriveKnowledgeBase": "{{string}}",
      "GoogleMeetAction": "{{string}}",
      "GoogleSheetsAction": "{{string}}",
      "GoogleSheetsDataSource": "{{string}}",
      "GoogleSlidesAction": "{{string}}",
      "HGInsightsAction": "{{string}}",
      "HubspotAction": "{{string}}",
      "HuggingFaceAction": "{{string}}",
      "IDCKnowledgeBase": "{{string}}",
      "ImpalaDataSource": "{{string}}",
      "InboundEmailTrigger": "{{string}}",
      "IncludeContentInScheduledReportsEmail": "{{string}}",
      "IntercomAction": "{{string}}",
      "InvokeAppsAIInference": "{{string}}",
      "JiraAction": "{{string}}",
      "JiraDataSource": "{{string}}",
      "KnowledgeBase": "{{string}}",
      "LinearAction": "{{string}}",
      "ManageSharedFolders": "{{string}}",
      "MariaDbDataSource": "{{string}}",
      "MCPAction": "{{string}}",
      "MondayAction": "{{string}}",
      "MongoAtlasDataSource": "{{string}}",
      "MongoDbDataSource": "{{string}}",
      "MoodysAction": "{{string}}",
      "MSExchangeAction": "{{string}}",
      "MSTeamsAction": "{{string}}",
      "MySqlDataSource": "{{string}}",
      "NewRelicAction": "{{string}}",
      "NotionAction": "{{string}}",
      "OneDriveAction": "{{string}}",
      "OneDriveKnowledgeBase": "{{string}}",
      "OneNoteAction": "{{string}}",
      "OpenAPIAction": "{{string}}",
      "OpenSearchDataSource": "{{string}}",
      "OracleDataSource": "{{string}}",
      "PagerDutyAction": "{{string}}",
      "PagerDutyAgentAction": "{{string}}",
      "PayPalDataSource": "{{string}}",
      "PerformFlowUiTask": "{{string}}",
      "PostgreSqlDataSource": "{{string}}",
      "PrestoDataSource": "{{string}}",
      "PrintReports": "{{string}}",
      "PublishWithoutApproval": "{{string}}",
      "QBusinessKnowledgeBase": "{{string}}",
      "QuickBooksAction": "{{string}}",
      "QuickEventTrigger": "{{string}}",
      "RadiantDataSource": "{{string}}",
      "RdsDataSource": "{{string}}",
      "RedshiftAutoDiscoveredDataSource": "{{string}}",
      "RedshiftManualDataSource": "{{string}}",
      "RenameSharedFolders": "{{string}}",
      "Research": "{{string}}",
      "S3AnalyticsDataSource": "{{string}}",
      "S3DataSource": "{{string}}",
      "S3KnowledgeBase": "{{string}}",
      "S3TablesDataSource": "{{string}}",
      "SalesforceAction": "{{string}}",
      "SalesforceDataSource": "{{string}}",
      "SandPGlobalEnergyAction": "{{string}}",
      "SandPGMIAction": "{{string}}",
      "SAPBillOfMaterialAction": "{{string}}",
      "SAPBusinessPartnerAction": "{{string}}",
      "SapHanaDataSource": "{{string}}",
      "SAPMaterialStockAction": "{{string}}",
      "SAPPhysicalInventoryAction": "{{string}}",
      "SAPProductMasterDataAction": "{{string}}",
      "Scenario": "{{string}}",
      "ScheduleTrigger": "{{string}}",
      "SelfUpgradeUserRole": "{{string}}",
      "ServiceNowAction": "{{string}}",
      "ServiceNowDataSource": "{{string}}",
      "ShareAdobeAction": "{{string}}",
      "ShareAdobeAnalyticsDataSource": "{{string}}",
      "ShareAirtableAction": "{{string}}",
      "ShareAmazonBedrockARSAction": "{{string}}",
      "ShareAmazonBedrockFSAction": "{{string}}",
      "ShareAmazonBedrockKRSAction": "{{string}}",
      "ShareAmazonSThreeAction": "{{string}}",
      "ShareAnalyses": "{{string}}",
      "ShareApps": "{{string}}",
      "ShareAsanaAction": "{{string}}",
      "ShareAthenaDataSource": "{{string}}",
      "ShareAuroraDataSource": "{{string}}",
      "ShareBambooHRAction": "{{string}}",
      "ShareBedrockManagedKnowledgeBase": "{{string}}",
      "ShareBeeAction": "{{string}}",
      "ShareBoxAgentAction": "{{string}}",
      "ShareBoxKnowledgeBase": "{{string}}",
      "ShareCanvaAgentAction": "{{string}}",
      "ShareChatAgents": "{{string}}",
      "ShareCiscoWebexMeetingsAction": "{{string}}",
      "ShareCiscoWebexVidcastAction": "{{string}}",
      "ShareComprehendAction": "{{string}}",
      "ShareComprehendMedicalAction": "{{string}}",
      "ShareConfluenceAction": "{{string}}",
      "ShareConfluenceKnowledgeBase": "{{string}}",
      "ShareDashboards": "{{string}}",
      "ShareDatabricksDataSource": "{{string}}",
      "ShareDatasets": "{{string}}",
      "ShareDataSources": "{{string}}",
      "ShareDb2DataSource": "{{string}}",
      "ShareDenodoDataSource": "{{string}}",
      "ShareDocumentDbDataSource": "{{string}}",
      "ShareDremioDataSource": "{{string}}",
      "ShareDropboxAction": "{{string}}",
      "ShareDunAndBradstreetAction": "{{string}}",
      "ShareDynamoDbDataSource": "{{string}}",
      "ShareExasolDataSource": "{{string}}",
      "ShareFactSetAction": "{{string}}",
      "ShareFigmaAction": "{{string}}",
      "ShareFileDataSource": "{{string}}",
      "ShareGenericHTTPAction": "{{string}}",
      "ShareGithubAction": "{{string}}",
      "ShareGitHubDataSource": "{{string}}",
      "ShareGmailAction": "{{string}}",
      "ShareGongAction": "{{string}}",
      "ShareGoogleAnalyticsAction": "{{string}}",
      "ShareGoogleAnalyticsDataSource": "{{string}}",
      "ShareGoogleBigQueryDataSource": "{{string}}",
      "ShareGoogleCalendarAction": "{{string}}",
      "ShareGoogleChatAction": "{{string}}",
      "ShareGoogleDocsAction": "{{string}}",
      "ShareGoogleDriveAction": "{{string}}",
      "ShareGoogleDriveKnowledgeBase": "{{string}}",
      "ShareGoogleMeetAction": "{{string}}",
      "ShareGoogleSheetsAction": "{{string}}",
      "ShareGoogleSheetsDataSource": "{{string}}",
      "ShareGoogleSlidesAction": "{{string}}",
      "ShareHGInsightsAction": "{{string}}",
      "ShareHubspotAction": "{{string}}",
      "ShareHuggingFaceAction": "{{string}}",
      "ShareIDCKnowledgeBase": "{{string}}",
      "ShareImpalaDataSource": "{{string}}",
      "ShareIntercomAction": "{{string}}",
      "ShareJiraAction": "{{string}}",
      "ShareJiraDataSource": "{{string}}",
      "ShareKnowledgeBases": "{{string}}",
      "ShareLinearAction": "{{string}}",
      "ShareMariaDbDataSource": "{{string}}",
      "ShareMCPAction": "{{string}}",
      "ShareMondayAction": "{{string}}",
      "ShareMongoAtlasDataSource": "{{string}}",
      "ShareMongoDbDataSource": "{{string}}",
      "ShareMoodysAction": "{{string}}",
      "ShareMSExchangeAction": "{{string}}",
      "ShareMSTeamsAction": "{{string}}",
      "ShareMySqlDataSource": "{{string}}",
      "ShareNewRelicAction": "{{string}}",
      "ShareNotionAction": "{{string}}",
      "ShareOneDriveAction": "{{string}}",
      "ShareOneDriveKnowledgeBase": "{{string}}",
      "ShareOneNoteAction": "{{string}}",
      "ShareOpenAPIAction": "{{string}}",
      "ShareOpenSearchDataSource": "{{string}}",
      "ShareOracleDataSource": "{{string}}",
      "SharePagerDutyAction": "{{string}}",
      "SharePagerDutyAgentAction": "{{string}}",
      "SharePayPalDataSource": "{{string}}",
      "SharePointAction": "{{string}}",
      "SharePointKnowledgeBase": "{{string}}",
      "SharePostgreSqlDataSource": "{{string}}",
      "SharePrestoDataSource": "{{string}}",
      "ShareQBusinessKnowledgeBase": "{{string}}",
      "ShareQuickBooksAction": "{{string}}",
      "ShareRadiantDataSource": "{{string}}",
      "ShareRdsDataSource": "{{string}}",
      "ShareRedshiftAutoDiscoveredDataSource": "{{string}}",
      "ShareRedshiftManualDataSource": "{{string}}",
      "ShareS3AnalyticsDataSource": "{{string}}",
      "ShareS3DataSource": "{{string}}",
      "ShareS3KnowledgeBase": "{{string}}",
      "ShareS3TablesDataSource": "{{string}}",
      "ShareSalesforceAction": "{{string}}",
      "ShareSalesforceDataSource": "{{string}}",
      "ShareSandPGlobalEnergyAction": "{{string}}",
      "ShareSandPGMIAction": "{{string}}",
      "ShareSAPBillOfMaterialAction": "{{string}}",
      "ShareSAPBusinessPartnerAction": "{{string}}",
      "ShareSapHanaDataSource": "{{string}}",
      "ShareSAPMaterialStockAction": "{{string}}",
      "ShareSAPPhysicalInventoryAction": "{{string}}",
      "ShareSAPProductMasterDataAction": "{{string}}",
      "ShareServiceNowAction": "{{string}}",
      "ShareServiceNowDataSource": "{{string}}",
      "ShareSharePointAction": "{{string}}",
      "ShareSharePointKnowledgeBase": "{{string}}",
      "ShareShopifyAction": "{{string}}",
      "ShareSlackAction": "{{string}}",
      "ShareSmartsheetAction": "{{string}}",
      "ShareSnowFlakeAction": "{{string}}",
      "ShareSnowflakeDataSource": "{{string}}",
      "ShareSpaces": "{{string}}",
      "ShareSparkDataSource": "{{string}}",
      "ShareSqlServerDataSource": "{{string}}",
      "ShareSquareDataSource": "{{string}}",
      "ShareStarburstDataSource": "{{string}}",
      "ShareTeradataDataSource": "{{string}}",
      "ShareTextractAction": "{{string}}",
      "ShareTimestreamDataSource": "{{string}}",
      "ShareTrinoDataSource": "{{string}}",
      "ShareTwitterDataSource": "{{string}}",
      "ShareVisierAgentAction": "{{string}}",
      "ShareWebCrawlerKnowledgeBase": "{{string}}",
      "ShareWhatsAppAction": "{{string}}",
      "ShareZapierAction": "{{string}}",
      "ShareZendeskAction": "{{string}}",
      "ShareZoomAction": "{{string}}",
      "ShareZoomInfoAction": "{{string}}",
      "ShopifyAction": "{{string}}",
      "SlackAction": "{{string}}",
      "SmartsheetAction": "{{string}}",
      "SnowFlakeAction": "{{string}}",
      "SnowflakeDataSource": "{{string}}",
      "Space": "{{string}}",
      "SparkDataSource": "{{string}}",
      "SqlServerDataSource": "{{string}}",
      "SquareDataSource": "{{string}}",
      "StarburstDataSource": "{{string}}",
      "Story": "{{string}}",
      "SubscribeDashboardEmailReports": "{{string}}",
      "TeradataDataSource": "{{string}}",
      "TextractAction": "{{string}}",
      "TimestreamDataSource": "{{string}}",
      "Topic": "{{string}}",
      "Trigger": "{{string}}",
      "TrinoDataSource": "{{string}}",
      "TwitterDataSource": "{{string}}",
      "UpdateAdobeAnalyticsDataSource": "{{string}}",
      "UpdateAthenaDataSource": "{{string}}",
      "UpdateAuroraDataSource": "{{string}}",
      "UpdateDatabricksDataSource": "{{string}}",
      "UpdateDb2DataSource": "{{string}}",
      "UpdateDenodoDataSource": "{{string}}",
      "UpdateDocumentDbDataSource": "{{string}}",
      "UpdateDremioDataSource": "{{string}}",
      "UpdateDynamoDbDataSource": "{{string}}",
      "UpdateExasolDataSource": "{{string}}",
      "UpdateFileDataSource": "{{string}}",
      "UpdateGitHubDataSource": "{{string}}",
      "UpdateGoogleAnalyticsDataSource": "{{string}}",
      "UpdateGoogleBigQueryDataSource": "{{string}}",
      "UpdateGoogleSheetsDataSource": "{{string}}",
      "UpdateImpalaDataSource": "{{string}}",
      "UpdateJiraDataSource": "{{string}}",
      "UpdateMariaDbDataSource": "{{string}}",
      "UpdateMongoAtlasDataSource": "{{string}}",
      "UpdateMongoDbDataSource": "{{string}}",
      "UpdateMySqlDataSource": "{{string}}",
      "UpdateOpenSearchDataSource": "{{string}}",
      "UpdateOracleDataSource": "{{string}}",
      "UpdatePayPalDataSource": "{{string}}",
      "UpdatePostgreSqlDataSource": "{{string}}",
      "UpdatePrestoDataSource": "{{string}}",
      "UpdateRadiantDataSource": "{{string}}",
      "UpdateRdsDataSource": "{{string}}",
      "UpdateRedshiftAutoDiscoveredDataSource": "{{string}}",
      "UpdateRedshiftManualDataSource": "{{string}}",
      "UpdateS3AnalyticsDataSource": "{{string}}",
      "UpdateS3DataSource": "{{string}}",
      "UpdateS3TablesDataSource": "{{string}}",
      "UpdateSalesforceDataSource": "{{string}}",
      "UpdateSapHanaDataSource": "{{string}}",
      "UpdateServiceNowDataSource": "{{string}}",
      "UpdateSnowflakeDataSource": "{{string}}",
      "UpdateSparkDataSource": "{{string}}",
      "UpdateSqlServerDataSource": "{{string}}",
      "UpdateSquareDataSource": "{{string}}",
      "UpdateStarburstDataSource": "{{string}}",
      "UpdateTeradataDataSource": "{{string}}",
      "UpdateTimestreamDataSource": "{{string}}",
      "UpdateTrinoDataSource": "{{string}}",
      "UpdateTwitterDataSource": "{{string}}",
      "UseAdobeAction": "{{string}}",
      "UseAgentWebSearch": "{{string}}",
      "UseAirtableAction": "{{string}}",
      "UseAmazonBedrockARSAction": "{{string}}",
      "UseAmazonBedrockFSAction": "{{string}}",
      "UseAmazonBedrockKRSAction": "{{string}}",
      "UseAmazonSThreeAction": "{{string}}",
      "UseAsanaAction": "{{string}}",
      "UseBambooHRAction": "{{string}}",
      "UseBedrockManagedKnowledgeBase": "{{string}}",
      "UseBedrockModels": "{{string}}",
      "UseBeeAction": "{{string}}",
      "UseBoxAgentAction": "{{string}}",
      "UseBoxKnowledgeBase": "{{string}}",
      "UseBrowserExtension": "{{string}}",
      "UseCanvaAgentAction": "{{string}}",
      "UseCiscoWebexMeetingsAction": "{{string}}",
      "UseCiscoWebexVidcastAction": "{{string}}",
      "UseComprehendAction": "{{string}}",
      "UseComprehendMedicalAction": "{{string}}",
      "UseConfluenceAction": "{{string}}",
      "UseConfluenceKnowledgeBase": "{{string}}",
      "UseDropboxAction": "{{string}}",
      "UseDunAndBradstreetAction": "{{string}}",
      "UseExcelAddInExtension": "{{string}}",
      "UseFactSetAction": "{{string}}",
      "UseFigmaAction": "{{string}}",
      "UseGenericHTTPAction": "{{string}}",
      "UseGithubAction": "{{string}}",
      "UseGmailAction": "{{string}}",
      "UseGongAction": "{{string}}",
      "UseGoogleAnalyticsAction": "{{string}}",
      "UseGoogleCalendarAction": "{{string}}",
      "UseGoogleChatAction": "{{string}}",
      "UseGoogleDocsAction": "{{string}}",
      "UseGoogleDriveAction": "{{string}}",
      "UseGoogleDriveKnowledgeBase": "{{string}}",
      "UseGoogleMeetAction": "{{string}}",
      "UseGoogleSheetsAction": "{{string}}",
      "UseGoogleSlidesAction": "{{string}}",
      "UseHGInsightsAction": "{{string}}",
      "UseHubspotAction": "{{string}}",
      "UseHuggingFaceAction": "{{string}}",
      "UseIDCKnowledgeBase": "{{string}}",
      "UseIntercomAction": "{{string}}",
      "UseJiraAction": "{{string}}",
      "UseLinearAction": "{{string}}",
      "UseMCPAction": "{{string}}",
      "UseMondayAction": "{{string}}",
      "UseMoodysAction": "{{string}}",
      "UseMSExchangeAction": "{{string}}",
      "UseMSTeamsAction": "{{string}}",
      "UseNewRelicAction": "{{string}}",
      "UseNotionAction": "{{string}}",
      "UseOneDriveAction": "{{string}}",
      "UseOneDriveKnowledgeBase": "{{string}}",
      "UseOneNoteAction": "{{string}}",
      "UseOpenAPIAction": "{{string}}",
      "UseOutlookAddInExtension": "{{string}}",
      "UsePagerDutyAction": "{{string}}",
      "UsePagerDutyAgentAction": "{{string}}",
      "UsePowerpointAddInExtension": "{{string}}",
      "UseQBusinessKnowledgeBase": "{{string}}",
      "UseQuickBooksAction": "{{string}}",
      "UseS3KnowledgeBase": "{{string}}",
      "UseSalesforceAction": "{{string}}",
      "UseSandPGlobalEnergyAction": "{{string}}",
      "UseSandPGMIAction": "{{string}}",
      "UseSAPBillOfMaterialAction": "{{string}}",
      "UseSAPBusinessPartnerAction": "{{string}}",
      "UseSAPMaterialStockAction": "{{string}}",
      "UseSAPPhysicalInventoryAction": "{{string}}",
      "UseSAPProductMasterDataAction": "{{string}}",
      "UseServiceNowAction": "{{string}}",
      "UseSharePointAction": "{{string}}",
      "UseSharePointKnowledgeBase": "{{string}}",
      "UseShopifyAction": "{{string}}",
      "UseSlackAction": "{{string}}",
      "UseSmartsheetAction": "{{string}}",
      "UseSnowFlakeAction": "{{string}}",
      "UseTextractAction": "{{string}}",
      "UseVisierAgentAction": "{{string}}",
      "UseWebCrawlerKnowledgeBase": "{{string}}",
      "UseWhatsAppAction": "{{string}}",
      "UseWordAddInExtension": "{{string}}",
      "UseZapierAction": "{{string}}",
      "UseZendeskAction": "{{string}}",
      "UseZoomAction": "{{string}}",
      "UseZoomInfoAction": "{{string}}",
      "ViewAccountSPICECapacity": "{{string}}",
      "VisierAgentAction": "{{string}}",
      "WebCrawlerKnowledgeBase": "{{string}}",
      "WhatsAppAction": "{{string}}",
      "ZapierAction": "{{string}}",
      "ZendeskAction": "{{string}}",
      "ZoomAction": "{{string}}",
      "ZoomInfoAction": "{{string}}"
   },
   "CustomPermissionsName": "{{string}}",
   "Governance": {
      "DefaultCategoryEffects": {
         "{{string}}" : "{{string}}"
      }
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateCustomPermissions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_CreateCustomPermissions_RequestSyntax) **   <a name="QS-CreateCustomPermissions-request-uri-AwsAccountId"></a>
The ID of the AWS account that you want to create the custom permissions profile in.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

## Request Body
<a name="API_CreateCustomPermissions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CustomPermissionsName](#API_CreateCustomPermissions_RequestSyntax) **   <a name="QS-CreateCustomPermissions-request-CustomPermissionsName"></a>
The name of the custom permissions profile that you want to create.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9+=,.@_-]+$`
Required: Yes

 ** [Capabilities](#API_CreateCustomPermissions_RequestSyntax) **   <a name="QS-CreateCustomPermissions-request-Capabilities"></a>
A set of actions to include in the custom permissions profile.
Type: [Capabilities](API_Capabilities.md) object
Required: No

 ** [Governance](#API_CreateCustomPermissions_RequestSyntax) **   <a name="QS-CreateCustomPermissions-request-Governance"></a>
The governance configuration for the custom permissions profile. When governance controls are defined for a category, any capabilities in that category not explicitly set to `ALLOW` in `Capabilities` are denied. Even newly added capabilities in the category are implicitly disabled when Amazon Quick releases them.
Type: [Governance](API_Governance.md) object
Required: No

 ** [Tags](#API_CreateCustomPermissions_RequestSyntax) **   <a name="QS-CreateCustomPermissions-request-Tags"></a>
The tags to associate with the custom permissions profile.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateCustomPermissions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "RequestId": "string",
   "Status": number
}
```

## Response Elements
<a name="API_CreateCustomPermissions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateCustomPermissions_ResponseSyntax) **   <a name="QS-CreateCustomPermissions-response-Arn"></a>
The Amazon Resource Name (ARN) of the custom permissions profile.
Type: String

 ** [RequestId](#API_CreateCustomPermissions_ResponseSyntax) **   <a name="QS-CreateCustomPermissions-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

 ** [Status](#API_CreateCustomPermissions_ResponseSyntax) **   <a name="QS-CreateCustomPermissions-response-Status"></a>
The HTTP status of the request.
Type: Integer

## Errors
<a name="API_CreateCustomPermissions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **
A limit is exceeded.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
Limit exceeded.
HTTP Status Code: 409

 ** PreconditionNotMetException **
One or more preconditions aren't met.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceExistsException **
The resource specified already exists.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 409

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ResourceUnavailableException **
This resource is currently unavailable.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 503

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_CreateCustomPermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/CreateCustomPermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/CreateCustomPermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CreateCustomPermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/CreateCustomPermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CreateCustomPermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/CreateCustomPermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/CreateCustomPermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/CreateCustomPermissions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/CreateCustomPermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CreateCustomPermissions)
