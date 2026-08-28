---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-ekscontainerenvironmentvariable.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition EksContainerEnvironmentVariable
<a name="aws-properties-batch-jobdefinition-ekscontainerenvironmentvariable"></a>

An environment variable.

## Syntax
<a name="aws-properties-batch-jobdefinition-ekscontainerenvironmentvariable-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-ekscontainerenvironmentvariable-syntax.json"></a>

```
{
  "[Name](#cfn-batch-jobdefinition-ekscontainerenvironmentvariable-name)" : {{String}},
  "[Value](#cfn-batch-jobdefinition-ekscontainerenvironmentvariable-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-ekscontainerenvironmentvariable-syntax.yaml"></a>

```
  [Name](#cfn-batch-jobdefinition-ekscontainerenvironmentvariable-name): {{String}}
  [Value](#cfn-batch-jobdefinition-ekscontainerenvironmentvariable-value): {{String}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-ekscontainerenvironmentvariable-properties"></a>

`Name`  <a name="cfn-batch-jobdefinition-ekscontainerenvironmentvariable-name"></a>
The name of the environment variable.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-batch-jobdefinition-ekscontainerenvironmentvariable-value"></a>
The value of the environment variable.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
