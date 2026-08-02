---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DashboardVersion.html
---

# DashboardVersion
<a name="API_DashboardVersion"></a>

Dashboard version.

## Contents
<a name="API_DashboardVersion_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-DashboardVersion-Arn"></a>
The Amazon Resource Name (ARN) of the resource.
Type: String
Required: No

 ** CreatedTime **   <a name="QS-Type-DashboardVersion-CreatedTime"></a>
The time that this dashboard version was created.
Type: Timestamp
Required: No

 ** DataSetArns **   <a name="QS-Type-DashboardVersion-DataSetArns"></a>
The Amazon Resource Numbers (ARNs) for the datasets that are associated with this version of the dashboard.
Type: Array of strings
Array Members: Maximum number of 100 items.
Required: No

 ** Description **   <a name="QS-Type-DashboardVersion-Description"></a>
Description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** Errors **   <a name="QS-Type-DashboardVersion-Errors"></a>
Errors associated with this dashboard version.
Type: Array of [DashboardError](API_DashboardError.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** Sheets **   <a name="QS-Type-DashboardVersion-Sheets"></a>
A list of the associated sheets with the unique identifier and name of each sheet.
Type: Array of [Sheet](API_Sheet.md) objects
Array Members: Maximum number of 20 items.
Required: No

 ** SourceEntityArn **   <a name="QS-Type-DashboardVersion-SourceEntityArn"></a>
Source entity ARN.
Type: String
Required: No

 ** Status **   <a name="QS-Type-DashboardVersion-Status"></a>
The HTTP status of the request.
Type: String
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETED`
Required: No

 ** ThemeArn **   <a name="QS-Type-DashboardVersion-ThemeArn"></a>
The ARN of the theme associated with a version of the dashboard.
Type: String
Required: No

 ** VersionNumber **   <a name="QS-Type-DashboardVersion-VersionNumber"></a>
Version number for this version of the dashboard.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_DashboardVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DashboardVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DashboardVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DashboardVersion)
