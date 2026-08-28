---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-databrew-dataset-filtervalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataBrew::Dataset FilterValue
<a name="aws-properties-databrew-dataset-filtervalue"></a>

Represents a single entry in the `ValuesMap` of a `FilterExpression`. A `FilterValue` associates the name of a substitution variable in an expression to its value.

## Syntax
<a name="aws-properties-databrew-dataset-filtervalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-databrew-dataset-filtervalue-syntax.json"></a>

```
{
  "[Value](#cfn-databrew-dataset-filtervalue-value)" : {{String}},
  "[ValueReference](#cfn-databrew-dataset-filtervalue-valuereference)" : {{String}}
}
```

### YAML
<a name="aws-properties-databrew-dataset-filtervalue-syntax.yaml"></a>

```
  [Value](#cfn-databrew-dataset-filtervalue-value): {{String}}
  [ValueReference](#cfn-databrew-dataset-filtervalue-valuereference): {{String}}
```

## Properties
<a name="aws-properties-databrew-dataset-filtervalue-properties"></a>

`Value`  <a name="cfn-databrew-dataset-filtervalue-value"></a>
The value to be associated with the substitution variable.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValueReference`  <a name="cfn-databrew-dataset-filtervalue-valuereference"></a>
The substitution variable reference.
*Required*: Yes
*Type*: String
*Pattern*: `^:[A-Za-z0-9_]+$`
*Minimum*: `2`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
