---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flowversion-flowdataconnectionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::FlowVersion FlowDataConnectionConfiguration
<a name="aws-properties-bedrock-flowversion-flowdataconnectionconfiguration"></a>

The configuration of a connection originating from a node that isn't a Condition node.

## Syntax
<a name="aws-properties-bedrock-flowversion-flowdataconnectionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flowversion-flowdataconnectionconfiguration-syntax.json"></a>

```
{
  "[SourceOutput](#cfn-bedrock-flowversion-flowdataconnectionconfiguration-sourceoutput)" : {{String}},
  "[TargetInput](#cfn-bedrock-flowversion-flowdataconnectionconfiguration-targetinput)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flowversion-flowdataconnectionconfiguration-syntax.yaml"></a>

```
  [SourceOutput](#cfn-bedrock-flowversion-flowdataconnectionconfiguration-sourceoutput): {{String}}
  [TargetInput](#cfn-bedrock-flowversion-flowdataconnectionconfiguration-targetinput): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flowversion-flowdataconnectionconfiguration-properties"></a>

`SourceOutput`  <a name="cfn-bedrock-flowversion-flowdataconnectionconfiguration-sourceoutput"></a>
The name of the output in the source node that the connection begins from.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetInput`  <a name="cfn-bedrock-flowversion-flowdataconnectionconfiguration-targetinput"></a>
The name of the input in the target node that the connection ends at.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
