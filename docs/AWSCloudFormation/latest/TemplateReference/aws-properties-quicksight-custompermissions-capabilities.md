---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-custompermissions-capabilities.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::CustomPermissions Capabilities
<a name="aws-properties-quicksight-custompermissions-capabilities"></a>

A set of actions that correspond to Amazon Quick Sight permissions.

## Syntax
<a name="aws-properties-quicksight-custompermissions-capabilities-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-custompermissions-capabilities-syntax.json"></a>

```
{
  "[AccessAppsNativeDataStore](#cfn-quicksight-custompermissions-capabilities-accessappsnativedatastore)" : {{String}},
  "[Action](#cfn-quicksight-custompermissions-capabilities-action)" : {{String}},
  "[AddOrRunAnomalyDetectionForAnalyses](#cfn-quicksight-custompermissions-capabilities-addorrunanomalydetectionforanalyses)" : {{String}},
  "[AdobeAnalyticsDataSource](#cfn-quicksight-custompermissions-capabilities-adobeanalyticsdatasource)" : {{String}},
  "[AmazonBedrockARSAction](#cfn-quicksight-custompermissions-capabilities-amazonbedrockarsaction)" : {{String}},
  "[AmazonBedrockFSAction](#cfn-quicksight-custompermissions-capabilities-amazonbedrockfsaction)" : {{String}},
  "[AmazonBedrockKRSAction](#cfn-quicksight-custompermissions-capabilities-amazonbedrockkrsaction)" : {{String}},
  "[AmazonSThreeAction](#cfn-quicksight-custompermissions-capabilities-amazonsthreeaction)" : {{String}},
  "[Analysis](#cfn-quicksight-custompermissions-capabilities-analysis)" : {{String}},
  "[ApproveFlowShareRequests](#cfn-quicksight-custompermissions-capabilities-approveflowsharerequests)" : {{String}},
  "[Apps](#cfn-quicksight-custompermissions-capabilities-apps)" : {{String}},
  "[AsanaAction](#cfn-quicksight-custompermissions-capabilities-asanaaction)" : {{String}},
  "[AthenaDataSource](#cfn-quicksight-custompermissions-capabilities-athenadatasource)" : {{String}},
  "[AuroraDataSource](#cfn-quicksight-custompermissions-capabilities-auroradatasource)" : {{String}},
  "[Automate](#cfn-quicksight-custompermissions-capabilities-automate)" : {{String}},
  "[BambooHRAction](#cfn-quicksight-custompermissions-capabilities-bamboohraction)" : {{String}},
  "[BedrockManagedKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-bedrockmanagedknowledgebase)" : {{String}},
  "[BoxAgentAction](#cfn-quicksight-custompermissions-capabilities-boxagentaction)" : {{String}},
  "[BoxKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-boxknowledgebase)" : {{String}},
  "[BuildCalculatedFieldWithQ](#cfn-quicksight-custompermissions-capabilities-buildcalculatedfieldwithq)" : {{String}},
  "[CanvaAgentAction](#cfn-quicksight-custompermissions-capabilities-canvaagentaction)" : {{String}},
  "[ChatAgent](#cfn-quicksight-custompermissions-capabilities-chatagent)" : {{String}},
  "[ComprehendAction](#cfn-quicksight-custompermissions-capabilities-comprehendaction)" : {{String}},
  "[ComprehendMedicalAction](#cfn-quicksight-custompermissions-capabilities-comprehendmedicalaction)" : {{String}},
  "[ConfluenceAction](#cfn-quicksight-custompermissions-capabilities-confluenceaction)" : {{String}},
  "[ConfluenceKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-confluenceknowledgebase)" : {{String}},
  "[CreateAdobeAnalyticsDataSource](#cfn-quicksight-custompermissions-capabilities-createadobeanalyticsdatasource)" : {{String}},
  "[CreateAndUpdateAmazonBedrockARSAction](#cfn-quicksight-custompermissions-capabilities-createandupdateamazonbedrockarsaction)" : {{String}},
  "[CreateAndUpdateAmazonBedrockFSAction](#cfn-quicksight-custompermissions-capabilities-createandupdateamazonbedrockfsaction)" : {{String}},
  "[CreateAndUpdateAmazonBedrockKRSAction](#cfn-quicksight-custompermissions-capabilities-createandupdateamazonbedrockkrsaction)" : {{String}},
  "[CreateAndUpdateAmazonSThreeAction](#cfn-quicksight-custompermissions-capabilities-createandupdateamazonsthreeaction)" : {{String}},
  "[CreateAndUpdateApps](#cfn-quicksight-custompermissions-capabilities-createandupdateapps)" : {{String}},
  "[CreateAndUpdateAsanaAction](#cfn-quicksight-custompermissions-capabilities-createandupdateasanaaction)" : {{String}},
  "[CreateAndUpdateBambooHRAction](#cfn-quicksight-custompermissions-capabilities-createandupdatebamboohraction)" : {{String}},
  "[CreateAndUpdateBedrockManagedKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-createandupdatebedrockmanagedknowledgebase)" : {{String}},
  "[CreateAndUpdateBoxAgentAction](#cfn-quicksight-custompermissions-capabilities-createandupdateboxagentaction)" : {{String}},
  "[CreateAndUpdateBoxKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-createandupdateboxknowledgebase)" : {{String}},
  "[CreateAndUpdateCanvaAgentAction](#cfn-quicksight-custompermissions-capabilities-createandupdatecanvaagentaction)" : {{String}},
  "[CreateAndUpdateComprehendAction](#cfn-quicksight-custompermissions-capabilities-createandupdatecomprehendaction)" : {{String}},
  "[CreateAndUpdateComprehendMedicalAction](#cfn-quicksight-custompermissions-capabilities-createandupdatecomprehendmedicalaction)" : {{String}},
  "[CreateAndUpdateConfluenceAction](#cfn-quicksight-custompermissions-capabilities-createandupdateconfluenceaction)" : {{String}},
  "[CreateAndUpdateConfluenceKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-createandupdateconfluenceknowledgebase)" : {{String}},
  "[CreateAndUpdateDashboardEmailReports](#cfn-quicksight-custompermissions-capabilities-createandupdatedashboardemailreports)" : {{String}},
  "[CreateAndUpdateDatasets](#cfn-quicksight-custompermissions-capabilities-createandupdatedatasets)" : {{String}},
  "[CreateAndUpdateDataSources](#cfn-quicksight-custompermissions-capabilities-createandupdatedatasources)" : {{String}},
  "[CreateAndUpdateFactSetAction](#cfn-quicksight-custompermissions-capabilities-createandupdatefactsetaction)" : {{String}},
  "[CreateAndUpdateGenericHTTPAction](#cfn-quicksight-custompermissions-capabilities-createandupdategenerichttpaction)" : {{String}},
  "[CreateAndUpdateGithubAction](#cfn-quicksight-custompermissions-capabilities-createandupdategithubaction)" : {{String}},
  "[CreateAndUpdateGoogleCalendarAction](#cfn-quicksight-custompermissions-capabilities-createandupdategooglecalendaraction)" : {{String}},
  "[CreateAndUpdateGoogleDriveKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-createandupdategoogledriveknowledgebase)" : {{String}},
  "[CreateAndUpdateHubspotAction](#cfn-quicksight-custompermissions-capabilities-createandupdatehubspotaction)" : {{String}},
  "[CreateAndUpdateHuggingFaceAction](#cfn-quicksight-custompermissions-capabilities-createandupdatehuggingfaceaction)" : {{String}},
  "[CreateAndUpdateIDCKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-createandupdateidcknowledgebase)" : {{String}},
  "[CreateAndUpdateIntercomAction](#cfn-quicksight-custompermissions-capabilities-createandupdateintercomaction)" : {{String}},
  "[CreateAndUpdateJiraAction](#cfn-quicksight-custompermissions-capabilities-createandupdatejiraaction)" : {{String}},
  "[CreateAndUpdateKnowledgeBases](#cfn-quicksight-custompermissions-capabilities-createandupdateknowledgebases)" : {{String}},
  "[CreateAndUpdateLinearAction](#cfn-quicksight-custompermissions-capabilities-createandupdatelinearaction)" : {{String}},
  "[CreateAndUpdateMCPAction](#cfn-quicksight-custompermissions-capabilities-createandupdatemcpaction)" : {{String}},
  "[CreateAndUpdateMondayAction](#cfn-quicksight-custompermissions-capabilities-createandupdatemondayaction)" : {{String}},
  "[CreateAndUpdateMSExchangeAction](#cfn-quicksight-custompermissions-capabilities-createandupdatemsexchangeaction)" : {{String}},
  "[CreateAndUpdateMSTeamsAction](#cfn-quicksight-custompermissions-capabilities-createandupdatemsteamsaction)" : {{String}},
  "[CreateAndUpdateNewRelicAction](#cfn-quicksight-custompermissions-capabilities-createandupdatenewrelicaction)" : {{String}},
  "[CreateAndUpdateNotionAction](#cfn-quicksight-custompermissions-capabilities-createandupdatenotionaction)" : {{String}},
  "[CreateAndUpdateOneDriveAction](#cfn-quicksight-custompermissions-capabilities-createandupdateonedriveaction)" : {{String}},
  "[CreateAndUpdateOneDriveKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-createandupdateonedriveknowledgebase)" : {{String}},
  "[CreateAndUpdateOpenAPIAction](#cfn-quicksight-custompermissions-capabilities-createandupdateopenapiaction)" : {{String}},
  "[CreateAndUpdatePagerDutyAction](#cfn-quicksight-custompermissions-capabilities-createandupdatepagerdutyaction)" : {{String}},
  "[CreateAndUpdateQBusinessKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-createandupdateqbusinessknowledgebase)" : {{String}},
  "[CreateAndUpdateS3KnowledgeBase](#cfn-quicksight-custompermissions-capabilities-createandupdates3knowledgebase)" : {{String}},
  "[CreateAndUpdateSalesforceAction](#cfn-quicksight-custompermissions-capabilities-createandupdatesalesforceaction)" : {{String}},
  "[CreateAndUpdateSandPGlobalEnergyAction](#cfn-quicksight-custompermissions-capabilities-createandupdatesandpglobalenergyaction)" : {{String}},
  "[CreateAndUpdateSandPGMIAction](#cfn-quicksight-custompermissions-capabilities-createandupdatesandpgmiaction)" : {{String}},
  "[CreateAndUpdateSAPBillOfMaterialAction](#cfn-quicksight-custompermissions-capabilities-createandupdatesapbillofmaterialaction)" : {{String}},
  "[CreateAndUpdateSAPBusinessPartnerAction](#cfn-quicksight-custompermissions-capabilities-createandupdatesapbusinesspartneraction)" : {{String}},
  "[CreateAndUpdateSAPMaterialStockAction](#cfn-quicksight-custompermissions-capabilities-createandupdatesapmaterialstockaction)" : {{String}},
  "[CreateAndUpdateSAPPhysicalInventoryAction](#cfn-quicksight-custompermissions-capabilities-createandupdatesapphysicalinventoryaction)" : {{String}},
  "[CreateAndUpdateSAPProductMasterDataAction](#cfn-quicksight-custompermissions-capabilities-createandupdatesapproductmasterdataaction)" : {{String}},
  "[CreateAndUpdateServiceNowAction](#cfn-quicksight-custompermissions-capabilities-createandupdateservicenowaction)" : {{String}},
  "[CreateAndUpdateSharePointAction](#cfn-quicksight-custompermissions-capabilities-createandupdatesharepointaction)" : {{String}},
  "[CreateAndUpdateSharePointKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-createandupdatesharepointknowledgebase)" : {{String}},
  "[CreateAndUpdateSlackAction](#cfn-quicksight-custompermissions-capabilities-createandupdateslackaction)" : {{String}},
  "[CreateAndUpdateSmartsheetAction](#cfn-quicksight-custompermissions-capabilities-createandupdatesmartsheetaction)" : {{String}},
  "[CreateAndUpdateTextractAction](#cfn-quicksight-custompermissions-capabilities-createandupdatetextractaction)" : {{String}},
  "[CreateAndUpdateThemes](#cfn-quicksight-custompermissions-capabilities-createandupdatethemes)" : {{String}},
  "[CreateAndUpdateThresholdAlerts](#cfn-quicksight-custompermissions-capabilities-createandupdatethresholdalerts)" : {{String}},
  "[CreateAndUpdateWebCrawlerKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-createandupdatewebcrawlerknowledgebase)" : {{String}},
  "[CreateAndUpdateZendeskAction](#cfn-quicksight-custompermissions-capabilities-createandupdatezendeskaction)" : {{String}},
  "[CreateAthenaDataSource](#cfn-quicksight-custompermissions-capabilities-createathenadatasource)" : {{String}},
  "[CreateAuroraDataSource](#cfn-quicksight-custompermissions-capabilities-createauroradatasource)" : {{String}},
  "[CreateChatAgents](#cfn-quicksight-custompermissions-capabilities-createchatagents)" : {{String}},
  "[CreateDashboardExecutiveSummaryWithQ](#cfn-quicksight-custompermissions-capabilities-createdashboardexecutivesummarywithq)" : {{String}},
  "[CreateDatabricksDataSource](#cfn-quicksight-custompermissions-capabilities-createdatabricksdatasource)" : {{String}},
  "[CreateDb2DataSource](#cfn-quicksight-custompermissions-capabilities-createdb2datasource)" : {{String}},
  "[CreateDenodoDataSource](#cfn-quicksight-custompermissions-capabilities-createdenododatasource)" : {{String}},
  "[CreateDocumentDbDataSource](#cfn-quicksight-custompermissions-capabilities-createdocumentdbdatasource)" : {{String}},
  "[CreateDremioDataSource](#cfn-quicksight-custompermissions-capabilities-createdremiodatasource)" : {{String}},
  "[CreateDynamoDbDataSource](#cfn-quicksight-custompermissions-capabilities-createdynamodbdatasource)" : {{String}},
  "[CreateExasolDataSource](#cfn-quicksight-custompermissions-capabilities-createexasoldatasource)" : {{String}},
  "[CreateFileDataSource](#cfn-quicksight-custompermissions-capabilities-createfiledatasource)" : {{String}},
  "[CreateGitHubDataSource](#cfn-quicksight-custompermissions-capabilities-creategithubdatasource)" : {{String}},
  "[CreateGoogleAnalyticsDataSource](#cfn-quicksight-custompermissions-capabilities-creategoogleanalyticsdatasource)" : {{String}},
  "[CreateGoogleBigQueryDataSource](#cfn-quicksight-custompermissions-capabilities-creategooglebigquerydatasource)" : {{String}},
  "[CreateGoogleSheetsDataSource](#cfn-quicksight-custompermissions-capabilities-creategooglesheetsdatasource)" : {{String}},
  "[CreateImpalaDataSource](#cfn-quicksight-custompermissions-capabilities-createimpaladatasource)" : {{String}},
  "[CreateJiraDataSource](#cfn-quicksight-custompermissions-capabilities-createjiradatasource)" : {{String}},
  "[CreateMariaDbDataSource](#cfn-quicksight-custompermissions-capabilities-createmariadbdatasource)" : {{String}},
  "[CreateMongoAtlasDataSource](#cfn-quicksight-custompermissions-capabilities-createmongoatlasdatasource)" : {{String}},
  "[CreateMongoDbDataSource](#cfn-quicksight-custompermissions-capabilities-createmongodbdatasource)" : {{String}},
  "[CreateMySqlDataSource](#cfn-quicksight-custompermissions-capabilities-createmysqldatasource)" : {{String}},
  "[CreateOpenSearchDataSource](#cfn-quicksight-custompermissions-capabilities-createopensearchdatasource)" : {{String}},
  "[CreateOracleDataSource](#cfn-quicksight-custompermissions-capabilities-createoracledatasource)" : {{String}},
  "[CreatePayPalDataSource](#cfn-quicksight-custompermissions-capabilities-createpaypaldatasource)" : {{String}},
  "[CreatePostgreSqlDataSource](#cfn-quicksight-custompermissions-capabilities-createpostgresqldatasource)" : {{String}},
  "[CreatePrestoDataSource](#cfn-quicksight-custompermissions-capabilities-createprestodatasource)" : {{String}},
  "[CreateRadiantDataSource](#cfn-quicksight-custompermissions-capabilities-createradiantdatasource)" : {{String}},
  "[CreateRdsDataSource](#cfn-quicksight-custompermissions-capabilities-createrdsdatasource)" : {{String}},
  "[CreateRedshiftAutoDiscoveredDataSource](#cfn-quicksight-custompermissions-capabilities-createredshiftautodiscovereddatasource)" : {{String}},
  "[CreateRedshiftManualDataSource](#cfn-quicksight-custompermissions-capabilities-createredshiftmanualdatasource)" : {{String}},
  "[CreateS3AnalyticsDataSource](#cfn-quicksight-custompermissions-capabilities-creates3analyticsdatasource)" : {{String}},
  "[CreateS3DataSource](#cfn-quicksight-custompermissions-capabilities-creates3datasource)" : {{String}},
  "[CreateS3TablesDataSource](#cfn-quicksight-custompermissions-capabilities-creates3tablesdatasource)" : {{String}},
  "[CreateSalesforceDataSource](#cfn-quicksight-custompermissions-capabilities-createsalesforcedatasource)" : {{String}},
  "[CreateSapHanaDataSource](#cfn-quicksight-custompermissions-capabilities-createsaphanadatasource)" : {{String}},
  "[CreateServiceNowDataSource](#cfn-quicksight-custompermissions-capabilities-createservicenowdatasource)" : {{String}},
  "[CreateSharedFolders](#cfn-quicksight-custompermissions-capabilities-createsharedfolders)" : {{String}},
  "[CreateSnowflakeDataSource](#cfn-quicksight-custompermissions-capabilities-createsnowflakedatasource)" : {{String}},
  "[CreateSpaces](#cfn-quicksight-custompermissions-capabilities-createspaces)" : {{String}},
  "[CreateSparkDataSource](#cfn-quicksight-custompermissions-capabilities-createsparkdatasource)" : {{String}},
  "[CreateSPICEDataset](#cfn-quicksight-custompermissions-capabilities-createspicedataset)" : {{String}},
  "[CreateSqlServerDataSource](#cfn-quicksight-custompermissions-capabilities-createsqlserverdatasource)" : {{String}},
  "[CreateSquareDataSource](#cfn-quicksight-custompermissions-capabilities-createsquaredatasource)" : {{String}},
  "[CreateStarburstDataSource](#cfn-quicksight-custompermissions-capabilities-createstarburstdatasource)" : {{String}},
  "[CreateTeradataDataSource](#cfn-quicksight-custompermissions-capabilities-createteradatadatasource)" : {{String}},
  "[CreateTimestreamDataSource](#cfn-quicksight-custompermissions-capabilities-createtimestreamdatasource)" : {{String}},
  "[CreateTrinoDataSource](#cfn-quicksight-custompermissions-capabilities-createtrinodatasource)" : {{String}},
  "[CreateTwitterDataSource](#cfn-quicksight-custompermissions-capabilities-createtwitterdatasource)" : {{String}},
  "[Dashboard](#cfn-quicksight-custompermissions-capabilities-dashboard)" : {{String}},
  "[DatabricksDataSource](#cfn-quicksight-custompermissions-capabilities-databricksdatasource)" : {{String}},
  "[Db2DataSource](#cfn-quicksight-custompermissions-capabilities-db2datasource)" : {{String}},
  "[DenodoDataSource](#cfn-quicksight-custompermissions-capabilities-denododatasource)" : {{String}},
  "[DocumentDbDataSource](#cfn-quicksight-custompermissions-capabilities-documentdbdatasource)" : {{String}},
  "[DremioDataSource](#cfn-quicksight-custompermissions-capabilities-dremiodatasource)" : {{String}},
  "[DynamoDbDataSource](#cfn-quicksight-custompermissions-capabilities-dynamodbdatasource)" : {{String}},
  "[EditVisualWithQ](#cfn-quicksight-custompermissions-capabilities-editvisualwithq)" : {{String}},
  "[ExasolDataSource](#cfn-quicksight-custompermissions-capabilities-exasoldatasource)" : {{String}},
  "[ExportToCsv](#cfn-quicksight-custompermissions-capabilities-exporttocsv)" : {{String}},
  "[ExportToCsvInScheduledReports](#cfn-quicksight-custompermissions-capabilities-exporttocsvinscheduledreports)" : {{String}},
  "[ExportToExcel](#cfn-quicksight-custompermissions-capabilities-exporttoexcel)" : {{String}},
  "[ExportToExcelInScheduledReports](#cfn-quicksight-custompermissions-capabilities-exporttoexcelinscheduledreports)" : {{String}},
  "[ExportToPdf](#cfn-quicksight-custompermissions-capabilities-exporttopdf)" : {{String}},
  "[ExportToPdfInScheduledReports](#cfn-quicksight-custompermissions-capabilities-exporttopdfinscheduledreports)" : {{String}},
  "[Extension](#cfn-quicksight-custompermissions-capabilities-extension)" : {{String}},
  "[FactSetAction](#cfn-quicksight-custompermissions-capabilities-factsetaction)" : {{String}},
  "[FileDataSource](#cfn-quicksight-custompermissions-capabilities-filedatasource)" : {{String}},
  "[Flow](#cfn-quicksight-custompermissions-capabilities-flow)" : {{String}},
  "[GenericHTTPAction](#cfn-quicksight-custompermissions-capabilities-generichttpaction)" : {{String}},
  "[GithubAction](#cfn-quicksight-custompermissions-capabilities-githubaction)" : {{String}},
  "[GitHubDataSource](#cfn-quicksight-custompermissions-capabilities-githubdatasource)" : {{String}},
  "[GoogleAnalyticsDataSource](#cfn-quicksight-custompermissions-capabilities-googleanalyticsdatasource)" : {{String}},
  "[GoogleBigQueryDataSource](#cfn-quicksight-custompermissions-capabilities-googlebigquerydatasource)" : {{String}},
  "[GoogleCalendarAction](#cfn-quicksight-custompermissions-capabilities-googlecalendaraction)" : {{String}},
  "[GoogleDriveKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-googledriveknowledgebase)" : {{String}},
  "[GoogleSheetsDataSource](#cfn-quicksight-custompermissions-capabilities-googlesheetsdatasource)" : {{String}},
  "[HubspotAction](#cfn-quicksight-custompermissions-capabilities-hubspotaction)" : {{String}},
  "[HuggingFaceAction](#cfn-quicksight-custompermissions-capabilities-huggingfaceaction)" : {{String}},
  "[IDCKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-idcknowledgebase)" : {{String}},
  "[ImpalaDataSource](#cfn-quicksight-custompermissions-capabilities-impaladatasource)" : {{String}},
  "[InboundEmailTrigger](#cfn-quicksight-custompermissions-capabilities-inboundemailtrigger)" : {{String}},
  "[IncludeContentInScheduledReportsEmail](#cfn-quicksight-custompermissions-capabilities-includecontentinscheduledreportsemail)" : {{String}},
  "[IntercomAction](#cfn-quicksight-custompermissions-capabilities-intercomaction)" : {{String}},
  "[InvokeAppsAIInference](#cfn-quicksight-custompermissions-capabilities-invokeappsaiinference)" : {{String}},
  "[JiraAction](#cfn-quicksight-custompermissions-capabilities-jiraaction)" : {{String}},
  "[JiraDataSource](#cfn-quicksight-custompermissions-capabilities-jiradatasource)" : {{String}},
  "[KnowledgeBase](#cfn-quicksight-custompermissions-capabilities-knowledgebase)" : {{String}},
  "[LinearAction](#cfn-quicksight-custompermissions-capabilities-linearaction)" : {{String}},
  "[ManageSharedFolders](#cfn-quicksight-custompermissions-capabilities-managesharedfolders)" : {{String}},
  "[MariaDbDataSource](#cfn-quicksight-custompermissions-capabilities-mariadbdatasource)" : {{String}},
  "[MCPAction](#cfn-quicksight-custompermissions-capabilities-mcpaction)" : {{String}},
  "[MondayAction](#cfn-quicksight-custompermissions-capabilities-mondayaction)" : {{String}},
  "[MongoAtlasDataSource](#cfn-quicksight-custompermissions-capabilities-mongoatlasdatasource)" : {{String}},
  "[MongoDbDataSource](#cfn-quicksight-custompermissions-capabilities-mongodbdatasource)" : {{String}},
  "[MSExchangeAction](#cfn-quicksight-custompermissions-capabilities-msexchangeaction)" : {{String}},
  "[MSTeamsAction](#cfn-quicksight-custompermissions-capabilities-msteamsaction)" : {{String}},
  "[MySqlDataSource](#cfn-quicksight-custompermissions-capabilities-mysqldatasource)" : {{String}},
  "[NewRelicAction](#cfn-quicksight-custompermissions-capabilities-newrelicaction)" : {{String}},
  "[NotionAction](#cfn-quicksight-custompermissions-capabilities-notionaction)" : {{String}},
  "[OneDriveAction](#cfn-quicksight-custompermissions-capabilities-onedriveaction)" : {{String}},
  "[OneDriveKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-onedriveknowledgebase)" : {{String}},
  "[OpenAPIAction](#cfn-quicksight-custompermissions-capabilities-openapiaction)" : {{String}},
  "[OpenSearchDataSource](#cfn-quicksight-custompermissions-capabilities-opensearchdatasource)" : {{String}},
  "[OracleDataSource](#cfn-quicksight-custompermissions-capabilities-oracledatasource)" : {{String}},
  "[PagerDutyAction](#cfn-quicksight-custompermissions-capabilities-pagerdutyaction)" : {{String}},
  "[PayPalDataSource](#cfn-quicksight-custompermissions-capabilities-paypaldatasource)" : {{String}},
  "[PerformFlowUiTask](#cfn-quicksight-custompermissions-capabilities-performflowuitask)" : {{String}},
  "[PostgreSqlDataSource](#cfn-quicksight-custompermissions-capabilities-postgresqldatasource)" : {{String}},
  "[PrestoDataSource](#cfn-quicksight-custompermissions-capabilities-prestodatasource)" : {{String}},
  "[PrintReports](#cfn-quicksight-custompermissions-capabilities-printreports)" : {{String}},
  "[PublishWithoutApproval](#cfn-quicksight-custompermissions-capabilities-publishwithoutapproval)" : {{String}},
  "[QBusinessKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-qbusinessknowledgebase)" : {{String}},
  "[QuickEventTrigger](#cfn-quicksight-custompermissions-capabilities-quickeventtrigger)" : {{String}},
  "[RadiantDataSource](#cfn-quicksight-custompermissions-capabilities-radiantdatasource)" : {{String}},
  "[RdsDataSource](#cfn-quicksight-custompermissions-capabilities-rdsdatasource)" : {{String}},
  "[RedshiftAutoDiscoveredDataSource](#cfn-quicksight-custompermissions-capabilities-redshiftautodiscovereddatasource)" : {{String}},
  "[RedshiftManualDataSource](#cfn-quicksight-custompermissions-capabilities-redshiftmanualdatasource)" : {{String}},
  "[RenameSharedFolders](#cfn-quicksight-custompermissions-capabilities-renamesharedfolders)" : {{String}},
  "[Research](#cfn-quicksight-custompermissions-capabilities-research)" : {{String}},
  "[S3AnalyticsDataSource](#cfn-quicksight-custompermissions-capabilities-s3analyticsdatasource)" : {{String}},
  "[S3DataSource](#cfn-quicksight-custompermissions-capabilities-s3datasource)" : {{String}},
  "[S3KnowledgeBase](#cfn-quicksight-custompermissions-capabilities-s3knowledgebase)" : {{String}},
  "[S3TablesDataSource](#cfn-quicksight-custompermissions-capabilities-s3tablesdatasource)" : {{String}},
  "[SalesforceAction](#cfn-quicksight-custompermissions-capabilities-salesforceaction)" : {{String}},
  "[SalesforceDataSource](#cfn-quicksight-custompermissions-capabilities-salesforcedatasource)" : {{String}},
  "[SandPGlobalEnergyAction](#cfn-quicksight-custompermissions-capabilities-sandpglobalenergyaction)" : {{String}},
  "[SandPGMIAction](#cfn-quicksight-custompermissions-capabilities-sandpgmiaction)" : {{String}},
  "[SAPBillOfMaterialAction](#cfn-quicksight-custompermissions-capabilities-sapbillofmaterialaction)" : {{String}},
  "[SAPBusinessPartnerAction](#cfn-quicksight-custompermissions-capabilities-sapbusinesspartneraction)" : {{String}},
  "[SapHanaDataSource](#cfn-quicksight-custompermissions-capabilities-saphanadatasource)" : {{String}},
  "[SAPMaterialStockAction](#cfn-quicksight-custompermissions-capabilities-sapmaterialstockaction)" : {{String}},
  "[SAPPhysicalInventoryAction](#cfn-quicksight-custompermissions-capabilities-sapphysicalinventoryaction)" : {{String}},
  "[SAPProductMasterDataAction](#cfn-quicksight-custompermissions-capabilities-sapproductmasterdataaction)" : {{String}},
  "[ScheduleTrigger](#cfn-quicksight-custompermissions-capabilities-scheduletrigger)" : {{String}},
  "[ServiceNowAction](#cfn-quicksight-custompermissions-capabilities-servicenowaction)" : {{String}},
  "[ServiceNowDataSource](#cfn-quicksight-custompermissions-capabilities-servicenowdatasource)" : {{String}},
  "[ShareAdobeAnalyticsDataSource](#cfn-quicksight-custompermissions-capabilities-shareadobeanalyticsdatasource)" : {{String}},
  "[ShareAmazonBedrockARSAction](#cfn-quicksight-custompermissions-capabilities-shareamazonbedrockarsaction)" : {{String}},
  "[ShareAmazonBedrockFSAction](#cfn-quicksight-custompermissions-capabilities-shareamazonbedrockfsaction)" : {{String}},
  "[ShareAmazonBedrockKRSAction](#cfn-quicksight-custompermissions-capabilities-shareamazonbedrockkrsaction)" : {{String}},
  "[ShareAmazonSThreeAction](#cfn-quicksight-custompermissions-capabilities-shareamazonsthreeaction)" : {{String}},
  "[ShareAnalyses](#cfn-quicksight-custompermissions-capabilities-shareanalyses)" : {{String}},
  "[ShareApps](#cfn-quicksight-custompermissions-capabilities-shareapps)" : {{String}},
  "[ShareAsanaAction](#cfn-quicksight-custompermissions-capabilities-shareasanaaction)" : {{String}},
  "[ShareAthenaDataSource](#cfn-quicksight-custompermissions-capabilities-shareathenadatasource)" : {{String}},
  "[ShareAuroraDataSource](#cfn-quicksight-custompermissions-capabilities-shareauroradatasource)" : {{String}},
  "[ShareBambooHRAction](#cfn-quicksight-custompermissions-capabilities-sharebamboohraction)" : {{String}},
  "[ShareBedrockManagedKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-sharebedrockmanagedknowledgebase)" : {{String}},
  "[ShareBoxAgentAction](#cfn-quicksight-custompermissions-capabilities-shareboxagentaction)" : {{String}},
  "[ShareBoxKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-shareboxknowledgebase)" : {{String}},
  "[ShareCanvaAgentAction](#cfn-quicksight-custompermissions-capabilities-sharecanvaagentaction)" : {{String}},
  "[ShareChatAgents](#cfn-quicksight-custompermissions-capabilities-sharechatagents)" : {{String}},
  "[ShareComprehendAction](#cfn-quicksight-custompermissions-capabilities-sharecomprehendaction)" : {{String}},
  "[ShareComprehendMedicalAction](#cfn-quicksight-custompermissions-capabilities-sharecomprehendmedicalaction)" : {{String}},
  "[ShareConfluenceAction](#cfn-quicksight-custompermissions-capabilities-shareconfluenceaction)" : {{String}},
  "[ShareConfluenceKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-shareconfluenceknowledgebase)" : {{String}},
  "[ShareDashboards](#cfn-quicksight-custompermissions-capabilities-sharedashboards)" : {{String}},
  "[ShareDatabricksDataSource](#cfn-quicksight-custompermissions-capabilities-sharedatabricksdatasource)" : {{String}},
  "[ShareDatasets](#cfn-quicksight-custompermissions-capabilities-sharedatasets)" : {{String}},
  "[ShareDataSources](#cfn-quicksight-custompermissions-capabilities-sharedatasources)" : {{String}},
  "[ShareDb2DataSource](#cfn-quicksight-custompermissions-capabilities-sharedb2datasource)" : {{String}},
  "[ShareDenodoDataSource](#cfn-quicksight-custompermissions-capabilities-sharedenododatasource)" : {{String}},
  "[ShareDocumentDbDataSource](#cfn-quicksight-custompermissions-capabilities-sharedocumentdbdatasource)" : {{String}},
  "[ShareDremioDataSource](#cfn-quicksight-custompermissions-capabilities-sharedremiodatasource)" : {{String}},
  "[ShareDynamoDbDataSource](#cfn-quicksight-custompermissions-capabilities-sharedynamodbdatasource)" : {{String}},
  "[ShareExasolDataSource](#cfn-quicksight-custompermissions-capabilities-shareexasoldatasource)" : {{String}},
  "[ShareFactSetAction](#cfn-quicksight-custompermissions-capabilities-sharefactsetaction)" : {{String}},
  "[ShareFileDataSource](#cfn-quicksight-custompermissions-capabilities-sharefiledatasource)" : {{String}},
  "[ShareGenericHTTPAction](#cfn-quicksight-custompermissions-capabilities-sharegenerichttpaction)" : {{String}},
  "[ShareGithubAction](#cfn-quicksight-custompermissions-capabilities-sharegithubaction)" : {{String}},
  "[ShareGitHubDataSource](#cfn-quicksight-custompermissions-capabilities-sharegithubdatasource)" : {{String}},
  "[ShareGoogleAnalyticsDataSource](#cfn-quicksight-custompermissions-capabilities-sharegoogleanalyticsdatasource)" : {{String}},
  "[ShareGoogleBigQueryDataSource](#cfn-quicksight-custompermissions-capabilities-sharegooglebigquerydatasource)" : {{String}},
  "[ShareGoogleCalendarAction](#cfn-quicksight-custompermissions-capabilities-sharegooglecalendaraction)" : {{String}},
  "[ShareGoogleDriveKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-sharegoogledriveknowledgebase)" : {{String}},
  "[ShareGoogleSheetsDataSource](#cfn-quicksight-custompermissions-capabilities-sharegooglesheetsdatasource)" : {{String}},
  "[ShareHubspotAction](#cfn-quicksight-custompermissions-capabilities-sharehubspotaction)" : {{String}},
  "[ShareHuggingFaceAction](#cfn-quicksight-custompermissions-capabilities-sharehuggingfaceaction)" : {{String}},
  "[ShareIDCKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-shareidcknowledgebase)" : {{String}},
  "[ShareImpalaDataSource](#cfn-quicksight-custompermissions-capabilities-shareimpaladatasource)" : {{String}},
  "[ShareIntercomAction](#cfn-quicksight-custompermissions-capabilities-shareintercomaction)" : {{String}},
  "[ShareJiraAction](#cfn-quicksight-custompermissions-capabilities-sharejiraaction)" : {{String}},
  "[ShareJiraDataSource](#cfn-quicksight-custompermissions-capabilities-sharejiradatasource)" : {{String}},
  "[ShareKnowledgeBases](#cfn-quicksight-custompermissions-capabilities-shareknowledgebases)" : {{String}},
  "[ShareLinearAction](#cfn-quicksight-custompermissions-capabilities-sharelinearaction)" : {{String}},
  "[ShareMariaDbDataSource](#cfn-quicksight-custompermissions-capabilities-sharemariadbdatasource)" : {{String}},
  "[ShareMCPAction](#cfn-quicksight-custompermissions-capabilities-sharemcpaction)" : {{String}},
  "[ShareMondayAction](#cfn-quicksight-custompermissions-capabilities-sharemondayaction)" : {{String}},
  "[ShareMongoAtlasDataSource](#cfn-quicksight-custompermissions-capabilities-sharemongoatlasdatasource)" : {{String}},
  "[ShareMongoDbDataSource](#cfn-quicksight-custompermissions-capabilities-sharemongodbdatasource)" : {{String}},
  "[ShareMSExchangeAction](#cfn-quicksight-custompermissions-capabilities-sharemsexchangeaction)" : {{String}},
  "[ShareMSTeamsAction](#cfn-quicksight-custompermissions-capabilities-sharemsteamsaction)" : {{String}},
  "[ShareMySqlDataSource](#cfn-quicksight-custompermissions-capabilities-sharemysqldatasource)" : {{String}},
  "[ShareNewRelicAction](#cfn-quicksight-custompermissions-capabilities-sharenewrelicaction)" : {{String}},
  "[ShareNotionAction](#cfn-quicksight-custompermissions-capabilities-sharenotionaction)" : {{String}},
  "[ShareOneDriveAction](#cfn-quicksight-custompermissions-capabilities-shareonedriveaction)" : {{String}},
  "[ShareOneDriveKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-shareonedriveknowledgebase)" : {{String}},
  "[ShareOpenAPIAction](#cfn-quicksight-custompermissions-capabilities-shareopenapiaction)" : {{String}},
  "[ShareOpenSearchDataSource](#cfn-quicksight-custompermissions-capabilities-shareopensearchdatasource)" : {{String}},
  "[ShareOracleDataSource](#cfn-quicksight-custompermissions-capabilities-shareoracledatasource)" : {{String}},
  "[SharePagerDutyAction](#cfn-quicksight-custompermissions-capabilities-sharepagerdutyaction)" : {{String}},
  "[SharePayPalDataSource](#cfn-quicksight-custompermissions-capabilities-sharepaypaldatasource)" : {{String}},
  "[SharePointAction](#cfn-quicksight-custompermissions-capabilities-sharepointaction)" : {{String}},
  "[SharePointKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-sharepointknowledgebase)" : {{String}},
  "[SharePostgreSqlDataSource](#cfn-quicksight-custompermissions-capabilities-sharepostgresqldatasource)" : {{String}},
  "[SharePrestoDataSource](#cfn-quicksight-custompermissions-capabilities-shareprestodatasource)" : {{String}},
  "[ShareQBusinessKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-shareqbusinessknowledgebase)" : {{String}},
  "[ShareRadiantDataSource](#cfn-quicksight-custompermissions-capabilities-shareradiantdatasource)" : {{String}},
  "[ShareRdsDataSource](#cfn-quicksight-custompermissions-capabilities-sharerdsdatasource)" : {{String}},
  "[ShareRedshiftAutoDiscoveredDataSource](#cfn-quicksight-custompermissions-capabilities-shareredshiftautodiscovereddatasource)" : {{String}},
  "[ShareRedshiftManualDataSource](#cfn-quicksight-custompermissions-capabilities-shareredshiftmanualdatasource)" : {{String}},
  "[ShareS3AnalyticsDataSource](#cfn-quicksight-custompermissions-capabilities-shares3analyticsdatasource)" : {{String}},
  "[ShareS3DataSource](#cfn-quicksight-custompermissions-capabilities-shares3datasource)" : {{String}},
  "[ShareS3KnowledgeBase](#cfn-quicksight-custompermissions-capabilities-shares3knowledgebase)" : {{String}},
  "[ShareS3TablesDataSource](#cfn-quicksight-custompermissions-capabilities-shares3tablesdatasource)" : {{String}},
  "[ShareSalesforceAction](#cfn-quicksight-custompermissions-capabilities-sharesalesforceaction)" : {{String}},
  "[ShareSalesforceDataSource](#cfn-quicksight-custompermissions-capabilities-sharesalesforcedatasource)" : {{String}},
  "[ShareSandPGlobalEnergyAction](#cfn-quicksight-custompermissions-capabilities-sharesandpglobalenergyaction)" : {{String}},
  "[ShareSandPGMIAction](#cfn-quicksight-custompermissions-capabilities-sharesandpgmiaction)" : {{String}},
  "[ShareSAPBillOfMaterialAction](#cfn-quicksight-custompermissions-capabilities-sharesapbillofmaterialaction)" : {{String}},
  "[ShareSAPBusinessPartnerAction](#cfn-quicksight-custompermissions-capabilities-sharesapbusinesspartneraction)" : {{String}},
  "[ShareSapHanaDataSource](#cfn-quicksight-custompermissions-capabilities-sharesaphanadatasource)" : {{String}},
  "[ShareSAPMaterialStockAction](#cfn-quicksight-custompermissions-capabilities-sharesapmaterialstockaction)" : {{String}},
  "[ShareSAPPhysicalInventoryAction](#cfn-quicksight-custompermissions-capabilities-sharesapphysicalinventoryaction)" : {{String}},
  "[ShareSAPProductMasterDataAction](#cfn-quicksight-custompermissions-capabilities-sharesapproductmasterdataaction)" : {{String}},
  "[ShareServiceNowAction](#cfn-quicksight-custompermissions-capabilities-shareservicenowaction)" : {{String}},
  "[ShareServiceNowDataSource](#cfn-quicksight-custompermissions-capabilities-shareservicenowdatasource)" : {{String}},
  "[ShareSharePointAction](#cfn-quicksight-custompermissions-capabilities-sharesharepointaction)" : {{String}},
  "[ShareSharePointKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-sharesharepointknowledgebase)" : {{String}},
  "[ShareSlackAction](#cfn-quicksight-custompermissions-capabilities-shareslackaction)" : {{String}},
  "[ShareSmartsheetAction](#cfn-quicksight-custompermissions-capabilities-sharesmartsheetaction)" : {{String}},
  "[ShareSnowflakeDataSource](#cfn-quicksight-custompermissions-capabilities-sharesnowflakedatasource)" : {{String}},
  "[ShareSpaces](#cfn-quicksight-custompermissions-capabilities-sharespaces)" : {{String}},
  "[ShareSparkDataSource](#cfn-quicksight-custompermissions-capabilities-sharesparkdatasource)" : {{String}},
  "[ShareSqlServerDataSource](#cfn-quicksight-custompermissions-capabilities-sharesqlserverdatasource)" : {{String}},
  "[ShareSquareDataSource](#cfn-quicksight-custompermissions-capabilities-sharesquaredatasource)" : {{String}},
  "[ShareStarburstDataSource](#cfn-quicksight-custompermissions-capabilities-sharestarburstdatasource)" : {{String}},
  "[ShareTeradataDataSource](#cfn-quicksight-custompermissions-capabilities-shareteradatadatasource)" : {{String}},
  "[ShareTextractAction](#cfn-quicksight-custompermissions-capabilities-sharetextractaction)" : {{String}},
  "[ShareTimestreamDataSource](#cfn-quicksight-custompermissions-capabilities-sharetimestreamdatasource)" : {{String}},
  "[ShareTrinoDataSource](#cfn-quicksight-custompermissions-capabilities-sharetrinodatasource)" : {{String}},
  "[ShareTwitterDataSource](#cfn-quicksight-custompermissions-capabilities-sharetwitterdatasource)" : {{String}},
  "[ShareWebCrawlerKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-sharewebcrawlerknowledgebase)" : {{String}},
  "[ShareZendeskAction](#cfn-quicksight-custompermissions-capabilities-sharezendeskaction)" : {{String}},
  "[SlackAction](#cfn-quicksight-custompermissions-capabilities-slackaction)" : {{String}},
  "[SmartsheetAction](#cfn-quicksight-custompermissions-capabilities-smartsheetaction)" : {{String}},
  "[SnowflakeDataSource](#cfn-quicksight-custompermissions-capabilities-snowflakedatasource)" : {{String}},
  "[Space](#cfn-quicksight-custompermissions-capabilities-space)" : {{String}},
  "[SparkDataSource](#cfn-quicksight-custompermissions-capabilities-sparkdatasource)" : {{String}},
  "[SqlServerDataSource](#cfn-quicksight-custompermissions-capabilities-sqlserverdatasource)" : {{String}},
  "[SquareDataSource](#cfn-quicksight-custompermissions-capabilities-squaredatasource)" : {{String}},
  "[StarburstDataSource](#cfn-quicksight-custompermissions-capabilities-starburstdatasource)" : {{String}},
  "[SubscribeDashboardEmailReports](#cfn-quicksight-custompermissions-capabilities-subscribedashboardemailreports)" : {{String}},
  "[TeradataDataSource](#cfn-quicksight-custompermissions-capabilities-teradatadatasource)" : {{String}},
  "[TextractAction](#cfn-quicksight-custompermissions-capabilities-textractaction)" : {{String}},
  "[TimestreamDataSource](#cfn-quicksight-custompermissions-capabilities-timestreamdatasource)" : {{String}},
  "[Topic](#cfn-quicksight-custompermissions-capabilities-topic)" : {{String}},
  "[Trigger](#cfn-quicksight-custompermissions-capabilities-trigger)" : {{String}},
  "[TrinoDataSource](#cfn-quicksight-custompermissions-capabilities-trinodatasource)" : {{String}},
  "[TwitterDataSource](#cfn-quicksight-custompermissions-capabilities-twitterdatasource)" : {{String}},
  "[UpdateAdobeAnalyticsDataSource](#cfn-quicksight-custompermissions-capabilities-updateadobeanalyticsdatasource)" : {{String}},
  "[UpdateAthenaDataSource](#cfn-quicksight-custompermissions-capabilities-updateathenadatasource)" : {{String}},
  "[UpdateAuroraDataSource](#cfn-quicksight-custompermissions-capabilities-updateauroradatasource)" : {{String}},
  "[UpdateDatabricksDataSource](#cfn-quicksight-custompermissions-capabilities-updatedatabricksdatasource)" : {{String}},
  "[UpdateDb2DataSource](#cfn-quicksight-custompermissions-capabilities-updatedb2datasource)" : {{String}},
  "[UpdateDenodoDataSource](#cfn-quicksight-custompermissions-capabilities-updatedenododatasource)" : {{String}},
  "[UpdateDocumentDbDataSource](#cfn-quicksight-custompermissions-capabilities-updatedocumentdbdatasource)" : {{String}},
  "[UpdateDremioDataSource](#cfn-quicksight-custompermissions-capabilities-updatedremiodatasource)" : {{String}},
  "[UpdateDynamoDbDataSource](#cfn-quicksight-custompermissions-capabilities-updatedynamodbdatasource)" : {{String}},
  "[UpdateExasolDataSource](#cfn-quicksight-custompermissions-capabilities-updateexasoldatasource)" : {{String}},
  "[UpdateFileDataSource](#cfn-quicksight-custompermissions-capabilities-updatefiledatasource)" : {{String}},
  "[UpdateGitHubDataSource](#cfn-quicksight-custompermissions-capabilities-updategithubdatasource)" : {{String}},
  "[UpdateGoogleAnalyticsDataSource](#cfn-quicksight-custompermissions-capabilities-updategoogleanalyticsdatasource)" : {{String}},
  "[UpdateGoogleBigQueryDataSource](#cfn-quicksight-custompermissions-capabilities-updategooglebigquerydatasource)" : {{String}},
  "[UpdateGoogleSheetsDataSource](#cfn-quicksight-custompermissions-capabilities-updategooglesheetsdatasource)" : {{String}},
  "[UpdateImpalaDataSource](#cfn-quicksight-custompermissions-capabilities-updateimpaladatasource)" : {{String}},
  "[UpdateJiraDataSource](#cfn-quicksight-custompermissions-capabilities-updatejiradatasource)" : {{String}},
  "[UpdateMariaDbDataSource](#cfn-quicksight-custompermissions-capabilities-updatemariadbdatasource)" : {{String}},
  "[UpdateMongoAtlasDataSource](#cfn-quicksight-custompermissions-capabilities-updatemongoatlasdatasource)" : {{String}},
  "[UpdateMongoDbDataSource](#cfn-quicksight-custompermissions-capabilities-updatemongodbdatasource)" : {{String}},
  "[UpdateMySqlDataSource](#cfn-quicksight-custompermissions-capabilities-updatemysqldatasource)" : {{String}},
  "[UpdateOpenSearchDataSource](#cfn-quicksight-custompermissions-capabilities-updateopensearchdatasource)" : {{String}},
  "[UpdateOracleDataSource](#cfn-quicksight-custompermissions-capabilities-updateoracledatasource)" : {{String}},
  "[UpdatePayPalDataSource](#cfn-quicksight-custompermissions-capabilities-updatepaypaldatasource)" : {{String}},
  "[UpdatePostgreSqlDataSource](#cfn-quicksight-custompermissions-capabilities-updatepostgresqldatasource)" : {{String}},
  "[UpdatePrestoDataSource](#cfn-quicksight-custompermissions-capabilities-updateprestodatasource)" : {{String}},
  "[UpdateRadiantDataSource](#cfn-quicksight-custompermissions-capabilities-updateradiantdatasource)" : {{String}},
  "[UpdateRdsDataSource](#cfn-quicksight-custompermissions-capabilities-updaterdsdatasource)" : {{String}},
  "[UpdateRedshiftAutoDiscoveredDataSource](#cfn-quicksight-custompermissions-capabilities-updateredshiftautodiscovereddatasource)" : {{String}},
  "[UpdateRedshiftManualDataSource](#cfn-quicksight-custompermissions-capabilities-updateredshiftmanualdatasource)" : {{String}},
  "[UpdateS3AnalyticsDataSource](#cfn-quicksight-custompermissions-capabilities-updates3analyticsdatasource)" : {{String}},
  "[UpdateS3DataSource](#cfn-quicksight-custompermissions-capabilities-updates3datasource)" : {{String}},
  "[UpdateS3TablesDataSource](#cfn-quicksight-custompermissions-capabilities-updates3tablesdatasource)" : {{String}},
  "[UpdateSalesforceDataSource](#cfn-quicksight-custompermissions-capabilities-updatesalesforcedatasource)" : {{String}},
  "[UpdateSapHanaDataSource](#cfn-quicksight-custompermissions-capabilities-updatesaphanadatasource)" : {{String}},
  "[UpdateServiceNowDataSource](#cfn-quicksight-custompermissions-capabilities-updateservicenowdatasource)" : {{String}},
  "[UpdateSnowflakeDataSource](#cfn-quicksight-custompermissions-capabilities-updatesnowflakedatasource)" : {{String}},
  "[UpdateSparkDataSource](#cfn-quicksight-custompermissions-capabilities-updatesparkdatasource)" : {{String}},
  "[UpdateSqlServerDataSource](#cfn-quicksight-custompermissions-capabilities-updatesqlserverdatasource)" : {{String}},
  "[UpdateSquareDataSource](#cfn-quicksight-custompermissions-capabilities-updatesquaredatasource)" : {{String}},
  "[UpdateStarburstDataSource](#cfn-quicksight-custompermissions-capabilities-updatestarburstdatasource)" : {{String}},
  "[UpdateTeradataDataSource](#cfn-quicksight-custompermissions-capabilities-updateteradatadatasource)" : {{String}},
  "[UpdateTimestreamDataSource](#cfn-quicksight-custompermissions-capabilities-updatetimestreamdatasource)" : {{String}},
  "[UpdateTrinoDataSource](#cfn-quicksight-custompermissions-capabilities-updatetrinodatasource)" : {{String}},
  "[UpdateTwitterDataSource](#cfn-quicksight-custompermissions-capabilities-updatetwitterdatasource)" : {{String}},
  "[UseAgentWebSearch](#cfn-quicksight-custompermissions-capabilities-useagentwebsearch)" : {{String}},
  "[UseAmazonBedrockARSAction](#cfn-quicksight-custompermissions-capabilities-useamazonbedrockarsaction)" : {{String}},
  "[UseAmazonBedrockFSAction](#cfn-quicksight-custompermissions-capabilities-useamazonbedrockfsaction)" : {{String}},
  "[UseAmazonBedrockKRSAction](#cfn-quicksight-custompermissions-capabilities-useamazonbedrockkrsaction)" : {{String}},
  "[UseAmazonSThreeAction](#cfn-quicksight-custompermissions-capabilities-useamazonsthreeaction)" : {{String}},
  "[UseAsanaAction](#cfn-quicksight-custompermissions-capabilities-useasanaaction)" : {{String}},
  "[UseBambooHRAction](#cfn-quicksight-custompermissions-capabilities-usebamboohraction)" : {{String}},
  "[UseBedrockManagedKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-usebedrockmanagedknowledgebase)" : {{String}},
  "[UseBedrockModels](#cfn-quicksight-custompermissions-capabilities-usebedrockmodels)" : {{String}},
  "[UseBoxAgentAction](#cfn-quicksight-custompermissions-capabilities-useboxagentaction)" : {{String}},
  "[UseBoxKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-useboxknowledgebase)" : {{String}},
  "[UseBrowserExtension](#cfn-quicksight-custompermissions-capabilities-usebrowserextension)" : {{String}},
  "[UseCanvaAgentAction](#cfn-quicksight-custompermissions-capabilities-usecanvaagentaction)" : {{String}},
  "[UseComprehendAction](#cfn-quicksight-custompermissions-capabilities-usecomprehendaction)" : {{String}},
  "[UseComprehendMedicalAction](#cfn-quicksight-custompermissions-capabilities-usecomprehendmedicalaction)" : {{String}},
  "[UseConfluenceAction](#cfn-quicksight-custompermissions-capabilities-useconfluenceaction)" : {{String}},
  "[UseConfluenceKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-useconfluenceknowledgebase)" : {{String}},
  "[UseExcelAddInExtension](#cfn-quicksight-custompermissions-capabilities-useexceladdinextension)" : {{String}},
  "[UseFactSetAction](#cfn-quicksight-custompermissions-capabilities-usefactsetaction)" : {{String}},
  "[UseGenericHTTPAction](#cfn-quicksight-custompermissions-capabilities-usegenerichttpaction)" : {{String}},
  "[UseGithubAction](#cfn-quicksight-custompermissions-capabilities-usegithubaction)" : {{String}},
  "[UseGoogleCalendarAction](#cfn-quicksight-custompermissions-capabilities-usegooglecalendaraction)" : {{String}},
  "[UseGoogleDriveKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-usegoogledriveknowledgebase)" : {{String}},
  "[UseHubspotAction](#cfn-quicksight-custompermissions-capabilities-usehubspotaction)" : {{String}},
  "[UseHuggingFaceAction](#cfn-quicksight-custompermissions-capabilities-usehuggingfaceaction)" : {{String}},
  "[UseIDCKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-useidcknowledgebase)" : {{String}},
  "[UseIntercomAction](#cfn-quicksight-custompermissions-capabilities-useintercomaction)" : {{String}},
  "[UseJiraAction](#cfn-quicksight-custompermissions-capabilities-usejiraaction)" : {{String}},
  "[UseLinearAction](#cfn-quicksight-custompermissions-capabilities-uselinearaction)" : {{String}},
  "[UseMCPAction](#cfn-quicksight-custompermissions-capabilities-usemcpaction)" : {{String}},
  "[UseMondayAction](#cfn-quicksight-custompermissions-capabilities-usemondayaction)" : {{String}},
  "[UseMSExchangeAction](#cfn-quicksight-custompermissions-capabilities-usemsexchangeaction)" : {{String}},
  "[UseMSTeamsAction](#cfn-quicksight-custompermissions-capabilities-usemsteamsaction)" : {{String}},
  "[UseNewRelicAction](#cfn-quicksight-custompermissions-capabilities-usenewrelicaction)" : {{String}},
  "[UseNotionAction](#cfn-quicksight-custompermissions-capabilities-usenotionaction)" : {{String}},
  "[UseOneDriveAction](#cfn-quicksight-custompermissions-capabilities-useonedriveaction)" : {{String}},
  "[UseOneDriveKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-useonedriveknowledgebase)" : {{String}},
  "[UseOpenAPIAction](#cfn-quicksight-custompermissions-capabilities-useopenapiaction)" : {{String}},
  "[UseOutlookAddInExtension](#cfn-quicksight-custompermissions-capabilities-useoutlookaddinextension)" : {{String}},
  "[UsePagerDutyAction](#cfn-quicksight-custompermissions-capabilities-usepagerdutyaction)" : {{String}},
  "[UsePowerpointAddInExtension](#cfn-quicksight-custompermissions-capabilities-usepowerpointaddinextension)" : {{String}},
  "[UseQBusinessKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-useqbusinessknowledgebase)" : {{String}},
  "[UseS3KnowledgeBase](#cfn-quicksight-custompermissions-capabilities-uses3knowledgebase)" : {{String}},
  "[UseSalesforceAction](#cfn-quicksight-custompermissions-capabilities-usesalesforceaction)" : {{String}},
  "[UseSandPGlobalEnergyAction](#cfn-quicksight-custompermissions-capabilities-usesandpglobalenergyaction)" : {{String}},
  "[UseSandPGMIAction](#cfn-quicksight-custompermissions-capabilities-usesandpgmiaction)" : {{String}},
  "[UseSAPBillOfMaterialAction](#cfn-quicksight-custompermissions-capabilities-usesapbillofmaterialaction)" : {{String}},
  "[UseSAPBusinessPartnerAction](#cfn-quicksight-custompermissions-capabilities-usesapbusinesspartneraction)" : {{String}},
  "[UseSAPMaterialStockAction](#cfn-quicksight-custompermissions-capabilities-usesapmaterialstockaction)" : {{String}},
  "[UseSAPPhysicalInventoryAction](#cfn-quicksight-custompermissions-capabilities-usesapphysicalinventoryaction)" : {{String}},
  "[UseSAPProductMasterDataAction](#cfn-quicksight-custompermissions-capabilities-usesapproductmasterdataaction)" : {{String}},
  "[UseServiceNowAction](#cfn-quicksight-custompermissions-capabilities-useservicenowaction)" : {{String}},
  "[UseSharePointAction](#cfn-quicksight-custompermissions-capabilities-usesharepointaction)" : {{String}},
  "[UseSharePointKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-usesharepointknowledgebase)" : {{String}},
  "[UseSlackAction](#cfn-quicksight-custompermissions-capabilities-useslackaction)" : {{String}},
  "[UseSmartsheetAction](#cfn-quicksight-custompermissions-capabilities-usesmartsheetaction)" : {{String}},
  "[UseTextractAction](#cfn-quicksight-custompermissions-capabilities-usetextractaction)" : {{String}},
  "[UseWebCrawlerKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-usewebcrawlerknowledgebase)" : {{String}},
  "[UseWordAddInExtension](#cfn-quicksight-custompermissions-capabilities-usewordaddinextension)" : {{String}},
  "[UseZendeskAction](#cfn-quicksight-custompermissions-capabilities-usezendeskaction)" : {{String}},
  "[ViewAccountSPICECapacity](#cfn-quicksight-custompermissions-capabilities-viewaccountspicecapacity)" : {{String}},
  "[WebCrawlerKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-webcrawlerknowledgebase)" : {{String}},
  "[ZendeskAction](#cfn-quicksight-custompermissions-capabilities-zendeskaction)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-custompermissions-capabilities-syntax.yaml"></a>

```
  [AccessAppsNativeDataStore](#cfn-quicksight-custompermissions-capabilities-accessappsnativedatastore): {{String}}
  [Action](#cfn-quicksight-custompermissions-capabilities-action): {{String}}
  [AddOrRunAnomalyDetectionForAnalyses](#cfn-quicksight-custompermissions-capabilities-addorrunanomalydetectionforanalyses): {{String}}
  [AdobeAnalyticsDataSource](#cfn-quicksight-custompermissions-capabilities-adobeanalyticsdatasource): {{String}}
  [AmazonBedrockARSAction](#cfn-quicksight-custompermissions-capabilities-amazonbedrockarsaction): {{String}}
  [AmazonBedrockFSAction](#cfn-quicksight-custompermissions-capabilities-amazonbedrockfsaction): {{String}}
  [AmazonBedrockKRSAction](#cfn-quicksight-custompermissions-capabilities-amazonbedrockkrsaction): {{String}}
  [AmazonSThreeAction](#cfn-quicksight-custompermissions-capabilities-amazonsthreeaction): {{String}}
  [Analysis](#cfn-quicksight-custompermissions-capabilities-analysis): {{String}}
  [ApproveFlowShareRequests](#cfn-quicksight-custompermissions-capabilities-approveflowsharerequests): {{String}}
  [Apps](#cfn-quicksight-custompermissions-capabilities-apps): {{String}}
  [AsanaAction](#cfn-quicksight-custompermissions-capabilities-asanaaction): {{String}}
  [AthenaDataSource](#cfn-quicksight-custompermissions-capabilities-athenadatasource): {{String}}
  [AuroraDataSource](#cfn-quicksight-custompermissions-capabilities-auroradatasource): {{String}}
  [Automate](#cfn-quicksight-custompermissions-capabilities-automate): {{String}}
  [BambooHRAction](#cfn-quicksight-custompermissions-capabilities-bamboohraction): {{String}}
  [BedrockManagedKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-bedrockmanagedknowledgebase): {{String}}
  [BoxAgentAction](#cfn-quicksight-custompermissions-capabilities-boxagentaction): {{String}}
  [BoxKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-boxknowledgebase): {{String}}
  [BuildCalculatedFieldWithQ](#cfn-quicksight-custompermissions-capabilities-buildcalculatedfieldwithq): {{String}}
  [CanvaAgentAction](#cfn-quicksight-custompermissions-capabilities-canvaagentaction): {{String}}
  [ChatAgent](#cfn-quicksight-custompermissions-capabilities-chatagent): {{String}}
  [ComprehendAction](#cfn-quicksight-custompermissions-capabilities-comprehendaction): {{String}}
  [ComprehendMedicalAction](#cfn-quicksight-custompermissions-capabilities-comprehendmedicalaction): {{String}}
  [ConfluenceAction](#cfn-quicksight-custompermissions-capabilities-confluenceaction): {{String}}
  [ConfluenceKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-confluenceknowledgebase): {{String}}
  [CreateAdobeAnalyticsDataSource](#cfn-quicksight-custompermissions-capabilities-createadobeanalyticsdatasource): {{String}}
  [CreateAndUpdateAmazonBedrockARSAction](#cfn-quicksight-custompermissions-capabilities-createandupdateamazonbedrockarsaction): {{String}}
  [CreateAndUpdateAmazonBedrockFSAction](#cfn-quicksight-custompermissions-capabilities-createandupdateamazonbedrockfsaction): {{String}}
  [CreateAndUpdateAmazonBedrockKRSAction](#cfn-quicksight-custompermissions-capabilities-createandupdateamazonbedrockkrsaction): {{String}}
  [CreateAndUpdateAmazonSThreeAction](#cfn-quicksight-custompermissions-capabilities-createandupdateamazonsthreeaction): {{String}}
  [CreateAndUpdateApps](#cfn-quicksight-custompermissions-capabilities-createandupdateapps): {{String}}
  [CreateAndUpdateAsanaAction](#cfn-quicksight-custompermissions-capabilities-createandupdateasanaaction): {{String}}
  [CreateAndUpdateBambooHRAction](#cfn-quicksight-custompermissions-capabilities-createandupdatebamboohraction): {{String}}
  [CreateAndUpdateBedrockManagedKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-createandupdatebedrockmanagedknowledgebase): {{String}}
  [CreateAndUpdateBoxAgentAction](#cfn-quicksight-custompermissions-capabilities-createandupdateboxagentaction): {{String}}
  [CreateAndUpdateBoxKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-createandupdateboxknowledgebase): {{String}}
  [CreateAndUpdateCanvaAgentAction](#cfn-quicksight-custompermissions-capabilities-createandupdatecanvaagentaction): {{String}}
  [CreateAndUpdateComprehendAction](#cfn-quicksight-custompermissions-capabilities-createandupdatecomprehendaction): {{String}}
  [CreateAndUpdateComprehendMedicalAction](#cfn-quicksight-custompermissions-capabilities-createandupdatecomprehendmedicalaction): {{String}}
  [CreateAndUpdateConfluenceAction](#cfn-quicksight-custompermissions-capabilities-createandupdateconfluenceaction): {{String}}
  [CreateAndUpdateConfluenceKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-createandupdateconfluenceknowledgebase): {{String}}
  [CreateAndUpdateDashboardEmailReports](#cfn-quicksight-custompermissions-capabilities-createandupdatedashboardemailreports): {{String}}
  [CreateAndUpdateDatasets](#cfn-quicksight-custompermissions-capabilities-createandupdatedatasets): {{String}}
  [CreateAndUpdateDataSources](#cfn-quicksight-custompermissions-capabilities-createandupdatedatasources): {{String}}
  [CreateAndUpdateFactSetAction](#cfn-quicksight-custompermissions-capabilities-createandupdatefactsetaction): {{String}}
  [CreateAndUpdateGenericHTTPAction](#cfn-quicksight-custompermissions-capabilities-createandupdategenerichttpaction): {{String}}
  [CreateAndUpdateGithubAction](#cfn-quicksight-custompermissions-capabilities-createandupdategithubaction): {{String}}
  [CreateAndUpdateGoogleCalendarAction](#cfn-quicksight-custompermissions-capabilities-createandupdategooglecalendaraction): {{String}}
  [CreateAndUpdateGoogleDriveKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-createandupdategoogledriveknowledgebase): {{String}}
  [CreateAndUpdateHubspotAction](#cfn-quicksight-custompermissions-capabilities-createandupdatehubspotaction): {{String}}
  [CreateAndUpdateHuggingFaceAction](#cfn-quicksight-custompermissions-capabilities-createandupdatehuggingfaceaction): {{String}}
  [CreateAndUpdateIDCKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-createandupdateidcknowledgebase): {{String}}
  [CreateAndUpdateIntercomAction](#cfn-quicksight-custompermissions-capabilities-createandupdateintercomaction): {{String}}
  [CreateAndUpdateJiraAction](#cfn-quicksight-custompermissions-capabilities-createandupdatejiraaction): {{String}}
  [CreateAndUpdateKnowledgeBases](#cfn-quicksight-custompermissions-capabilities-createandupdateknowledgebases): {{String}}
  [CreateAndUpdateLinearAction](#cfn-quicksight-custompermissions-capabilities-createandupdatelinearaction): {{String}}
  [CreateAndUpdateMCPAction](#cfn-quicksight-custompermissions-capabilities-createandupdatemcpaction): {{String}}
  [CreateAndUpdateMondayAction](#cfn-quicksight-custompermissions-capabilities-createandupdatemondayaction): {{String}}
  [CreateAndUpdateMSExchangeAction](#cfn-quicksight-custompermissions-capabilities-createandupdatemsexchangeaction): {{String}}
  [CreateAndUpdateMSTeamsAction](#cfn-quicksight-custompermissions-capabilities-createandupdatemsteamsaction): {{String}}
  [CreateAndUpdateNewRelicAction](#cfn-quicksight-custompermissions-capabilities-createandupdatenewrelicaction): {{String}}
  [CreateAndUpdateNotionAction](#cfn-quicksight-custompermissions-capabilities-createandupdatenotionaction): {{String}}
  [CreateAndUpdateOneDriveAction](#cfn-quicksight-custompermissions-capabilities-createandupdateonedriveaction): {{String}}
  [CreateAndUpdateOneDriveKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-createandupdateonedriveknowledgebase): {{String}}
  [CreateAndUpdateOpenAPIAction](#cfn-quicksight-custompermissions-capabilities-createandupdateopenapiaction): {{String}}
  [CreateAndUpdatePagerDutyAction](#cfn-quicksight-custompermissions-capabilities-createandupdatepagerdutyaction): {{String}}
  [CreateAndUpdateQBusinessKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-createandupdateqbusinessknowledgebase): {{String}}
  [CreateAndUpdateS3KnowledgeBase](#cfn-quicksight-custompermissions-capabilities-createandupdates3knowledgebase): {{String}}
  [CreateAndUpdateSalesforceAction](#cfn-quicksight-custompermissions-capabilities-createandupdatesalesforceaction): {{String}}
  [CreateAndUpdateSandPGlobalEnergyAction](#cfn-quicksight-custompermissions-capabilities-createandupdatesandpglobalenergyaction): {{String}}
  [CreateAndUpdateSandPGMIAction](#cfn-quicksight-custompermissions-capabilities-createandupdatesandpgmiaction): {{String}}
  [CreateAndUpdateSAPBillOfMaterialAction](#cfn-quicksight-custompermissions-capabilities-createandupdatesapbillofmaterialaction): {{String}}
  [CreateAndUpdateSAPBusinessPartnerAction](#cfn-quicksight-custompermissions-capabilities-createandupdatesapbusinesspartneraction): {{String}}
  [CreateAndUpdateSAPMaterialStockAction](#cfn-quicksight-custompermissions-capabilities-createandupdatesapmaterialstockaction): {{String}}
  [CreateAndUpdateSAPPhysicalInventoryAction](#cfn-quicksight-custompermissions-capabilities-createandupdatesapphysicalinventoryaction): {{String}}
  [CreateAndUpdateSAPProductMasterDataAction](#cfn-quicksight-custompermissions-capabilities-createandupdatesapproductmasterdataaction): {{String}}
  [CreateAndUpdateServiceNowAction](#cfn-quicksight-custompermissions-capabilities-createandupdateservicenowaction): {{String}}
  [CreateAndUpdateSharePointAction](#cfn-quicksight-custompermissions-capabilities-createandupdatesharepointaction): {{String}}
  [CreateAndUpdateSharePointKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-createandupdatesharepointknowledgebase): {{String}}
  [CreateAndUpdateSlackAction](#cfn-quicksight-custompermissions-capabilities-createandupdateslackaction): {{String}}
  [CreateAndUpdateSmartsheetAction](#cfn-quicksight-custompermissions-capabilities-createandupdatesmartsheetaction): {{String}}
  [CreateAndUpdateTextractAction](#cfn-quicksight-custompermissions-capabilities-createandupdatetextractaction): {{String}}
  [CreateAndUpdateThemes](#cfn-quicksight-custompermissions-capabilities-createandupdatethemes): {{String}}
  [CreateAndUpdateThresholdAlerts](#cfn-quicksight-custompermissions-capabilities-createandupdatethresholdalerts): {{String}}
  [CreateAndUpdateWebCrawlerKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-createandupdatewebcrawlerknowledgebase): {{String}}
  [CreateAndUpdateZendeskAction](#cfn-quicksight-custompermissions-capabilities-createandupdatezendeskaction): {{String}}
  [CreateAthenaDataSource](#cfn-quicksight-custompermissions-capabilities-createathenadatasource): {{String}}
  [CreateAuroraDataSource](#cfn-quicksight-custompermissions-capabilities-createauroradatasource): {{String}}
  [CreateChatAgents](#cfn-quicksight-custompermissions-capabilities-createchatagents): {{String}}
  [CreateDashboardExecutiveSummaryWithQ](#cfn-quicksight-custompermissions-capabilities-createdashboardexecutivesummarywithq): {{String}}
  [CreateDatabricksDataSource](#cfn-quicksight-custompermissions-capabilities-createdatabricksdatasource): {{String}}
  [CreateDb2DataSource](#cfn-quicksight-custompermissions-capabilities-createdb2datasource): {{String}}
  [CreateDenodoDataSource](#cfn-quicksight-custompermissions-capabilities-createdenododatasource): {{String}}
  [CreateDocumentDbDataSource](#cfn-quicksight-custompermissions-capabilities-createdocumentdbdatasource): {{String}}
  [CreateDremioDataSource](#cfn-quicksight-custompermissions-capabilities-createdremiodatasource): {{String}}
  [CreateDynamoDbDataSource](#cfn-quicksight-custompermissions-capabilities-createdynamodbdatasource): {{String}}
  [CreateExasolDataSource](#cfn-quicksight-custompermissions-capabilities-createexasoldatasource): {{String}}
  [CreateFileDataSource](#cfn-quicksight-custompermissions-capabilities-createfiledatasource): {{String}}
  [CreateGitHubDataSource](#cfn-quicksight-custompermissions-capabilities-creategithubdatasource): {{String}}
  [CreateGoogleAnalyticsDataSource](#cfn-quicksight-custompermissions-capabilities-creategoogleanalyticsdatasource): {{String}}
  [CreateGoogleBigQueryDataSource](#cfn-quicksight-custompermissions-capabilities-creategooglebigquerydatasource): {{String}}
  [CreateGoogleSheetsDataSource](#cfn-quicksight-custompermissions-capabilities-creategooglesheetsdatasource): {{String}}
  [CreateImpalaDataSource](#cfn-quicksight-custompermissions-capabilities-createimpaladatasource): {{String}}
  [CreateJiraDataSource](#cfn-quicksight-custompermissions-capabilities-createjiradatasource): {{String}}
  [CreateMariaDbDataSource](#cfn-quicksight-custompermissions-capabilities-createmariadbdatasource): {{String}}
  [CreateMongoAtlasDataSource](#cfn-quicksight-custompermissions-capabilities-createmongoatlasdatasource): {{String}}
  [CreateMongoDbDataSource](#cfn-quicksight-custompermissions-capabilities-createmongodbdatasource): {{String}}
  [CreateMySqlDataSource](#cfn-quicksight-custompermissions-capabilities-createmysqldatasource): {{String}}
  [CreateOpenSearchDataSource](#cfn-quicksight-custompermissions-capabilities-createopensearchdatasource): {{String}}
  [CreateOracleDataSource](#cfn-quicksight-custompermissions-capabilities-createoracledatasource): {{String}}
  [CreatePayPalDataSource](#cfn-quicksight-custompermissions-capabilities-createpaypaldatasource): {{String}}
  [CreatePostgreSqlDataSource](#cfn-quicksight-custompermissions-capabilities-createpostgresqldatasource): {{String}}
  [CreatePrestoDataSource](#cfn-quicksight-custompermissions-capabilities-createprestodatasource): {{String}}
  [CreateRadiantDataSource](#cfn-quicksight-custompermissions-capabilities-createradiantdatasource): {{String}}
  [CreateRdsDataSource](#cfn-quicksight-custompermissions-capabilities-createrdsdatasource): {{String}}
  [CreateRedshiftAutoDiscoveredDataSource](#cfn-quicksight-custompermissions-capabilities-createredshiftautodiscovereddatasource): {{String}}
  [CreateRedshiftManualDataSource](#cfn-quicksight-custompermissions-capabilities-createredshiftmanualdatasource): {{String}}
  [CreateS3AnalyticsDataSource](#cfn-quicksight-custompermissions-capabilities-creates3analyticsdatasource): {{String}}
  [CreateS3DataSource](#cfn-quicksight-custompermissions-capabilities-creates3datasource): {{String}}
  [CreateS3TablesDataSource](#cfn-quicksight-custompermissions-capabilities-creates3tablesdatasource): {{String}}
  [CreateSalesforceDataSource](#cfn-quicksight-custompermissions-capabilities-createsalesforcedatasource): {{String}}
  [CreateSapHanaDataSource](#cfn-quicksight-custompermissions-capabilities-createsaphanadatasource): {{String}}
  [CreateServiceNowDataSource](#cfn-quicksight-custompermissions-capabilities-createservicenowdatasource): {{String}}
  [CreateSharedFolders](#cfn-quicksight-custompermissions-capabilities-createsharedfolders): {{String}}
  [CreateSnowflakeDataSource](#cfn-quicksight-custompermissions-capabilities-createsnowflakedatasource): {{String}}
  [CreateSpaces](#cfn-quicksight-custompermissions-capabilities-createspaces): {{String}}
  [CreateSparkDataSource](#cfn-quicksight-custompermissions-capabilities-createsparkdatasource): {{String}}
  [CreateSPICEDataset](#cfn-quicksight-custompermissions-capabilities-createspicedataset): {{String}}
  [CreateSqlServerDataSource](#cfn-quicksight-custompermissions-capabilities-createsqlserverdatasource): {{String}}
  [CreateSquareDataSource](#cfn-quicksight-custompermissions-capabilities-createsquaredatasource): {{String}}
  [CreateStarburstDataSource](#cfn-quicksight-custompermissions-capabilities-createstarburstdatasource): {{String}}
  [CreateTeradataDataSource](#cfn-quicksight-custompermissions-capabilities-createteradatadatasource): {{String}}
  [CreateTimestreamDataSource](#cfn-quicksight-custompermissions-capabilities-createtimestreamdatasource): {{String}}
  [CreateTrinoDataSource](#cfn-quicksight-custompermissions-capabilities-createtrinodatasource): {{String}}
  [CreateTwitterDataSource](#cfn-quicksight-custompermissions-capabilities-createtwitterdatasource): {{String}}
  [Dashboard](#cfn-quicksight-custompermissions-capabilities-dashboard): {{String}}
  [DatabricksDataSource](#cfn-quicksight-custompermissions-capabilities-databricksdatasource): {{String}}
  [Db2DataSource](#cfn-quicksight-custompermissions-capabilities-db2datasource): {{String}}
  [DenodoDataSource](#cfn-quicksight-custompermissions-capabilities-denododatasource): {{String}}
  [DocumentDbDataSource](#cfn-quicksight-custompermissions-capabilities-documentdbdatasource): {{String}}
  [DremioDataSource](#cfn-quicksight-custompermissions-capabilities-dremiodatasource): {{String}}
  [DynamoDbDataSource](#cfn-quicksight-custompermissions-capabilities-dynamodbdatasource): {{String}}
  [EditVisualWithQ](#cfn-quicksight-custompermissions-capabilities-editvisualwithq): {{String}}
  [ExasolDataSource](#cfn-quicksight-custompermissions-capabilities-exasoldatasource): {{String}}
  [ExportToCsv](#cfn-quicksight-custompermissions-capabilities-exporttocsv): {{String}}
  [ExportToCsvInScheduledReports](#cfn-quicksight-custompermissions-capabilities-exporttocsvinscheduledreports): {{String}}
  [ExportToExcel](#cfn-quicksight-custompermissions-capabilities-exporttoexcel): {{String}}
  [ExportToExcelInScheduledReports](#cfn-quicksight-custompermissions-capabilities-exporttoexcelinscheduledreports): {{String}}
  [ExportToPdf](#cfn-quicksight-custompermissions-capabilities-exporttopdf): {{String}}
  [ExportToPdfInScheduledReports](#cfn-quicksight-custompermissions-capabilities-exporttopdfinscheduledreports): {{String}}
  [Extension](#cfn-quicksight-custompermissions-capabilities-extension): {{String}}
  [FactSetAction](#cfn-quicksight-custompermissions-capabilities-factsetaction): {{String}}
  [FileDataSource](#cfn-quicksight-custompermissions-capabilities-filedatasource): {{String}}
  [Flow](#cfn-quicksight-custompermissions-capabilities-flow): {{String}}
  [GenericHTTPAction](#cfn-quicksight-custompermissions-capabilities-generichttpaction): {{String}}
  [GithubAction](#cfn-quicksight-custompermissions-capabilities-githubaction): {{String}}
  [GitHubDataSource](#cfn-quicksight-custompermissions-capabilities-githubdatasource): {{String}}
  [GoogleAnalyticsDataSource](#cfn-quicksight-custompermissions-capabilities-googleanalyticsdatasource): {{String}}
  [GoogleBigQueryDataSource](#cfn-quicksight-custompermissions-capabilities-googlebigquerydatasource): {{String}}
  [GoogleCalendarAction](#cfn-quicksight-custompermissions-capabilities-googlecalendaraction): {{String}}
  [GoogleDriveKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-googledriveknowledgebase): {{String}}
  [GoogleSheetsDataSource](#cfn-quicksight-custompermissions-capabilities-googlesheetsdatasource): {{String}}
  [HubspotAction](#cfn-quicksight-custompermissions-capabilities-hubspotaction): {{String}}
  [HuggingFaceAction](#cfn-quicksight-custompermissions-capabilities-huggingfaceaction): {{String}}
  [IDCKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-idcknowledgebase): {{String}}
  [ImpalaDataSource](#cfn-quicksight-custompermissions-capabilities-impaladatasource): {{String}}
  [InboundEmailTrigger](#cfn-quicksight-custompermissions-capabilities-inboundemailtrigger): {{String}}
  [IncludeContentInScheduledReportsEmail](#cfn-quicksight-custompermissions-capabilities-includecontentinscheduledreportsemail): {{String}}
  [IntercomAction](#cfn-quicksight-custompermissions-capabilities-intercomaction): {{String}}
  [InvokeAppsAIInference](#cfn-quicksight-custompermissions-capabilities-invokeappsaiinference): {{String}}
  [JiraAction](#cfn-quicksight-custompermissions-capabilities-jiraaction): {{String}}
  [JiraDataSource](#cfn-quicksight-custompermissions-capabilities-jiradatasource): {{String}}
  [KnowledgeBase](#cfn-quicksight-custompermissions-capabilities-knowledgebase): {{String}}
  [LinearAction](#cfn-quicksight-custompermissions-capabilities-linearaction): {{String}}
  [ManageSharedFolders](#cfn-quicksight-custompermissions-capabilities-managesharedfolders): {{String}}
  [MariaDbDataSource](#cfn-quicksight-custompermissions-capabilities-mariadbdatasource): {{String}}
  [MCPAction](#cfn-quicksight-custompermissions-capabilities-mcpaction): {{String}}
  [MondayAction](#cfn-quicksight-custompermissions-capabilities-mondayaction): {{String}}
  [MongoAtlasDataSource](#cfn-quicksight-custompermissions-capabilities-mongoatlasdatasource): {{String}}
  [MongoDbDataSource](#cfn-quicksight-custompermissions-capabilities-mongodbdatasource): {{String}}
  [MSExchangeAction](#cfn-quicksight-custompermissions-capabilities-msexchangeaction): {{String}}
  [MSTeamsAction](#cfn-quicksight-custompermissions-capabilities-msteamsaction): {{String}}
  [MySqlDataSource](#cfn-quicksight-custompermissions-capabilities-mysqldatasource): {{String}}
  [NewRelicAction](#cfn-quicksight-custompermissions-capabilities-newrelicaction): {{String}}
  [NotionAction](#cfn-quicksight-custompermissions-capabilities-notionaction): {{String}}
  [OneDriveAction](#cfn-quicksight-custompermissions-capabilities-onedriveaction): {{String}}
  [OneDriveKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-onedriveknowledgebase): {{String}}
  [OpenAPIAction](#cfn-quicksight-custompermissions-capabilities-openapiaction): {{String}}
  [OpenSearchDataSource](#cfn-quicksight-custompermissions-capabilities-opensearchdatasource): {{String}}
  [OracleDataSource](#cfn-quicksight-custompermissions-capabilities-oracledatasource): {{String}}
  [PagerDutyAction](#cfn-quicksight-custompermissions-capabilities-pagerdutyaction): {{String}}
  [PayPalDataSource](#cfn-quicksight-custompermissions-capabilities-paypaldatasource): {{String}}
  [PerformFlowUiTask](#cfn-quicksight-custompermissions-capabilities-performflowuitask): {{String}}
  [PostgreSqlDataSource](#cfn-quicksight-custompermissions-capabilities-postgresqldatasource): {{String}}
  [PrestoDataSource](#cfn-quicksight-custompermissions-capabilities-prestodatasource): {{String}}
  [PrintReports](#cfn-quicksight-custompermissions-capabilities-printreports): {{String}}
  [PublishWithoutApproval](#cfn-quicksight-custompermissions-capabilities-publishwithoutapproval): {{String}}
  [QBusinessKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-qbusinessknowledgebase): {{String}}
  [QuickEventTrigger](#cfn-quicksight-custompermissions-capabilities-quickeventtrigger): {{String}}
  [RadiantDataSource](#cfn-quicksight-custompermissions-capabilities-radiantdatasource): {{String}}
  [RdsDataSource](#cfn-quicksight-custompermissions-capabilities-rdsdatasource): {{String}}
  [RedshiftAutoDiscoveredDataSource](#cfn-quicksight-custompermissions-capabilities-redshiftautodiscovereddatasource): {{String}}
  [RedshiftManualDataSource](#cfn-quicksight-custompermissions-capabilities-redshiftmanualdatasource): {{String}}
  [RenameSharedFolders](#cfn-quicksight-custompermissions-capabilities-renamesharedfolders): {{String}}
  [Research](#cfn-quicksight-custompermissions-capabilities-research): {{String}}
  [S3AnalyticsDataSource](#cfn-quicksight-custompermissions-capabilities-s3analyticsdatasource): {{String}}
  [S3DataSource](#cfn-quicksight-custompermissions-capabilities-s3datasource): {{String}}
  [S3KnowledgeBase](#cfn-quicksight-custompermissions-capabilities-s3knowledgebase): {{String}}
  [S3TablesDataSource](#cfn-quicksight-custompermissions-capabilities-s3tablesdatasource): {{String}}
  [SalesforceAction](#cfn-quicksight-custompermissions-capabilities-salesforceaction): {{String}}
  [SalesforceDataSource](#cfn-quicksight-custompermissions-capabilities-salesforcedatasource): {{String}}
  [SandPGlobalEnergyAction](#cfn-quicksight-custompermissions-capabilities-sandpglobalenergyaction): {{String}}
  [SandPGMIAction](#cfn-quicksight-custompermissions-capabilities-sandpgmiaction): {{String}}
  [SAPBillOfMaterialAction](#cfn-quicksight-custompermissions-capabilities-sapbillofmaterialaction): {{String}}
  [SAPBusinessPartnerAction](#cfn-quicksight-custompermissions-capabilities-sapbusinesspartneraction): {{String}}
  [SapHanaDataSource](#cfn-quicksight-custompermissions-capabilities-saphanadatasource): {{String}}
  [SAPMaterialStockAction](#cfn-quicksight-custompermissions-capabilities-sapmaterialstockaction): {{String}}
  [SAPPhysicalInventoryAction](#cfn-quicksight-custompermissions-capabilities-sapphysicalinventoryaction): {{String}}
  [SAPProductMasterDataAction](#cfn-quicksight-custompermissions-capabilities-sapproductmasterdataaction): {{String}}
  [ScheduleTrigger](#cfn-quicksight-custompermissions-capabilities-scheduletrigger): {{String}}
  [ServiceNowAction](#cfn-quicksight-custompermissions-capabilities-servicenowaction): {{String}}
  [ServiceNowDataSource](#cfn-quicksight-custompermissions-capabilities-servicenowdatasource): {{String}}
  [ShareAdobeAnalyticsDataSource](#cfn-quicksight-custompermissions-capabilities-shareadobeanalyticsdatasource): {{String}}
  [ShareAmazonBedrockARSAction](#cfn-quicksight-custompermissions-capabilities-shareamazonbedrockarsaction): {{String}}
  [ShareAmazonBedrockFSAction](#cfn-quicksight-custompermissions-capabilities-shareamazonbedrockfsaction): {{String}}
  [ShareAmazonBedrockKRSAction](#cfn-quicksight-custompermissions-capabilities-shareamazonbedrockkrsaction): {{String}}
  [ShareAmazonSThreeAction](#cfn-quicksight-custompermissions-capabilities-shareamazonsthreeaction): {{String}}
  [ShareAnalyses](#cfn-quicksight-custompermissions-capabilities-shareanalyses): {{String}}
  [ShareApps](#cfn-quicksight-custompermissions-capabilities-shareapps): {{String}}
  [ShareAsanaAction](#cfn-quicksight-custompermissions-capabilities-shareasanaaction): {{String}}
  [ShareAthenaDataSource](#cfn-quicksight-custompermissions-capabilities-shareathenadatasource): {{String}}
  [ShareAuroraDataSource](#cfn-quicksight-custompermissions-capabilities-shareauroradatasource): {{String}}
  [ShareBambooHRAction](#cfn-quicksight-custompermissions-capabilities-sharebamboohraction): {{String}}
  [ShareBedrockManagedKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-sharebedrockmanagedknowledgebase): {{String}}
  [ShareBoxAgentAction](#cfn-quicksight-custompermissions-capabilities-shareboxagentaction): {{String}}
  [ShareBoxKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-shareboxknowledgebase): {{String}}
  [ShareCanvaAgentAction](#cfn-quicksight-custompermissions-capabilities-sharecanvaagentaction): {{String}}
  [ShareChatAgents](#cfn-quicksight-custompermissions-capabilities-sharechatagents): {{String}}
  [ShareComprehendAction](#cfn-quicksight-custompermissions-capabilities-sharecomprehendaction): {{String}}
  [ShareComprehendMedicalAction](#cfn-quicksight-custompermissions-capabilities-sharecomprehendmedicalaction): {{String}}
  [ShareConfluenceAction](#cfn-quicksight-custompermissions-capabilities-shareconfluenceaction): {{String}}
  [ShareConfluenceKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-shareconfluenceknowledgebase): {{String}}
  [ShareDashboards](#cfn-quicksight-custompermissions-capabilities-sharedashboards): {{String}}
  [ShareDatabricksDataSource](#cfn-quicksight-custompermissions-capabilities-sharedatabricksdatasource): {{String}}
  [ShareDatasets](#cfn-quicksight-custompermissions-capabilities-sharedatasets): {{String}}
  [ShareDataSources](#cfn-quicksight-custompermissions-capabilities-sharedatasources): {{String}}
  [ShareDb2DataSource](#cfn-quicksight-custompermissions-capabilities-sharedb2datasource): {{String}}
  [ShareDenodoDataSource](#cfn-quicksight-custompermissions-capabilities-sharedenododatasource): {{String}}
  [ShareDocumentDbDataSource](#cfn-quicksight-custompermissions-capabilities-sharedocumentdbdatasource): {{String}}
  [ShareDremioDataSource](#cfn-quicksight-custompermissions-capabilities-sharedremiodatasource): {{String}}
  [ShareDynamoDbDataSource](#cfn-quicksight-custompermissions-capabilities-sharedynamodbdatasource): {{String}}
  [ShareExasolDataSource](#cfn-quicksight-custompermissions-capabilities-shareexasoldatasource): {{String}}
  [ShareFactSetAction](#cfn-quicksight-custompermissions-capabilities-sharefactsetaction): {{String}}
  [ShareFileDataSource](#cfn-quicksight-custompermissions-capabilities-sharefiledatasource): {{String}}
  [ShareGenericHTTPAction](#cfn-quicksight-custompermissions-capabilities-sharegenerichttpaction): {{String}}
  [ShareGithubAction](#cfn-quicksight-custompermissions-capabilities-sharegithubaction): {{String}}
  [ShareGitHubDataSource](#cfn-quicksight-custompermissions-capabilities-sharegithubdatasource): {{String}}
  [ShareGoogleAnalyticsDataSource](#cfn-quicksight-custompermissions-capabilities-sharegoogleanalyticsdatasource): {{String}}
  [ShareGoogleBigQueryDataSource](#cfn-quicksight-custompermissions-capabilities-sharegooglebigquerydatasource): {{String}}
  [ShareGoogleCalendarAction](#cfn-quicksight-custompermissions-capabilities-sharegooglecalendaraction): {{String}}
  [ShareGoogleDriveKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-sharegoogledriveknowledgebase): {{String}}
  [ShareGoogleSheetsDataSource](#cfn-quicksight-custompermissions-capabilities-sharegooglesheetsdatasource): {{String}}
  [ShareHubspotAction](#cfn-quicksight-custompermissions-capabilities-sharehubspotaction): {{String}}
  [ShareHuggingFaceAction](#cfn-quicksight-custompermissions-capabilities-sharehuggingfaceaction): {{String}}
  [ShareIDCKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-shareidcknowledgebase): {{String}}
  [ShareImpalaDataSource](#cfn-quicksight-custompermissions-capabilities-shareimpaladatasource): {{String}}
  [ShareIntercomAction](#cfn-quicksight-custompermissions-capabilities-shareintercomaction): {{String}}
  [ShareJiraAction](#cfn-quicksight-custompermissions-capabilities-sharejiraaction): {{String}}
  [ShareJiraDataSource](#cfn-quicksight-custompermissions-capabilities-sharejiradatasource): {{String}}
  [ShareKnowledgeBases](#cfn-quicksight-custompermissions-capabilities-shareknowledgebases): {{String}}
  [ShareLinearAction](#cfn-quicksight-custompermissions-capabilities-sharelinearaction): {{String}}
  [ShareMariaDbDataSource](#cfn-quicksight-custompermissions-capabilities-sharemariadbdatasource): {{String}}
  [ShareMCPAction](#cfn-quicksight-custompermissions-capabilities-sharemcpaction): {{String}}
  [ShareMondayAction](#cfn-quicksight-custompermissions-capabilities-sharemondayaction): {{String}}
  [ShareMongoAtlasDataSource](#cfn-quicksight-custompermissions-capabilities-sharemongoatlasdatasource): {{String}}
  [ShareMongoDbDataSource](#cfn-quicksight-custompermissions-capabilities-sharemongodbdatasource): {{String}}
  [ShareMSExchangeAction](#cfn-quicksight-custompermissions-capabilities-sharemsexchangeaction): {{String}}
  [ShareMSTeamsAction](#cfn-quicksight-custompermissions-capabilities-sharemsteamsaction): {{String}}
  [ShareMySqlDataSource](#cfn-quicksight-custompermissions-capabilities-sharemysqldatasource): {{String}}
  [ShareNewRelicAction](#cfn-quicksight-custompermissions-capabilities-sharenewrelicaction): {{String}}
  [ShareNotionAction](#cfn-quicksight-custompermissions-capabilities-sharenotionaction): {{String}}
  [ShareOneDriveAction](#cfn-quicksight-custompermissions-capabilities-shareonedriveaction): {{String}}
  [ShareOneDriveKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-shareonedriveknowledgebase): {{String}}
  [ShareOpenAPIAction](#cfn-quicksight-custompermissions-capabilities-shareopenapiaction): {{String}}
  [ShareOpenSearchDataSource](#cfn-quicksight-custompermissions-capabilities-shareopensearchdatasource): {{String}}
  [ShareOracleDataSource](#cfn-quicksight-custompermissions-capabilities-shareoracledatasource): {{String}}
  [SharePagerDutyAction](#cfn-quicksight-custompermissions-capabilities-sharepagerdutyaction): {{String}}
  [SharePayPalDataSource](#cfn-quicksight-custompermissions-capabilities-sharepaypaldatasource): {{String}}
  [SharePointAction](#cfn-quicksight-custompermissions-capabilities-sharepointaction): {{String}}
  [SharePointKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-sharepointknowledgebase): {{String}}
  [SharePostgreSqlDataSource](#cfn-quicksight-custompermissions-capabilities-sharepostgresqldatasource): {{String}}
  [SharePrestoDataSource](#cfn-quicksight-custompermissions-capabilities-shareprestodatasource): {{String}}
  [ShareQBusinessKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-shareqbusinessknowledgebase): {{String}}
  [ShareRadiantDataSource](#cfn-quicksight-custompermissions-capabilities-shareradiantdatasource): {{String}}
  [ShareRdsDataSource](#cfn-quicksight-custompermissions-capabilities-sharerdsdatasource): {{String}}
  [ShareRedshiftAutoDiscoveredDataSource](#cfn-quicksight-custompermissions-capabilities-shareredshiftautodiscovereddatasource): {{String}}
  [ShareRedshiftManualDataSource](#cfn-quicksight-custompermissions-capabilities-shareredshiftmanualdatasource): {{String}}
  [ShareS3AnalyticsDataSource](#cfn-quicksight-custompermissions-capabilities-shares3analyticsdatasource): {{String}}
  [ShareS3DataSource](#cfn-quicksight-custompermissions-capabilities-shares3datasource): {{String}}
  [ShareS3KnowledgeBase](#cfn-quicksight-custompermissions-capabilities-shares3knowledgebase): {{String}}
  [ShareS3TablesDataSource](#cfn-quicksight-custompermissions-capabilities-shares3tablesdatasource): {{String}}
  [ShareSalesforceAction](#cfn-quicksight-custompermissions-capabilities-sharesalesforceaction): {{String}}
  [ShareSalesforceDataSource](#cfn-quicksight-custompermissions-capabilities-sharesalesforcedatasource): {{String}}
  [ShareSandPGlobalEnergyAction](#cfn-quicksight-custompermissions-capabilities-sharesandpglobalenergyaction): {{String}}
  [ShareSandPGMIAction](#cfn-quicksight-custompermissions-capabilities-sharesandpgmiaction): {{String}}
  [ShareSAPBillOfMaterialAction](#cfn-quicksight-custompermissions-capabilities-sharesapbillofmaterialaction): {{String}}
  [ShareSAPBusinessPartnerAction](#cfn-quicksight-custompermissions-capabilities-sharesapbusinesspartneraction): {{String}}
  [ShareSapHanaDataSource](#cfn-quicksight-custompermissions-capabilities-sharesaphanadatasource): {{String}}
  [ShareSAPMaterialStockAction](#cfn-quicksight-custompermissions-capabilities-sharesapmaterialstockaction): {{String}}
  [ShareSAPPhysicalInventoryAction](#cfn-quicksight-custompermissions-capabilities-sharesapphysicalinventoryaction): {{String}}
  [ShareSAPProductMasterDataAction](#cfn-quicksight-custompermissions-capabilities-sharesapproductmasterdataaction): {{String}}
  [ShareServiceNowAction](#cfn-quicksight-custompermissions-capabilities-shareservicenowaction): {{String}}
  [ShareServiceNowDataSource](#cfn-quicksight-custompermissions-capabilities-shareservicenowdatasource): {{String}}
  [ShareSharePointAction](#cfn-quicksight-custompermissions-capabilities-sharesharepointaction): {{String}}
  [ShareSharePointKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-sharesharepointknowledgebase): {{String}}
  [ShareSlackAction](#cfn-quicksight-custompermissions-capabilities-shareslackaction): {{String}}
  [ShareSmartsheetAction](#cfn-quicksight-custompermissions-capabilities-sharesmartsheetaction): {{String}}
  [ShareSnowflakeDataSource](#cfn-quicksight-custompermissions-capabilities-sharesnowflakedatasource): {{String}}
  [ShareSpaces](#cfn-quicksight-custompermissions-capabilities-sharespaces): {{String}}
  [ShareSparkDataSource](#cfn-quicksight-custompermissions-capabilities-sharesparkdatasource): {{String}}
  [ShareSqlServerDataSource](#cfn-quicksight-custompermissions-capabilities-sharesqlserverdatasource): {{String}}
  [ShareSquareDataSource](#cfn-quicksight-custompermissions-capabilities-sharesquaredatasource): {{String}}
  [ShareStarburstDataSource](#cfn-quicksight-custompermissions-capabilities-sharestarburstdatasource): {{String}}
  [ShareTeradataDataSource](#cfn-quicksight-custompermissions-capabilities-shareteradatadatasource): {{String}}
  [ShareTextractAction](#cfn-quicksight-custompermissions-capabilities-sharetextractaction): {{String}}
  [ShareTimestreamDataSource](#cfn-quicksight-custompermissions-capabilities-sharetimestreamdatasource): {{String}}
  [ShareTrinoDataSource](#cfn-quicksight-custompermissions-capabilities-sharetrinodatasource): {{String}}
  [ShareTwitterDataSource](#cfn-quicksight-custompermissions-capabilities-sharetwitterdatasource): {{String}}
  [ShareWebCrawlerKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-sharewebcrawlerknowledgebase): {{String}}
  [ShareZendeskAction](#cfn-quicksight-custompermissions-capabilities-sharezendeskaction): {{String}}
  [SlackAction](#cfn-quicksight-custompermissions-capabilities-slackaction): {{String}}
  [SmartsheetAction](#cfn-quicksight-custompermissions-capabilities-smartsheetaction): {{String}}
  [SnowflakeDataSource](#cfn-quicksight-custompermissions-capabilities-snowflakedatasource): {{String}}
  [Space](#cfn-quicksight-custompermissions-capabilities-space): {{String}}
  [SparkDataSource](#cfn-quicksight-custompermissions-capabilities-sparkdatasource): {{String}}
  [SqlServerDataSource](#cfn-quicksight-custompermissions-capabilities-sqlserverdatasource): {{String}}
  [SquareDataSource](#cfn-quicksight-custompermissions-capabilities-squaredatasource): {{String}}
  [StarburstDataSource](#cfn-quicksight-custompermissions-capabilities-starburstdatasource): {{String}}
  [SubscribeDashboardEmailReports](#cfn-quicksight-custompermissions-capabilities-subscribedashboardemailreports): {{String}}
  [TeradataDataSource](#cfn-quicksight-custompermissions-capabilities-teradatadatasource): {{String}}
  [TextractAction](#cfn-quicksight-custompermissions-capabilities-textractaction): {{String}}
  [TimestreamDataSource](#cfn-quicksight-custompermissions-capabilities-timestreamdatasource): {{String}}
  [Topic](#cfn-quicksight-custompermissions-capabilities-topic): {{String}}
  [Trigger](#cfn-quicksight-custompermissions-capabilities-trigger): {{String}}
  [TrinoDataSource](#cfn-quicksight-custompermissions-capabilities-trinodatasource): {{String}}
  [TwitterDataSource](#cfn-quicksight-custompermissions-capabilities-twitterdatasource): {{String}}
  [UpdateAdobeAnalyticsDataSource](#cfn-quicksight-custompermissions-capabilities-updateadobeanalyticsdatasource): {{String}}
  [UpdateAthenaDataSource](#cfn-quicksight-custompermissions-capabilities-updateathenadatasource): {{String}}
  [UpdateAuroraDataSource](#cfn-quicksight-custompermissions-capabilities-updateauroradatasource): {{String}}
  [UpdateDatabricksDataSource](#cfn-quicksight-custompermissions-capabilities-updatedatabricksdatasource): {{String}}
  [UpdateDb2DataSource](#cfn-quicksight-custompermissions-capabilities-updatedb2datasource): {{String}}
  [UpdateDenodoDataSource](#cfn-quicksight-custompermissions-capabilities-updatedenododatasource): {{String}}
  [UpdateDocumentDbDataSource](#cfn-quicksight-custompermissions-capabilities-updatedocumentdbdatasource): {{String}}
  [UpdateDremioDataSource](#cfn-quicksight-custompermissions-capabilities-updatedremiodatasource): {{String}}
  [UpdateDynamoDbDataSource](#cfn-quicksight-custompermissions-capabilities-updatedynamodbdatasource): {{String}}
  [UpdateExasolDataSource](#cfn-quicksight-custompermissions-capabilities-updateexasoldatasource): {{String}}
  [UpdateFileDataSource](#cfn-quicksight-custompermissions-capabilities-updatefiledatasource): {{String}}
  [UpdateGitHubDataSource](#cfn-quicksight-custompermissions-capabilities-updategithubdatasource): {{String}}
  [UpdateGoogleAnalyticsDataSource](#cfn-quicksight-custompermissions-capabilities-updategoogleanalyticsdatasource): {{String}}
  [UpdateGoogleBigQueryDataSource](#cfn-quicksight-custompermissions-capabilities-updategooglebigquerydatasource): {{String}}
  [UpdateGoogleSheetsDataSource](#cfn-quicksight-custompermissions-capabilities-updategooglesheetsdatasource): {{String}}
  [UpdateImpalaDataSource](#cfn-quicksight-custompermissions-capabilities-updateimpaladatasource): {{String}}
  [UpdateJiraDataSource](#cfn-quicksight-custompermissions-capabilities-updatejiradatasource): {{String}}
  [UpdateMariaDbDataSource](#cfn-quicksight-custompermissions-capabilities-updatemariadbdatasource): {{String}}
  [UpdateMongoAtlasDataSource](#cfn-quicksight-custompermissions-capabilities-updatemongoatlasdatasource): {{String}}
  [UpdateMongoDbDataSource](#cfn-quicksight-custompermissions-capabilities-updatemongodbdatasource): {{String}}
  [UpdateMySqlDataSource](#cfn-quicksight-custompermissions-capabilities-updatemysqldatasource): {{String}}
  [UpdateOpenSearchDataSource](#cfn-quicksight-custompermissions-capabilities-updateopensearchdatasource): {{String}}
  [UpdateOracleDataSource](#cfn-quicksight-custompermissions-capabilities-updateoracledatasource): {{String}}
  [UpdatePayPalDataSource](#cfn-quicksight-custompermissions-capabilities-updatepaypaldatasource): {{String}}
  [UpdatePostgreSqlDataSource](#cfn-quicksight-custompermissions-capabilities-updatepostgresqldatasource): {{String}}
  [UpdatePrestoDataSource](#cfn-quicksight-custompermissions-capabilities-updateprestodatasource): {{String}}
  [UpdateRadiantDataSource](#cfn-quicksight-custompermissions-capabilities-updateradiantdatasource): {{String}}
  [UpdateRdsDataSource](#cfn-quicksight-custompermissions-capabilities-updaterdsdatasource): {{String}}
  [UpdateRedshiftAutoDiscoveredDataSource](#cfn-quicksight-custompermissions-capabilities-updateredshiftautodiscovereddatasource): {{String}}
  [UpdateRedshiftManualDataSource](#cfn-quicksight-custompermissions-capabilities-updateredshiftmanualdatasource): {{String}}
  [UpdateS3AnalyticsDataSource](#cfn-quicksight-custompermissions-capabilities-updates3analyticsdatasource): {{String}}
  [UpdateS3DataSource](#cfn-quicksight-custompermissions-capabilities-updates3datasource): {{String}}
  [UpdateS3TablesDataSource](#cfn-quicksight-custompermissions-capabilities-updates3tablesdatasource): {{String}}
  [UpdateSalesforceDataSource](#cfn-quicksight-custompermissions-capabilities-updatesalesforcedatasource): {{String}}
  [UpdateSapHanaDataSource](#cfn-quicksight-custompermissions-capabilities-updatesaphanadatasource): {{String}}
  [UpdateServiceNowDataSource](#cfn-quicksight-custompermissions-capabilities-updateservicenowdatasource): {{String}}
  [UpdateSnowflakeDataSource](#cfn-quicksight-custompermissions-capabilities-updatesnowflakedatasource): {{String}}
  [UpdateSparkDataSource](#cfn-quicksight-custompermissions-capabilities-updatesparkdatasource): {{String}}
  [UpdateSqlServerDataSource](#cfn-quicksight-custompermissions-capabilities-updatesqlserverdatasource): {{String}}
  [UpdateSquareDataSource](#cfn-quicksight-custompermissions-capabilities-updatesquaredatasource): {{String}}
  [UpdateStarburstDataSource](#cfn-quicksight-custompermissions-capabilities-updatestarburstdatasource): {{String}}
  [UpdateTeradataDataSource](#cfn-quicksight-custompermissions-capabilities-updateteradatadatasource): {{String}}
  [UpdateTimestreamDataSource](#cfn-quicksight-custompermissions-capabilities-updatetimestreamdatasource): {{String}}
  [UpdateTrinoDataSource](#cfn-quicksight-custompermissions-capabilities-updatetrinodatasource): {{String}}
  [UpdateTwitterDataSource](#cfn-quicksight-custompermissions-capabilities-updatetwitterdatasource): {{String}}
  [UseAgentWebSearch](#cfn-quicksight-custompermissions-capabilities-useagentwebsearch): {{String}}
  [UseAmazonBedrockARSAction](#cfn-quicksight-custompermissions-capabilities-useamazonbedrockarsaction): {{String}}
  [UseAmazonBedrockFSAction](#cfn-quicksight-custompermissions-capabilities-useamazonbedrockfsaction): {{String}}
  [UseAmazonBedrockKRSAction](#cfn-quicksight-custompermissions-capabilities-useamazonbedrockkrsaction): {{String}}
  [UseAmazonSThreeAction](#cfn-quicksight-custompermissions-capabilities-useamazonsthreeaction): {{String}}
  [UseAsanaAction](#cfn-quicksight-custompermissions-capabilities-useasanaaction): {{String}}
  [UseBambooHRAction](#cfn-quicksight-custompermissions-capabilities-usebamboohraction): {{String}}
  [UseBedrockManagedKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-usebedrockmanagedknowledgebase): {{String}}
  [UseBedrockModels](#cfn-quicksight-custompermissions-capabilities-usebedrockmodels): {{String}}
  [UseBoxAgentAction](#cfn-quicksight-custompermissions-capabilities-useboxagentaction): {{String}}
  [UseBoxKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-useboxknowledgebase): {{String}}
  [UseBrowserExtension](#cfn-quicksight-custompermissions-capabilities-usebrowserextension): {{String}}
  [UseCanvaAgentAction](#cfn-quicksight-custompermissions-capabilities-usecanvaagentaction): {{String}}
  [UseComprehendAction](#cfn-quicksight-custompermissions-capabilities-usecomprehendaction): {{String}}
  [UseComprehendMedicalAction](#cfn-quicksight-custompermissions-capabilities-usecomprehendmedicalaction): {{String}}
  [UseConfluenceAction](#cfn-quicksight-custompermissions-capabilities-useconfluenceaction): {{String}}
  [UseConfluenceKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-useconfluenceknowledgebase): {{String}}
  [UseExcelAddInExtension](#cfn-quicksight-custompermissions-capabilities-useexceladdinextension): {{String}}
  [UseFactSetAction](#cfn-quicksight-custompermissions-capabilities-usefactsetaction): {{String}}
  [UseGenericHTTPAction](#cfn-quicksight-custompermissions-capabilities-usegenerichttpaction): {{String}}
  [UseGithubAction](#cfn-quicksight-custompermissions-capabilities-usegithubaction): {{String}}
  [UseGoogleCalendarAction](#cfn-quicksight-custompermissions-capabilities-usegooglecalendaraction): {{String}}
  [UseGoogleDriveKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-usegoogledriveknowledgebase): {{String}}
  [UseHubspotAction](#cfn-quicksight-custompermissions-capabilities-usehubspotaction): {{String}}
  [UseHuggingFaceAction](#cfn-quicksight-custompermissions-capabilities-usehuggingfaceaction): {{String}}
  [UseIDCKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-useidcknowledgebase): {{String}}
  [UseIntercomAction](#cfn-quicksight-custompermissions-capabilities-useintercomaction): {{String}}
  [UseJiraAction](#cfn-quicksight-custompermissions-capabilities-usejiraaction): {{String}}
  [UseLinearAction](#cfn-quicksight-custompermissions-capabilities-uselinearaction): {{String}}
  [UseMCPAction](#cfn-quicksight-custompermissions-capabilities-usemcpaction): {{String}}
  [UseMondayAction](#cfn-quicksight-custompermissions-capabilities-usemondayaction): {{String}}
  [UseMSExchangeAction](#cfn-quicksight-custompermissions-capabilities-usemsexchangeaction): {{String}}
  [UseMSTeamsAction](#cfn-quicksight-custompermissions-capabilities-usemsteamsaction): {{String}}
  [UseNewRelicAction](#cfn-quicksight-custompermissions-capabilities-usenewrelicaction): {{String}}
  [UseNotionAction](#cfn-quicksight-custompermissions-capabilities-usenotionaction): {{String}}
  [UseOneDriveAction](#cfn-quicksight-custompermissions-capabilities-useonedriveaction): {{String}}
  [UseOneDriveKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-useonedriveknowledgebase): {{String}}
  [UseOpenAPIAction](#cfn-quicksight-custompermissions-capabilities-useopenapiaction): {{String}}
  [UseOutlookAddInExtension](#cfn-quicksight-custompermissions-capabilities-useoutlookaddinextension): {{String}}
  [UsePagerDutyAction](#cfn-quicksight-custompermissions-capabilities-usepagerdutyaction): {{String}}
  [UsePowerpointAddInExtension](#cfn-quicksight-custompermissions-capabilities-usepowerpointaddinextension): {{String}}
  [UseQBusinessKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-useqbusinessknowledgebase): {{String}}
  [UseS3KnowledgeBase](#cfn-quicksight-custompermissions-capabilities-uses3knowledgebase): {{String}}
  [UseSalesforceAction](#cfn-quicksight-custompermissions-capabilities-usesalesforceaction): {{String}}
  [UseSandPGlobalEnergyAction](#cfn-quicksight-custompermissions-capabilities-usesandpglobalenergyaction): {{String}}
  [UseSandPGMIAction](#cfn-quicksight-custompermissions-capabilities-usesandpgmiaction): {{String}}
  [UseSAPBillOfMaterialAction](#cfn-quicksight-custompermissions-capabilities-usesapbillofmaterialaction): {{String}}
  [UseSAPBusinessPartnerAction](#cfn-quicksight-custompermissions-capabilities-usesapbusinesspartneraction): {{String}}
  [UseSAPMaterialStockAction](#cfn-quicksight-custompermissions-capabilities-usesapmaterialstockaction): {{String}}
  [UseSAPPhysicalInventoryAction](#cfn-quicksight-custompermissions-capabilities-usesapphysicalinventoryaction): {{String}}
  [UseSAPProductMasterDataAction](#cfn-quicksight-custompermissions-capabilities-usesapproductmasterdataaction): {{String}}
  [UseServiceNowAction](#cfn-quicksight-custompermissions-capabilities-useservicenowaction): {{String}}
  [UseSharePointAction](#cfn-quicksight-custompermissions-capabilities-usesharepointaction): {{String}}
  [UseSharePointKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-usesharepointknowledgebase): {{String}}
  [UseSlackAction](#cfn-quicksight-custompermissions-capabilities-useslackaction): {{String}}
  [UseSmartsheetAction](#cfn-quicksight-custompermissions-capabilities-usesmartsheetaction): {{String}}
  [UseTextractAction](#cfn-quicksight-custompermissions-capabilities-usetextractaction): {{String}}
  [UseWebCrawlerKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-usewebcrawlerknowledgebase): {{String}}
  [UseWordAddInExtension](#cfn-quicksight-custompermissions-capabilities-usewordaddinextension): {{String}}
  [UseZendeskAction](#cfn-quicksight-custompermissions-capabilities-usezendeskaction): {{String}}
  [ViewAccountSPICECapacity](#cfn-quicksight-custompermissions-capabilities-viewaccountspicecapacity): {{String}}
  [WebCrawlerKnowledgeBase](#cfn-quicksight-custompermissions-capabilities-webcrawlerknowledgebase): {{String}}
  [ZendeskAction](#cfn-quicksight-custompermissions-capabilities-zendeskaction): {{String}}
```

## Properties
<a name="aws-properties-quicksight-custompermissions-capabilities-properties"></a>

`AccessAppsNativeDataStore`  <a name="cfn-quicksight-custompermissions-capabilities-accessappsnativedatastore"></a>
The ability to access the native data store for new and existing apps.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Action`  <a name="cfn-quicksight-custompermissions-capabilities-action"></a>
The ability to perform actions in external services through Action connectors. Actions allow users to interact with third-party systems.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AddOrRunAnomalyDetectionForAnalyses`  <a name="cfn-quicksight-custompermissions-capabilities-addorrunanomalydetectionforanalyses"></a>
The ability to add or run anomaly detection.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AdobeAnalyticsDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-adobeanalyticsdatasource"></a>
The ability to create, update, and share Adobe Analytics data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AmazonBedrockARSAction`  <a name="cfn-quicksight-custompermissions-capabilities-amazonbedrockarsaction"></a>
The ability to perform actions using Bedrock Agent connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AmazonBedrockFSAction`  <a name="cfn-quicksight-custompermissions-capabilities-amazonbedrockfsaction"></a>
The ability to perform actions using Bedrock Runtime connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AmazonBedrockKRSAction`  <a name="cfn-quicksight-custompermissions-capabilities-amazonbedrockkrsaction"></a>
The ability to perform actions using Bedrock Data Automation Runtime connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AmazonSThreeAction`  <a name="cfn-quicksight-custompermissions-capabilities-amazonsthreeaction"></a>
The ability to perform actions using Amazon S3 connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Analysis`  <a name="cfn-quicksight-custompermissions-capabilities-analysis"></a>
The ability to perform analysis-related actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApproveFlowShareRequests`  <a name="cfn-quicksight-custompermissions-capabilities-approveflowsharerequests"></a>
The ability to review and approve sharing requests of Flows.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Apps`  <a name="cfn-quicksight-custompermissions-capabilities-apps"></a>
The ability to perform apps-related actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AsanaAction`  <a name="cfn-quicksight-custompermissions-capabilities-asanaaction"></a>
The ability to perform actions using Asana connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AthenaDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-athenadatasource"></a>
The ability to create, update, and share Amazon Athena data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuroraDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-auroradatasource"></a>
The ability to create, update, and share Amazon Aurora data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Automate`  <a name="cfn-quicksight-custompermissions-capabilities-automate"></a>
The ability to perform automate-related actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BambooHRAction`  <a name="cfn-quicksight-custompermissions-capabilities-bamboohraction"></a>
The ability to perform actions using BambooHR connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BedrockManagedKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-bedrockmanagedknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BoxAgentAction`  <a name="cfn-quicksight-custompermissions-capabilities-boxagentaction"></a>
The ability to perform actions using Box Agent connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BoxKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-boxknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BuildCalculatedFieldWithQ`  <a name="cfn-quicksight-custompermissions-capabilities-buildcalculatedfieldwithq"></a>
The ability to Build Calculation with AI
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CanvaAgentAction`  <a name="cfn-quicksight-custompermissions-capabilities-canvaagentaction"></a>
The ability to perform actions using Canva Agent connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ChatAgent`  <a name="cfn-quicksight-custompermissions-capabilities-chatagent"></a>
The ability to perform chat-related actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComprehendAction`  <a name="cfn-quicksight-custompermissions-capabilities-comprehendaction"></a>
The ability to perform actions using Comprehend connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComprehendMedicalAction`  <a name="cfn-quicksight-custompermissions-capabilities-comprehendmedicalaction"></a>
The ability to perform actions using Comprehend Medical connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConfluenceAction`  <a name="cfn-quicksight-custompermissions-capabilities-confluenceaction"></a>
The ability to perform actions using Atlassian Confluence Cloud connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConfluenceKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-confluenceknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAdobeAnalyticsDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createadobeanalyticsdatasource"></a>
The ability to create Adobe Analytics data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateAmazonBedrockARSAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateamazonbedrockarsaction"></a>
The ability to create and update Bedrock Agent actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateAmazonBedrockFSAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateamazonbedrockfsaction"></a>
The ability to create and update Bedrock Runtime actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateAmazonBedrockKRSAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateamazonbedrockkrsaction"></a>
The ability to create and update Bedrock Data Automation Runtime actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateAmazonSThreeAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateamazonsthreeaction"></a>
The ability to create and update Amazon S3 actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateApps`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateapps"></a>
The ability to create or update apps.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateAsanaAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateasanaaction"></a>
The ability to create and update Asana actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateBambooHRAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatebamboohraction"></a>
The ability to create and update BambooHR actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateBedrockManagedKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatebedrockmanagedknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateBoxAgentAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateboxagentaction"></a>
The ability to create and update Box Agent actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateBoxKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateboxknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateCanvaAgentAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatecanvaagentaction"></a>
The ability to create and update Canva Agent actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateComprehendAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatecomprehendaction"></a>
The ability to create and update Comprehend actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateComprehendMedicalAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatecomprehendmedicalaction"></a>
The ability to create and update Comprehend Medical actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateConfluenceAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateconfluenceaction"></a>
The ability to create and update Atlassian Confluence Cloud actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateConfluenceKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateconfluenceknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateDashboardEmailReports`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatedashboardemailreports"></a>
The ability to create and update email reports.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateDatasets`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatedatasets"></a>
The ability to create and update datasets.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateDataSources`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatedatasources"></a>
The ability to create and update data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateFactSetAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatefactsetaction"></a>
The ability to create and update FactSet actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateGenericHTTPAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdategenerichttpaction"></a>
The ability to create and update REST API connection actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateGithubAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdategithubaction"></a>
The ability to create and update GitHub actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateGoogleCalendarAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdategooglecalendaraction"></a>
The ability to create and update Google Calendar actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateGoogleDriveKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdategoogledriveknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateHubspotAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatehubspotaction"></a>
The ability to create and update Hubspot actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateHuggingFaceAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatehuggingfaceaction"></a>
The ability to create and update HuggingFace actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateIDCKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateidcknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateIntercomAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateintercomaction"></a>
The ability to create and update Intercom actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateJiraAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatejiraaction"></a>
The ability to create and update Jira actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateKnowledgeBases`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateknowledgebases"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateLinearAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatelinearaction"></a>
The ability to create and update Linear actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateMCPAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatemcpaction"></a>
The ability to create and update Model Context Protocol actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateMondayAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatemondayaction"></a>
The ability to create and update Monday actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateMSExchangeAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatemsexchangeaction"></a>
The ability to create and update Microsoft Outlook actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateMSTeamsAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatemsteamsaction"></a>
The ability to create and update Microsoft Teams actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateNewRelicAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatenewrelicaction"></a>
The ability to create and update New Relic actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateNotionAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatenotionaction"></a>
The ability to create and update Notion actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateOneDriveAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateonedriveaction"></a>
The ability to create and update Microsoft OneDrive actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateOneDriveKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateonedriveknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateOpenAPIAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateopenapiaction"></a>
The ability to create and update OpenAPI Specification actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdatePagerDutyAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatepagerdutyaction"></a>
The ability to create and update PagerDuty Advance actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateQBusinessKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateqbusinessknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateS3KnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdates3knowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateSalesforceAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatesalesforceaction"></a>
The ability to create and update Salesforce actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateSandPGlobalEnergyAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatesandpglobalenergyaction"></a>
The ability to create and update S&P Global Energy actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateSandPGMIAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatesandpgmiaction"></a>
The ability to create and update S&P Global Market Intelligence actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateSAPBillOfMaterialAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatesapbillofmaterialaction"></a>
The ability to create and update SAP Bill of Materials actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateSAPBusinessPartnerAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatesapbusinesspartneraction"></a>
The ability to create and update SAP Business Partner actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateSAPMaterialStockAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatesapmaterialstockaction"></a>
The ability to create and update SAP Material Stock actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateSAPPhysicalInventoryAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatesapphysicalinventoryaction"></a>
The ability to create and update SAP Physical Inventory actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateSAPProductMasterDataAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatesapproductmasterdataaction"></a>
The ability to create and update SAP Product Master actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateServiceNowAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateservicenowaction"></a>
The ability to create and update ServiceNow actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateSharePointAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatesharepointaction"></a>
The ability to create and update Microsoft SharePoint Online actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateSharePointKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatesharepointknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateSlackAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateslackaction"></a>
The ability to create and update Slack actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateSmartsheetAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatesmartsheetaction"></a>
The ability to create and update Smartsheet actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateTextractAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatetextractaction"></a>
The ability to create and update Textract actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateThemes`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatethemes"></a>
The ability to export to Create and Update themes.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateThresholdAlerts`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatethresholdalerts"></a>
The ability to create and update threshold alerts.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateWebCrawlerKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatewebcrawlerknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateZendeskAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatezendeskaction"></a>
The ability to create and update Zendesk actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAthenaDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createathenadatasource"></a>
The ability to create Amazon Athena data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAuroraDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createauroradatasource"></a>
The ability to create Amazon Aurora data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateChatAgents`  <a name="cfn-quicksight-custompermissions-capabilities-createchatagents"></a>
The ability to create chat agents.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateDashboardExecutiveSummaryWithQ`  <a name="cfn-quicksight-custompermissions-capabilities-createdashboardexecutivesummarywithq"></a>
The ability to Create Executive Summary
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateDatabricksDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createdatabricksdatasource"></a>
The ability to create Databricks data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateDb2DataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createdb2datasource"></a>
The ability to create Db2 data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateDenodoDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createdenododatasource"></a>
The ability to create Denodo data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateDocumentDbDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createdocumentdbdatasource"></a>
The ability to create Amazon DocumentDB data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateDremioDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createdremiodatasource"></a>
The ability to create Dremio data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateDynamoDbDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createdynamodbdatasource"></a>
The ability to create Amazon DynamoDB data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateExasolDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createexasoldatasource"></a>
The ability to create Exasol data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateFileDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createfiledatasource"></a>
The ability to create file data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateGitHubDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-creategithubdatasource"></a>
The ability to create GitHub data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateGoogleAnalyticsDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-creategoogleanalyticsdatasource"></a>
The ability to create Google Analytics data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateGoogleBigQueryDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-creategooglebigquerydatasource"></a>
The ability to create Google BigQuery data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateGoogleSheetsDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-creategooglesheetsdatasource"></a>
The ability to create Google Sheets data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateImpalaDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createimpaladatasource"></a>
The ability to create Impala data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateJiraDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createjiradatasource"></a>
The ability to create Jira data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateMariaDbDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createmariadbdatasource"></a>
The ability to create MariaDB data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateMongoAtlasDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createmongoatlasdatasource"></a>
The ability to create MongoDB Atlas data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateMongoDbDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createmongodbdatasource"></a>
The ability to create MongoDB data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateMySqlDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createmysqldatasource"></a>
The ability to create MySQL data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateOpenSearchDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createopensearchdatasource"></a>
The ability to create Amazon OpenSearch Service data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateOracleDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createoracledatasource"></a>
The ability to create Oracle data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreatePayPalDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createpaypaldatasource"></a>
The ability to create PayPal data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreatePostgreSqlDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createpostgresqldatasource"></a>
The ability to create PostgreSQL data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreatePrestoDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createprestodatasource"></a>
The ability to create Presto data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateRadiantDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createradiantdatasource"></a>
The ability to create Amazon QuickSight data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateRdsDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createrdsdatasource"></a>
The ability to create auto-discovered Amazon RDS data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateRedshiftAutoDiscoveredDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createredshiftautodiscovereddatasource"></a>
The ability to create auto-discovered Amazon Redshift data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateRedshiftManualDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createredshiftmanualdatasource"></a>
The ability to create manually configured Amazon Redshift data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateS3AnalyticsDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-creates3analyticsdatasource"></a>
The ability to create Amazon S3 Analytics data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateS3DataSource`  <a name="cfn-quicksight-custompermissions-capabilities-creates3datasource"></a>
The ability to create Amazon S3 data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateS3TablesDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-creates3tablesdatasource"></a>
The ability to create Amazon S3 Tables data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateSalesforceDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createsalesforcedatasource"></a>
The ability to create Salesforce data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateSapHanaDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createsaphanadatasource"></a>
The ability to create SAP HANA data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateServiceNowDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createservicenowdatasource"></a>
The ability to create ServiceNow data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateSharedFolders`  <a name="cfn-quicksight-custompermissions-capabilities-createsharedfolders"></a>
The ability to create shared folders.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateSnowflakeDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createsnowflakedatasource"></a>
The ability to create Snowflake data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateSpaces`  <a name="cfn-quicksight-custompermissions-capabilities-createspaces"></a>
The ability to create spaces.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateSparkDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createsparkdatasource"></a>
The ability to create Spark data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateSPICEDataset`  <a name="cfn-quicksight-custompermissions-capabilities-createspicedataset"></a>
The ability to create a SPICE dataset.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateSqlServerDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createsqlserverdatasource"></a>
The ability to create SQL Server data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateSquareDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createsquaredatasource"></a>
The ability to create Square data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateStarburstDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createstarburstdatasource"></a>
The ability to create Starburst data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateTeradataDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createteradatadatasource"></a>
The ability to create Teradata data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateTimestreamDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createtimestreamdatasource"></a>
The ability to create Amazon Timestream data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateTrinoDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createtrinodatasource"></a>
The ability to create Trino data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateTwitterDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-createtwitterdatasource"></a>
The ability to create Twitter data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Dashboard`  <a name="cfn-quicksight-custompermissions-capabilities-dashboard"></a>
The ability to perform dashboard-related actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatabricksDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-databricksdatasource"></a>
The ability to create, update, and share Databricks data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Db2DataSource`  <a name="cfn-quicksight-custompermissions-capabilities-db2datasource"></a>
The ability to create, update, and share Db2 data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DenodoDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-denododatasource"></a>
The ability to create, update, and share Denodo data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DocumentDbDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-documentdbdatasource"></a>
The ability to create, update, and share Amazon DocumentDB data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DremioDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-dremiodatasource"></a>
The ability to create, update, and share Dremio data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DynamoDbDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-dynamodbdatasource"></a>
The ability to create, update, and share Amazon DynamoDB data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EditVisualWithQ`  <a name="cfn-quicksight-custompermissions-capabilities-editvisualwithq"></a>
The ability to Edit Visual with AI
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExasolDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-exasoldatasource"></a>
The ability to create, update, and share Exasol data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExportToCsv`  <a name="cfn-quicksight-custompermissions-capabilities-exporttocsv"></a>
The ability to export to CSV files from the UI.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExportToCsvInScheduledReports`  <a name="cfn-quicksight-custompermissions-capabilities-exporttocsvinscheduledreports"></a>
The ability to export to CSV files in scheduled email reports.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExportToExcel`  <a name="cfn-quicksight-custompermissions-capabilities-exporttoexcel"></a>
The ability to export to Excel files from the UI.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExportToExcelInScheduledReports`  <a name="cfn-quicksight-custompermissions-capabilities-exporttoexcelinscheduledreports"></a>
The ability to export to Excel files in scheduled email reports.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExportToPdf`  <a name="cfn-quicksight-custompermissions-capabilities-exporttopdf"></a>
The ability to export to PDF files from the UI.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExportToPdfInScheduledReports`  <a name="cfn-quicksight-custompermissions-capabilities-exporttopdfinscheduledreports"></a>
The ability to export to PDF files in scheduled email reports.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Extension`  <a name="cfn-quicksight-custompermissions-capabilities-extension"></a>
The ability to perform Extension-related actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FactSetAction`  <a name="cfn-quicksight-custompermissions-capabilities-factsetaction"></a>
The ability to perform actions using FactSet connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FileDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-filedatasource"></a>
The ability to create, update, and share file data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Flow`  <a name="cfn-quicksight-custompermissions-capabilities-flow"></a>
The ability to perform flow-related actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GenericHTTPAction`  <a name="cfn-quicksight-custompermissions-capabilities-generichttpaction"></a>
The ability to perform actions using REST API connection connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GithubAction`  <a name="cfn-quicksight-custompermissions-capabilities-githubaction"></a>
The ability to perform actions using GitHub connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GitHubDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-githubdatasource"></a>
The ability to create, update, and share GitHub data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GoogleAnalyticsDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-googleanalyticsdatasource"></a>
The ability to create, update, and share Google Analytics data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GoogleBigQueryDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-googlebigquerydatasource"></a>
The ability to create, update, and share Google BigQuery data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GoogleCalendarAction`  <a name="cfn-quicksight-custompermissions-capabilities-googlecalendaraction"></a>
The ability to perform actions using Google Calendar connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GoogleDriveKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-googledriveknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GoogleSheetsDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-googlesheetsdatasource"></a>
The ability to create, update, and share Google Sheets data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HubspotAction`  <a name="cfn-quicksight-custompermissions-capabilities-hubspotaction"></a>
The ability to perform actions using Hubspot connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HuggingFaceAction`  <a name="cfn-quicksight-custompermissions-capabilities-huggingfaceaction"></a>
The ability to perform actions using HuggingFace connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IDCKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-idcknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImpalaDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-impaladatasource"></a>
The ability to create, update, and share Impala data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InboundEmailTrigger`  <a name="cfn-quicksight-custompermissions-capabilities-inboundemailtrigger"></a>
The ability to create, view, edit, delete, and run inbound email triggers for flows and automations.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncludeContentInScheduledReportsEmail`  <a name="cfn-quicksight-custompermissions-capabilities-includecontentinscheduledreportsemail"></a>
The ability to include content in scheduled email reports.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IntercomAction`  <a name="cfn-quicksight-custompermissions-capabilities-intercomaction"></a>
The ability to perform actions using Intercom connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InvokeAppsAIInference`  <a name="cfn-quicksight-custompermissions-capabilities-invokeappsaiinference"></a>
The ability to add and invoke AI inference in new and existing apps.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JiraAction`  <a name="cfn-quicksight-custompermissions-capabilities-jiraaction"></a>
The ability to perform actions using Jira connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JiraDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-jiradatasource"></a>
The ability to create, update, and share Jira data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-knowledgebase"></a>
The ability to use knowledge bases to specify content from external applications.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LinearAction`  <a name="cfn-quicksight-custompermissions-capabilities-linearaction"></a>
The ability to perform actions using Linear connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManageSharedFolders`  <a name="cfn-quicksight-custompermissions-capabilities-managesharedfolders"></a>
The ability to create, update, delete and view shared folders (both restricted and unrestricted), ability to add any asset to shared folders, and ability to share the folders.
**Note:** This does *not* prevent inheriting access to assets that others share with them through folder membership.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MariaDbDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-mariadbdatasource"></a>
The ability to create, update, and share MariaDB data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MCPAction`  <a name="cfn-quicksight-custompermissions-capabilities-mcpaction"></a>
The ability to perform actions using Model Context Protocol connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MondayAction`  <a name="cfn-quicksight-custompermissions-capabilities-mondayaction"></a>
The ability to perform actions using Monday connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MongoAtlasDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-mongoatlasdatasource"></a>
The ability to create, update, and share MongoDB Atlas data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MongoDbDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-mongodbdatasource"></a>
The ability to create, update, and share MongoDB data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MSExchangeAction`  <a name="cfn-quicksight-custompermissions-capabilities-msexchangeaction"></a>
The ability to perform actions using Microsoft Outlook connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MSTeamsAction`  <a name="cfn-quicksight-custompermissions-capabilities-msteamsaction"></a>
The ability to perform actions using Microsoft Teams connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MySqlDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-mysqldatasource"></a>
The ability to create, update, and share MySQL data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NewRelicAction`  <a name="cfn-quicksight-custompermissions-capabilities-newrelicaction"></a>
The ability to perform actions using New Relic connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotionAction`  <a name="cfn-quicksight-custompermissions-capabilities-notionaction"></a>
The ability to perform actions using Notion connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OneDriveAction`  <a name="cfn-quicksight-custompermissions-capabilities-onedriveaction"></a>
The ability to perform actions using Microsoft OneDrive connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OneDriveKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-onedriveknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OpenAPIAction`  <a name="cfn-quicksight-custompermissions-capabilities-openapiaction"></a>
The ability to perform actions using OpenAPI Specification connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OpenSearchDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-opensearchdatasource"></a>
The ability to create, update, and share Amazon OpenSearch Service data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OracleDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-oracledatasource"></a>
The ability to create, update, and share Oracle data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PagerDutyAction`  <a name="cfn-quicksight-custompermissions-capabilities-pagerdutyaction"></a>
The ability to perform actions using PagerDuty Advance connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PayPalDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-paypaldatasource"></a>
The ability to create, update, and share PayPal data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PerformFlowUiTask`  <a name="cfn-quicksight-custompermissions-capabilities-performflowuitask"></a>
The ability to use UI Agent step to perform tasks on public websites.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PostgreSqlDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-postgresqldatasource"></a>
The ability to create, update, and share PostgreSQL data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrestoDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-prestodatasource"></a>
The ability to create, update, and share Presto data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrintReports`  <a name="cfn-quicksight-custompermissions-capabilities-printreports"></a>
The ability to print reports.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PublishWithoutApproval`  <a name="cfn-quicksight-custompermissions-capabilities-publishwithoutapproval"></a>
The ability to enable approvals for flow share.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QBusinessKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-qbusinessknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QuickEventTrigger`  <a name="cfn-quicksight-custompermissions-capabilities-quickeventtrigger"></a>
The ability to create, view, edit, delete, and run Quick event triggers for flows and automations.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RadiantDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-radiantdatasource"></a>
The ability to create, update, and share Amazon QuickSight data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RdsDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-rdsdatasource"></a>
The ability to create, update, and share auto-discovered Amazon RDS data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RedshiftAutoDiscoveredDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-redshiftautodiscovereddatasource"></a>
The ability to create, update, and share auto-discovered Amazon Redshift data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RedshiftManualDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-redshiftmanualdatasource"></a>
The ability to create, update, and share manually configured Amazon Redshift data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RenameSharedFolders`  <a name="cfn-quicksight-custompermissions-capabilities-renamesharedfolders"></a>
The ability to rename shared folders.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Research`  <a name="cfn-quicksight-custompermissions-capabilities-research"></a>
The ability to perform research-related actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3AnalyticsDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-s3analyticsdatasource"></a>
The ability to create, update, and share Amazon S3 Analytics data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3DataSource`  <a name="cfn-quicksight-custompermissions-capabilities-s3datasource"></a>
The ability to create, update, and share Amazon S3 data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3KnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-s3knowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3TablesDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-s3tablesdatasource"></a>
The ability to create, update, and share Amazon S3 Tables data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SalesforceAction`  <a name="cfn-quicksight-custompermissions-capabilities-salesforceaction"></a>
The ability to perform actions using Salesforce connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SalesforceDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-salesforcedatasource"></a>
The ability to create, update, and share Salesforce data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SandPGlobalEnergyAction`  <a name="cfn-quicksight-custompermissions-capabilities-sandpglobalenergyaction"></a>
The ability to perform actions using S&P Global Energy connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SandPGMIAction`  <a name="cfn-quicksight-custompermissions-capabilities-sandpgmiaction"></a>
The ability to perform actions using S&P Global Market Intelligence connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SAPBillOfMaterialAction`  <a name="cfn-quicksight-custompermissions-capabilities-sapbillofmaterialaction"></a>
The ability to perform actions using SAP Bill of Materials connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SAPBusinessPartnerAction`  <a name="cfn-quicksight-custompermissions-capabilities-sapbusinesspartneraction"></a>
The ability to perform actions using SAP Business Partner connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SapHanaDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-saphanadatasource"></a>
The ability to create, update, and share SAP HANA data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SAPMaterialStockAction`  <a name="cfn-quicksight-custompermissions-capabilities-sapmaterialstockaction"></a>
The ability to perform actions using SAP Material Stock connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SAPPhysicalInventoryAction`  <a name="cfn-quicksight-custompermissions-capabilities-sapphysicalinventoryaction"></a>
The ability to perform actions using SAP Physical Inventory connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SAPProductMasterDataAction`  <a name="cfn-quicksight-custompermissions-capabilities-sapproductmasterdataaction"></a>
The ability to perform actions using SAP Product Master connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScheduleTrigger`  <a name="cfn-quicksight-custompermissions-capabilities-scheduletrigger"></a>
The ability to create, view, edit, delete, and run schedule triggers for flows and automations.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceNowAction`  <a name="cfn-quicksight-custompermissions-capabilities-servicenowaction"></a>
The ability to perform actions using ServiceNow connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceNowDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-servicenowdatasource"></a>
The ability to create, update, and share ServiceNow data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareAdobeAnalyticsDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-shareadobeanalyticsdatasource"></a>
The ability to share Adobe Analytics data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareAmazonBedrockARSAction`  <a name="cfn-quicksight-custompermissions-capabilities-shareamazonbedrockarsaction"></a>
The ability to share Bedrock Agent actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareAmazonBedrockFSAction`  <a name="cfn-quicksight-custompermissions-capabilities-shareamazonbedrockfsaction"></a>
The ability to share Bedrock Runtime actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareAmazonBedrockKRSAction`  <a name="cfn-quicksight-custompermissions-capabilities-shareamazonbedrockkrsaction"></a>
The ability to share Bedrock Data Automation Runtime actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareAmazonSThreeAction`  <a name="cfn-quicksight-custompermissions-capabilities-shareamazonsthreeaction"></a>
The ability to share Amazon S3 actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareAnalyses`  <a name="cfn-quicksight-custompermissions-capabilities-shareanalyses"></a>
The ability to share analyses.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareApps`  <a name="cfn-quicksight-custompermissions-capabilities-shareapps"></a>
The ability to share apps with other users.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareAsanaAction`  <a name="cfn-quicksight-custompermissions-capabilities-shareasanaaction"></a>
The ability to share Asana actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareAthenaDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-shareathenadatasource"></a>
The ability to share Amazon Athena data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareAuroraDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-shareauroradatasource"></a>
The ability to share Amazon Aurora data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareBambooHRAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharebamboohraction"></a>
The ability to share BambooHR actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareBedrockManagedKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-sharebedrockmanagedknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareBoxAgentAction`  <a name="cfn-quicksight-custompermissions-capabilities-shareboxagentaction"></a>
The ability to share Box Agent actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareBoxKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-shareboxknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareCanvaAgentAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharecanvaagentaction"></a>
The ability to share Canva Agent actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareChatAgents`  <a name="cfn-quicksight-custompermissions-capabilities-sharechatagents"></a>
The ability to share chat agents with other users and groups.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareComprehendAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharecomprehendaction"></a>
The ability to share Comprehend actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareComprehendMedicalAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharecomprehendmedicalaction"></a>
The ability to share Comprehend Medical actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareConfluenceAction`  <a name="cfn-quicksight-custompermissions-capabilities-shareconfluenceaction"></a>
The ability to share Atlassian Confluence Cloud actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareConfluenceKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-shareconfluenceknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareDashboards`  <a name="cfn-quicksight-custompermissions-capabilities-sharedashboards"></a>
The ability to share dashboards.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareDatabricksDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sharedatabricksdatasource"></a>
The ability to share Databricks data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareDatasets`  <a name="cfn-quicksight-custompermissions-capabilities-sharedatasets"></a>
The ability to share datasets.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareDataSources`  <a name="cfn-quicksight-custompermissions-capabilities-sharedatasources"></a>
The ability to share data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareDb2DataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sharedb2datasource"></a>
The ability to share Db2 data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareDenodoDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sharedenododatasource"></a>
The ability to share Denodo data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareDocumentDbDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sharedocumentdbdatasource"></a>
The ability to share Amazon DocumentDB data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareDremioDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sharedremiodatasource"></a>
The ability to share Dremio data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareDynamoDbDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sharedynamodbdatasource"></a>
The ability to share Amazon DynamoDB data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareExasolDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-shareexasoldatasource"></a>
The ability to share Exasol data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareFactSetAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharefactsetaction"></a>
The ability to share FactSet actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareFileDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sharefiledatasource"></a>
The ability to share file data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareGenericHTTPAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharegenerichttpaction"></a>
The ability to share REST API connection actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareGithubAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharegithubaction"></a>
The ability to share GitHub actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareGitHubDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sharegithubdatasource"></a>
The ability to share GitHub data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareGoogleAnalyticsDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sharegoogleanalyticsdatasource"></a>
The ability to share Google Analytics data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareGoogleBigQueryDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sharegooglebigquerydatasource"></a>
The ability to share Google BigQuery data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareGoogleCalendarAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharegooglecalendaraction"></a>
The ability to share Google Calendar actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareGoogleDriveKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-sharegoogledriveknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareGoogleSheetsDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sharegooglesheetsdatasource"></a>
The ability to share Google Sheets data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareHubspotAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharehubspotaction"></a>
The ability to share Hubspot actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareHuggingFaceAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharehuggingfaceaction"></a>
The ability to share HuggingFace actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareIDCKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-shareidcknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareImpalaDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-shareimpaladatasource"></a>
The ability to share Impala data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareIntercomAction`  <a name="cfn-quicksight-custompermissions-capabilities-shareintercomaction"></a>
The ability to share Intercom actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareJiraAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharejiraaction"></a>
The ability to share Jira actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareJiraDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sharejiradatasource"></a>
The ability to share Jira data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareKnowledgeBases`  <a name="cfn-quicksight-custompermissions-capabilities-shareknowledgebases"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareLinearAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharelinearaction"></a>
The ability to share Linear actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareMariaDbDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sharemariadbdatasource"></a>
The ability to share MariaDB data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareMCPAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharemcpaction"></a>
The ability to share Model Context Protocol actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareMondayAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharemondayaction"></a>
The ability to share Monday actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareMongoAtlasDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sharemongoatlasdatasource"></a>
The ability to share MongoDB Atlas data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareMongoDbDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sharemongodbdatasource"></a>
The ability to share MongoDB data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareMSExchangeAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharemsexchangeaction"></a>
The ability to share Microsoft Outlook actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareMSTeamsAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharemsteamsaction"></a>
The ability to share Microsoft Teams actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareMySqlDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sharemysqldatasource"></a>
The ability to share MySQL data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareNewRelicAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharenewrelicaction"></a>
The ability to share New Relic actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareNotionAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharenotionaction"></a>
The ability to share Notion actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareOneDriveAction`  <a name="cfn-quicksight-custompermissions-capabilities-shareonedriveaction"></a>
The ability to share Microsoft OneDrive actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareOneDriveKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-shareonedriveknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareOpenAPIAction`  <a name="cfn-quicksight-custompermissions-capabilities-shareopenapiaction"></a>
The ability to share OpenAPI Specification actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareOpenSearchDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-shareopensearchdatasource"></a>
The ability to share Amazon OpenSearch Service data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareOracleDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-shareoracledatasource"></a>
The ability to share Oracle data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SharePagerDutyAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharepagerdutyaction"></a>
The ability to share PagerDuty Advance actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SharePayPalDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sharepaypaldatasource"></a>
The ability to share PayPal data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SharePointAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharepointaction"></a>
The ability to perform actions using Microsoft SharePoint Online connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SharePointKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-sharepointknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SharePostgreSqlDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sharepostgresqldatasource"></a>
The ability to share PostgreSQL data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SharePrestoDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-shareprestodatasource"></a>
The ability to share Presto data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareQBusinessKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-shareqbusinessknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareRadiantDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-shareradiantdatasource"></a>
The ability to share Amazon QuickSight data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareRdsDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sharerdsdatasource"></a>
The ability to share auto-discovered Amazon RDS data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareRedshiftAutoDiscoveredDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-shareredshiftautodiscovereddatasource"></a>
The ability to share auto-discovered Amazon Redshift data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareRedshiftManualDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-shareredshiftmanualdatasource"></a>
The ability to share manually configured Amazon Redshift data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareS3AnalyticsDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-shares3analyticsdatasource"></a>
The ability to share Amazon S3 Analytics data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareS3DataSource`  <a name="cfn-quicksight-custompermissions-capabilities-shares3datasource"></a>
The ability to share Amazon S3 data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareS3KnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-shares3knowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareS3TablesDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-shares3tablesdatasource"></a>
The ability to share Amazon S3 Tables data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSalesforceAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharesalesforceaction"></a>
The ability to share Salesforce actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSalesforceDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sharesalesforcedatasource"></a>
The ability to share Salesforce data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSandPGlobalEnergyAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharesandpglobalenergyaction"></a>
The ability to share S&P Global Energy actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSandPGMIAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharesandpgmiaction"></a>
The ability to share S&P Global Market Intelligence actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSAPBillOfMaterialAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharesapbillofmaterialaction"></a>
The ability to share SAP Bill of Materials actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSAPBusinessPartnerAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharesapbusinesspartneraction"></a>
The ability to share SAP Business Partner actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSapHanaDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sharesaphanadatasource"></a>
The ability to share SAP HANA data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSAPMaterialStockAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharesapmaterialstockaction"></a>
The ability to share SAP Material Stock actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSAPPhysicalInventoryAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharesapphysicalinventoryaction"></a>
The ability to share SAP Physical Inventory actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSAPProductMasterDataAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharesapproductmasterdataaction"></a>
The ability to share SAP Product Master actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareServiceNowAction`  <a name="cfn-quicksight-custompermissions-capabilities-shareservicenowaction"></a>
The ability to share ServiceNow actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareServiceNowDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-shareservicenowdatasource"></a>
The ability to share ServiceNow data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSharePointAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharesharepointaction"></a>
The ability to share Microsoft SharePoint Online actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSharePointKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-sharesharepointknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSlackAction`  <a name="cfn-quicksight-custompermissions-capabilities-shareslackaction"></a>
The ability to share Slack actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSmartsheetAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharesmartsheetaction"></a>
The ability to share Smartsheet actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSnowflakeDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sharesnowflakedatasource"></a>
The ability to share Snowflake data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSpaces`  <a name="cfn-quicksight-custompermissions-capabilities-sharespaces"></a>
The ability to share spaces with other users and groups.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSparkDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sharesparkdatasource"></a>
The ability to share Spark data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSqlServerDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sharesqlserverdatasource"></a>
The ability to share SQL Server data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSquareDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sharesquaredatasource"></a>
The ability to share Square data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareStarburstDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sharestarburstdatasource"></a>
The ability to share Starburst data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareTeradataDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-shareteradatadatasource"></a>
The ability to share Teradata data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareTextractAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharetextractaction"></a>
The ability to share Textract actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareTimestreamDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sharetimestreamdatasource"></a>
The ability to share Amazon Timestream data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareTrinoDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sharetrinodatasource"></a>
The ability to share Trino data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareTwitterDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sharetwitterdatasource"></a>
The ability to share Twitter data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareWebCrawlerKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-sharewebcrawlerknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareZendeskAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharezendeskaction"></a>
The ability to share Zendesk actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SlackAction`  <a name="cfn-quicksight-custompermissions-capabilities-slackaction"></a>
The ability to perform actions using Slack connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SmartsheetAction`  <a name="cfn-quicksight-custompermissions-capabilities-smartsheetaction"></a>
The ability to perform actions using Smartsheet connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnowflakeDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-snowflakedatasource"></a>
The ability to create, update, and share Snowflake data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Space`  <a name="cfn-quicksight-custompermissions-capabilities-space"></a>
The ability to perform space-related actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SparkDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sparkdatasource"></a>
The ability to create, update, and share Spark data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SqlServerDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-sqlserverdatasource"></a>
The ability to create, update, and share SQL Server data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SquareDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-squaredatasource"></a>
The ability to create, update, and share Square data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StarburstDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-starburstdatasource"></a>
The ability to create, update, and share Starburst data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubscribeDashboardEmailReports`  <a name="cfn-quicksight-custompermissions-capabilities-subscribedashboardemailreports"></a>
The ability to subscribe to email reports.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TeradataDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-teradatadatasource"></a>
The ability to create, update, and share Teradata data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextractAction`  <a name="cfn-quicksight-custompermissions-capabilities-textractaction"></a>
The ability to perform actions using Textract connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimestreamDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-timestreamdatasource"></a>
The ability to create, update, and share Amazon Timestream data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Topic`  <a name="cfn-quicksight-custompermissions-capabilities-topic"></a>
The ability to perform Topic-related actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Trigger`  <a name="cfn-quicksight-custompermissions-capabilities-trigger"></a>
The ability to manage trigger-related settings for flows and automations.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrinoDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-trinodatasource"></a>
The ability to create, update, and share Trino data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TwitterDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-twitterdatasource"></a>
The ability to create, update, and share Twitter data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateAdobeAnalyticsDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updateadobeanalyticsdatasource"></a>
The ability to update Adobe Analytics data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateAthenaDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updateathenadatasource"></a>
The ability to update Amazon Athena data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateAuroraDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updateauroradatasource"></a>
The ability to update Amazon Aurora data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateDatabricksDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updatedatabricksdatasource"></a>
The ability to update Databricks data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateDb2DataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updatedb2datasource"></a>
The ability to update Db2 data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateDenodoDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updatedenododatasource"></a>
The ability to update Denodo data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateDocumentDbDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updatedocumentdbdatasource"></a>
The ability to update Amazon DocumentDB data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateDremioDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updatedremiodatasource"></a>
The ability to update Dremio data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateDynamoDbDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updatedynamodbdatasource"></a>
The ability to update Amazon DynamoDB data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateExasolDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updateexasoldatasource"></a>
The ability to update Exasol data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateFileDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updatefiledatasource"></a>
The ability to update file data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateGitHubDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updategithubdatasource"></a>
The ability to update GitHub data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateGoogleAnalyticsDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updategoogleanalyticsdatasource"></a>
The ability to update Google Analytics data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateGoogleBigQueryDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updategooglebigquerydatasource"></a>
The ability to update Google BigQuery data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateGoogleSheetsDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updategooglesheetsdatasource"></a>
The ability to update Google Sheets data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateImpalaDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updateimpaladatasource"></a>
The ability to update Impala data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateJiraDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updatejiradatasource"></a>
The ability to update Jira data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateMariaDbDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updatemariadbdatasource"></a>
The ability to update MariaDB data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateMongoAtlasDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updatemongoatlasdatasource"></a>
The ability to update MongoDB Atlas data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateMongoDbDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updatemongodbdatasource"></a>
The ability to update MongoDB data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateMySqlDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updatemysqldatasource"></a>
The ability to update MySQL data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateOpenSearchDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updateopensearchdatasource"></a>
The ability to update Amazon OpenSearch Service data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateOracleDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updateoracledatasource"></a>
The ability to update Oracle data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdatePayPalDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updatepaypaldatasource"></a>
The ability to update PayPal data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdatePostgreSqlDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updatepostgresqldatasource"></a>
The ability to update PostgreSQL data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdatePrestoDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updateprestodatasource"></a>
The ability to update Presto data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateRadiantDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updateradiantdatasource"></a>
The ability to update Amazon QuickSight data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateRdsDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updaterdsdatasource"></a>
The ability to update auto-discovered Amazon RDS data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateRedshiftAutoDiscoveredDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updateredshiftautodiscovereddatasource"></a>
The ability to update auto-discovered Amazon Redshift data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateRedshiftManualDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updateredshiftmanualdatasource"></a>
The ability to update manually configured Amazon Redshift data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateS3AnalyticsDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updates3analyticsdatasource"></a>
The ability to update Amazon S3 Analytics data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateS3DataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updates3datasource"></a>
The ability to update Amazon S3 data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateS3TablesDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updates3tablesdatasource"></a>
The ability to update Amazon S3 Tables data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateSalesforceDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updatesalesforcedatasource"></a>
The ability to update Salesforce data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateSapHanaDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updatesaphanadatasource"></a>
The ability to update SAP HANA data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateServiceNowDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updateservicenowdatasource"></a>
The ability to update ServiceNow data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateSnowflakeDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updatesnowflakedatasource"></a>
The ability to update Snowflake data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateSparkDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updatesparkdatasource"></a>
The ability to update Spark data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateSqlServerDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updatesqlserverdatasource"></a>
The ability to update SQL Server data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateSquareDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updatesquaredatasource"></a>
The ability to update Square data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateStarburstDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updatestarburstdatasource"></a>
The ability to update Starburst data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateTeradataDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updateteradatadatasource"></a>
The ability to update Teradata data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateTimestreamDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updatetimestreamdatasource"></a>
The ability to update Amazon Timestream data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateTrinoDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updatetrinodatasource"></a>
The ability to update Trino data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateTwitterDataSource`  <a name="cfn-quicksight-custompermissions-capabilities-updatetwitterdatasource"></a>
The ability to update Twitter data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseAgentWebSearch`  <a name="cfn-quicksight-custompermissions-capabilities-useagentwebsearch"></a>
The ability to use internet to enhance results in Chat Agents, Flows, and Quick Research. Web search queries will be processed securely in an AWS region `us-east-1`.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseAmazonBedrockARSAction`  <a name="cfn-quicksight-custompermissions-capabilities-useamazonbedrockarsaction"></a>
The ability to use Bedrock Agent actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseAmazonBedrockFSAction`  <a name="cfn-quicksight-custompermissions-capabilities-useamazonbedrockfsaction"></a>
The ability to use Bedrock Runtime actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseAmazonBedrockKRSAction`  <a name="cfn-quicksight-custompermissions-capabilities-useamazonbedrockkrsaction"></a>
The ability to use Bedrock Data Automation Runtime actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseAmazonSThreeAction`  <a name="cfn-quicksight-custompermissions-capabilities-useamazonsthreeaction"></a>
The ability to use Amazon S3 actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseAsanaAction`  <a name="cfn-quicksight-custompermissions-capabilities-useasanaaction"></a>
The ability to use Asana actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseBambooHRAction`  <a name="cfn-quicksight-custompermissions-capabilities-usebamboohraction"></a>
The ability to use BambooHR actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseBedrockManagedKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-usebedrockmanagedknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseBedrockModels`  <a name="cfn-quicksight-custompermissions-capabilities-usebedrockmodels"></a>
The ability to use Bedrock models for general knowledge step in flows.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseBoxAgentAction`  <a name="cfn-quicksight-custompermissions-capabilities-useboxagentaction"></a>
The ability to use Box Agent actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseBoxKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-useboxknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseBrowserExtension`  <a name="cfn-quicksight-custompermissions-capabilities-usebrowserextension"></a>
The ability to use Amazon Quick through the browser extension for Chrome, Firefox, and Edge.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseCanvaAgentAction`  <a name="cfn-quicksight-custompermissions-capabilities-usecanvaagentaction"></a>
The ability to use Canva Agent actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseComprehendAction`  <a name="cfn-quicksight-custompermissions-capabilities-usecomprehendaction"></a>
The ability to use Comprehend actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseComprehendMedicalAction`  <a name="cfn-quicksight-custompermissions-capabilities-usecomprehendmedicalaction"></a>
The ability to use Comprehend Medical actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseConfluenceAction`  <a name="cfn-quicksight-custompermissions-capabilities-useconfluenceaction"></a>
The ability to use Atlassian Confluence Cloud actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseConfluenceKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-useconfluenceknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseExcelAddInExtension`  <a name="cfn-quicksight-custompermissions-capabilities-useexceladdinextension"></a>
The ability to use Amazon Quick through the Microsoft Excel add-in.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseFactSetAction`  <a name="cfn-quicksight-custompermissions-capabilities-usefactsetaction"></a>
The ability to use FactSet actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseGenericHTTPAction`  <a name="cfn-quicksight-custompermissions-capabilities-usegenerichttpaction"></a>
The ability to use REST API connection actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseGithubAction`  <a name="cfn-quicksight-custompermissions-capabilities-usegithubaction"></a>
The ability to use GitHub actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseGoogleCalendarAction`  <a name="cfn-quicksight-custompermissions-capabilities-usegooglecalendaraction"></a>
The ability to use Google Calendar actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseGoogleDriveKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-usegoogledriveknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseHubspotAction`  <a name="cfn-quicksight-custompermissions-capabilities-usehubspotaction"></a>
The ability to use Hubspot actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseHuggingFaceAction`  <a name="cfn-quicksight-custompermissions-capabilities-usehuggingfaceaction"></a>
The ability to use HuggingFace actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseIDCKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-useidcknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseIntercomAction`  <a name="cfn-quicksight-custompermissions-capabilities-useintercomaction"></a>
The ability to use Intercom actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseJiraAction`  <a name="cfn-quicksight-custompermissions-capabilities-usejiraaction"></a>
The ability to use Jira actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseLinearAction`  <a name="cfn-quicksight-custompermissions-capabilities-uselinearaction"></a>
The ability to use Linear actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseMCPAction`  <a name="cfn-quicksight-custompermissions-capabilities-usemcpaction"></a>
The ability to use Model Context Protocol actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseMondayAction`  <a name="cfn-quicksight-custompermissions-capabilities-usemondayaction"></a>
The ability to use Monday actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseMSExchangeAction`  <a name="cfn-quicksight-custompermissions-capabilities-usemsexchangeaction"></a>
The ability to use Microsoft Outlook actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseMSTeamsAction`  <a name="cfn-quicksight-custompermissions-capabilities-usemsteamsaction"></a>
The ability to use Microsoft Teams actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseNewRelicAction`  <a name="cfn-quicksight-custompermissions-capabilities-usenewrelicaction"></a>
The ability to use New Relic actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseNotionAction`  <a name="cfn-quicksight-custompermissions-capabilities-usenotionaction"></a>
The ability to use Notion actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseOneDriveAction`  <a name="cfn-quicksight-custompermissions-capabilities-useonedriveaction"></a>
The ability to use Microsoft OneDrive actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseOneDriveKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-useonedriveknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseOpenAPIAction`  <a name="cfn-quicksight-custompermissions-capabilities-useopenapiaction"></a>
The ability to use OpenAPI Specification actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseOutlookAddInExtension`  <a name="cfn-quicksight-custompermissions-capabilities-useoutlookaddinextension"></a>
The ability to use Amazon Quick through the Microsoft Outlook add-in.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UsePagerDutyAction`  <a name="cfn-quicksight-custompermissions-capabilities-usepagerdutyaction"></a>
The ability to use PagerDuty Advance actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UsePowerpointAddInExtension`  <a name="cfn-quicksight-custompermissions-capabilities-usepowerpointaddinextension"></a>
The ability to use Amazon Quick through the Microsoft PowerPoint add-in.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseQBusinessKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-useqbusinessknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseS3KnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-uses3knowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseSalesforceAction`  <a name="cfn-quicksight-custompermissions-capabilities-usesalesforceaction"></a>
The ability to use Salesforce actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseSandPGlobalEnergyAction`  <a name="cfn-quicksight-custompermissions-capabilities-usesandpglobalenergyaction"></a>
The ability to use S&P Global Energy actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseSandPGMIAction`  <a name="cfn-quicksight-custompermissions-capabilities-usesandpgmiaction"></a>
The ability to use S&P Global Market Intelligence actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseSAPBillOfMaterialAction`  <a name="cfn-quicksight-custompermissions-capabilities-usesapbillofmaterialaction"></a>
The ability to use SAP Bill of Materials actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseSAPBusinessPartnerAction`  <a name="cfn-quicksight-custompermissions-capabilities-usesapbusinesspartneraction"></a>
The ability to use SAP Business Partner actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseSAPMaterialStockAction`  <a name="cfn-quicksight-custompermissions-capabilities-usesapmaterialstockaction"></a>
The ability to use SAP Material Stock actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseSAPPhysicalInventoryAction`  <a name="cfn-quicksight-custompermissions-capabilities-usesapphysicalinventoryaction"></a>
The ability to use SAP Physical Inventory actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseSAPProductMasterDataAction`  <a name="cfn-quicksight-custompermissions-capabilities-usesapproductmasterdataaction"></a>
The ability to use SAP Product Master actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseServiceNowAction`  <a name="cfn-quicksight-custompermissions-capabilities-useservicenowaction"></a>
The ability to use ServiceNow actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseSharePointAction`  <a name="cfn-quicksight-custompermissions-capabilities-usesharepointaction"></a>
The ability to use Microsoft SharePoint Online actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseSharePointKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-usesharepointknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseSlackAction`  <a name="cfn-quicksight-custompermissions-capabilities-useslackaction"></a>
The ability to use Slack actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseSmartsheetAction`  <a name="cfn-quicksight-custompermissions-capabilities-usesmartsheetaction"></a>
The ability to use Smartsheet actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseTextractAction`  <a name="cfn-quicksight-custompermissions-capabilities-usetextractaction"></a>
The ability to use Textract actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseWebCrawlerKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-usewebcrawlerknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseWordAddInExtension`  <a name="cfn-quicksight-custompermissions-capabilities-usewordaddinextension"></a>
The ability to use Amazon Quick through the Microsoft Word add-in.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseZendeskAction`  <a name="cfn-quicksight-custompermissions-capabilities-usezendeskaction"></a>
The ability to use Zendesk actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ViewAccountSPICECapacity`  <a name="cfn-quicksight-custompermissions-capabilities-viewaccountspicecapacity"></a>
The ability to view account SPICE capacity.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WebCrawlerKnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-webcrawlerknowledgebase"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ZendeskAction`  <a name="cfn-quicksight-custompermissions-capabilities-zendeskaction"></a>
The ability to perform actions using Zendesk connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY | ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
