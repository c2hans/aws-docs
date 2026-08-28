---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-dataset-s3source.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Dataset S3Source
<a name="aws-properties-bedrockagentcore-dataset-s3source"></a>

 Amazon S3 location of a JSONL file containing dataset examples.

## Syntax
<a name="aws-properties-bedrockagentcore-dataset-s3source-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-dataset-s3source-syntax.json"></a>

```
{
  "[S3Uri](#cfn-bedrockagentcore-dataset-s3source-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-dataset-s3source-syntax.yaml"></a>

```
  [S3Uri](#cfn-bedrockagentcore-dataset-s3source-s3uri): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-dataset-s3source-properties"></a>

`S3Uri`  <a name="cfn-bedrockagentcore-dataset-s3source-s3uri"></a>
 Amazon S3 URI of the JSONL file (for example, `s3://my-bucket/path/to/examples.jsonl`).
*Required*: Yes
*Type*: String
*Pattern*: `^s3://[a-z0-9][a-z0-9.\-]{1,61}[a-z0-9]/.{1,1024}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
