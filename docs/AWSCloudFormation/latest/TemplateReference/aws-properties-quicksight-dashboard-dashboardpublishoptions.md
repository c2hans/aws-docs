---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-dashboardpublishoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard DashboardPublishOptions
<a name="aws-properties-quicksight-dashboard-dashboardpublishoptions"></a>

Dashboard publish options:
+ `AvailabilityStatus` for `AdHocFilteringOption` - This status can be either `ENABLED` or `DISABLED`. When this is set to `DISABLED`, Amazon Quick Sight disables the left filter pane on the published dashboard, which can be used for ad hoc (one-time) filtering. This option is `ENABLED` by default.
+ `AvailabilityStatus` for `ExportToCSVOption` - This status can be either `ENABLED` or `DISABLED`. The visual option to export data to .CSV format isn't enabled when this is set to `DISABLED`. This option is `ENABLED` by default.
+ `VisibilityState` for `SheetControlsOption` - This visibility state can be either `COLLAPSED` or `EXPANDED`. This option is `COLLAPSED` by default.
+ `AvailabilityStatus` for `QuickSuiteActionsOption` - This status can be either `ENABLED` or `DISABLED`. Features related to Actions in Amazon Quick Suite on dashboards are disabled when this is set to `DISABLED`. This option is `DISABLED` by default.
+ `AvailabilityStatus` for `ExecutiveSummaryOption` - This status can be either `ENABLED` or `DISABLED`. The option to build an executive summary is disabled when this is set to `DISABLED`. This option is `ENABLED` by default.
+ `AvailabilityStatus` for `DataStoriesSharingOption` - This status can be either `ENABLED` or `DISABLED`. The option to share a data story is disabled when this is set to `DISABLED`. This option is `ENABLED` by default.

## Syntax
<a name="aws-properties-quicksight-dashboard-dashboardpublishoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-dashboardpublishoptions-syntax.json"></a>

