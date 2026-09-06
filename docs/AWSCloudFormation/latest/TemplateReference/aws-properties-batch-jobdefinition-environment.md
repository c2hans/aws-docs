---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-environment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition Environment
<a name="aws-properties-batch-jobdefinition-environment"></a>

The Environment property type specifies environment variables to use in a job definition.

## Syntax
<a name="aws-properties-batch-jobdefinition-environment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-environment-syntax.json"></a>

```
{
  "[Name](#cfn-batch-jobdefinition-environment-name)" : {{String}},
  "[Value](#cfn-batch-jobdefinition-environment-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-environment-syntax.yaml"></a>

```
  [Name](#cfn-batch-jobdefinition-environment-name): {{String}}
  [Value](#cfn-batch-jobdefinition-environment-value): {{String}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-environment-properties"></a>

`Name`  <a name="cfn-batch-jobdefinition-environment-name"></a>
The name of the environment variable.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-batch-jobdefinition-environment-value"></a>
The value of the environment variable.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
