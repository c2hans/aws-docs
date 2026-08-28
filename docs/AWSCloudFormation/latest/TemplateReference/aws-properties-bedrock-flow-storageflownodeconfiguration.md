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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
