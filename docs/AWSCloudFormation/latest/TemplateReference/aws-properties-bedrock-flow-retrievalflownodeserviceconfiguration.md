---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flow-retrievalflownodeserviceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Flow RetrievalFlowNodeServiceConfiguration
<a name="aws-properties-bedrock-flow-retrievalflownodeserviceconfiguration"></a>

Contains configurations for the service to use for retrieving data to return as the output from the node.

## Syntax
<a name="aws-properties-bedrock-flow-retrievalflownodeserviceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flow-retrievalflownodeserviceconfiguration-syntax.json"></a>

```
{
  "[S3](#cfn-bedrock-flow-retrievalflownodeserviceconfiguration-s3)" : {{RetrievalFlowNodeS3Configuration}}
}
```

### YAML
<a name="aws-properties-bedrock-flow-retrievalflownodeserviceconfiguration-syntax.yaml"></a>

```
  [S3](#cfn-bedrock-flow-retrievalflownodeserviceconfiguration-s3): {{
    RetrievalFlowNodeS3Configuration}}
```

## Properties
<a name="aws-properties-bedrock-flow-retrievalflownodeserviceconfiguration-properties"></a>

`S3`  <a name="cfn-bedrock-flow-retrievalflownodeserviceconfiguration-s3"></a>
Contains configurations for the Amazon S3 location from which to retrieve data to return as the output from the node.
*Required*: No
*Type*: [RetrievalFlowNodeS3Configuration](aws-properties-bedrock-flow-retrievalflownodes3configuration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
