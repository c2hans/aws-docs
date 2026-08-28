---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flow-retrievalflownodeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Flow RetrievalFlowNodeConfiguration
<a name="aws-properties-bedrock-flow-retrievalflownodeconfiguration"></a>

Contains configurations for a Retrieval node in a flow. This node retrieves data from the Amazon S3 location that you specify and returns it as the output.

## Syntax
<a name="aws-properties-bedrock-flow-retrievalflownodeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flow-retrievalflownodeconfiguration-syntax.json"></a>

```
{
  "[ServiceConfiguration](#cfn-bedrock-flow-retrievalflownodeconfiguration-serviceconfiguration)" : {{RetrievalFlowNodeServiceConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-flow-retrievalflownodeconfiguration-syntax.yaml"></a>

```
  [ServiceConfiguration](#cfn-bedrock-flow-retrievalflownodeconfiguration-serviceconfiguration): {{
    RetrievalFlowNodeServiceConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-flow-retrievalflownodeconfiguration-properties"></a>

`ServiceConfiguration`  <a name="cfn-bedrock-flow-retrievalflownodeconfiguration-serviceconfiguration"></a>
Contains configurations for the service to use for retrieving data to return as the output from the node.
*Required*: Yes
*Type*: [RetrievalFlowNodeServiceConfiguration](aws-properties-bedrock-flow-retrievalflownodeserviceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
