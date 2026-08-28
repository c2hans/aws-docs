---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flow-flowdataconnectionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Flow FlowDataConnectionConfiguration
<a name="aws-properties-bedrock-flow-flowdataconnectionconfiguration"></a>

The configuration of a connection originating from a node that isn't a Condition node.

## Syntax
<a name="aws-properties-bedrock-flow-flowdataconnectionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flow-flowdataconnectionconfiguration-syntax.json"></a>

```
{
  "[SourceOutput](#cfn-bedrock-flow-flowdataconnectionconfiguration-sourceoutput)" : {{String}},
  "[TargetInput](#cfn-bedrock-flow-flowdataconnectionconfiguration-targetinput)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flow-flowdataconnectionconfiguration-syntax.yaml"></a>

```
  [SourceOutput](#cfn-bedrock-flow-flowdataconnectionconfiguration-sourceoutput): {{String}}
  [TargetInput](#cfn-bedrock-flow-flowdataconnectionconfiguration-targetinput): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flow-flowdataconnectionconfiguration-properties"></a>

`SourceOutput`  <a name="cfn-bedrock-flow-flowdataconnectionconfiguration-sourceoutput"></a>
The name of the output in the source node that the connection begins from.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetInput`  <a name="cfn-bedrock-flow-flowdataconnectionconfiguration-targetinput"></a>
The name of the input in the target node that the connection ends at.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
