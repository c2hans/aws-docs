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
  "[AmazonBedrockARSAction](#cfn-quicksight-custompermissions-capabilities-amazonbedrockarsaction)" : {{String}},
  "[AmazonBedrockFSAction](#cfn-quicksight-custompermissions-capabilities-amazonbedrockfsaction)" : {{String}},
  "[AmazonBedrockKRSAction](#cfn-quicksight-custompermissions-capabilities-amazonbedrockkrsaction)" : {{String}},
  "[AmazonSThreeAction](#cfn-quicksight-custompermissions-capabilities-amazonsthreeaction)" : {{String}},
  "[Analysis](#cfn-quicksight-custompermissions-capabilities-analysis)" : {{String}},
  "[ApproveFlowShareRequests](#cfn-quicksight-custompermissions-capabilities-approveflowsharerequests)" : {{String}},
  "[Apps](#cfn-quicksight-custompermissions-capabilities-apps)" : {{String}},
  "[AsanaAction](#cfn-quicksight-custompermissions-capabilities-asanaaction)" : {{String}},
  "[Automate](#cfn-quicksight-custompermissions-capabilities-automate)" : {{String}},
  "[BambooHRAction](#cfn-quicksight-custompermissions-capabilities-bamboohraction)" : {{String}},
  "[BoxAgentAction](#cfn-quicksight-custompermissions-capabilities-boxagentaction)" : {{String}},
  "[BuildCalculatedFieldWithQ](#cfn-quicksight-custompermissions-capabilities-buildcalculatedfieldwithq)" : {{String}},
  "[CanvaAgentAction](#cfn-quicksight-custompermissions-capabilities-canvaagentaction)" : {{String}},
  "[ChatAgent](#cfn-quicksight-custompermissions-capabilities-chatagent)" : {{String}},
  "[ComprehendAction](#cfn-quicksight-custompermissions-capabilities-comprehendaction)" : {{String}},
  "[ComprehendMedicalAction](#cfn-quicksight-custompermissions-capabilities-comprehendmedicalaction)" : {{String}},
  "[ConfluenceAction](#cfn-quicksight-custompermissions-capabilities-confluenceaction)" : {{String}},
  "[CreateAndUpdateAmazonBedrockARSAction](#cfn-quicksight-custompermissions-capabilities-createandupdateamazonbedrockarsaction)" : {{String}},
  "[CreateAndUpdateAmazonBedrockFSAction](#cfn-quicksight-custompermissions-capabilities-createandupdateamazonbedrockfsaction)" : {{String}},
  "[CreateAndUpdateAmazonBedrockKRSAction](#cfn-quicksight-custompermissions-capabilities-createandupdateamazonbedrockkrsaction)" : {{String}},
  "[CreateAndUpdateAmazonSThreeAction](#cfn-quicksight-custompermissions-capabilities-createandupdateamazonsthreeaction)" : {{String}},
  "[CreateAndUpdateApps](#cfn-quicksight-custompermissions-capabilities-createandupdateapps)" : {{String}},
  "[CreateAndUpdateAsanaAction](#cfn-quicksight-custompermissions-capabilities-createandupdateasanaaction)" : {{String}},
  "[CreateAndUpdateBambooHRAction](#cfn-quicksight-custompermissions-capabilities-createandupdatebamboohraction)" : {{String}},
  "[CreateAndUpdateBoxAgentAction](#cfn-quicksight-custompermissions-capabilities-createandupdateboxagentaction)" : {{String}},
  "[CreateAndUpdateCanvaAgentAction](#cfn-quicksight-custompermissions-capabilities-createandupdatecanvaagentaction)" : {{String}},
  "[CreateAndUpdateComprehendAction](#cfn-quicksight-custompermissions-capabilities-createandupdatecomprehendaction)" : {{String}},
  "[CreateAndUpdateComprehendMedicalAction](#cfn-quicksight-custompermissions-capabilities-createandupdatecomprehendmedicalaction)" : {{String}},
  "[CreateAndUpdateConfluenceAction](#cfn-quicksight-custompermissions-capabilities-createandupdateconfluenceaction)" : {{String}},
  "[CreateAndUpdateDashboardEmailReports](#cfn-quicksight-custompermissions-capabilities-createandupdatedashboardemailreports)" : {{String}},
  "[CreateAndUpdateDatasets](#cfn-quicksight-custompermissions-capabilities-createandupdatedatasets)" : {{String}},
  "[CreateAndUpdateDataSources](#cfn-quicksight-custompermissions-capabilities-createandupdatedatasources)" : {{String}},
  "[CreateAndUpdateFactSetAction](#cfn-quicksight-custompermissions-capabilities-createandupdatefactsetaction)" : {{String}},
  "[CreateAndUpdateGenericHTTPAction](#cfn-quicksight-custompermissions-capabilities-createandupdategenerichttpaction)" : {{String}},
  "[CreateAndUpdateGithubAction](#cfn-quicksight-custompermissions-capabilities-createandupdategithubaction)" : {{String}},
  "[CreateAndUpdateGoogleCalendarAction](#cfn-quicksight-custompermissions-capabilities-createandupdategooglecalendaraction)" : {{String}},
  "[CreateAndUpdateHubspotAction](#cfn-quicksight-custompermissions-capabilities-createandupdatehubspotaction)" : {{String}},
  "[CreateAndUpdateHuggingFaceAction](#cfn-quicksight-custompermissions-capabilities-createandupdatehuggingfaceaction)" : {{String}},
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
  "[CreateAndUpdateOpenAPIAction](#cfn-quicksight-custompermissions-capabilities-createandupdateopenapiaction)" : {{String}},
  "[CreateAndUpdatePagerDutyAction](#cfn-quicksight-custompermissions-capabilities-createandupdatepagerdutyaction)" : {{String}},
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
  "[CreateAndUpdateSlackAction](#cfn-quicksight-custompermissions-capabilities-createandupdateslackaction)" : {{String}},
  "[CreateAndUpdateSmartsheetAction](#cfn-quicksight-custompermissions-capabilities-createandupdatesmartsheetaction)" : {{String}},
  "[CreateAndUpdateTextractAction](#cfn-quicksight-custompermissions-capabilities-createandupdatetextractaction)" : {{String}},
  "[CreateAndUpdateThemes](#cfn-quicksight-custompermissions-capabilities-createandupdatethemes)" : {{String}},
  "[CreateAndUpdateThresholdAlerts](#cfn-quicksight-custompermissions-capabilities-createandupdatethresholdalerts)" : {{String}},
  "[CreateAndUpdateZendeskAction](#cfn-quicksight-custompermissions-capabilities-createandupdatezendeskaction)" : {{String}},
  "[CreateChatAgents](#cfn-quicksight-custompermissions-capabilities-createchatagents)" : {{String}},
  "[CreateDashboardExecutiveSummaryWithQ](#cfn-quicksight-custompermissions-capabilities-createdashboardexecutivesummarywithq)" : {{String}},
  "[CreateSharedFolders](#cfn-quicksight-custompermissions-capabilities-createsharedfolders)" : {{String}},
  "[CreateSpaces](#cfn-quicksight-custompermissions-capabilities-createspaces)" : {{String}},
  "[CreateSPICEDataset](#cfn-quicksight-custompermissions-capabilities-createspicedataset)" : {{String}},
  "[Dashboard](#cfn-quicksight-custompermissions-capabilities-dashboard)" : {{String}},
  "[EditVisualWithQ](#cfn-quicksight-custompermissions-capabilities-editvisualwithq)" : {{String}},
  "[ExportToCsv](#cfn-quicksight-custompermissions-capabilities-exporttocsv)" : {{String}},
  "[ExportToCsvInScheduledReports](#cfn-quicksight-custompermissions-capabilities-exporttocsvinscheduledreports)" : {{String}},
  "[ExportToExcel](#cfn-quicksight-custompermissions-capabilities-exporttoexcel)" : {{String}},
  "[ExportToExcelInScheduledReports](#cfn-quicksight-custompermissions-capabilities-exporttoexcelinscheduledreports)" : {{String}},
  "[ExportToPdf](#cfn-quicksight-custompermissions-capabilities-exporttopdf)" : {{String}},
  "[ExportToPdfInScheduledReports](#cfn-quicksight-custompermissions-capabilities-exporttopdfinscheduledreports)" : {{String}},
  "[Extension](#cfn-quicksight-custompermissions-capabilities-extension)" : {{String}},
  "[FactSetAction](#cfn-quicksight-custompermissions-capabilities-factsetaction)" : {{String}},
  "[Flow](#cfn-quicksight-custompermissions-capabilities-flow)" : {{String}},
  "[GenericHTTPAction](#cfn-quicksight-custompermissions-capabilities-generichttpaction)" : {{String}},
  "[GithubAction](#cfn-quicksight-custompermissions-capabilities-githubaction)" : {{String}},
  "[GoogleCalendarAction](#cfn-quicksight-custompermissions-capabilities-googlecalendaraction)" : {{String}},
  "[HubspotAction](#cfn-quicksight-custompermissions-capabilities-hubspotaction)" : {{String}},
  "[HuggingFaceAction](#cfn-quicksight-custompermissions-capabilities-huggingfaceaction)" : {{String}},
  "[IncludeContentInScheduledReportsEmail](#cfn-quicksight-custompermissions-capabilities-includecontentinscheduledreportsemail)" : {{String}},
  "[IntercomAction](#cfn-quicksight-custompermissions-capabilities-intercomaction)" : {{String}},
  "[InvokeAppsAIInference](#cfn-quicksight-custompermissions-capabilities-invokeappsaiinference)" : {{String}},
  "[JiraAction](#cfn-quicksight-custompermissions-capabilities-jiraaction)" : {{String}},
  "[KnowledgeBase](#cfn-quicksight-custompermissions-capabilities-knowledgebase)" : {{String}},
  "[LinearAction](#cfn-quicksight-custompermissions-capabilities-linearaction)" : {{String}},
  "[ManageSharedFolders](#cfn-quicksight-custompermissions-capabilities-managesharedfolders)" : {{String}},
  "[MCPAction](#cfn-quicksight-custompermissions-capabilities-mcpaction)" : {{String}},
  "[MondayAction](#cfn-quicksight-custompermissions-capabilities-mondayaction)" : {{String}},
  "[MSExchangeAction](#cfn-quicksight-custompermissions-capabilities-msexchangeaction)" : {{String}},
  "[MSTeamsAction](#cfn-quicksight-custompermissions-capabilities-msteamsaction)" : {{String}},
  "[NewRelicAction](#cfn-quicksight-custompermissions-capabilities-newrelicaction)" : {{String}},
  "[NotionAction](#cfn-quicksight-custompermissions-capabilities-notionaction)" : {{String}},
  "[OneDriveAction](#cfn-quicksight-custompermissions-capabilities-onedriveaction)" : {{String}},
  "[OpenAPIAction](#cfn-quicksight-custompermissions-capabilities-openapiaction)" : {{String}},
  "[PagerDutyAction](#cfn-quicksight-custompermissions-capabilities-pagerdutyaction)" : {{String}},
  "[PerformFlowUiTask](#cfn-quicksight-custompermissions-capabilities-performflowuitask)" : {{String}},
  "[PrintReports](#cfn-quicksight-custompermissions-capabilities-printreports)" : {{String}},
  "[PublishWithoutApproval](#cfn-quicksight-custompermissions-capabilities-publishwithoutapproval)" : {{String}},
  "[RenameSharedFolders](#cfn-quicksight-custompermissions-capabilities-renamesharedfolders)" : {{String}},
  "[Research](#cfn-quicksight-custompermissions-capabilities-research)" : {{String}},
  "[SalesforceAction](#cfn-quicksight-custompermissions-capabilities-salesforceaction)" : {{String}},
  "[SandPGlobalEnergyAction](#cfn-quicksight-custompermissions-capabilities-sandpglobalenergyaction)" : {{String}},
  "[SandPGMIAction](#cfn-quicksight-custompermissions-capabilities-sandpgmiaction)" : {{String}},
  "[SAPBillOfMaterialAction](#cfn-quicksight-custompermissions-capabilities-sapbillofmaterialaction)" : {{String}},
  "[SAPBusinessPartnerAction](#cfn-quicksight-custompermissions-capabilities-sapbusinesspartneraction)" : {{String}},
  "[SAPMaterialStockAction](#cfn-quicksight-custompermissions-capabilities-sapmaterialstockaction)" : {{String}},
  "[SAPPhysicalInventoryAction](#cfn-quicksight-custompermissions-capabilities-sapphysicalinventoryaction)" : {{String}},
  "[SAPProductMasterDataAction](#cfn-quicksight-custompermissions-capabilities-sapproductmasterdataaction)" : {{String}},
  "[ServiceNowAction](#cfn-quicksight-custompermissions-capabilities-servicenowaction)" : {{String}},
  "[ShareAmazonBedrockARSAction](#cfn-quicksight-custompermissions-capabilities-shareamazonbedrockarsaction)" : {{String}},
  "[ShareAmazonBedrockFSAction](#cfn-quicksight-custompermissions-capabilities-shareamazonbedrockfsaction)" : {{String}},
  "[ShareAmazonBedrockKRSAction](#cfn-quicksight-custompermissions-capabilities-shareamazonbedrockkrsaction)" : {{String}},
  "[ShareAmazonSThreeAction](#cfn-quicksight-custompermissions-capabilities-shareamazonsthreeaction)" : {{String}},
  "[ShareAnalyses](#cfn-quicksight-custompermissions-capabilities-shareanalyses)" : {{String}},
  "[ShareApps](#cfn-quicksight-custompermissions-capabilities-shareapps)" : {{String}},
  "[ShareAsanaAction](#cfn-quicksight-custompermissions-capabilities-shareasanaaction)" : {{String}},
  "[ShareBambooHRAction](#cfn-quicksight-custompermissions-capabilities-sharebamboohraction)" : {{String}},
  "[ShareBoxAgentAction](#cfn-quicksight-custompermissions-capabilities-shareboxagentaction)" : {{String}},
  "[ShareCanvaAgentAction](#cfn-quicksight-custompermissions-capabilities-sharecanvaagentaction)" : {{String}},
  "[ShareChatAgents](#cfn-quicksight-custompermissions-capabilities-sharechatagents)" : {{String}},
  "[ShareComprehendAction](#cfn-quicksight-custompermissions-capabilities-sharecomprehendaction)" : {{String}},
  "[ShareComprehendMedicalAction](#cfn-quicksight-custompermissions-capabilities-sharecomprehendmedicalaction)" : {{String}},
  "[ShareConfluenceAction](#cfn-quicksight-custompermissions-capabilities-shareconfluenceaction)" : {{String}},
  "[ShareDashboards](#cfn-quicksight-custompermissions-capabilities-sharedashboards)" : {{String}},
  "[ShareDatasets](#cfn-quicksight-custompermissions-capabilities-sharedatasets)" : {{String}},
  "[ShareDataSources](#cfn-quicksight-custompermissions-capabilities-sharedatasources)" : {{String}},
  "[ShareFactSetAction](#cfn-quicksight-custompermissions-capabilities-sharefactsetaction)" : {{String}},
  "[ShareGenericHTTPAction](#cfn-quicksight-custompermissions-capabilities-sharegenerichttpaction)" : {{String}},
  "[ShareGithubAction](#cfn-quicksight-custompermissions-capabilities-sharegithubaction)" : {{String}},
  "[ShareGoogleCalendarAction](#cfn-quicksight-custompermissions-capabilities-sharegooglecalendaraction)" : {{String}},
  "[ShareHubspotAction](#cfn-quicksight-custompermissions-capabilities-sharehubspotaction)" : {{String}},
  "[ShareHuggingFaceAction](#cfn-quicksight-custompermissions-capabilities-sharehuggingfaceaction)" : {{String}},
  "[ShareIntercomAction](#cfn-quicksight-custompermissions-capabilities-shareintercomaction)" : {{String}},
  "[ShareJiraAction](#cfn-quicksight-custompermissions-capabilities-sharejiraaction)" : {{String}},
  "[ShareKnowledgeBases](#cfn-quicksight-custompermissions-capabilities-shareknowledgebases)" : {{String}},
  "[ShareLinearAction](#cfn-quicksight-custompermissions-capabilities-sharelinearaction)" : {{String}},
  "[ShareMCPAction](#cfn-quicksight-custompermissions-capabilities-sharemcpaction)" : {{String}},
  "[ShareMondayAction](#cfn-quicksight-custompermissions-capabilities-sharemondayaction)" : {{String}},
  "[ShareMSExchangeAction](#cfn-quicksight-custompermissions-capabilities-sharemsexchangeaction)" : {{String}},
  "[ShareMSTeamsAction](#cfn-quicksight-custompermissions-capabilities-sharemsteamsaction)" : {{String}},
  "[ShareNewRelicAction](#cfn-quicksight-custompermissions-capabilities-sharenewrelicaction)" : {{String}},
  "[ShareNotionAction](#cfn-quicksight-custompermissions-capabilities-sharenotionaction)" : {{String}},
  "[ShareOneDriveAction](#cfn-quicksight-custompermissions-capabilities-shareonedriveaction)" : {{String}},
  "[ShareOpenAPIAction](#cfn-quicksight-custompermissions-capabilities-shareopenapiaction)" : {{String}},
  "[SharePagerDutyAction](#cfn-quicksight-custompermissions-capabilities-sharepagerdutyaction)" : {{String}},
  "[SharePointAction](#cfn-quicksight-custompermissions-capabilities-sharepointaction)" : {{String}},
  "[ShareSalesforceAction](#cfn-quicksight-custompermissions-capabilities-sharesalesforceaction)" : {{String}},
  "[ShareSandPGlobalEnergyAction](#cfn-quicksight-custompermissions-capabilities-sharesandpglobalenergyaction)" : {{String}},
  "[ShareSandPGMIAction](#cfn-quicksight-custompermissions-capabilities-sharesandpgmiaction)" : {{String}},
  "[ShareSAPBillOfMaterialAction](#cfn-quicksight-custompermissions-capabilities-sharesapbillofmaterialaction)" : {{String}},
  "[ShareSAPBusinessPartnerAction](#cfn-quicksight-custompermissions-capabilities-sharesapbusinesspartneraction)" : {{String}},
  "[ShareSAPMaterialStockAction](#cfn-quicksight-custompermissions-capabilities-sharesapmaterialstockaction)" : {{String}},
  "[ShareSAPPhysicalInventoryAction](#cfn-quicksight-custompermissions-capabilities-sharesapphysicalinventoryaction)" : {{String}},
  "[ShareSAPProductMasterDataAction](#cfn-quicksight-custompermissions-capabilities-sharesapproductmasterdataaction)" : {{String}},
  "[ShareServiceNowAction](#cfn-quicksight-custompermissions-capabilities-shareservicenowaction)" : {{String}},
  "[ShareSharePointAction](#cfn-quicksight-custompermissions-capabilities-sharesharepointaction)" : {{String}},
  "[ShareSlackAction](#cfn-quicksight-custompermissions-capabilities-shareslackaction)" : {{String}},
  "[ShareSmartsheetAction](#cfn-quicksight-custompermissions-capabilities-sharesmartsheetaction)" : {{String}},
  "[ShareSpaces](#cfn-quicksight-custompermissions-capabilities-sharespaces)" : {{String}},
  "[ShareTextractAction](#cfn-quicksight-custompermissions-capabilities-sharetextractaction)" : {{String}},
  "[ShareZendeskAction](#cfn-quicksight-custompermissions-capabilities-sharezendeskaction)" : {{String}},
  "[SlackAction](#cfn-quicksight-custompermissions-capabilities-slackaction)" : {{String}},
  "[SmartsheetAction](#cfn-quicksight-custompermissions-capabilities-smartsheetaction)" : {{String}},
  "[Space](#cfn-quicksight-custompermissions-capabilities-space)" : {{String}},
  "[SubscribeDashboardEmailReports](#cfn-quicksight-custompermissions-capabilities-subscribedashboardemailreports)" : {{String}},
  "[TextractAction](#cfn-quicksight-custompermissions-capabilities-textractaction)" : {{String}},
  "[Topic](#cfn-quicksight-custompermissions-capabilities-topic)" : {{String}},
  "[UseAgentWebSearch](#cfn-quicksight-custompermissions-capabilities-useagentwebsearch)" : {{String}},
  "[UseAmazonBedrockARSAction](#cfn-quicksight-custompermissions-capabilities-useamazonbedrockarsaction)" : {{String}},
  "[UseAmazonBedrockFSAction](#cfn-quicksight-custompermissions-capabilities-useamazonbedrockfsaction)" : {{String}},
  "[UseAmazonBedrockKRSAction](#cfn-quicksight-custompermissions-capabilities-useamazonbedrockkrsaction)" : {{String}},
  "[UseAmazonSThreeAction](#cfn-quicksight-custompermissions-capabilities-useamazonsthreeaction)" : {{String}},
  "[UseAsanaAction](#cfn-quicksight-custompermissions-capabilities-useasanaaction)" : {{String}},
  "[UseBambooHRAction](#cfn-quicksight-custompermissions-capabilities-usebamboohraction)" : {{String}},
  "[UseBedrockModels](#cfn-quicksight-custompermissions-capabilities-usebedrockmodels)" : {{String}},
  "[UseBoxAgentAction](#cfn-quicksight-custompermissions-capabilities-useboxagentaction)" : {{String}},
  "[UseCanvaAgentAction](#cfn-quicksight-custompermissions-capabilities-usecanvaagentaction)" : {{String}},
  "[UseComprehendAction](#cfn-quicksight-custompermissions-capabilities-usecomprehendaction)" : {{String}},
  "[UseComprehendMedicalAction](#cfn-quicksight-custompermissions-capabilities-usecomprehendmedicalaction)" : {{String}},
  "[UseConfluenceAction](#cfn-quicksight-custompermissions-capabilities-useconfluenceaction)" : {{String}},
  "[UseFactSetAction](#cfn-quicksight-custompermissions-capabilities-usefactsetaction)" : {{String}},
  "[UseGenericHTTPAction](#cfn-quicksight-custompermissions-capabilities-usegenerichttpaction)" : {{String}},
  "[UseGithubAction](#cfn-quicksight-custompermissions-capabilities-usegithubaction)" : {{String}},
  "[UseGoogleCalendarAction](#cfn-quicksight-custompermissions-capabilities-usegooglecalendaraction)" : {{String}},
  "[UseHubspotAction](#cfn-quicksight-custompermissions-capabilities-usehubspotaction)" : {{String}},
  "[UseHuggingFaceAction](#cfn-quicksight-custompermissions-capabilities-usehuggingfaceaction)" : {{String}},
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
  "[UseOpenAPIAction](#cfn-quicksight-custompermissions-capabilities-useopenapiaction)" : {{String}},
  "[UsePagerDutyAction](#cfn-quicksight-custompermissions-capabilities-usepagerdutyaction)" : {{String}},
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
  "[UseSlackAction](#cfn-quicksight-custompermissions-capabilities-useslackaction)" : {{String}},
  "[UseSmartsheetAction](#cfn-quicksight-custompermissions-capabilities-usesmartsheetaction)" : {{String}},
  "[UseTextractAction](#cfn-quicksight-custompermissions-capabilities-usetextractaction)" : {{String}},
  "[UseZendeskAction](#cfn-quicksight-custompermissions-capabilities-usezendeskaction)" : {{String}},
  "[ViewAccountSPICECapacity](#cfn-quicksight-custompermissions-capabilities-viewaccountspicecapacity)" : {{String}},
  "[ZendeskAction](#cfn-quicksight-custompermissions-capabilities-zendeskaction)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-custompermissions-capabilities-syntax.yaml"></a>

