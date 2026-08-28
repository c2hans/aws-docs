---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-datapathvalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template DataPathValue
<a name="aws-properties-quicksight-template-datapathvalue"></a>

The data path that needs to be sorted.

## Syntax
<a name="aws-properties-quicksight-template-datapathvalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-datapathvalue-syntax.json"></a>

```
{
  "[DataPathType](#cfn-quicksight-template-datapathvalue-datapathtype)" : {{DataPathType}},
  "[FieldId](#cfn-quicksight-template-datapathvalue-fieldid)" : {{String}},
  "[FieldValue](#cfn-quicksight-template-datapathvalue-fieldvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-datapathvalue-syntax.yaml"></a>

```
  [DataPathType](#cfn-quicksight-template-datapathvalue-datapathtype): {{
    DataPathType}}
  [FieldId](#cfn-quicksight-template-datapathvalue-fieldid): {{String}}
  [FieldValue](#cfn-quicksight-template-datapathvalue-fieldvalue): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-datapathvalue-properties"></a>

`DataPathType`  <a name="cfn-quicksight-template-datapathvalue-datapathtype"></a>
The type configuration of the field.
*Required*: No
*Type*: [DataPathType](aws-properties-quicksight-template-datapathtype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldId`  <a name="cfn-quicksight-template-datapathvalue-fieldid"></a>
The field ID of the field that needs to be sorted.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldValue`  <a name="cfn-quicksight-template-datapathvalue-fieldvalue"></a>
The actual value of the field that needs to be sorted.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
