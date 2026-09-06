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