```
  [AccessAppsNativeDataStore](#cfn-quicksight-custompermissions-capabilities-accessappsnativedatastore): {{String}}
  [Action](#cfn-quicksight-custompermissions-capabilities-action): {{String}}
  [AddOrRunAnomalyDetectionForAnalyses](#cfn-quicksight-custompermissions-capabilities-addorrunanomalydetectionforanalyses): {{String}}
  [AmazonBedrockARSAction](#cfn-quicksight-custompermissions-capabilities-amazonbedrockarsaction): {{String}}
  [AmazonBedrockFSAction](#cfn-quicksight-custompermissions-capabilities-amazonbedrockfsaction): {{String}}
  [AmazonBedrockKRSAction](#cfn-quicksight-custompermissions-capabilities-amazonbedrockkrsaction): {{String}}
  [AmazonSThreeAction](#cfn-quicksight-custompermissions-capabilities-amazonsthreeaction): {{String}}
  [Analysis](#cfn-quicksight-custompermissions-capabilities-analysis): {{String}}
  [ApproveFlowShareRequests](#cfn-quicksight-custompermissions-capabilities-approveflowsharerequests): {{String}}
  [Apps](#cfn-quicksight-custompermissions-capabilities-apps): {{String}}
  [AsanaAction](#cfn-quicksight-custompermissions-capabilities-asanaaction): {{String}}
  [Automate](#cfn-quicksight-custompermissions-capabilities-automate): {{String}}
  [BambooHRAction](#cfn-quicksight-custompermissions-capabilities-bamboohraction): {{String}}
  [BoxAgentAction](#cfn-quicksight-custompermissions-capabilities-boxagentaction): {{String}}
  [BuildCalculatedFieldWithQ](#cfn-quicksight-custompermissions-capabilities-buildcalculatedfieldwithq): {{String}}
  [CanvaAgentAction](#cfn-quicksight-custompermissions-capabilities-canvaagentaction): {{String}}
  [ChatAgent](#cfn-quicksight-custompermissions-capabilities-chatagent): {{String}}
  [ComprehendAction](#cfn-quicksight-custompermissions-capabilities-comprehendaction): {{String}}
  [ComprehendMedicalAction](#cfn-quicksight-custompermissions-capabilities-comprehendmedicalaction): {{String}}
  [ConfluenceAction](#cfn-quicksight-custompermissions-capabilities-confluenceaction): {{String}}
  [CreateAndUpdateAmazonBedrockARSAction](#cfn-quicksight-custompermissions-capabilities-createandupdateamazonbedrockarsaction): {{String}}
  [CreateAndUpdateAmazonBedrockFSAction](#cfn-quicksight-custompermissions-capabilities-createandupdateamazonbedrockfsaction): {{String}}
  [CreateAndUpdateAmazonBedrockKRSAction](#cfn-quicksight-custompermissions-capabilities-createandupdateamazonbedrockkrsaction): {{String}}
  [CreateAndUpdateAmazonSThreeAction](#cfn-quicksight-custompermissions-capabilities-createandupdateamazonsthreeaction): {{String}}
  [CreateAndUpdateApps](#cfn-quicksight-custompermissions-capabilities-createandupdateapps): {{String}}
  [CreateAndUpdateAsanaAction](#cfn-quicksight-custompermissions-capabilities-createandupdateasanaaction): {{String}}
  [CreateAndUpdateBambooHRAction](#cfn-quicksight-custompermissions-capabilities-createandupdatebamboohraction): {{String}}
  [CreateAndUpdateBoxAgentAction](#cfn-quicksight-custompermissions-capabilities-createandupdateboxagentaction): {{String}}
  [CreateAndUpdateCanvaAgentAction](#cfn-quicksight-custompermissions-capabilities-createandupdatecanvaagentaction): {{String}}
  [CreateAndUpdateComprehendAction](#cfn-quicksight-custompermissions-capabilities-createandupdatecomprehendaction): {{String}}
  [CreateAndUpdateComprehendMedicalAction](#cfn-quicksight-custompermissions-capabilities-createandupdatecomprehendmedicalaction): {{String}}
  [CreateAndUpdateConfluenceAction](#cfn-quicksight-custompermissions-capabilities-createandupdateconfluenceaction): {{String}}
  [CreateAndUpdateDashboardEmailReports](#cfn-quicksight-custompermissions-capabilities-createandupdatedashboardemailreports): {{String}}
  [CreateAndUpdateDatasets](#cfn-quicksight-custompermissions-capabilities-createandupdatedatasets): {{String}}
  [CreateAndUpdateDataSources](#cfn-quicksight-custompermissions-capabilities-createandupdatedatasources): {{String}}
  [CreateAndUpdateFactSetAction](#cfn-quicksight-custompermissions-capabilities-createandupdatefactsetaction): {{String}}
  [CreateAndUpdateGenericHTTPAction](#cfn-quicksight-custompermissions-capabilities-createandupdategenerichttpaction): {{String}}
  [CreateAndUpdateGithubAction](#cfn-quicksight-custompermissions-capabilities-createandupdategithubaction): {{String}}
  [CreateAndUpdateGoogleCalendarAction](#cfn-quicksight-custompermissions-capabilities-createandupdategooglecalendaraction): {{String}}
  [CreateAndUpdateHubspotAction](#cfn-quicksight-custompermissions-capabilities-createandupdatehubspotaction): {{String}}
  [CreateAndUpdateHuggingFaceAction](#cfn-quicksight-custompermissions-capabilities-createandupdatehuggingfaceaction): {{String}}
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
  [CreateAndUpdateOpenAPIAction](#cfn-quicksight-custompermissions-capabilities-createandupdateopenapiaction): {{String}}
  [CreateAndUpdatePagerDutyAction](#cfn-quicksight-custompermissions-capabilities-createandupdatepagerdutyaction): {{String}}
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
  [CreateAndUpdateSlackAction](#cfn-quicksight-custompermissions-capabilities-createandupdateslackaction): {{String}}
  [CreateAndUpdateSmartsheetAction](#cfn-quicksight-custompermissions-capabilities-createandupdatesmartsheetaction): {{String}}
  [CreateAndUpdateTextractAction](#cfn-quicksight-custompermissions-capabilities-createandupdatetextractaction): {{String}}
  [CreateAndUpdateThemes](#cfn-quicksight-custompermissions-capabilities-createandupdatethemes): {{String}}
  [CreateAndUpdateThresholdAlerts](#cfn-quicksight-custompermissions-capabilities-createandupdatethresholdalerts): {{String}}
  [CreateAndUpdateZendeskAction](#cfn-quicksight-custompermissions-capabilities-createandupdatezendeskaction): {{String}}
  [CreateChatAgents](#cfn-quicksight-custompermissions-capabilities-createchatagents): {{String}}
  [CreateDashboardExecutiveSummaryWithQ](#cfn-quicksight-custompermissions-capabilities-createdashboardexecutivesummarywithq): {{String}}
  [CreateSharedFolders](#cfn-quicksight-custompermissions-capabilities-createsharedfolders): {{String}}
  [CreateSpaces](#cfn-quicksight-custompermissions-capabilities-createspaces): {{String}}
  [CreateSPICEDataset](#cfn-quicksight-custompermissions-capabilities-createspicedataset): {{String}}
  [Dashboard](#cfn-quicksight-custompermissions-capabilities-dashboard): {{String}}
  [EditVisualWithQ](#cfn-quicksight-custompermissions-capabilities-editvisualwithq): {{String}}
  [ExportToCsv](#cfn-quicksight-custompermissions-capabilities-exporttocsv): {{String}}
  [ExportToCsvInScheduledReports](#cfn-quicksight-custompermissions-capabilities-exporttocsvinscheduledreports): {{String}}
  [ExportToExcel](#cfn-quicksight-custompermissions-capabilities-exporttoexcel): {{String}}
  [ExportToExcelInScheduledReports](#cfn-quicksight-custompermissions-capabilities-exporttoexcelinscheduledreports): {{String}}
  [ExportToPdf](#cfn-quicksight-custompermissions-capabilities-exporttopdf): {{String}}
  [ExportToPdfInScheduledReports](#cfn-quicksight-custompermissions-capabilities-exporttopdfinscheduledreports): {{String}}
  [Extension](#cfn-quicksight-custompermissions-capabilities-extension): {{String}}
  [FactSetAction](#cfn-quicksight-custompermissions-capabilities-factsetaction): {{String}}
  [Flow](#cfn-quicksight-custompermissions-capabilities-flow): {{String}}
  [GenericHTTPAction](#cfn-quicksight-custompermissions-capabilities-generichttpaction): {{String}}
  [GithubAction](#cfn-quicksight-custompermissions-capabilities-githubaction): {{String}}
  [GoogleCalendarAction](#cfn-quicksight-custompermissions-capabilities-googlecalendaraction): {{String}}
  [HubspotAction](#cfn-quicksight-custompermissions-capabilities-hubspotaction): {{String}}
  [HuggingFaceAction](#cfn-quicksight-custompermissions-capabilities-huggingfaceaction): {{String}}
  [IncludeContentInScheduledReportsEmail](#cfn-quicksight-custompermissions-capabilities-includecontentinscheduledreportsemail): {{String}}
  [IntercomAction](#cfn-quicksight-custompermissions-capabilities-intercomaction): {{String}}
  [InvokeAppsAIInference](#cfn-quicksight-custompermissions-capabilities-invokeappsaiinference): {{String}}
  [JiraAction](#cfn-quicksight-custompermissions-capabilities-jiraaction): {{String}}
  [KnowledgeBase](#cfn-quicksight-custompermissions-capabilities-knowledgebase): {{String}}
  [LinearAction](#cfn-quicksight-custompermissions-capabilities-linearaction): {{String}}
  [ManageSharedFolders](#cfn-quicksight-custompermissions-capabilities-managesharedfolders): {{String}}
  [MCPAction](#cfn-quicksight-custompermissions-capabilities-mcpaction): {{String}}
  [MondayAction](#cfn-quicksight-custompermissions-capabilities-mondayaction): {{String}}
  [MSExchangeAction](#cfn-quicksight-custompermissions-capabilities-msexchangeaction): {{String}}
  [MSTeamsAction](#cfn-quicksight-custompermissions-capabilities-msteamsaction): {{String}}
  [NewRelicAction](#cfn-quicksight-custompermissions-capabilities-newrelicaction): {{String}}
  [NotionAction](#cfn-quicksight-custompermissions-capabilities-notionaction): {{String}}
  [OneDriveAction](#cfn-quicksight-custompermissions-capabilities-onedriveaction): {{String}}
  [OpenAPIAction](#cfn-quicksight-custompermissions-capabilities-openapiaction): {{String}}
  [PagerDutyAction](#cfn-quicksight-custompermissions-capabilities-pagerdutyaction): {{String}}
  [PerformFlowUiTask](#cfn-quicksight-custompermissions-capabilities-performflowuitask): {{String}}
  [PrintReports](#cfn-quicksight-custompermissions-capabilities-printreports): {{String}}
  [PublishWithoutApproval](#cfn-quicksight-custompermissions-capabilities-publishwithoutapproval): {{String}}
  [RenameSharedFolders](#cfn-quicksight-custompermissions-capabilities-renamesharedfolders): {{String}}
  [Research](#cfn-quicksight-custompermissions-capabilities-research): {{String}}
  [SalesforceAction](#cfn-quicksight-custompermissions-capabilities-salesforceaction): {{String}}
  [SandPGlobalEnergyAction](#cfn-quicksight-custompermissions-capabilities-sandpglobalenergyaction): {{String}}
  [SandPGMIAction](#cfn-quicksight-custompermissions-capabilities-sandpgmiaction): {{String}}
  [SAPBillOfMaterialAction](#cfn-quicksight-custompermissions-capabilities-sapbillofmaterialaction): {{String}}
  [SAPBusinessPartnerAction](#cfn-quicksight-custompermissions-capabilities-sapbusinesspartneraction): {{String}}
  [SAPMaterialStockAction](#cfn-quicksight-custompermissions-capabilities-sapmaterialstockaction): {{String}}
  [SAPPhysicalInventoryAction](#cfn-quicksight-custompermissions-capabilities-sapphysicalinventoryaction): {{String}}
  [SAPProductMasterDataAction](#cfn-quicksight-custompermissions-capabilities-sapproductmasterdataaction): {{String}}
  [ServiceNowAction](#cfn-quicksight-custompermissions-capabilities-servicenowaction): {{String}}
  [ShareAmazonBedrockARSAction](#cfn-quicksight-custompermissions-capabilities-shareamazonbedrockarsaction): {{String}}
  [ShareAmazonBedrockFSAction](#cfn-quicksight-custompermissions-capabilities-shareamazonbedrockfsaction): {{String}}
  [ShareAmazonBedrockKRSAction](#cfn-quicksight-custompermissions-capabilities-shareamazonbedrockkrsaction): {{String}}
  [ShareAmazonSThreeAction](#cfn-quicksight-custompermissions-capabilities-shareamazonsthreeaction): {{String}}
  [ShareAnalyses](#cfn-quicksight-custompermissions-capabilities-shareanalyses): {{String}}
  [ShareApps](#cfn-quicksight-custompermissions-capabilities-shareapps): {{String}}
  [ShareAsanaAction](#cfn-quicksight-custompermissions-capabilities-shareasanaaction): {{String}}
  [ShareBambooHRAction](#cfn-quicksight-custompermissions-capabilities-sharebamboohraction): {{String}}
  [ShareBoxAgentAction](#cfn-quicksight-custompermissions-capabilities-shareboxagentaction): {{String}}
  [ShareCanvaAgentAction](#cfn-quicksight-custompermissions-capabilities-sharecanvaagentaction): {{String}}
  [ShareChatAgents](#cfn-quicksight-custompermissions-capabilities-sharechatagents): {{String}}
  [ShareComprehendAction](#cfn-quicksight-custompermissions-capabilities-sharecomprehendaction): {{String}}
  [ShareComprehendMedicalAction](#cfn-quicksight-custompermissions-capabilities-sharecomprehendmedicalaction): {{String}}
  [ShareConfluenceAction](#cfn-quicksight-custompermissions-capabilities-shareconfluenceaction): {{String}}
  [ShareDashboards](#cfn-quicksight-custompermissions-capabilities-sharedashboards): {{String}}
  [ShareDatasets](#cfn-quicksight-custompermissions-capabilities-sharedatasets): {{String}}
  [ShareDataSources](#cfn-quicksight-custompermissions-capabilities-sharedatasources): {{String}}
  [ShareFactSetAction](#cfn-quicksight-custompermissions-capabilities-sharefactsetaction): {{String}}
  [ShareGenericHTTPAction](#cfn-quicksight-custompermissions-capabilities-sharegenerichttpaction): {{String}}
  [ShareGithubAction](#cfn-quicksight-custompermissions-capabilities-sharegithubaction): {{String}}
  [ShareGoogleCalendarAction](#cfn-quicksight-custompermissions-capabilities-sharegooglecalendaraction): {{String}}
  [ShareHubspotAction](#cfn-quicksight-custompermissions-capabilities-sharehubspotaction): {{String}}
  [ShareHuggingFaceAction](#cfn-quicksight-custompermissions-capabilities-sharehuggingfaceaction): {{String}}
  [ShareIntercomAction](#cfn-quicksight-custompermissions-capabilities-shareintercomaction): {{String}}
  [ShareJiraAction](#cfn-quicksight-custompermissions-capabilities-sharejiraaction): {{String}}
  [ShareKnowledgeBases](#cfn-quicksight-custompermissions-capabilities-shareknowledgebases): {{String}}
  [ShareLinearAction](#cfn-quicksight-custompermissions-capabilities-sharelinearaction): {{String}}
  [ShareMCPAction](#cfn-quicksight-custompermissions-capabilities-sharemcpaction): {{String}}
  [ShareMondayAction](#cfn-quicksight-custompermissions-capabilities-sharemondayaction): {{String}}
  [ShareMSExchangeAction](#cfn-quicksight-custompermissions-capabilities-sharemsexchangeaction): {{String}}
  [ShareMSTeamsAction](#cfn-quicksight-custompermissions-capabilities-sharemsteamsaction): {{String}}
  [ShareNewRelicAction](#cfn-quicksight-custompermissions-capabilities-sharenewrelicaction): {{String}}
  [ShareNotionAction](#cfn-quicksight-custompermissions-capabilities-sharenotionaction): {{String}}
  [ShareOneDriveAction](#cfn-quicksight-custompermissions-capabilities-shareonedriveaction): {{String}}
  [ShareOpenAPIAction](#cfn-quicksight-custompermissions-capabilities-shareopenapiaction): {{String}}
  [SharePagerDutyAction](#cfn-quicksight-custompermissions-capabilities-sharepagerdutyaction): {{String}}
  [SharePointAction](#cfn-quicksight-custompermissions-capabilities-sharepointaction): {{String}}
  [ShareSalesforceAction](#cfn-quicksight-custompermissions-capabilities-sharesalesforceaction): {{String}}
  [ShareSandPGlobalEnergyAction](#cfn-quicksight-custompermissions-capabilities-sharesandpglobalenergyaction): {{String}}
  [ShareSandPGMIAction](#cfn-quicksight-custompermissions-capabilities-sharesandpgmiaction): {{String}}
  [ShareSAPBillOfMaterialAction](#cfn-quicksight-custompermissions-capabilities-sharesapbillofmaterialaction): {{String}}
  [ShareSAPBusinessPartnerAction](#cfn-quicksight-custompermissions-capabilities-sharesapbusinesspartneraction): {{String}}
  [ShareSAPMaterialStockAction](#cfn-quicksight-custompermissions-capabilities-sharesapmaterialstockaction): {{String}}
  [ShareSAPPhysicalInventoryAction](#cfn-quicksight-custompermissions-capabilities-sharesapphysicalinventoryaction): {{String}}
  [ShareSAPProductMasterDataAction](#cfn-quicksight-custompermissions-capabilities-sharesapproductmasterdataaction): {{String}}
  [ShareServiceNowAction](#cfn-quicksight-custompermissions-capabilities-shareservicenowaction): {{String}}
  [ShareSharePointAction](#cfn-quicksight-custompermissions-capabilities-sharesharepointaction): {{String}}
  [ShareSlackAction](#cfn-quicksight-custompermissions-capabilities-shareslackaction): {{String}}
  [ShareSmartsheetAction](#cfn-quicksight-custompermissions-capabilities-sharesmartsheetaction): {{String}}
  [ShareSpaces](#cfn-quicksight-custompermissions-capabilities-sharespaces): {{String}}
  [ShareTextractAction](#cfn-quicksight-custompermissions-capabilities-sharetextractaction): {{String}}
  [ShareZendeskAction](#cfn-quicksight-custompermissions-capabilities-sharezendeskaction): {{String}}
  [SlackAction](#cfn-quicksight-custompermissions-capabilities-slackaction): {{String}}
  [SmartsheetAction](#cfn-quicksight-custompermissions-capabilities-smartsheetaction): {{String}}
  [Space](#cfn-quicksight-custompermissions-capabilities-space): {{String}}
  [SubscribeDashboardEmailReports](#cfn-quicksight-custompermissions-capabilities-subscribedashboardemailreports): {{String}}
  [TextractAction](#cfn-quicksight-custompermissions-capabilities-textractaction): {{String}}
  [Topic](#cfn-quicksight-custompermissions-capabilities-topic): {{String}}
  [UseAgentWebSearch](#cfn-quicksight-custompermissions-capabilities-useagentwebsearch): {{String}}
  [UseAmazonBedrockARSAction](#cfn-quicksight-custompermissions-capabilities-useamazonbedrockarsaction): {{String}}
  [UseAmazonBedrockFSAction](#cfn-quicksight-custompermissions-capabilities-useamazonbedrockfsaction): {{String}}
  [UseAmazonBedrockKRSAction](#cfn-quicksight-custompermissions-capabilities-useamazonbedrockkrsaction): {{String}}
  [UseAmazonSThreeAction](#cfn-quicksight-custompermissions-capabilities-useamazonsthreeaction): {{String}}
  [UseAsanaAction](#cfn-quicksight-custompermissions-capabilities-useasanaaction): {{String}}
  [UseBambooHRAction](#cfn-quicksight-custompermissions-capabilities-usebamboohraction): {{String}}
  [UseBedrockModels](#cfn-quicksight-custompermissions-capabilities-usebedrockmodels): {{String}}
  [UseBoxAgentAction](#cfn-quicksight-custompermissions-capabilities-useboxagentaction): {{String}}
  [UseCanvaAgentAction](#cfn-quicksight-custompermissions-capabilities-usecanvaagentaction): {{String}}
  [UseComprehendAction](#cfn-quicksight-custompermissions-capabilities-usecomprehendaction): {{String}}
  [UseComprehendMedicalAction](#cfn-quicksight-custompermissions-capabilities-usecomprehendmedicalaction): {{String}}
  [UseConfluenceAction](#cfn-quicksight-custompermissions-capabilities-useconfluenceaction): {{String}}
  [UseFactSetAction](#cfn-quicksight-custompermissions-capabilities-usefactsetaction): {{String}}
  [UseGenericHTTPAction](#cfn-quicksight-custompermissions-capabilities-usegenerichttpaction): {{String}}
  [UseGithubAction](#cfn-quicksight-custompermissions-capabilities-usegithubaction): {{String}}
  [UseGoogleCalendarAction](#cfn-quicksight-custompermissions-capabilities-usegooglecalendaraction): {{String}}
  [UseHubspotAction](#cfn-quicksight-custompermissions-capabilities-usehubspotaction): {{String}}
  [UseHuggingFaceAction](#cfn-quicksight-custompermissions-capabilities-usehuggingfaceaction): {{String}}
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
  [UseOpenAPIAction](#cfn-quicksight-custompermissions-capabilities-useopenapiaction): {{String}}
  [UsePagerDutyAction](#cfn-quicksight-custompermissions-capabilities-usepagerdutyaction): {{String}}
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
  [UseSlackAction](#cfn-quicksight-custompermissions-capabilities-useslackaction): {{String}}
  [UseSmartsheetAction](#cfn-quicksight-custompermissions-capabilities-usesmartsheetaction): {{String}}
  [UseTextractAction](#cfn-quicksight-custompermissions-capabilities-usetextractaction): {{String}}
  [UseZendeskAction](#cfn-quicksight-custompermissions-capabilities-usezendeskaction): {{String}}
  [ViewAccountSPICECapacity](#cfn-quicksight-custompermissions-capabilities-viewaccountspicecapacity): {{String}}
  [ZendeskAction](#cfn-quicksight-custompermissions-capabilities-zendeskaction): {{String}}
```

