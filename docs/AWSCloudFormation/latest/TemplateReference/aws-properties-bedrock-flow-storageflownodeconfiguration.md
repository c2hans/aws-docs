---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flow-storageflownodeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Flow StorageFlowNodeConfiguration
<a name="aws-properties-bedrock-flow-storageflownodeconfiguration"></a>

Contains configurations for a Storage node in a flow. This node stores the input in an Amazon S3 location that you specify.

## Syntax
<a name="aws-properties-bedrock-flow-storageflownodeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flow-storageflownodeconfiguration-syntax.json"></a>

```
{
  "[ServiceConfiguration](#cfn-bedrock-flow-storageflownodeconfiguration-serviceconfiguration)" : {{StorageFlowNodeServiceConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-flow-storageflownodeconfiguration-syntax.yaml"></a>

```
  [ServiceConfiguration](#cfn-bedrock-flow-storageflownodeconfiguration-serviceconfiguration): {{
    StorageFlowNodeServiceConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-flow-storageflownodeconfiguration-properties"></a>

`ServiceConfiguration`  <a name="cfn-bedrock-flow-storageflownodeconfiguration-serviceconfiguration"></a>
Contains configurations for the service to use for storing the input into the node.
*Required*: Yes
*Type*: [StorageFlowNodeServiceConfiguration](aws-properties-bedrock-flow-storageflownodeserviceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
