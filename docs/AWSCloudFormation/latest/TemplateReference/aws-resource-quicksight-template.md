---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-quicksight-template.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template
<a name="aws-resource-quicksight-template"></a>

Creates a template from an existing Quick analysis or template. You can use the resulting template to create a dashboard.

A *template* is an entity in Quick that encapsulates the metadata required to create an analysis and that you can use to create s dashboard. A template adds a layer of abstraction by using placeholders to replace the dataset associated with the analysis. You can use templates to create dashboards by replacing dataset placeholders with datasets that follow the same schema that was used to create the source analysis and template.

## Syntax
<a name="aws-resource-quicksight-template-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-quicksight-template-syntax.json"></a>

```
{
  "Type" : "AWS::QuickSight::Template",
  "Properties" : {
      "[AwsAccountId](#cfn-quicksight-template-awsaccountid)" : {{String}},
      "[Definition](#cfn-quicksight-template-definition)" : {{TemplateVersionDefinition}},
      "[Name](#cfn-quicksight-template-name)" : {{String}},
      "[Permissions](#cfn-quicksight-template-permissions)" : {{[ ResourcePermission, ... ]}},
      "[SourceEntity](#cfn-quicksight-template-sourceentity)" : {{TemplateSourceEntity}},
      "[Tags](#cfn-quicksight-template-tags)" : {{[ Tag, ... ]}},
      "[TemplateId](#cfn-quicksight-template-templateid)" : {{String}},
      "[ValidationStrategy](#cfn-quicksight-template-validationstrategy)" : {{ValidationStrategy}},
      "[VersionDescription](#cfn-quicksight-template-versiondescription)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-quicksight-template-syntax.yaml"></a>

```
Type: AWS::QuickSight::Template
Properties:
  [AwsAccountId](#cfn-quicksight-template-awsaccountid): {{String}}
  [Definition](#cfn-quicksight-template-definition): {{
    TemplateVersionDefinition}}
  [Name](#cfn-quicksight-template-name): {{String}}
  [Permissions](#cfn-quicksight-template-permissions): {{
    - ResourcePermission}}
  [SourceEntity](#cfn-quicksight-template-sourceentity): {{
    TemplateSourceEntity}}
  [Tags](#cfn-quicksight-template-tags): {{
    - Tag}}
  [TemplateId](#cfn-quicksight-template-templateid): {{String}}
  [ValidationStrategy](#cfn-quicksight-template-validationstrategy): {{
    ValidationStrategy}}
  [VersionDescription](#cfn-quicksight-template-versiondescription): {{String}}
```

## Properties
<a name="aws-resource-quicksight-template-properties"></a>

`AwsAccountId`  <a name="cfn-quicksight-template-awsaccountid"></a>
The ID for the AWS account that the group is in. You use the ID for the AWS account that contains your Amazon Quick Sight account.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Definition`  <a name="cfn-quicksight-template-definition"></a>
Property description not available.
*Required*: No
*Type*: [TemplateVersionDefinition](aws-properties-quicksight-template-templateversiondefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-template-name"></a>
A display name for the template.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Permissions`  <a name="cfn-quicksight-template-permissions"></a>
A list of resource permissions to be set on the template.
*Required*: No
*Type*: Array of [ResourcePermission](aws-properties-quicksight-template-resourcepermission.md)
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceEntity`  <a name="cfn-quicksight-template-sourceentity"></a>
The entity that you are using as a source when you create the template. In `SourceEntity`, you specify the type of object you're using as source: `SourceTemplate` for a template or `SourceAnalysis` for an analysis. Both of these require an Amazon Resource Name (ARN). For `SourceTemplate`, specify the ARN of the source template. For `SourceAnalysis`, specify the ARN of the source analysis. The `SourceTemplate` ARN can contain any AWS account and any Quick Sight-supported AWS Region.
Use the `DataSetReferences` entity within `SourceTemplate` or `SourceAnalysis` to list the replacement datasets for the placeholders listed in the original. The schema in each dataset must match its placeholder.
Either a `SourceEntity` or a `Definition` must be provided in order for the request to be valid.
*Required*: No
*Type*: [TemplateSourceEntity](aws-properties-quicksight-template-templatesourceentity.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-quicksight-template-tags"></a>
Contains a map of the key-value pairs for the resource tag or tags assigned to the resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-quicksight-template-tag.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateId`  <a name="cfn-quicksight-template-templateid"></a>
An ID for the template that you want to create. This template is unique per AWS Region; in each AWS account.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ValidationStrategy`  <a name="cfn-quicksight-template-validationstrategy"></a>
The option to relax the validation that is required to create and update analyses, dashboards, and templates with definition objects. When you set this value to `LENIENT`, validation is skipped for specific errors.
*Required*: No
*Type*: [ValidationStrategy](aws-properties-quicksight-template-validationstrategy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VersionDescription`  <a name="cfn-quicksight-template-versiondescription"></a>
A description of the current template version being created. This API operation creates the first version of the template. Every time `UpdateTemplate` is called, a new version is created. Each version of the template maintains a description of the version in the `VersionDescription` field.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-quicksight-template-return-values"></a>

### Fn::GetAtt
<a name="aws-resource-quicksight-template-return-values-fn--getatt"></a>

####
<a name="aws-resource-quicksight-template-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the template.

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
The time this template was created.

`LastUpdatedTime`  <a name="LastUpdatedTime-fn::getatt"></a>
The time this template was last updated.
