---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DashboardPublishOptions.html
---

# DashboardPublishOptions
<a name="API_DashboardPublishOptions"></a>

Dashboard publish options.

## Contents
<a name="API_DashboardPublishOptions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AdHocFilteringOption **   <a name="QS-Type-DashboardPublishOptions-AdHocFilteringOption"></a>
Ad hoc (one-time) filtering option.
Type: [AdHocFilteringOption](API_AdHocFilteringOption.md) object
Required: No

 ** DataPointDrillUpDownOption **   <a name="QS-Type-DashboardPublishOptions-DataPointDrillUpDownOption"></a>
The drill-down options of data points in a dashboard.
Type: [DataPointDrillUpDownOption](API_DataPointDrillUpDownOption.md) object
Required: No

 ** DataPointMenuLabelOption **   <a name="QS-Type-DashboardPublishOptions-DataPointMenuLabelOption"></a>
The data point menu label options of a dashboard.
Type: [DataPointMenuLabelOption](API_DataPointMenuLabelOption.md) object
Required: No

 ** DataPointTooltipOption **   <a name="QS-Type-DashboardPublishOptions-DataPointTooltipOption"></a>
The data point tool tip options of a dashboard.
Type: [DataPointTooltipOption](API_DataPointTooltipOption.md) object
Required: No

 ** DataQAEnabledOption **   <a name="QS-Type-DashboardPublishOptions-DataQAEnabledOption"></a>
Adds Q&A capabilities to an Quick Sight dashboard. If no topic is linked, Dashboard Q&A uses the data values that are rendered on the dashboard. End users can use Dashboard Q&A to ask for different slices of the data that they see on the dashboard. If a topic is linked, Topic Q&A is used.
Type: [DataQAEnabledOption](API_DataQAEnabledOption.md) object
Required: No

 ** DataStoriesSharingOption **   <a name="QS-Type-DashboardPublishOptions-DataStoriesSharingOption"></a>
Data stories sharing option.
Type: [DataStoriesSharingOption](API_DataStoriesSharingOption.md) object
Required: No

 ** ExecutiveSummaryOption **   <a name="QS-Type-DashboardPublishOptions-ExecutiveSummaryOption"></a>
Executive summary option.
Type: [ExecutiveSummaryOption](API_ExecutiveSummaryOption.md) object
Required: No

 ** ExportToCSVOption **   <a name="QS-Type-DashboardPublishOptions-ExportToCSVOption"></a>
Export to .csv option.
Type: [ExportToCSVOption](API_ExportToCSVOption.md) object
Required: No

 ** ExportWithHiddenFieldsOption **   <a name="QS-Type-DashboardPublishOptions-ExportWithHiddenFieldsOption"></a>
Determines if hidden fields are exported with a dashboard.
Type: [ExportWithHiddenFieldsOption](API_ExportWithHiddenFieldsOption.md) object
Required: No

 ** QuickSuiteActionsOption **   <a name="QS-Type-DashboardPublishOptions-QuickSuiteActionsOption"></a>
Determines if Actions in Amazon Quick Suite are enabled in a dashboard.
Type: [QuickSuiteActionsOption](API_QuickSuiteActionsOption.md) object
Required: No

 ** SheetControlsOption **   <a name="QS-Type-DashboardPublishOptions-SheetControlsOption"></a>
Sheet controls option.
Type: [SheetControlsOption](API_SheetControlsOption.md) object
Required: No

 ** SheetLayoutElementMaximizationOption **   <a name="QS-Type-DashboardPublishOptions-SheetLayoutElementMaximizationOption"></a>
The sheet layout maximization options of a dashbaord.
Type: [SheetLayoutElementMaximizationOption](API_SheetLayoutElementMaximizationOption.md) object
Required: No

 ** VisualAxisSortOption **   <a name="QS-Type-DashboardPublishOptions-VisualAxisSortOption"></a>
The axis sort options of a dashboard.
Type: [VisualAxisSortOption](API_VisualAxisSortOption.md) object
Required: No

 ** VisualMenuOption **   <a name="QS-Type-DashboardPublishOptions-VisualMenuOption"></a>
The menu options of a visual in a dashboard.
Type: [VisualMenuOption](API_VisualMenuOption.md) object
Required: No

 ** VisualPublishOptions **   <a name="QS-Type-DashboardPublishOptions-VisualPublishOptions"></a>
 *This member has been deprecated.*
The visual publish options of a visual in a dashboard.
Type: [DashboardVisualPublishOptions](API_DashboardVisualPublishOptions.md) object
Required: No

## See Also
<a name="API_DashboardPublishOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DashboardPublishOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DashboardPublishOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DashboardPublishOptions)
