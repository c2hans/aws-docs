---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-quicksight-dashboard.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard
<a name="aws-resource-quicksight-dashboard"></a>

Creates a dashboard from a template. To first create a template, see the `CreateTemplate` API operation.

A dashboard is an entity in Quick that identifies Quick reports, created from analyses. You can share Quick dashboards. With the right permissions, you can create scheduled email reports from them. If you have the correct permissions, you can create a dashboard from a template that exists in a different AWS account.

## Syntax
<a name="aws-resource-quicksight-dashboard-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-quicksight-dashboard-syntax.json"></a>

```
{
  "Type" : "AWS::QuickSight::Dashboard",
  "Properties" : {
      "[AwsAccountId](#cfn-quicksight-dashboard-awsaccountid)" : {{String}},
      "[DashboardId](#cfn-quicksight-dashboard-dashboardid)" : {{String}},
      "[DashboardPublishOptions](#cfn-quicksight-dashboard-dashboardpublishoptions)" : {{DashboardPublishOptions}},
      "[Definition](#cfn-quicksight-dashboard-definition)" : {{DashboardVersionDefinition}},
      "[FolderArns](#cfn-quicksight-dashboard-folderarns)" : {{[ String, ... ]}},
      "[LinkEntities](#cfn-quicksight-dashboard-linkentities)" : {{[ String, ... ]}},
      "[LinkSharingConfiguration](#cfn-quicksight-dashboard-linksharingconfiguration)" : {{LinkSharingConfiguration}},
      "[Name](#cfn-quicksight-dashboard-name)" : {{String}},
      "[Parameters](#cfn-quicksight-dashboard-parameters)" : {{Parameters}},
      "[Permissions](#cfn-quicksight-dashboard-permissions)" : {{[ ResourcePermission, ... ]}},
      "[SourceEntity](#cfn-quicksight-dashboard-sourceentity)" : {{DashboardSourceEntity}},
      "[Tags](#cfn-quicksight-dashboard-tags)" : {{[ Tag, ... ]}},
      "[ThemeArn](#cfn-quicksight-dashboard-themearn)" : {{String}},
      "[ValidationStrategy](#cfn-quicksight-dashboard-validationstrategy)" : {{ValidationStrategy}},
      "[VersionDescription](#cfn-quicksight-dashboard-versiondescription)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-quicksight-dashboard-syntax.yaml"></a>

```
Type: AWS::QuickSight::Dashboard
Properties:
  [AwsAccountId](#cfn-quicksight-dashboard-awsaccountid): {{String}}
  [DashboardId](#cfn-quicksight-dashboard-dashboardid): {{String}}
  [DashboardPublishOptions](#cfn-quicksight-dashboard-dashboardpublishoptions): {{
    DashboardPublishOptions}}
  [Definition](#cfn-quicksight-dashboard-definition): {{
    DashboardVersionDefinition}}
  [FolderArns](#cfn-quicksight-dashboard-folderarns): {{
    - String}}
  [LinkEntities](#cfn-quicksight-dashboard-linkentities): {{
    - String}}
  [LinkSharingConfiguration](#cfn-quicksight-dashboard-linksharingconfiguration): {{
    LinkSharingConfiguration}}
  [Name](#cfn-quicksight-dashboard-name): {{String}}
  [Parameters](#cfn-quicksight-dashboard-parameters): {{
    Parameters}}
  [Permissions](#cfn-quicksight-dashboard-permissions): {{
    - ResourcePermission}}
  [SourceEntity](#cfn-quicksight-dashboard-sourceentity): {{
    DashboardSourceEntity}}
  [Tags](#cfn-quicksight-dashboard-tags): {{
    - Tag}}
  [ThemeArn](#cfn-quicksight-dashboard-themearn): {{String}}
  [ValidationStrategy](#cfn-quicksight-dashboard-validationstrategy): {{
    ValidationStrategy}}
  [VersionDescription](#cfn-quicksight-dashboard-versiondescription): {{String}}
```

## Properties
<a name="aws-resource-quicksight-dashboard-properties"></a>

`AwsAccountId`  <a name="cfn-quicksight-dashboard-awsaccountid"></a>
The ID of the AWS account where you want to create the dashboard.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DashboardId`  <a name="cfn-quicksight-dashboard-dashboardid"></a>
The ID for the dashboard, also added to the IAM policy.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DashboardPublishOptions`  <a name="cfn-quicksight-dashboard-dashboardpublishoptions"></a>
Options for publishing the dashboard when you create it:
+ `AvailabilityStatus` for `AdHocFilteringOption` - This status can be either `ENABLED` or `DISABLED`. When this is set to `DISABLED`, Amazon Quick Sight disables the left filter pane on the published dashboard, which can be used for ad hoc (one-time) filtering. This option is `ENABLED` by default.
+ `AvailabilityStatus` for `ExportToCSVOption` - This status can be either `ENABLED` or `DISABLED`. The visual option to export data to .CSV format isn't enabled when this is set to `DISABLED`. This option is `ENABLED` by default.
+ `VisibilityState` for `SheetControlsOption` - This visibility state can be either `COLLAPSED` or `EXPANDED`. This option is `COLLAPSED` by default.
+ `AvailabilityStatus` for `QuickSuiteActionsOption` - This status can be either `ENABLED` or `DISABLED`. Features related to Actions in Amazon Quick Suite on dashboards are disabled when this is set to `DISABLED`. This option is `DISABLED` by default.
+ `AvailabilityStatus` for `ExecutiveSummaryOption` - This status can be either `ENABLED` or `DISABLED`. The option to build an executive summary is disabled when this is set to `DISABLED`. This option is `ENABLED` by default.
+ `AvailabilityStatus` for `DataStoriesSharingOption` - This status can be either `ENABLED` or `DISABLED`. The option to share a data story is disabled when this is set to `DISABLED`. This option is `ENABLED` by default.
*Required*: No
*Type*: [DashboardPublishOptions](aws-properties-quicksight-dashboard-dashboardpublishoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Definition`  <a name="cfn-quicksight-dashboard-definition"></a>
Property description not available.
*Required*: No
*Type*: [DashboardVersionDefinition](aws-properties-quicksight-dashboard-dashboardversiondefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FolderArns`  <a name="cfn-quicksight-dashboard-folderarns"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LinkEntities`  <a name="cfn-quicksight-dashboard-linkentities"></a>
A list of analysis Amazon Resource Names (ARNs) to be linked to the dashboard.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `1024 | 5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LinkSharingConfiguration`  <a name="cfn-quicksight-dashboard-linksharingconfiguration"></a>
A structure that contains the link sharing configurations that you want to apply overrides to.
*Required*: No
*Type*: [LinkSharingConfiguration](aws-properties-quicksight-dashboard-linksharingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-dashboard-name"></a>
The display name of the dashboard.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Parameters`  <a name="cfn-quicksight-dashboard-parameters"></a>
The parameters for the creation of the dashboard, which you want to use to override the default settings. A dashboard can have any type of parameters, and some parameters might accept multiple values.
*Required*: No
*Type*: [Parameters](aws-properties-quicksight-dashboard-parameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Permissions`  <a name="cfn-quicksight-dashboard-permissions"></a>
A structure that contains the permissions of the dashboard. You can use this structure for granting permissions by providing a list of IAM action information for each principal ARN.
To specify no permissions, omit the permissions list.
*Required*: No
*Type*: Array of [ResourcePermission](aws-properties-quicksight-dashboard-resourcepermission.md)
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceEntity`  <a name="cfn-quicksight-dashboard-sourceentity"></a>
The entity that you are using as a source when you create the dashboard. In `SourceEntity`, you specify the type of object that you want to use. You can only create a dashboard from a template, so you use a `SourceTemplate` entity. If you need to create a dashboard from an analysis, first convert the analysis to a template by using the `CreateTemplate` API operation. For `SourceTemplate`, specify the Amazon Resource Name (ARN) of the source template. The `SourceTemplate`ARN can contain any AWS account; and any QuickSight-supported AWS Region.
Use the `DataSetReferences` entity within `SourceTemplate` to list the replacement datasets for the placeholders listed in the original. The schema in each dataset must match its placeholder.
*Required*: No
*Type*: [DashboardSourceEntity](aws-properties-quicksight-dashboard-dashboardsourceentity.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-quicksight-dashboard-tags"></a>
Contains a map of the key-value pairs for the resource tag or tags assigned to the dashboard.
*Required*: No
*Type*: Array of [Tag](aws-properties-quicksight-dashboard-tag.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThemeArn`  <a name="cfn-quicksight-dashboard-themearn"></a>
The Amazon Resource Name (ARN) of the theme that is being used for this dashboard. If you add a value for this field, it overrides the value that is used in the source entity. The theme ARN must exist in the same AWS account where you create the dashboard.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValidationStrategy`  <a name="cfn-quicksight-dashboard-validationstrategy"></a>
The option to relax the validation that is required to create and update analyses, dashboards, and templates with definition objects. When you set this value to `LENIENT`, validation is skipped for specific errors.
*Required*: No
*Type*: [ValidationStrategy](aws-properties-quicksight-dashboard-validationstrategy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VersionDescription`  <a name="cfn-quicksight-dashboard-versiondescription"></a>
A description for the first version of the dashboard being created.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-quicksight-dashboard-return-values"></a>

### Fn::GetAtt
<a name="aws-resource-quicksight-dashboard-return-values-fn--getatt"></a>

####
<a name="aws-resource-quicksight-dashboard-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the dashboard.

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
The time this dashboard version was created.

`LastPublishedTime`  <a name="LastPublishedTime-fn::getatt"></a>
The time that the dashboard was last published.

`LastUpdatedTime`  <a name="LastUpdatedTime-fn::getatt"></a>
The time that the dashboard was last updated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
