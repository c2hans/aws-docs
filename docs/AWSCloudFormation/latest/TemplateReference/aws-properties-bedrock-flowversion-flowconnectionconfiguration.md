---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flowversion-flowconnectionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::FlowVersion FlowConnectionConfiguration
<a name="aws-properties-bedrock-flowversion-flowconnectionconfiguration"></a>

The configuration of the connection.

## Syntax
<a name="aws-properties-bedrock-flowversion-flowconnectionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flowversion-flowconnectionconfiguration-syntax.json"></a>

```
{
  "[Conditional](#cfn-bedrock-flowversion-flowconnectionconfiguration-conditional)" : {{FlowConditionalConnectionConfiguration}},
  "[Data](#cfn-bedrock-flowversion-flowconnectionconfiguration-data)" : {{FlowDataConnectionConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-flowversion-flowconnectionconfiguration-syntax.yaml"></a>

```
  [Conditional](#cfn-bedrock-flowversion-flowconnectionconfiguration-conditional): {{
    FlowConditionalConnectionConfiguration}}
  [Data](#cfn-bedrock-flowversion-flowconnectionconfiguration-data): {{
    FlowDataConnectionConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-flowversion-flowconnectionconfiguration-properties"></a>

`Conditional`  <a name="cfn-bedrock-flowversion-flowconnectionconfiguration-conditional"></a>
The configuration of a connection originating from a Condition node.
*Required*: No
*Type*: [FlowConditionalConnectionConfiguration](aws-properties-bedrock-flowversion-flowconditionalconnectionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Data`  <a name="cfn-bedrock-flowversion-flowconnectionconfiguration-data"></a>
The configuration of a connection originating from a node that isn't a Condition node.
*Required*: No
*Type*: [FlowDataConnectionConfiguration](aws-properties-bedrock-flowversion-flowdataconnectionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
