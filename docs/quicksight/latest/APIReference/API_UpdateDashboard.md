---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDashboard.html
---

# UpdateDashboard
<a name="API_UpdateDashboard"></a>

Updates a dashboard in an AWS account.

**Note**
Updating a Dashboard creates a new dashboard version but does not immediately publish the new version. You can update the published version of a dashboard by using the ` [UpdateDashboardPublishedVersion](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDashboardPublishedVersion.html) ` API operation.

## Request Syntax
<a name="API_UpdateDashboard_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/dashboards/{{DashboardId}} HTTP/1.1
Content-type: application/json

{
   "DashboardPublishOptions": {
      "AdHocFilteringOption": {
         "AvailabilityStatus": "{{string}}"
      },
      "DataPointDrillUpDownOption": {
         "AvailabilityStatus": "{{string}}"
      },
      "DataPointMenuLabelOption": {
         "AvailabilityStatus": "{{string}}"
      },
      "DataPointTooltipOption": {
         "AvailabilityStatus": "{{string}}"
      },
      "DataQAEnabledOption": {
         "AvailabilityStatus": "{{string}}"
      },
      "DataStoriesSharingOption": {
         "AvailabilityStatus": "{{string}}"
      },
      "ExecutiveSummaryOption": {
         "AvailabilityStatus": "{{string}}"
      },
      "ExportToCSVOption": {
         "AvailabilityStatus": "{{string}}"
      },
      "ExportWithHiddenFieldsOption": {
         "AvailabilityStatus": "{{string}}"
      },
      "QuickSuiteActionsOption": {
         "AvailabilityStatus": "{{string}}"
      },
      "SheetControlsOption": {
         "VisibilityState": "{{string}}"
      },
      "SheetLayoutElementMaximizationOption": {
         "AvailabilityStatus": "{{string}}"
      },
      "VisualAxisSortOption": {
         "AvailabilityStatus": "{{string}}"
      },
      "VisualMenuOption": {
         "AvailabilityStatus": "{{string}}"
      },
      "VisualPublishOptions": {
         "ExportHiddenFieldsOption": {
            "AvailabilityStatus": "{{string}}"
         }
      }
   },
   "Definition": {
      "AnalysisDefaults": {
         "DefaultNewSheetConfiguration": { ... }
      },
      "CalculatedFields": [
         { ... }
      ],
      "ColumnConfigurations": [
         { ... }
      ],
      "DataSetIdentifierDeclarations": [
         { ... }
      ],
      "FilterGroups": [
         { ... }
      ],
      "Options": {
         "CustomActionDefaults": { ... },
         "ExcludedDataSetArns": [ "{{string}}" ],
         "QBusinessInsightsStatus": "{{string}}",
         "Timezone": "{{string}}",
         "VisualMessages": { ... },
         "WeekStart": "{{string}}"
      },
      "ParameterDeclarations": [
         { ... }
      ],
      "Sheets": [
         { ... }
      ],
      "StaticFiles": [
         { ... }
      ],
      "TooltipSheets": [
         { ... }
      ],
      "TopicIdentifierDeclarations": [
         { ... }
      ]
   },
   "Name": "{{string}}",
   "Parameters": {
      "DateTimeParameters": [
         {
            "Name": "{{string}}",
            "Values": [ {{number}} ]
         }
      ],
      "DecimalParameters": [
         {
            "Name": "{{string}}",
            "Values": [ {{number}} ]
         }
      ],
      "IntegerParameters": [
         {
            "Name": "{{string}}",
            "Values": [ {{number}} ]
         }
      ],
      "StringParameters": [
         {
            "Name": "{{string}}",
            "Values": [ "{{string}}" ]
         }
      ]
   },
   "SourceEntity": {
      "SourceTemplate": {
         "Arn": "{{string}}",
         "DataSetReferences": [
            {
               "DataSetArn": "{{string}}",
               "DataSetPlaceholder": "{{string}}"
            }
         ],
         "TopicReferences": [
            {
               "TopicArn": "{{string}}",
               "TopicPlaceholder": "{{string}}"
            }
         ]
      }
   },
   "ThemeArn": "{{string}}",
   "ValidationStrategy": {
      "Mode": "{{string}}"
   },
   "VersionDescription": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateDashboard_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateDashboard_RequestSyntax) **   <a name="QS-UpdateDashboard-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the dashboard that you're updating.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [DashboardId](#API_UpdateDashboard_RequestSyntax) **   <a name="QS-UpdateDashboard-request-uri-DashboardId"></a>
The ID for the dashboard.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

