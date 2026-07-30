---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flow-performanceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Flow PerformanceConfiguration
<a name="aws-properties-bedrock-flow-performanceconfiguration"></a>

Performance settings for a model.

## Syntax
<a name="aws-properties-bedrock-flow-performanceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flow-performanceconfiguration-syntax.json"></a>

```
{
  "[Latency](#cfn-bedrock-flow-performanceconfiguration-latency)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flow-performanceconfiguration-syntax.yaml"></a>

```
  [Latency](#cfn-bedrock-flow-performanceconfiguration-latency): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flow-performanceconfiguration-properties"></a>

`Latency`  <a name="cfn-bedrock-flow-performanceconfiguration-latency"></a>
To use a latency-optimized version of the model, set to `optimized`.
*Required*: No
*Type*: String
*Allowed values*: `standard | optimized`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
