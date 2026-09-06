---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flow-storageflownodeserviceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Flow StorageFlowNodeServiceConfiguration
<a name="aws-properties-bedrock-flow-storageflownodeserviceconfiguration"></a>

Contains configurations for the service to use for storing the input into the node.

## Syntax
<a name="aws-properties-bedrock-flow-storageflownodeserviceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flow-storageflownodeserviceconfiguration-syntax.json"></a>

```
{
  "[S3](#cfn-bedrock-flow-storageflownodeserviceconfiguration-s3)" : {{StorageFlowNodeS3Configuration}}
}
```

### YAML
<a name="aws-properties-bedrock-flow-storageflownodeserviceconfiguration-syntax.yaml"></a>

```
  [S3](#cfn-bedrock-flow-storageflownodeserviceconfiguration-s3): {{
    StorageFlowNodeS3Configuration}}
```

## Properties
<a name="aws-properties-bedrock-flow-storageflownodeserviceconfiguration-properties"></a>

`S3`  <a name="cfn-bedrock-flow-storageflownodeserviceconfiguration-s3"></a>
Contains configurations for the Amazon S3 location in which to store the input into the node.
*Required*: No
*Type*: [StorageFlowNodeS3Configuration](aws-properties-bedrock-flow-storageflownodes3configuration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
