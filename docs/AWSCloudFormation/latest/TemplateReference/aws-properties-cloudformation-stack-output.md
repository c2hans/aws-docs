---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudformation-stack-output.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::Stack Output
<a name="aws-properties-cloudformation-stack-output"></a>

The `Output` data type.

## Syntax
<a name="aws-properties-cloudformation-stack-output-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudformation-stack-output-syntax.json"></a>

```
{
  "[Description](#cfn-cloudformation-stack-output-description)" : {{String}},
  "[ExportName](#cfn-cloudformation-stack-output-exportname)" : {{String}},
  "[OutputKey](#cfn-cloudformation-stack-output-outputkey)" : {{String}},
  "[OutputValue](#cfn-cloudformation-stack-output-outputvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudformation-stack-output-syntax.yaml"></a>

```
  [Description](#cfn-cloudformation-stack-output-description): {{String}}
  [ExportName](#cfn-cloudformation-stack-output-exportname): {{String}}
  [OutputKey](#cfn-cloudformation-stack-output-outputkey): {{String}}
  [OutputValue](#cfn-cloudformation-stack-output-outputvalue): {{String}}
```

## Properties
<a name="aws-properties-cloudformation-stack-output-properties"></a>

`Description`  <a name="cfn-cloudformation-stack-output-description"></a>
User defined description associated with the output.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExportName`  <a name="cfn-cloudformation-stack-output-exportname"></a>
The name of the export associated with the output.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputKey`  <a name="cfn-cloudformation-stack-output-outputkey"></a>
The key associated with the output.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputValue`  <a name="cfn-cloudformation-stack-output-outputvalue"></a>
The value associated with the output.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
