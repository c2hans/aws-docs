---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-fieldsort.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template FieldSort
<a name="aws-properties-quicksight-template-fieldsort"></a>

The sort configuration for a field in a field well.

## Syntax
<a name="aws-properties-quicksight-template-fieldsort-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-fieldsort-syntax.json"></a>

```
{
  "[Direction](#cfn-quicksight-template-fieldsort-direction)" : {{String}},
  "[FieldId](#cfn-quicksight-template-fieldsort-fieldid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-fieldsort-syntax.yaml"></a>

```
  [Direction](#cfn-quicksight-template-fieldsort-direction): {{String}}
  [FieldId](#cfn-quicksight-template-fieldsort-fieldid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-fieldsort-properties"></a>

`Direction`  <a name="cfn-quicksight-template-fieldsort-direction"></a>
The sort direction. Choose one of the following options:
+ `ASC`: Ascending
+ `DESC`: Descending
*Required*: Yes
*Type*: String
*Allowed values*: `ASC | DESC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldId`  <a name="cfn-quicksight-template-fieldsort-fieldid"></a>
The sort configuration target field.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
