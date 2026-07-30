---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flowversion-retrievalflownodes3configuration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::FlowVersion RetrievalFlowNodeS3Configuration
<a name="aws-properties-bedrock-flowversion-retrievalflownodes3configuration"></a>

Contains configurations for the Amazon S3 location from which to retrieve data to return as the output from the node.

## Syntax
<a name="aws-properties-bedrock-flowversion-retrievalflownodes3configuration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flowversion-retrievalflownodes3configuration-syntax.json"></a>

```
{
  "[BucketName](#cfn-bedrock-flowversion-retrievalflownodes3configuration-bucketname)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flowversion-retrievalflownodes3configuration-syntax.yaml"></a>

```
  [BucketName](#cfn-bedrock-flowversion-retrievalflownodes3configuration-bucketname): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flowversion-retrievalflownodes3configuration-properties"></a>

`BucketName`  <a name="cfn-bedrock-flowversion-retrievalflownodes3configuration-bucketname"></a>
The name of the Amazon S3 bucket from which to retrieve data.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
