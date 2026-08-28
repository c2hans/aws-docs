---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flowversion-storageflownodes3configuration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::FlowVersion StorageFlowNodeS3Configuration
<a name="aws-properties-bedrock-flowversion-storageflownodes3configuration"></a>

Contains configurations for the Amazon S3 location in which to store the input into the node.

## Syntax
<a name="aws-properties-bedrock-flowversion-storageflownodes3configuration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flowversion-storageflownodes3configuration-syntax.json"></a>

```
{
  "[BucketName](#cfn-bedrock-flowversion-storageflownodes3configuration-bucketname)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flowversion-storageflownodes3configuration-syntax.yaml"></a>

```
  [BucketName](#cfn-bedrock-flowversion-storageflownodes3configuration-bucketname): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flowversion-storageflownodes3configuration-properties"></a>

`BucketName`  <a name="cfn-bedrock-flowversion-storageflownodes3configuration-bucketname"></a>
The name of the Amazon S3 bucket in which to store the input into the node.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
