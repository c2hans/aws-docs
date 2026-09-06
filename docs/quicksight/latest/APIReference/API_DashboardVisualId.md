---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DashboardVisualId.html
---

# DashboardVisualId
<a name="API_DashboardVisualId"></a>

A structure that contains the following elements:
+ The `DashboardId` of the dashboard that has the visual that you want to embed.
+ The `SheetId` of the sheet that has the visual that you want to embed.
+ The `VisualId` of the visual that you want to embed.

The `DashboardId`, `SheetId`, and `VisualId` can be found in the `IDs for developers` section of the `Embed visual` pane of the visual's on-visual menu of the Amazon Quick Sight console. You can also get the `DashboardId` with a `ListDashboards` API operation.

## Contents
<a name="API_DashboardVisualId_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DashboardId **   <a name="QS-Type-DashboardVisualId-DashboardId"></a>
The ID of the dashboard that has the visual that you want to embed. The `DashboardId` can be found in the `IDs for developers` section of the `Embed visual` pane of the visual's on-visual menu of the Quick console. You can also get the `DashboardId` with a `ListDashboards` API operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** SheetId **   <a name="QS-Type-DashboardVisualId-SheetId"></a>
The ID of the sheet that the has visual that you want to embed. The `SheetId` can be found in the `IDs for developers` section of the `Embed visual` pane of the visual's on-visual menu of the Quick console.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** VisualId **   <a name="QS-Type-DashboardVisualId-VisualId"></a>
The ID of the visual that you want to embed. The `VisualID` can be found in the `IDs for developers` section of the `Embed visual` pane of the visual's on-visual menu of the Amazon Quick Sight console.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

## See Also
<a name="API_DashboardVisualId_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DashboardVisualId)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DashboardVisualId)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DashboardVisualId)