## Properties
<a name="aws-properties-quicksight-custompermissions-capabilities-properties"></a>

`AccessAppsNativeDataStore`  <a name="cfn-quicksight-custompermissions-capabilities-accessappsnativedatastore"></a>
The ability to access the native data store for new and existing apps.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Action`  <a name="cfn-quicksight-custompermissions-capabilities-action"></a>
The ability to perform actions in external services through Action connectors. Actions allow users to interact with third-party systems.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AddOrRunAnomalyDetectionForAnalyses`  <a name="cfn-quicksight-custompermissions-capabilities-addorrunanomalydetectionforanalyses"></a>
The ability to add or run anomaly detection.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AmazonBedrockARSAction`  <a name="cfn-quicksight-custompermissions-capabilities-amazonbedrockarsaction"></a>
The ability to perform actions using Bedrock Agent connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AmazonBedrockFSAction`  <a name="cfn-quicksight-custompermissions-capabilities-amazonbedrockfsaction"></a>
The ability to perform actions using Bedrock Runtime connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AmazonBedrockKRSAction`  <a name="cfn-quicksight-custompermissions-capabilities-amazonbedrockkrsaction"></a>
The ability to perform actions using Bedrock Data Automation Runtime connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AmazonSThreeAction`  <a name="cfn-quicksight-custompermissions-capabilities-amazonsthreeaction"></a>
The ability to perform actions using Amazon S3 connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Analysis`  <a name="cfn-quicksight-custompermissions-capabilities-analysis"></a>
The ability to perform analysis-related actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApproveFlowShareRequests`  <a name="cfn-quicksight-custompermissions-capabilities-approveflowsharerequests"></a>
The ability to review and approve sharing requests of Flows.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Apps`  <a name="cfn-quicksight-custompermissions-capabilities-apps"></a>
The ability to perform apps-related actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AsanaAction`  <a name="cfn-quicksight-custompermissions-capabilities-asanaaction"></a>
The ability to perform actions using Asana connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Automate`  <a name="cfn-quicksight-custompermissions-capabilities-automate"></a>
The ability to perform automate-related actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BambooHRAction`  <a name="cfn-quicksight-custompermissions-capabilities-bamboohraction"></a>
The ability to perform actions using BambooHR connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BoxAgentAction`  <a name="cfn-quicksight-custompermissions-capabilities-boxagentaction"></a>
The ability to perform actions using Box Agent connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BuildCalculatedFieldWithQ`  <a name="cfn-quicksight-custompermissions-capabilities-buildcalculatedfieldwithq"></a>
The ability to Build Calculation with AI
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CanvaAgentAction`  <a name="cfn-quicksight-custompermissions-capabilities-canvaagentaction"></a>
The ability to perform actions using Canva Agent connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ChatAgent`  <a name="cfn-quicksight-custompermissions-capabilities-chatagent"></a>
The ability to perform chat-related actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComprehendAction`  <a name="cfn-quicksight-custompermissions-capabilities-comprehendaction"></a>
The ability to perform actions using Comprehend connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComprehendMedicalAction`  <a name="cfn-quicksight-custompermissions-capabilities-comprehendmedicalaction"></a>
The ability to perform actions using Comprehend Medical connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConfluenceAction`  <a name="cfn-quicksight-custompermissions-capabilities-confluenceaction"></a>
The ability to perform actions using Atlassian Confluence Cloud connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateAmazonBedrockARSAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateamazonbedrockarsaction"></a>
The ability to create and update Bedrock Agent actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateAmazonBedrockFSAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateamazonbedrockfsaction"></a>
The ability to create and update Bedrock Runtime actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateAmazonBedrockKRSAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateamazonbedrockkrsaction"></a>
The ability to create and update Bedrock Data Automation Runtime actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateAmazonSThreeAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateamazonsthreeaction"></a>
The ability to create and update Amazon S3 actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateApps`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateapps"></a>
The ability to create or update apps.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateAsanaAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateasanaaction"></a>
The ability to create and update Asana actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateBambooHRAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatebamboohraction"></a>
The ability to create and update BambooHR actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateBoxAgentAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateboxagentaction"></a>
The ability to create and update Box Agent actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateCanvaAgentAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatecanvaagentaction"></a>
The ability to create and update Canva Agent actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateComprehendAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatecomprehendaction"></a>
The ability to create and update Comprehend actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateComprehendMedicalAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatecomprehendmedicalaction"></a>
The ability to create and update Comprehend Medical actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateConfluenceAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateconfluenceaction"></a>
The ability to create and update Atlassian Confluence Cloud actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateDashboardEmailReports`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatedashboardemailreports"></a>
The ability to create and update email reports.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateDatasets`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatedatasets"></a>
The ability to create and update datasets.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateDataSources`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatedatasources"></a>
The ability to create and update data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateFactSetAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatefactsetaction"></a>
The ability to create and update FactSet actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateGenericHTTPAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdategenerichttpaction"></a>
The ability to create and update REST API connection actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateGithubAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdategithubaction"></a>
The ability to create and update GitHub actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateGoogleCalendarAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdategooglecalendaraction"></a>
The ability to create and update Google Calendar actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateHubspotAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatehubspotaction"></a>
The ability to create and update Hubspot actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateHuggingFaceAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatehuggingfaceaction"></a>
The ability to create and update HuggingFace actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateIntercomAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateintercomaction"></a>
The ability to create and update Intercom actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateJiraAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatejiraaction"></a>
The ability to create and update Jira actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateKnowledgeBases`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateknowledgebases"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateLinearAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatelinearaction"></a>
The ability to create and update Linear actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateMCPAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatemcpaction"></a>
The ability to create and update Model Context Protocol actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateMondayAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatemondayaction"></a>
The ability to create and update Monday actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateMSExchangeAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatemsexchangeaction"></a>
The ability to create and update Microsoft Outlook actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateMSTeamsAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatemsteamsaction"></a>
The ability to create and update Microsoft Teams actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateNewRelicAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatenewrelicaction"></a>
The ability to create and update New Relic actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateNotionAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatenotionaction"></a>
The ability to create and update Notion actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateOneDriveAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateonedriveaction"></a>
The ability to create and update Microsoft OneDrive actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateOpenAPIAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateopenapiaction"></a>
The ability to create and update OpenAPI Specification actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdatePagerDutyAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatepagerdutyaction"></a>
The ability to create and update PagerDuty Advance actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateSalesforceAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatesalesforceaction"></a>
The ability to create and update Salesforce actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateSandPGlobalEnergyAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatesandpglobalenergyaction"></a>
The ability to create and update S&P Global Energy actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateSandPGMIAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatesandpgmiaction"></a>
The ability to create and update S&P Global Market Intelligence actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateSAPBillOfMaterialAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatesapbillofmaterialaction"></a>
The ability to create and update SAP Bill of Materials actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateSAPBusinessPartnerAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatesapbusinesspartneraction"></a>
The ability to create and update SAP Business Partner actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateSAPMaterialStockAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatesapmaterialstockaction"></a>
The ability to create and update SAP Material Stock actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateSAPPhysicalInventoryAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatesapphysicalinventoryaction"></a>
The ability to create and update SAP Physical Inventory actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateSAPProductMasterDataAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatesapproductmasterdataaction"></a>
The ability to create and update SAP Product Master actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateServiceNowAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateservicenowaction"></a>
The ability to create and update ServiceNow actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateSharePointAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatesharepointaction"></a>
The ability to create and update Microsoft SharePoint Online actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateSlackAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdateslackaction"></a>
The ability to create and update Slack actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateSmartsheetAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatesmartsheetaction"></a>
The ability to create and update Smartsheet actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateTextractAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatetextractaction"></a>
The ability to create and update Textract actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateThemes`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatethemes"></a>
The ability to export to Create and Update themes.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateThresholdAlerts`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatethresholdalerts"></a>
The ability to create and update threshold alerts.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateAndUpdateZendeskAction`  <a name="cfn-quicksight-custompermissions-capabilities-createandupdatezendeskaction"></a>
The ability to create and update Zendesk actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateChatAgents`  <a name="cfn-quicksight-custompermissions-capabilities-createchatagents"></a>
The ability to create chat agents.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateDashboardExecutiveSummaryWithQ`  <a name="cfn-quicksight-custompermissions-capabilities-createdashboardexecutivesummarywithq"></a>
The ability to Create Executive Summary
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateSharedFolders`  <a name="cfn-quicksight-custompermissions-capabilities-createsharedfolders"></a>
The ability to create shared folders.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateSpaces`  <a name="cfn-quicksight-custompermissions-capabilities-createspaces"></a>
The ability to create spaces.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateSPICEDataset`  <a name="cfn-quicksight-custompermissions-capabilities-createspicedataset"></a>
The ability to create a SPICE dataset.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Dashboard`  <a name="cfn-quicksight-custompermissions-capabilities-dashboard"></a>
The ability to perform dashboard-related actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EditVisualWithQ`  <a name="cfn-quicksight-custompermissions-capabilities-editvisualwithq"></a>
The ability to Edit Visual with AI
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExportToCsv`  <a name="cfn-quicksight-custompermissions-capabilities-exporttocsv"></a>
The ability to export to CSV files from the UI.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExportToCsvInScheduledReports`  <a name="cfn-quicksight-custompermissions-capabilities-exporttocsvinscheduledreports"></a>
The ability to export to CSV files in scheduled email reports.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExportToExcel`  <a name="cfn-quicksight-custompermissions-capabilities-exporttoexcel"></a>
The ability to export to Excel files from the UI.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExportToExcelInScheduledReports`  <a name="cfn-quicksight-custompermissions-capabilities-exporttoexcelinscheduledreports"></a>
The ability to export to Excel files in scheduled email reports.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExportToPdf`  <a name="cfn-quicksight-custompermissions-capabilities-exporttopdf"></a>
The ability to export to PDF files from the UI.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExportToPdfInScheduledReports`  <a name="cfn-quicksight-custompermissions-capabilities-exporttopdfinscheduledreports"></a>
The ability to export to PDF files in scheduled email reports.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Extension`  <a name="cfn-quicksight-custompermissions-capabilities-extension"></a>
The ability to perform Extension-related actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FactSetAction`  <a name="cfn-quicksight-custompermissions-capabilities-factsetaction"></a>
The ability to perform actions using FactSet connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Flow`  <a name="cfn-quicksight-custompermissions-capabilities-flow"></a>
The ability to perform flow-related actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GenericHTTPAction`  <a name="cfn-quicksight-custompermissions-capabilities-generichttpaction"></a>
The ability to perform actions using REST API connection connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GithubAction`  <a name="cfn-quicksight-custompermissions-capabilities-githubaction"></a>
The ability to perform actions using GitHub connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GoogleCalendarAction`  <a name="cfn-quicksight-custompermissions-capabilities-googlecalendaraction"></a>
The ability to perform actions using Google Calendar connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HubspotAction`  <a name="cfn-quicksight-custompermissions-capabilities-hubspotaction"></a>
The ability to perform actions using Hubspot connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HuggingFaceAction`  <a name="cfn-quicksight-custompermissions-capabilities-huggingfaceaction"></a>
The ability to perform actions using HuggingFace connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncludeContentInScheduledReportsEmail`  <a name="cfn-quicksight-custompermissions-capabilities-includecontentinscheduledreportsemail"></a>
The ability to include content in scheduled email reports.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IntercomAction`  <a name="cfn-quicksight-custompermissions-capabilities-intercomaction"></a>
The ability to perform actions using Intercom connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InvokeAppsAIInference`  <a name="cfn-quicksight-custompermissions-capabilities-invokeappsaiinference"></a>
The ability to add and invoke AI inference in new and existing apps.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JiraAction`  <a name="cfn-quicksight-custompermissions-capabilities-jiraaction"></a>
The ability to perform actions using Jira connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KnowledgeBase`  <a name="cfn-quicksight-custompermissions-capabilities-knowledgebase"></a>
The ability to use knowledge bases to specify content from external applications.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LinearAction`  <a name="cfn-quicksight-custompermissions-capabilities-linearaction"></a>
The ability to perform actions using Linear connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManageSharedFolders`  <a name="cfn-quicksight-custompermissions-capabilities-managesharedfolders"></a>
The ability to create, update, delete and view shared folders (both restricted and unrestricted), ability to add any asset to shared folders, and ability to share the folders.
**Note:** This does *not* prevent inheriting access to assets that others share with them through folder membership.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MCPAction`  <a name="cfn-quicksight-custompermissions-capabilities-mcpaction"></a>
The ability to perform actions using Model Context Protocol connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MondayAction`  <a name="cfn-quicksight-custompermissions-capabilities-mondayaction"></a>
The ability to perform actions using Monday connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MSExchangeAction`  <a name="cfn-quicksight-custompermissions-capabilities-msexchangeaction"></a>
The ability to perform actions using Microsoft Outlook connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MSTeamsAction`  <a name="cfn-quicksight-custompermissions-capabilities-msteamsaction"></a>
The ability to perform actions using Microsoft Teams connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NewRelicAction`  <a name="cfn-quicksight-custompermissions-capabilities-newrelicaction"></a>
The ability to perform actions using New Relic connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotionAction`  <a name="cfn-quicksight-custompermissions-capabilities-notionaction"></a>
The ability to perform actions using Notion connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OneDriveAction`  <a name="cfn-quicksight-custompermissions-capabilities-onedriveaction"></a>
The ability to perform actions using Microsoft OneDrive connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OpenAPIAction`  <a name="cfn-quicksight-custompermissions-capabilities-openapiaction"></a>
The ability to perform actions using OpenAPI Specification connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PagerDutyAction`  <a name="cfn-quicksight-custompermissions-capabilities-pagerdutyaction"></a>
The ability to perform actions using PagerDuty Advance connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PerformFlowUiTask`  <a name="cfn-quicksight-custompermissions-capabilities-performflowuitask"></a>
The ability to use UI Agent step to perform tasks on public websites.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrintReports`  <a name="cfn-quicksight-custompermissions-capabilities-printreports"></a>
The ability to print reports.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PublishWithoutApproval`  <a name="cfn-quicksight-custompermissions-capabilities-publishwithoutapproval"></a>
The ability to enable approvals for flow share.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RenameSharedFolders`  <a name="cfn-quicksight-custompermissions-capabilities-renamesharedfolders"></a>
The ability to rename shared folders.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Research`  <a name="cfn-quicksight-custompermissions-capabilities-research"></a>
The ability to perform research-related actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SalesforceAction`  <a name="cfn-quicksight-custompermissions-capabilities-salesforceaction"></a>
The ability to perform actions using Salesforce connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SandPGlobalEnergyAction`  <a name="cfn-quicksight-custompermissions-capabilities-sandpglobalenergyaction"></a>
The ability to perform actions using S&P Global Energy connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SandPGMIAction`  <a name="cfn-quicksight-custompermissions-capabilities-sandpgmiaction"></a>
The ability to perform actions using S&P Global Market Intelligence connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SAPBillOfMaterialAction`  <a name="cfn-quicksight-custompermissions-capabilities-sapbillofmaterialaction"></a>
The ability to perform actions using SAP Bill of Materials connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SAPBusinessPartnerAction`  <a name="cfn-quicksight-custompermissions-capabilities-sapbusinesspartneraction"></a>
The ability to perform actions using SAP Business Partner connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SAPMaterialStockAction`  <a name="cfn-quicksight-custompermissions-capabilities-sapmaterialstockaction"></a>
The ability to perform actions using SAP Material Stock connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SAPPhysicalInventoryAction`  <a name="cfn-quicksight-custompermissions-capabilities-sapphysicalinventoryaction"></a>
The ability to perform actions using SAP Physical Inventory connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SAPProductMasterDataAction`  <a name="cfn-quicksight-custompermissions-capabilities-sapproductmasterdataaction"></a>
The ability to perform actions using SAP Product Master connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceNowAction`  <a name="cfn-quicksight-custompermissions-capabilities-servicenowaction"></a>
The ability to perform actions using ServiceNow connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareAmazonBedrockARSAction`  <a name="cfn-quicksight-custompermissions-capabilities-shareamazonbedrockarsaction"></a>
The ability to share Bedrock Agent actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareAmazonBedrockFSAction`  <a name="cfn-quicksight-custompermissions-capabilities-shareamazonbedrockfsaction"></a>
The ability to share Bedrock Runtime actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareAmazonBedrockKRSAction`  <a name="cfn-quicksight-custompermissions-capabilities-shareamazonbedrockkrsaction"></a>
The ability to share Bedrock Data Automation Runtime actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareAmazonSThreeAction`  <a name="cfn-quicksight-custompermissions-capabilities-shareamazonsthreeaction"></a>
The ability to share Amazon S3 actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareAnalyses`  <a name="cfn-quicksight-custompermissions-capabilities-shareanalyses"></a>
The ability to share analyses.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareApps`  <a name="cfn-quicksight-custompermissions-capabilities-shareapps"></a>
The ability to share apps with other users.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareAsanaAction`  <a name="cfn-quicksight-custompermissions-capabilities-shareasanaaction"></a>
The ability to share Asana actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareBambooHRAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharebamboohraction"></a>
The ability to share BambooHR actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareBoxAgentAction`  <a name="cfn-quicksight-custompermissions-capabilities-shareboxagentaction"></a>
The ability to share Box Agent actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareCanvaAgentAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharecanvaagentaction"></a>
The ability to share Canva Agent actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareChatAgents`  <a name="cfn-quicksight-custompermissions-capabilities-sharechatagents"></a>
The ability to share chat agents with other users and groups.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareComprehendAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharecomprehendaction"></a>
The ability to share Comprehend actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareComprehendMedicalAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharecomprehendmedicalaction"></a>
The ability to share Comprehend Medical actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareConfluenceAction`  <a name="cfn-quicksight-custompermissions-capabilities-shareconfluenceaction"></a>
The ability to share Atlassian Confluence Cloud actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareDashboards`  <a name="cfn-quicksight-custompermissions-capabilities-sharedashboards"></a>
The ability to share dashboards.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareDatasets`  <a name="cfn-quicksight-custompermissions-capabilities-sharedatasets"></a>
The ability to share datasets.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareDataSources`  <a name="cfn-quicksight-custompermissions-capabilities-sharedatasources"></a>
The ability to share data sources.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareFactSetAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharefactsetaction"></a>
The ability to share FactSet actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareGenericHTTPAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharegenerichttpaction"></a>
The ability to share REST API connection actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareGithubAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharegithubaction"></a>
The ability to share GitHub actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareGoogleCalendarAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharegooglecalendaraction"></a>
The ability to share Google Calendar actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareHubspotAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharehubspotaction"></a>
The ability to share Hubspot actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareHuggingFaceAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharehuggingfaceaction"></a>
The ability to share HuggingFace actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareIntercomAction`  <a name="cfn-quicksight-custompermissions-capabilities-shareintercomaction"></a>
The ability to share Intercom actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareJiraAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharejiraaction"></a>
The ability to share Jira actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareKnowledgeBases`  <a name="cfn-quicksight-custompermissions-capabilities-shareknowledgebases"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareLinearAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharelinearaction"></a>
The ability to share Linear actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareMCPAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharemcpaction"></a>
The ability to share Model Context Protocol actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareMondayAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharemondayaction"></a>
The ability to share Monday actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareMSExchangeAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharemsexchangeaction"></a>
The ability to share Microsoft Outlook actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareMSTeamsAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharemsteamsaction"></a>
The ability to share Microsoft Teams actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareNewRelicAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharenewrelicaction"></a>
The ability to share New Relic actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareNotionAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharenotionaction"></a>
The ability to share Notion actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareOneDriveAction`  <a name="cfn-quicksight-custompermissions-capabilities-shareonedriveaction"></a>
The ability to share Microsoft OneDrive actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareOpenAPIAction`  <a name="cfn-quicksight-custompermissions-capabilities-shareopenapiaction"></a>
The ability to share OpenAPI Specification actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SharePagerDutyAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharepagerdutyaction"></a>
The ability to share PagerDuty Advance actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SharePointAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharepointaction"></a>
The ability to perform actions using Microsoft SharePoint Online connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSalesforceAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharesalesforceaction"></a>
The ability to share Salesforce actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSandPGlobalEnergyAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharesandpglobalenergyaction"></a>
The ability to share S&P Global Energy actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSandPGMIAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharesandpgmiaction"></a>
The ability to share S&P Global Market Intelligence actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSAPBillOfMaterialAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharesapbillofmaterialaction"></a>
The ability to share SAP Bill of Materials actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSAPBusinessPartnerAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharesapbusinesspartneraction"></a>
The ability to share SAP Business Partner actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSAPMaterialStockAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharesapmaterialstockaction"></a>
The ability to share SAP Material Stock actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSAPPhysicalInventoryAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharesapphysicalinventoryaction"></a>
The ability to share SAP Physical Inventory actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSAPProductMasterDataAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharesapproductmasterdataaction"></a>
The ability to share SAP Product Master actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareServiceNowAction`  <a name="cfn-quicksight-custompermissions-capabilities-shareservicenowaction"></a>
The ability to share ServiceNow actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSharePointAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharesharepointaction"></a>
The ability to share Microsoft SharePoint Online actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSlackAction`  <a name="cfn-quicksight-custompermissions-capabilities-shareslackaction"></a>
The ability to share Slack actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSmartsheetAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharesmartsheetaction"></a>
The ability to share Smartsheet actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareSpaces`  <a name="cfn-quicksight-custompermissions-capabilities-sharespaces"></a>
The ability to share spaces with other users and groups.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareTextractAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharetextractaction"></a>
The ability to share Textract actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareZendeskAction`  <a name="cfn-quicksight-custompermissions-capabilities-sharezendeskaction"></a>
The ability to share Zendesk actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SlackAction`  <a name="cfn-quicksight-custompermissions-capabilities-slackaction"></a>
The ability to perform actions using Slack connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SmartsheetAction`  <a name="cfn-quicksight-custompermissions-capabilities-smartsheetaction"></a>
The ability to perform actions using Smartsheet connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Space`  <a name="cfn-quicksight-custompermissions-capabilities-space"></a>
The ability to perform space-related actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubscribeDashboardEmailReports`  <a name="cfn-quicksight-custompermissions-capabilities-subscribedashboardemailreports"></a>
The ability to subscribe to email reports.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextractAction`  <a name="cfn-quicksight-custompermissions-capabilities-textractaction"></a>
The ability to perform actions using Textract connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Topic`  <a name="cfn-quicksight-custompermissions-capabilities-topic"></a>
The ability to perform Topic-related actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseAgentWebSearch`  <a name="cfn-quicksight-custompermissions-capabilities-useagentwebsearch"></a>
The ability to use internet to enhance results in Chat Agents, Flows, and Quick Research. Web search queries will be processed securely in an AWS region `us-east-1`.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseAmazonBedrockARSAction`  <a name="cfn-quicksight-custompermissions-capabilities-useamazonbedrockarsaction"></a>
The ability to use Bedrock Agent actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseAmazonBedrockFSAction`  <a name="cfn-quicksight-custompermissions-capabilities-useamazonbedrockfsaction"></a>
The ability to use Bedrock Runtime actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseAmazonBedrockKRSAction`  <a name="cfn-quicksight-custompermissions-capabilities-useamazonbedrockkrsaction"></a>
The ability to use Bedrock Data Automation Runtime actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseAmazonSThreeAction`  <a name="cfn-quicksight-custompermissions-capabilities-useamazonsthreeaction"></a>
The ability to use Amazon S3 actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseAsanaAction`  <a name="cfn-quicksight-custompermissions-capabilities-useasanaaction"></a>
The ability to use Asana actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseBambooHRAction`  <a name="cfn-quicksight-custompermissions-capabilities-usebamboohraction"></a>
The ability to use BambooHR actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseBedrockModels`  <a name="cfn-quicksight-custompermissions-capabilities-usebedrockmodels"></a>
The ability to use Bedrock models for general knowledge step in flows.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseBoxAgentAction`  <a name="cfn-quicksight-custompermissions-capabilities-useboxagentaction"></a>
The ability to use Box Agent actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseCanvaAgentAction`  <a name="cfn-quicksight-custompermissions-capabilities-usecanvaagentaction"></a>
The ability to use Canva Agent actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseComprehendAction`  <a name="cfn-quicksight-custompermissions-capabilities-usecomprehendaction"></a>
The ability to use Comprehend actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseComprehendMedicalAction`  <a name="cfn-quicksight-custompermissions-capabilities-usecomprehendmedicalaction"></a>
The ability to use Comprehend Medical actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseConfluenceAction`  <a name="cfn-quicksight-custompermissions-capabilities-useconfluenceaction"></a>
The ability to use Atlassian Confluence Cloud actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseFactSetAction`  <a name="cfn-quicksight-custompermissions-capabilities-usefactsetaction"></a>
The ability to use FactSet actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseGenericHTTPAction`  <a name="cfn-quicksight-custompermissions-capabilities-usegenerichttpaction"></a>
The ability to use REST API connection actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseGithubAction`  <a name="cfn-quicksight-custompermissions-capabilities-usegithubaction"></a>
The ability to use GitHub actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseGoogleCalendarAction`  <a name="cfn-quicksight-custompermissions-capabilities-usegooglecalendaraction"></a>
The ability to use Google Calendar actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseHubspotAction`  <a name="cfn-quicksight-custompermissions-capabilities-usehubspotaction"></a>
The ability to use Hubspot actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseHuggingFaceAction`  <a name="cfn-quicksight-custompermissions-capabilities-usehuggingfaceaction"></a>
The ability to use HuggingFace actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseIntercomAction`  <a name="cfn-quicksight-custompermissions-capabilities-useintercomaction"></a>
The ability to use Intercom actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseJiraAction`  <a name="cfn-quicksight-custompermissions-capabilities-usejiraaction"></a>
The ability to use Jira actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseLinearAction`  <a name="cfn-quicksight-custompermissions-capabilities-uselinearaction"></a>
The ability to use Linear actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseMCPAction`  <a name="cfn-quicksight-custompermissions-capabilities-usemcpaction"></a>
The ability to use Model Context Protocol actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseMondayAction`  <a name="cfn-quicksight-custompermissions-capabilities-usemondayaction"></a>
The ability to use Monday actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseMSExchangeAction`  <a name="cfn-quicksight-custompermissions-capabilities-usemsexchangeaction"></a>
The ability to use Microsoft Outlook actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseMSTeamsAction`  <a name="cfn-quicksight-custompermissions-capabilities-usemsteamsaction"></a>
The ability to use Microsoft Teams actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseNewRelicAction`  <a name="cfn-quicksight-custompermissions-capabilities-usenewrelicaction"></a>
The ability to use New Relic actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseNotionAction`  <a name="cfn-quicksight-custompermissions-capabilities-usenotionaction"></a>
The ability to use Notion actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseOneDriveAction`  <a name="cfn-quicksight-custompermissions-capabilities-useonedriveaction"></a>
The ability to use Microsoft OneDrive actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseOpenAPIAction`  <a name="cfn-quicksight-custompermissions-capabilities-useopenapiaction"></a>
The ability to use OpenAPI Specification actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UsePagerDutyAction`  <a name="cfn-quicksight-custompermissions-capabilities-usepagerdutyaction"></a>
The ability to use PagerDuty Advance actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseSalesforceAction`  <a name="cfn-quicksight-custompermissions-capabilities-usesalesforceaction"></a>
The ability to use Salesforce actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseSandPGlobalEnergyAction`  <a name="cfn-quicksight-custompermissions-capabilities-usesandpglobalenergyaction"></a>
The ability to use S&P Global Energy actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseSandPGMIAction`  <a name="cfn-quicksight-custompermissions-capabilities-usesandpgmiaction"></a>
The ability to use S&P Global Market Intelligence actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseSAPBillOfMaterialAction`  <a name="cfn-quicksight-custompermissions-capabilities-usesapbillofmaterialaction"></a>
The ability to use SAP Bill of Materials actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseSAPBusinessPartnerAction`  <a name="cfn-quicksight-custompermissions-capabilities-usesapbusinesspartneraction"></a>
The ability to use SAP Business Partner actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseSAPMaterialStockAction`  <a name="cfn-quicksight-custompermissions-capabilities-usesapmaterialstockaction"></a>
The ability to use SAP Material Stock actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseSAPPhysicalInventoryAction`  <a name="cfn-quicksight-custompermissions-capabilities-usesapphysicalinventoryaction"></a>
The ability to use SAP Physical Inventory actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseSAPProductMasterDataAction`  <a name="cfn-quicksight-custompermissions-capabilities-usesapproductmasterdataaction"></a>
The ability to use SAP Product Master actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseServiceNowAction`  <a name="cfn-quicksight-custompermissions-capabilities-useservicenowaction"></a>
The ability to use ServiceNow actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseSharePointAction`  <a name="cfn-quicksight-custompermissions-capabilities-usesharepointaction"></a>
The ability to use Microsoft SharePoint Online actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseSlackAction`  <a name="cfn-quicksight-custompermissions-capabilities-useslackaction"></a>
The ability to use Slack actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseSmartsheetAction`  <a name="cfn-quicksight-custompermissions-capabilities-usesmartsheetaction"></a>
The ability to use Smartsheet actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseTextractAction`  <a name="cfn-quicksight-custompermissions-capabilities-usetextractaction"></a>
The ability to use Textract actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseZendeskAction`  <a name="cfn-quicksight-custompermissions-capabilities-usezendeskaction"></a>
The ability to use Zendesk actions.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ViewAccountSPICECapacity`  <a name="cfn-quicksight-custompermissions-capabilities-viewaccountspicecapacity"></a>
The ability to view account SPICE capacity.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ZendeskAction`  <a name="cfn-quicksight-custompermissions-capabilities-zendeskaction"></a>
The ability to perform actions using Zendesk connectors.
*Required*: No
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
