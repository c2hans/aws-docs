---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-quicksight-dataset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet
<a name="aws-resource-quicksight-dataset"></a>

Creates a dataset.

## Syntax
<a name="aws-resource-quicksight-dataset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-quicksight-dataset-syntax.json"></a>

```
{
  "Type" : "AWS::QuickSight::DataSet",
  "Properties" : {
      "[AwsAccountId](#cfn-quicksight-dataset-awsaccountid)" : {{String}},
      "[ColumnGroups](#cfn-quicksight-dataset-columngroups)" : {{[ ColumnGroup, ... ]}},
      "[ColumnLevelPermissionRules](#cfn-quicksight-dataset-columnlevelpermissionrules)" : {{[ ColumnLevelPermissionRule, ... ]}},
      "[DataPrepConfiguration](#cfn-quicksight-dataset-dataprepconfiguration)" : {{DataPrepConfiguration}},
      "[DataSetId](#cfn-quicksight-dataset-datasetid)" : {{String}},
      "[DatasetParameters](#cfn-quicksight-dataset-datasetparameters)" : {{[ DatasetParameter, ... ]}},
      "[DataSetRefreshProperties](#cfn-quicksight-dataset-datasetrefreshproperties)" : {{DataSetRefreshProperties}},
      "[DataSetUsageConfiguration](#cfn-quicksight-dataset-datasetusageconfiguration)" : {{DataSetUsageConfiguration}},
      "[FieldFolders](#cfn-quicksight-dataset-fieldfolders)" : {{{{{Key}}: {{Value}}, ...}}},
      "[FolderArns](#cfn-quicksight-dataset-folderarns)" : {{[ String, ... ]}},
      "[ImportMode](#cfn-quicksight-dataset-importmode)" : {{String}},
      "[IngestionWaitPolicy](#cfn-quicksight-dataset-ingestionwaitpolicy)" : {{IngestionWaitPolicy}},
      "[Name](#cfn-quicksight-dataset-name)" : {{String}},
      "[PerformanceConfiguration](#cfn-quicksight-dataset-performanceconfiguration)" : {{PerformanceConfiguration}},
      "[Permissions](#cfn-quicksight-dataset-permissions)" : {{[ ResourcePermission, ... ]}},
      "[PhysicalTableMap](#cfn-quicksight-dataset-physicaltablemap)" : {{{{{Key}}: {{Value}}, ...}}},
      "[SemanticModelConfiguration](#cfn-quicksight-dataset-semanticmodelconfiguration)" : {{SemanticModelConfiguration}},
      "[Tags](#cfn-quicksight-dataset-tags)" : {{[ Tag, ... ]}},
      "[UseAs](#cfn-quicksight-dataset-useas)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-quicksight-dataset-syntax.yaml"></a>

```
Type: AWS::QuickSight::DataSet
Properties:
  [AwsAccountId](#cfn-quicksight-dataset-awsaccountid): {{String}}
  [ColumnGroups](#cfn-quicksight-dataset-columngroups): {{
    - ColumnGroup}}
  [ColumnLevelPermissionRules](#cfn-quicksight-dataset-columnlevelpermissionrules): {{
    - ColumnLevelPermissionRule}}
  [DataPrepConfiguration](#cfn-quicksight-dataset-dataprepconfiguration): {{
    DataPrepConfiguration}}
  [DataSetId](#cfn-quicksight-dataset-datasetid): {{String}}
  [DatasetParameters](#cfn-quicksight-dataset-datasetparameters): {{
    - DatasetParameter}}
  [DataSetRefreshProperties](#cfn-quicksight-dataset-datasetrefreshproperties): {{
    DataSetRefreshProperties}}
  [DataSetUsageConfiguration](#cfn-quicksight-dataset-datasetusageconfiguration): {{
    DataSetUsageConfiguration}}
  [FieldFolders](#cfn-quicksight-dataset-fieldfolders): {{
    {{Key}}: {{Value}}}}
  [FolderArns](#cfn-quicksight-dataset-folderarns): {{
    - String}}
  [ImportMode](#cfn-quicksight-dataset-importmode): {{String}}
  [IngestionWaitPolicy](#cfn-quicksight-dataset-ingestionwaitpolicy): {{
    IngestionWaitPolicy}}
  [Name](#cfn-quicksight-dataset-name): {{String}}
  [PerformanceConfiguration](#cfn-quicksight-dataset-performanceconfiguration): {{
    PerformanceConfiguration}}
  [Permissions](#cfn-quicksight-dataset-permissions): {{
    - ResourcePermission}}
  [PhysicalTableMap](#cfn-quicksight-dataset-physicaltablemap): {{
    {{Key}}: {{Value}}}}
  [SemanticModelConfiguration](#cfn-quicksight-dataset-semanticmodelconfiguration): {{
    SemanticModelConfiguration}}
  [Tags](#cfn-quicksight-dataset-tags): {{
    - Tag}}
  [UseAs](#cfn-quicksight-dataset-useas): {{String}}
```

## Properties
<a name="aws-resource-quicksight-dataset-properties"></a>

`AwsAccountId`  <a name="cfn-quicksight-dataset-awsaccountid"></a>
The AWS account ID.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ColumnGroups`  <a name="cfn-quicksight-dataset-columngroups"></a>
Groupings of columns that work together in certain Amazon Quick Sight features. Currently, only geospatial hierarchy is supported.
*Required*: No
*Type*: Array of [ColumnGroup](aws-properties-quicksight-dataset-columngroup.md)
*Minimum*: `1`
*Maximum*: `8`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColumnLevelPermissionRules`  <a name="cfn-quicksight-dataset-columnlevelpermissionrules"></a>
A set of one or more definitions of a ` ColumnLevelPermissionRule `.
*Required*: No
*Type*: Array of [ColumnLevelPermissionRule](aws-properties-quicksight-dataset-columnlevelpermissionrule.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataPrepConfiguration`  <a name="cfn-quicksight-dataset-dataprepconfiguration"></a>
The data preparation configuration associated with this dataset.
*Required*: No
*Type*: [DataPrepConfiguration](aws-properties-quicksight-dataset-dataprepconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSetId`  <a name="cfn-quicksight-dataset-datasetid"></a>
An ID for the dataset that you want to create. This ID is unique per AWS Region for each AWS account.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DatasetParameters`  <a name="cfn-quicksight-dataset-datasetparameters"></a>
The parameters that are declared in a dataset.
*Required*: No
*Type*: Array of [DatasetParameter](aws-properties-quicksight-dataset-datasetparameter.md)
*Minimum*: `0`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSetRefreshProperties`  <a name="cfn-quicksight-dataset-datasetrefreshproperties"></a>
The refresh properties of a dataset.
*Required*: No
*Type*: [DataSetRefreshProperties](aws-properties-quicksight-dataset-datasetrefreshproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSetUsageConfiguration`  <a name="cfn-quicksight-dataset-datasetusageconfiguration"></a>
The usage configuration to apply to child datasets that reference this dataset as a source.
*Required*: No
*Type*: [DataSetUsageConfiguration](aws-properties-quicksight-dataset-datasetusageconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldFolders`  <a name="cfn-quicksight-dataset-fieldfolders"></a>
The folder that contains fields and nested subfolders for your dataset.
*Required*: No
*Type*: Object of [FieldFolder](aws-properties-quicksight-dataset-fieldfolder.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FolderArns`  <a name="cfn-quicksight-dataset-folderarns"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImportMode`  <a name="cfn-quicksight-dataset-importmode"></a>
Indicates whether you want to import the data into SPICE.
*Required*: No
*Type*: String
*Allowed values*: `SPICE | DIRECT_QUERY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IngestionWaitPolicy`  <a name="cfn-quicksight-dataset-ingestionwaitpolicy"></a>
The wait policy to use when creating or updating a Dataset. The default is to wait for SPICE ingestion to finish with timeout of 36 hours.
*Required*: No
*Type*: [IngestionWaitPolicy](aws-properties-quicksight-dataset-ingestionwaitpolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-dataset-name"></a>
The display name for the dataset.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PerformanceConfiguration`  <a name="cfn-quicksight-dataset-performanceconfiguration"></a>
The performance optimization configuration of a dataset.
*Required*: No
*Type*: [PerformanceConfiguration](aws-properties-quicksight-dataset-performanceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Permissions`  <a name="cfn-quicksight-dataset-permissions"></a>
A list of resource permissions on the dataset.
*Required*: No
*Type*: Array of [ResourcePermission](aws-properties-quicksight-dataset-resourcepermission.md)
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PhysicalTableMap`  <a name="cfn-quicksight-dataset-physicaltablemap"></a>
Declares the physical tables that are available in the underlying data sources.
*Required*: No
*Type*: Object of [PhysicalTable](aws-properties-quicksight-dataset-physicaltable.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SemanticModelConfiguration`  <a name="cfn-quicksight-dataset-semanticmodelconfiguration"></a>
The semantic model configuration associated with this dataset.
*Required*: No
*Type*: [SemanticModelConfiguration](aws-properties-quicksight-dataset-semanticmodelconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-quicksight-dataset-tags"></a>
Contains a map of the key-value pairs for the resource tag or tags assigned to the dataset.
*Required*: No
*Type*: Array of [Tag](aws-properties-quicksight-dataset-tag.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseAs`  <a name="cfn-quicksight-dataset-useas"></a>
The usage of the dataset.
*Required*: No
*Type*: String
*Allowed values*: `RLS_RULES`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-quicksight-dataset-return-values"></a>

### Fn::GetAtt
<a name="aws-resource-quicksight-dataset-return-values-fn--getatt"></a>

####
<a name="aws-resource-quicksight-dataset-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the dataset.

`ConsumedSpiceCapacityInBytes`  <a name="ConsumedSpiceCapacityInBytes-fn::getatt"></a>

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
The time this dataset version was created.

`LastUpdatedTime`  <a name="LastUpdatedTime-fn::getatt"></a>
The time this dataset version was last updated.

`OutputColumns`  <a name="OutputColumns-fn::getatt"></a>

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
