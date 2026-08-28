---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flow-flowconnection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Flow FlowConnection
<a name="aws-properties-bedrock-flow-flowconnection"></a>

Contains information about a connection between two nodes in the flow.

## Syntax
<a name="aws-properties-bedrock-flow-flowconnection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flow-flowconnection-syntax.json"></a>

```
{
  "[Configuration](#cfn-bedrock-flow-flowconnection-configuration)" : {{FlowConnectionConfiguration}},
  "[Name](#cfn-bedrock-flow-flowconnection-name)" : {{String}},
  "[Source](#cfn-bedrock-flow-flowconnection-source)" : {{String}},
  "[Target](#cfn-bedrock-flow-flowconnection-target)" : {{String}},
  "[Type](#cfn-bedrock-flow-flowconnection-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flow-flowconnection-syntax.yaml"></a>

```
  [Configuration](#cfn-bedrock-flow-flowconnection-configuration): {{
    FlowConnectionConfiguration}}
  [Name](#cfn-bedrock-flow-flowconnection-name): {{String}}
  [Source](#cfn-bedrock-flow-flowconnection-source): {{String}}
  [Target](#cfn-bedrock-flow-flowconnection-target): {{String}}
  [Type](#cfn-bedrock-flow-flowconnection-type): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flow-flowconnection-properties"></a>

`Configuration`  <a name="cfn-bedrock-flow-flowconnection-configuration"></a>
The configuration of the connection.
*Required*: No
*Type*: [FlowConnectionConfiguration](aws-properties-bedrock-flow-flowconnectionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrock-flow-flowconnection-name"></a>
A name for the connection that you can reference.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z]([_]?[0-9a-zA-Z]){1,100}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-bedrock-flow-flowconnection-source"></a>
The node that the connection starts at.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Target`  <a name="cfn-bedrock-flow-flowconnection-target"></a>
The node that the connection ends at.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-bedrock-flow-flowconnection-type"></a>
Whether the source node that the connection begins from is a condition node (`Conditional`) or not (`Data`).
*Required*: Yes
*Type*: String
*Allowed values*: `Data | Conditional`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
