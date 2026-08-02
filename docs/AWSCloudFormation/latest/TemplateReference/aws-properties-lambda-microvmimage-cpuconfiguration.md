---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-cpuconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::MicrovmImage CpuConfiguration
<a name="aws-properties-lambda-microvmimage-cpuconfiguration"></a>

Configuration for the CPU architecture of a MicroVM.

## Syntax
<a name="aws-properties-lambda-microvmimage-cpuconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-microvmimage-cpuconfiguration-syntax.json"></a>

```
{
  "[Architecture](#cfn-lambda-microvmimage-cpuconfiguration-architecture)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-microvmimage-cpuconfiguration-syntax.yaml"></a>

```
  [Architecture](#cfn-lambda-microvmimage-cpuconfiguration-architecture): {{String}}
```

## Properties
<a name="aws-properties-lambda-microvmimage-cpuconfiguration-properties"></a>

`Architecture`  <a name="cfn-lambda-microvmimage-cpuconfiguration-architecture"></a>
The CPU architecture.
*Required*: Yes
*Type*: String
*Allowed values*: `ARM_64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