```
{
  "[AdHocFilteringOption](#cfn-quicksight-dashboard-dashboardpublishoptions-adhocfilteringoption)" : {{AdHocFilteringOption}},
  "[DataPointDrillUpDownOption](#cfn-quicksight-dashboard-dashboardpublishoptions-datapointdrillupdownoption)" : {{DataPointDrillUpDownOption}},
  "[DataPointMenuLabelOption](#cfn-quicksight-dashboard-dashboardpublishoptions-datapointmenulabeloption)" : {{DataPointMenuLabelOption}},
  "[DataPointTooltipOption](#cfn-quicksight-dashboard-dashboardpublishoptions-datapointtooltipoption)" : {{DataPointTooltipOption}},
  "[DataQAEnabledOption](#cfn-quicksight-dashboard-dashboardpublishoptions-dataqaenabledoption)" : {{DataQAEnabledOption}},
  "[DataStoriesSharingOption](#cfn-quicksight-dashboard-dashboardpublishoptions-datastoriessharingoption)" : {{DataStoriesSharingOption}},
  "[ExecutiveSummaryOption](#cfn-quicksight-dashboard-dashboardpublishoptions-executivesummaryoption)" : {{ExecutiveSummaryOption}},
  "[ExportToCSVOption](#cfn-quicksight-dashboard-dashboardpublishoptions-exporttocsvoption)" : {{ExportToCSVOption}},
  "[ExportWithHiddenFieldsOption](#cfn-quicksight-dashboard-dashboardpublishoptions-exportwithhiddenfieldsoption)" : {{ExportWithHiddenFieldsOption}},
  "[QuickSuiteActionsOption](#cfn-quicksight-dashboard-dashboardpublishoptions-quicksuiteactionsoption)" : {{QuickSuiteActionsOption}},
  "[SheetControlsOption](#cfn-quicksight-dashboard-dashboardpublishoptions-sheetcontrolsoption)" : {{SheetControlsOption}},
  "[SheetLayoutElementMaximizationOption](#cfn-quicksight-dashboard-dashboardpublishoptions-sheetlayoutelementmaximizationoption)" : {{SheetLayoutElementMaximizationOption}},
  "[VisualAxisSortOption](#cfn-quicksight-dashboard-dashboardpublishoptions-visualaxissortoption)" : {{VisualAxisSortOption}},
  "[VisualMenuOption](#cfn-quicksight-dashboard-dashboardpublishoptions-visualmenuoption)" : {{VisualMenuOption}},
  "[VisualPublishOptions](#cfn-quicksight-dashboard-dashboardpublishoptions-visualpublishoptions)" : {{DashboardVisualPublishOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-dashboardpublishoptions-syntax.yaml"></a>

```
  [AdHocFilteringOption](#cfn-quicksight-dashboard-dashboardpublishoptions-adhocfilteringoption): {{
    AdHocFilteringOption}}
  [DataPointDrillUpDownOption](#cfn-quicksight-dashboard-dashboardpublishoptions-datapointdrillupdownoption): {{
    DataPointDrillUpDownOption}}
  [DataPointMenuLabelOption](#cfn-quicksight-dashboard-dashboardpublishoptions-datapointmenulabeloption): {{
    DataPointMenuLabelOption}}
  [DataPointTooltipOption](#cfn-quicksight-dashboard-dashboardpublishoptions-datapointtooltipoption): {{
    DataPointTooltipOption}}
  [DataQAEnabledOption](#cfn-quicksight-dashboard-dashboardpublishoptions-dataqaenabledoption): {{
    DataQAEnabledOption}}
  [DataStoriesSharingOption](#cfn-quicksight-dashboard-dashboardpublishoptions-datastoriessharingoption): {{
    DataStoriesSharingOption}}
  [ExecutiveSummaryOption](#cfn-quicksight-dashboard-dashboardpublishoptions-executivesummaryoption): {{
    ExecutiveSummaryOption}}
  [ExportToCSVOption](#cfn-quicksight-dashboard-dashboardpublishoptions-exporttocsvoption): {{
    ExportToCSVOption}}
  [ExportWithHiddenFieldsOption](#cfn-quicksight-dashboard-dashboardpublishoptions-exportwithhiddenfieldsoption): {{
    ExportWithHiddenFieldsOption}}
  [QuickSuiteActionsOption](#cfn-quicksight-dashboard-dashboardpublishoptions-quicksuiteactionsoption): {{
    QuickSuiteActionsOption}}
  [SheetControlsOption](#cfn-quicksight-dashboard-dashboardpublishoptions-sheetcontrolsoption): {{
    SheetControlsOption}}
  [SheetLayoutElementMaximizationOption](#cfn-quicksight-dashboard-dashboardpublishoptions-sheetlayoutelementmaximizationoption): {{
    SheetLayoutElementMaximizationOption}}
  [VisualAxisSortOption](#cfn-quicksight-dashboard-dashboardpublishoptions-visualaxissortoption): {{
    VisualAxisSortOption}}
  [VisualMenuOption](#cfn-quicksight-dashboard-dashboardpublishoptions-visualmenuoption): {{
    VisualMenuOption}}
  [VisualPublishOptions](#cfn-quicksight-dashboard-dashboardpublishoptions-visualpublishoptions): {{
    DashboardVisualPublishOptions}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-dashboardpublishoptions-properties"></a>