## Request Body
<a name="API_UpdateDashboard_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_UpdateDashboard_RequestSyntax) **   <a name="QS-UpdateDashboard-request-Name"></a>
The display name of the dashboard.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [DashboardPublishOptions](#API_UpdateDashboard_RequestSyntax) **   <a name="QS-UpdateDashboard-request-DashboardPublishOptions"></a>
Options for publishing the dashboard when you create it:
+  `AvailabilityStatus` for `AdHocFilteringOption` - This status can be either `ENABLED` or `DISABLED`. When this is set to `DISABLED`, Amazon Quick Sight disables the left filter pane on the published dashboard, which can be used for ad hoc (one-time) filtering. This option is `ENABLED` by default.
+  `AvailabilityStatus` for `ExportToCSVOption` - This status can be either `ENABLED` or `DISABLED`. The visual option to export data to .CSV format isn't enabled when this is set to `DISABLED`. This option is `ENABLED` by default.
+  `VisibilityState` for `SheetControlsOption` - This visibility state can be either `COLLAPSED` or `EXPANDED`. This option is `COLLAPSED` by default.
+  `AvailabilityStatus` for `QuickSuiteActionsOption` - This status can be either `ENABLED` or `DISABLED`. Features related to Actions in Amazon Quick Suite on dashboards are disabled when this is set to `DISABLED`. This option is `DISABLED` by default.
+  `AvailabilityStatus` for `ExecutiveSummaryOption` - This status can be either `ENABLED` or `DISABLED`. The option to build an executive summary is disabled when this is set to `DISABLED`. This option is `ENABLED` by default.
+  `AvailabilityStatus` for `DataStoriesSharingOption` - This status can be either `ENABLED` or `DISABLED`. The option to share a data story is disabled when this is set to `DISABLED`. This option is `ENABLED` by default.
Type: [DashboardPublishOptions](API_DashboardPublishOptions.md) object
Required: No

 ** [Definition](#API_UpdateDashboard_RequestSyntax) **   <a name="QS-UpdateDashboard-request-Definition"></a>
The definition of a dashboard.
A definition is the data model of all features in a Dashboard, Template, or Analysis.
Type: [DashboardVersionDefinition](API_DashboardVersionDefinition.md) object
Required: No

 ** [Parameters](#API_UpdateDashboard_RequestSyntax) **   <a name="QS-UpdateDashboard-request-Parameters"></a>
A structure that contains the parameters of the dashboard. These are parameter overrides for a dashboard. A dashboard can have any type of parameters, and some parameters might accept multiple values.
Type: [Parameters](API_Parameters.md) object
Required: No

 ** [SourceEntity](#API_UpdateDashboard_RequestSyntax) **   <a name="QS-UpdateDashboard-request-SourceEntity"></a>
The entity that you are using as a source when you update the dashboard. In `SourceEntity`, you specify the type of object you're using as source. You can only update a dashboard from a template, so you use a `SourceTemplate` entity. If you need to update a dashboard from an analysis, first convert the analysis to a template by using the ` [CreateTemplate](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateTemplate.html) ` API operation. For `SourceTemplate`, specify the Amazon Resource Name (ARN) of the source template. The `SourceTemplate` ARN can contain any AWS account and any Amazon Quick Sight-supported AWS Region.
Use the `DataSetReferences` entity within `SourceTemplate` to list the replacement datasets for the placeholders listed in the original. The schema in each dataset must match its placeholder. Use the `TopicReferences` entity to list the replacement topics for the topic placeholders listed in the original. The schema in each topic must match its placeholder.
Type: [DashboardSourceEntity](API_DashboardSourceEntity.md) object
Required: No

 ** [ThemeArn](#API_UpdateDashboard_RequestSyntax) **   <a name="QS-UpdateDashboard-request-ThemeArn"></a>
The Amazon Resource Name (ARN) of the theme that is being used for this dashboard. If you add a value for this field, it overrides the value that was originally associated with the entity. The theme ARN must exist in the same AWS account where you create the dashboard.
Type: String
Required: No

 ** [ValidationStrategy](#API_UpdateDashboard_RequestSyntax) **   <a name="QS-UpdateDashboard-request-ValidationStrategy"></a>
The option to relax the validation needed to update a dashboard with definition objects. This skips the validation step for specific errors.
Type: [ValidationStrategy](API_ValidationStrategy.md) object
Required: No

 ** [VersionDescription](#API_UpdateDashboard_RequestSyntax) **   <a name="QS-UpdateDashboard-request-VersionDescription"></a>
A description for the first version of the dashboard being created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## Response Syntax
<a name="API_UpdateDashboard_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "CreationStatus": "string",
   "DashboardId": "string",
   "RequestId": "string",
   "Status": number,
   "VersionArn": "string"
}
```

## Response Elements
<a name="API_UpdateDashboard_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateDashboard_ResponseSyntax) **   <a name="QS-UpdateDashboard-response-Arn"></a>
The Amazon Resource Name (ARN) of the resource.
Type: String

 ** [CreationStatus](#API_UpdateDashboard_ResponseSyntax) **   <a name="QS-UpdateDashboard-response-CreationStatus"></a>
The creation status of the request.
Type: String
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETED`

 ** [DashboardId](#API_UpdateDashboard_ResponseSyntax) **   <a name="QS-UpdateDashboard-response-DashboardId"></a>
The ID for the dashboard.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`

 ** [RequestId](#API_UpdateDashboard_ResponseSyntax) **   <a name="QS-UpdateDashboard-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

 ** [Status](#API_UpdateDashboard_ResponseSyntax) **   <a name="QS-UpdateDashboard-response-Status"></a>
The HTTP status of the request.
Type: Integer

 ** [VersionArn](#API_UpdateDashboard_ResponseSyntax) **   <a name="QS-UpdateDashboard-response-VersionArn"></a>
The ARN of the dashboard, including the version number.
Type: String

## Errors
<a name="API_UpdateDashboard_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

 ** UnsupportedUserEditionException **
This error indicates that you are calling an operation on an Amazon Quick Suite subscription where the edition doesn't include support for that operation. Amazon Quick Suite currently has Standard Edition and Enterprise Edition. Not every operation and capability is available in every edition.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 403

## See Also
<a name="API_UpdateDashboard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateDashboard)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateDashboard)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateDashboard)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateDashboard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateDashboard)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateDashboard)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateDashboard)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateDashboard)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateDashboard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateDashboard)
