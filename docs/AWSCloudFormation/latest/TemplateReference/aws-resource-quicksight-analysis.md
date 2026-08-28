---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-quicksight-analysis.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis
<a name="aws-resource-quicksight-analysis"></a>

Creates an analysis in Amazon QuickSight.

## Syntax
<a name="aws-resource-quicksight-analysis-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-quicksight-analysis-syntax.json"></a>

```
{
  "Type" : "AWS::QuickSight::Analysis",
  "Properties" : {
      "[AnalysisId](#cfn-quicksight-analysis-analysisid)" : {{String}},
      "[AwsAccountId](#cfn-quicksight-analysis-awsaccountid)" : {{String}},
      "[Definition](#cfn-quicksight-analysis-definition)" : {{AnalysisDefinition}},
      "[Errors](#cfn-quicksight-analysis-errors)" : {{[ AnalysisError, ... ]}},
      "[FolderArns](#cfn-quicksight-analysis-folderarns)" : {{[ String, ... ]}},
      "[Name](#cfn-quicksight-analysis-name)" : {{String}},
      "[Parameters](#cfn-quicksight-analysis-parameters)" : {{Parameters}},
      "[Permissions](#cfn-quicksight-analysis-permissions)" : {{[ ResourcePermission, ... ]}},
      "[Sheets](#cfn-quicksight-analysis-sheets)" : {{[ Sheet, ... ]}},
      "[SourceEntity](#cfn-quicksight-analysis-sourceentity)" : {{AnalysisSourceEntity}},
      "[Status](#cfn-quicksight-analysis-status)" : {{String}},
      "[Tags](#cfn-quicksight-analysis-tags)" : {{[ Tag, ... ]}},
      "[ThemeArn](#cfn-quicksight-analysis-themearn)" : {{String}},
      "[ValidationStrategy](#cfn-quicksight-analysis-validationstrategy)" : {{ValidationStrategy}}
    }
}
```

### YAML
<a name="aws-resource-quicksight-analysis-syntax.yaml"></a>

```
Type: AWS::QuickSight::Analysis
Properties:
  [AnalysisId](#cfn-quicksight-analysis-analysisid): {{String}}
  [AwsAccountId](#cfn-quicksight-analysis-awsaccountid): {{String}}
  [Definition](#cfn-quicksight-analysis-definition): {{
    AnalysisDefinition}}
  [Errors](#cfn-quicksight-analysis-errors): {{
    - AnalysisError}}
  [FolderArns](#cfn-quicksight-analysis-folderarns): {{
    - String}}
  [Name](#cfn-quicksight-analysis-name): {{String}}
  [Parameters](#cfn-quicksight-analysis-parameters): {{
    Parameters}}
  [Permissions](#cfn-quicksight-analysis-permissions): {{
    - ResourcePermission}}
  [Sheets](#cfn-quicksight-analysis-sheets): {{
    - Sheet}}
  [SourceEntity](#cfn-quicksight-analysis-sourceentity): {{
    AnalysisSourceEntity}}
  [Status](#cfn-quicksight-analysis-status): {{String}}
  [Tags](#cfn-quicksight-analysis-tags): {{
    - Tag}}
  [ThemeArn](#cfn-quicksight-analysis-themearn): {{String}}
  [ValidationStrategy](#cfn-quicksight-analysis-validationstrategy): {{
    ValidationStrategy}}
```

## Properties
<a name="aws-resource-quicksight-analysis-properties"></a>

`AnalysisId`  <a name="cfn-quicksight-analysis-analysisid"></a>
The ID for the analysis that you're creating. This ID displays in the URL of the analysis.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AwsAccountId`  <a name="cfn-quicksight-analysis-awsaccountid"></a>
The ID of the AWS account where you are creating an analysis.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Definition`  <a name="cfn-quicksight-analysis-definition"></a>
Property description not available.
*Required*: No
*Type*: [AnalysisDefinition](aws-properties-quicksight-analysis-analysisdefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Errors`  <a name="cfn-quicksight-analysis-errors"></a>
Errors associated with the analysis.
*Required*: No
*Type*: Array of [AnalysisError](aws-properties-quicksight-analysis-analysiserror.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FolderArns`  <a name="cfn-quicksight-analysis-folderarns"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-analysis-name"></a>
A descriptive name for the analysis that you're creating. This name displays for the analysis in the Amazon Quick Sight console.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Parameters`  <a name="cfn-quicksight-analysis-parameters"></a>
The parameter names and override values that you want to use. An analysis can have any parameter type, and some parameters might accept multiple values.
*Required*: No
*Type*: [Parameters](aws-properties-quicksight-analysis-parameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Permissions`  <a name="cfn-quicksight-analysis-permissions"></a>
A structure that describes the principals and the resource-level permissions on an analysis. You can use the `Permissions` structure to grant permissions by providing a list of AWS Identity and Access Management (IAM) action information for each principal listed by Amazon Resource Name (ARN).
To specify no permissions, omit `Permissions`.
*Required*: No
*Type*: Array of [ResourcePermission](aws-properties-quicksight-analysis-resourcepermission.md)
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sheets`  <a name="cfn-quicksight-analysis-sheets"></a>
A list of the associated sheets with the unique identifier and name of each sheet.
*Required*: No
*Type*: Array of [Sheet](aws-properties-quicksight-analysis-sheet.md)
*Minimum*: `0`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceEntity`  <a name="cfn-quicksight-analysis-sourceentity"></a>
A source entity to use for the analysis that you're creating. This metadata structure contains details that describe a source template and one or more datasets or topics.
Either a `SourceEntity` or a `Definition` must be provided in order for the request to be valid.
*Required*: No
*Type*: [AnalysisSourceEntity](aws-properties-quicksight-analysis-analysissourceentity.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-quicksight-analysis-status"></a>
Status associated with the analysis.
*Required*: No
*Type*: String
*Allowed values*: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | PENDING_UPDATE | DELETED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-quicksight-analysis-tags"></a>
Contains a map of the key-value pairs for the resource tag or tags assigned to the analysis.
*Required*: No
*Type*: Array of [Tag](aws-properties-quicksight-analysis-tag.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThemeArn`  <a name="cfn-quicksight-analysis-themearn"></a>
The ARN for the theme to apply to the analysis that you're creating. To see the theme in the Amazon Quick Sight console, make sure that you have access to it.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValidationStrategy`  <a name="cfn-quicksight-analysis-validationstrategy"></a>
The option to relax the validation that is required to create and update analyses, dashboards, and templates with definition objects. When you set this value to `LENIENT`, validation is skipped for specific errors.
*Required*: No
*Type*: [ValidationStrategy](aws-properties-quicksight-analysis-validationstrategy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-quicksight-analysis-return-values"></a>

### Fn::GetAtt
<a name="aws-resource-quicksight-analysis-return-values-fn--getatt"></a>

####
<a name="aws-resource-quicksight-analysis-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the analysis.

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
The time that the analysis was created.

`DataSetArns`  <a name="DataSetArns-fn::getatt"></a>
The ARNs of the datasets of the analysis.

`LastUpdatedTime`  <a name="LastUpdatedTime-fn::getatt"></a>
The time that the analysis was last updated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