`AdHocFilteringOption`  <a name="cfn-quicksight-dashboard-dashboardpublishoptions-adhocfilteringoption"></a>
Ad hoc (one-time) filtering option.
*Required*: No
*Type*: [AdHocFilteringOption](aws-properties-quicksight-dashboard-adhocfilteringoption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataPointDrillUpDownOption`  <a name="cfn-quicksight-dashboard-dashboardpublishoptions-datapointdrillupdownoption"></a>
The drill-down options of data points in a dashboard.
*Required*: No
*Type*: [DataPointDrillUpDownOption](aws-properties-quicksight-dashboard-datapointdrillupdownoption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataPointMenuLabelOption`  <a name="cfn-quicksight-dashboard-dashboardpublishoptions-datapointmenulabeloption"></a>
The data point menu label options of a dashboard.
*Required*: No
*Type*: [DataPointMenuLabelOption](aws-properties-quicksight-dashboard-datapointmenulabeloption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataPointTooltipOption`  <a name="cfn-quicksight-dashboard-dashboardpublishoptions-datapointtooltipoption"></a>
The data point tool tip options of a dashboard.
*Required*: No
*Type*: [DataPointTooltipOption](aws-properties-quicksight-dashboard-datapointtooltipoption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataQAEnabledOption`  <a name="cfn-quicksight-dashboard-dashboardpublishoptions-dataqaenabledoption"></a>
Adds Q&A capabilities to an Quick Sight dashboard. If no topic is linked, Dashboard Q&A uses the data values that are rendered on the dashboard. End users can use Dashboard Q&A to ask for different slices of the data that they see on the dashboard. If a topic is linked, Topic Q&A is used.
*Required*: No
*Type*: [DataQAEnabledOption](aws-properties-quicksight-dashboard-dataqaenabledoption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataStoriesSharingOption`  <a name="cfn-quicksight-dashboard-dashboardpublishoptions-datastoriessharingoption"></a>
Data stories sharing option.
*Required*: No
*Type*: [DataStoriesSharingOption](aws-properties-quicksight-dashboard-datastoriessharingoption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutiveSummaryOption`  <a name="cfn-quicksight-dashboard-dashboardpublishoptions-executivesummaryoption"></a>
Executive summary option.
*Required*: No
*Type*: [ExecutiveSummaryOption](aws-properties-quicksight-dashboard-executivesummaryoption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExportToCSVOption`  <a name="cfn-quicksight-dashboard-dashboardpublishoptions-exporttocsvoption"></a>
Export to .csv option.
*Required*: No
*Type*: [ExportToCSVOption](aws-properties-quicksight-dashboard-exporttocsvoption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExportWithHiddenFieldsOption`  <a name="cfn-quicksight-dashboard-dashboardpublishoptions-exportwithhiddenfieldsoption"></a>
Determines if hidden fields are exported with a dashboard.
*Required*: No
*Type*: [ExportWithHiddenFieldsOption](aws-properties-quicksight-dashboard-exportwithhiddenfieldsoption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QuickSuiteActionsOption`  <a name="cfn-quicksight-dashboard-dashboardpublishoptions-quicksuiteactionsoption"></a>
Determines if Actions in Amazon Quick Suite are enabled in a dashboard.
*Required*: No
*Type*: [QuickSuiteActionsOption](aws-properties-quicksight-dashboard-quicksuiteactionsoption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SheetControlsOption`  <a name="cfn-quicksight-dashboard-dashboardpublishoptions-sheetcontrolsoption"></a>
Sheet controls option.
*Required*: No
*Type*: [SheetControlsOption](aws-properties-quicksight-dashboard-sheetcontrolsoption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SheetLayoutElementMaximizationOption`  <a name="cfn-quicksight-dashboard-dashboardpublishoptions-sheetlayoutelementmaximizationoption"></a>
The sheet layout maximization options of a dashbaord.
*Required*: No
*Type*: [SheetLayoutElementMaximizationOption](aws-properties-quicksight-dashboard-sheetlayoutelementmaximizationoption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualAxisSortOption`  <a name="cfn-quicksight-dashboard-dashboardpublishoptions-visualaxissortoption"></a>
The axis sort options of a dashboard.
*Required*: No
*Type*: [VisualAxisSortOption](aws-properties-quicksight-dashboard-visualaxissortoption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualMenuOption`  <a name="cfn-quicksight-dashboard-dashboardpublishoptions-visualmenuoption"></a>
The menu options of a visual in a dashboard.
*Required*: No
*Type*: [VisualMenuOption](aws-properties-quicksight-dashboard-visualmenuoption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualPublishOptions`  <a name="cfn-quicksight-dashboard-dashboardpublishoptions-visualpublishoptions"></a>
The visual publish options of a visual in a dashboard.
*Required*: No
*Type*: [DashboardVisualPublishOptions](aws-properties-quicksight-dashboard-dashboardvisualpublishoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
