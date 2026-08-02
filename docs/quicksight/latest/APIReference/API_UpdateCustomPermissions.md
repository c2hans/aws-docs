---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateCustomPermissions.html
---

# UpdateCustomPermissions
<a name="API_UpdateCustomPermissions"></a>

Updates a custom permissions profile.

## Request Syntax
<a name="API_UpdateCustomPermissions_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/custom-permissions/{{CustomPermissionsName}} HTTP/1.1
Content-type: application/json

{
   "Capabilities": {
      "AccessAppsNativeDataStore": "{{string}}",
      "Action": "{{string}}",
      "AddOrRunAnomalyDetectionForAnalyses": "{{string}}",
      "AmazonBedrockARSAction": "{{string}}",
      "AmazonBedrockFSAction": "{{string}}",
      "AmazonBedrockKRSAction": "{{string}}",
      "AmazonSThreeAction": "{{string}}",
      "Analysis": "{{string}}",
      "ApproveFlowShareRequests": "{{string}}",
      "Apps": "{{string}}",
      "AsanaAction": "{{string}}",
      "Automate": "{{string}}",
      "BambooHRAction": "{{string}}",
      "BoxAgentAction": "{{string}}",
      "BuildCalculatedFieldWithQ": "{{string}}",
      "CanvaAgentAction": "{{string}}",
      "ChatAgent": "{{string}}",
      "ComprehendAction": "{{string}}",
      "ComprehendMedicalAction": "{{string}}",
      "ConfluenceAction": "{{string}}",
      "CreateAndUpdateAmazonBedrockARSAction": "{{string}}",
      "CreateAndUpdateAmazonBedrockFSAction": "{{string}}",
      "CreateAndUpdateAmazonBedrockKRSAction": "{{string}}",
      "CreateAndUpdateAmazonSThreeAction": "{{string}}",
      "CreateAndUpdateApps": "{{string}}",
      "CreateAndUpdateAsanaAction": "{{string}}",
      "CreateAndUpdateBambooHRAction": "{{string}}",
      "CreateAndUpdateBoxAgentAction": "{{string}}",
      "CreateAndUpdateCanvaAgentAction": "{{string}}",
      "CreateAndUpdateComprehendAction": "{{string}}",
      "CreateAndUpdateComprehendMedicalAction": "{{string}}",
      "CreateAndUpdateConfluenceAction": "{{string}}",
      "CreateAndUpdateDashboardEmailReports": "{{string}}",
      "CreateAndUpdateDatasets": "{{string}}",
      "CreateAndUpdateDataSources": "{{string}}",
      "CreateAndUpdateFactSetAction": "{{string}}",
      "CreateAndUpdateGenericHTTPAction": "{{string}}",
      "CreateAndUpdateGithubAction": "{{string}}",
      "CreateAndUpdateGoogleCalendarAction": "{{string}}",
      "CreateAndUpdateHubspotAction": "{{string}}",
      "CreateAndUpdateHuggingFaceAction": "{{string}}",
      "CreateAndUpdateIntercomAction": "{{string}}",
      "CreateAndUpdateJiraAction": "{{string}}",
      "CreateAndUpdateLinearAction": "{{string}}",
      "CreateAndUpdateMCPAction": "{{string}}",
      "CreateAndUpdateMondayAction": "{{string}}",
      "CreateAndUpdateMSExchangeAction": "{{string}}",
      "CreateAndUpdateMSTeamsAction": "{{string}}",
      "CreateAndUpdateNewRelicAction": "{{string}}",
      "CreateAndUpdateNotionAction": "{{string}}",
      "CreateAndUpdateOneDriveAction": "{{string}}",
      "CreateAndUpdateOpenAPIAction": "{{string}}",
      "CreateAndUpdatePagerDutyAction": "{{string}}",
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
      "CreateAndUpdateSlackAction": "{{string}}",
      "CreateAndUpdateSmartsheetAction": "{{string}}",
      "CreateAndUpdateTextractAction": "{{string}}",
      "CreateAndUpdateThemes": "{{string}}",
      "CreateAndUpdateThresholdAlerts": "{{string}}",
      "CreateAndUpdateZendeskAction": "{{string}}",
      "CreateChatAgents": "{{string}}",
      "CreateDashboardExecutiveSummaryWithQ": "{{string}}",
      "CreateSharedFolders": "{{string}}",
      "CreateSpaces": "{{string}}",
      "CreateSPICEDataset": "{{string}}",
      "Dashboard": "{{string}}",
      "EditVisualWithQ": "{{string}}",
      "ExportToCsv": "{{string}}",
      "ExportToCsvInScheduledReports": "{{string}}",
      "ExportToExcel": "{{string}}",
      "ExportToExcelInScheduledReports": "{{string}}",
      "ExportToPdf": "{{string}}",
      "ExportToPdfInScheduledReports": "{{string}}",
      "Extension": "{{string}}",
      "FactSetAction": "{{string}}",
      "Flow": "{{string}}",
      "GenerateAnalyses": "{{string}}",
      "GenericHTTPAction": "{{string}}",
      "GithubAction": "{{string}}",
      "GoogleCalendarAction": "{{string}}",
      "HubspotAction": "{{string}}",
      "HuggingFaceAction": "{{string}}",
      "InboundEmailTrigger": "{{string}}",
      "IncludeContentInScheduledReportsEmail": "{{string}}",
      "IntercomAction": "{{string}}",
      "InvokeAppsAIInference": "{{string}}",
      "JiraAction": "{{string}}",
      "KnowledgeBase": "{{string}}",
      "LinearAction": "{{string}}",
      "ManageSharedFolders": "{{string}}",
      "MCPAction": "{{string}}",
      "MondayAction": "{{string}}",
      "MSExchangeAction": "{{string}}",
      "MSTeamsAction": "{{string}}",
      "NewRelicAction": "{{string}}",
      "NotionAction": "{{string}}",
      "OneDriveAction": "{{string}}",
      "OpenAPIAction": "{{string}}",
      "PagerDutyAction": "{{string}}",
      "PerformFlowUiTask": "{{string}}",
      "PrintReports": "{{string}}",
      "PublishWithoutApproval": "{{string}}",
      "QuickEventTrigger": "{{string}}",
      "RenameSharedFolders": "{{string}}",
      "Research": "{{string}}",
      "SalesforceAction": "{{string}}",
      "SandPGlobalEnergyAction": "{{string}}",
      "SandPGMIAction": "{{string}}",
      "SAPBillOfMaterialAction": "{{string}}",
      "SAPBusinessPartnerAction": "{{string}}",
      "SAPMaterialStockAction": "{{string}}",
      "SAPPhysicalInventoryAction": "{{string}}",
      "SAPProductMasterDataAction": "{{string}}",
      "Scenario": "{{string}}",
      "ScheduleTrigger": "{{string}}",
      "SelfUpgradeUserRole": "{{string}}",
      "ServiceNowAction": "{{string}}",
      "ShareAmazonBedrockARSAction": "{{string}}",
      "ShareAmazonBedrockFSAction": "{{string}}",
      "ShareAmazonBedrockKRSAction": "{{string}}",
      "ShareAmazonSThreeAction": "{{string}}",
      "ShareAnalyses": "{{string}}",
      "ShareApps": "{{string}}",
      "ShareAsanaAction": "{{string}}",
      "ShareBambooHRAction": "{{string}}",
      "ShareBoxAgentAction": "{{string}}",
      "ShareCanvaAgentAction": "{{string}}",
      "ShareChatAgents": "{{string}}",
      "ShareComprehendAction": "{{string}}",
      "ShareComprehendMedicalAction": "{{string}}",
      "ShareConfluenceAction": "{{string}}",
      "ShareDashboards": "{{string}}",
      "ShareDatasets": "{{string}}",
      "ShareDataSources": "{{string}}",
      "ShareFactSetAction": "{{string}}",
      "ShareGenericHTTPAction": "{{string}}",
      "ShareGithubAction": "{{string}}",
      "ShareGoogleCalendarAction": "{{string}}",
      "ShareHubspotAction": "{{string}}",
      "ShareHuggingFaceAction": "{{string}}",
      "ShareIntercomAction": "{{string}}",
      "ShareJiraAction": "{{string}}",
      "ShareLinearAction": "{{string}}",
      "ShareMCPAction": "{{string}}",
      "ShareMondayAction": "{{string}}",
      "ShareMSExchangeAction": "{{string}}",
      "ShareMSTeamsAction": "{{string}}",
      "ShareNewRelicAction": "{{string}}",
      "ShareNotionAction": "{{string}}",
      "ShareOneDriveAction": "{{string}}",
      "ShareOpenAPIAction": "{{string}}",
      "SharePagerDutyAction": "{{string}}",
      "SharePointAction": "{{string}}",
      "ShareSalesforceAction": "{{string}}",
      "ShareSandPGlobalEnergyAction": "{{string}}",
      "ShareSandPGMIAction": "{{string}}",
      "ShareSAPBillOfMaterialAction": "{{string}}",
      "ShareSAPBusinessPartnerAction": "{{string}}",
      "ShareSAPMaterialStockAction": "{{string}}",
      "ShareSAPPhysicalInventoryAction": "{{string}}",
      "ShareSAPProductMasterDataAction": "{{string}}",
      "ShareServiceNowAction": "{{string}}",
      "ShareSharePointAction": "{{string}}",
      "ShareSlackAction": "{{string}}",
      "ShareSmartsheetAction": "{{string}}",
      "ShareSpaces": "{{string}}",
      "ShareTextractAction": "{{string}}",
      "ShareZendeskAction": "{{string}}",
      "SlackAction": "{{string}}",
      "SmartsheetAction": "{{string}}",
      "Space": "{{string}}",
      "Story": "{{string}}",
      "SubscribeDashboardEmailReports": "{{string}}",
      "TextractAction": "{{string}}",
      "Topic": "{{string}}",
      "Trigger": "{{string}}",
      "UseAgentWebSearch": "{{string}}",
      "UseAmazonBedrockARSAction": "{{string}}",
      "UseAmazonBedrockFSAction": "{{string}}",
      "UseAmazonBedrockKRSAction": "{{string}}",
      "UseAmazonSThreeAction": "{{string}}",
      "UseAsanaAction": "{{string}}",
      "UseBambooHRAction": "{{string}}",
      "UseBedrockModels": "{{string}}",
      "UseBoxAgentAction": "{{string}}",
      "UseBrowserExtension": "{{string}}",
      "UseCanvaAgentAction": "{{string}}",
      "UseComprehendAction": "{{string}}",
      "UseComprehendMedicalAction": "{{string}}",
      "UseConfluenceAction": "{{string}}",
      "UseExcelAddInExtension": "{{string}}",
      "UseFactSetAction": "{{string}}",
      "UseGenericHTTPAction": "{{string}}",
      "UseGithubAction": "{{string}}",
      "UseGoogleCalendarAction": "{{string}}",
      "UseHubspotAction": "{{string}}",
      "UseHuggingFaceAction": "{{string}}",
      "UseIntercomAction": "{{string}}",
      "UseJiraAction": "{{string}}",
      "UseLinearAction": "{{string}}",
      "UseMCPAction": "{{string}}",
      "UseMondayAction": "{{string}}",
      "UseMSExchangeAction": "{{string}}",
      "UseMSTeamsAction": "{{string}}",
      "UseNewRelicAction": "{{string}}",
      "UseNotionAction": "{{string}}",
      "UseOneDriveAction": "{{string}}",
      "UseOpenAPIAction": "{{string}}",
      "UseOutlookAddInExtension": "{{string}}",
      "UsePagerDutyAction": "{{string}}",
      "UsePowerpointAddInExtension": "{{string}}",
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
      "UseSlackAction": "{{string}}",
      "UseSmartsheetAction": "{{string}}",
      "UseTextractAction": "{{string}}",
      "UseWordAddInExtension": "{{string}}",
      "UseZendeskAction": "{{string}}",
      "ViewAccountSPICECapacity": "{{string}}",
      "ZendeskAction": "{{string}}"
   },
   "Governance": {
      "DefaultCategoryEffects": {
         "{{string}}" : "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_UpdateCustomPermissions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateCustomPermissions_RequestSyntax) **   <a name="QS-UpdateCustomPermissions-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the custom permissions profile that you want to update.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [CustomPermissionsName](#API_UpdateCustomPermissions_RequestSyntax) **   <a name="QS-UpdateCustomPermissions-request-uri-CustomPermissionsName"></a>
The name of the custom permissions profile that you want to update.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9+=,.@_-]+$`
Required: Yes

## Request Body
<a name="API_UpdateCustomPermissions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Capabilities](#API_UpdateCustomPermissions_RequestSyntax) **   <a name="QS-UpdateCustomPermissions-request-Capabilities"></a>
A set of actions to include in the custom permissions profile.
Type: [Capabilities](API_Capabilities.md) object
Required: No

 ** [Governance](#API_UpdateCustomPermissions_RequestSyntax) **   <a name="QS-UpdateCustomPermissions-request-Governance"></a>
The governance configuration for the custom permissions profile. The `UpdateCustomPermissions` operation replaces all existing `Capabilities` and `Governance` values. If you omit this parameter, Amazon Quick removes governance from the profile and the existing custom permission behavior applies.
Type: [Governance](API_Governance.md) object
Required: No

## Response Syntax
<a name="API_UpdateCustomPermissions_ResponseSyntax"></a>

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
<a name="API_UpdateCustomPermissions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateCustomPermissions_ResponseSyntax) **   <a name="QS-UpdateCustomPermissions-response-Arn"></a>
The Amazon Resource Name (ARN) of the custom permissions profile.
Type: String

 ** [RequestId](#API_UpdateCustomPermissions_ResponseSyntax) **   <a name="QS-UpdateCustomPermissions-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

 ** [Status](#API_UpdateCustomPermissions_ResponseSyntax) **   <a name="QS-UpdateCustomPermissions-response-Status"></a>
The HTTP status of the request.
Type: Integer

## Errors
<a name="API_UpdateCustomPermissions_Errors"></a>

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

 ** PreconditionNotMetException **
One or more preconditions aren't met.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

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
<a name="API_UpdateCustomPermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateCustomPermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateCustomPermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateCustomPermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateCustomPermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateCustomPermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateCustomPermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateCustomPermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateCustomPermissions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateCustomPermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateCustomPermissions)
